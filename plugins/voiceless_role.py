"""
This plugin allows users to receive a role when they connect to a voice channel
(this keeps in mind the server verification level as well) so that they can get
special permissions to do stuff when in a voice channel. You can have a default
role for all channels, or can specify what role goes to specifically what channel,
this allows you to have a different role assigned if the user joins a different
voice channel.
"""


from data.types.bot.plugin_config import PluginConfig
from data.types.discord.permissions import User
from data.types.discord.role import Role
from data.response import VoicelessRoles

from datetime import datetime, timedelta

from holster.emitter import Priority
from disco.bot import Plugin



space_character = "+"
plugin_name = "voiceless roles"
plugin_UUID = "VOICEROLES"



def guild_enabled(guild_id):
    guild_list = PluginConfig.load("guild_list.json")

    if plugin_UUID in guild_list[guild_id]:
        return True
    elif plugin_name in guild_list[guild_id]:
        return True
    else:
        return False



def find_channel(channel_list, name=None, ID=None):
    channels = []
    if name != None:
        name = name.lower().replace(space_character, " ")
    if ID != None:
        ID = ID.lower()

    #check if there is 
    if name == "-default":
        return "default"

    #filter through channel list
    for channel_id in channel_list:
        channel = channel_list[channel_id]

        #ensure channel is a voice channel
        if channel.type == 2:

            #gave a name
            if (name != None) and (ID == None):

                #ensure it is a match
                if channel.name.lower() == name:
                    channels.append(channel)
            
            #gave an ID
            if (ID != None) and (name == None):

                #ensure it is a match
                if channel.id == ID:
                    channels.append(channel)
    
    #verify that only one match occured
    if len(channels) > 1:
        return "NameError"
    
    #return channel ID as a string
    elif len(channels) == 1:
        return str(channels[0].id)

    #error upon finding no channels
    else:
        return "NoMatch"






def find_role(role_list, name=None, ID=None):
    roles = []
    if name != None:
        name = name.lower().replace(space_character, " ")
    if ID != None:
        ID = int(ID.lower())
        print(ID)

    #check if there is 
    if name == "--none":
        return None

    #filter through role list
    for role_id in role_list:
        role = role_list[role_id]

        #gave a name
        if (name != None) and (ID == None):

            #ensure it is a match
            if role.name.lower() == name:
                roles.append(role)
        
        #gave an ID
        if (ID != None) and (name == None):

            #ensure it is a match
            if role.id == ID:
                roles.append(role)
    
    #verify that only one match occured
    if len(roles) > 1:
        return "NameError"
    
    #return role ID as a string
    elif len(roles) == 1:
        return str(roles[0].id)

    #error upon finding no roles
    else:
        return "NoMatch"






class config():
    old_count = None





class VoicelessRolePlugin(Plugin):



    @Plugin.listen("VoiceStateUpdate", priority=Priority.BEFORE)
    def on_voice_update_before(self, event):
        if guild_enabled(str(event.state.guild.id)):
            config.old_count = len(event.state.guild.voice_states)
    









    @Plugin.listen("VoiceStateUpdate", priority=Priority.AFTER)
    def voice_state_update(self, event):
        custom_roles = PluginConfig.load("voiceless_role_mappings")
        role_list = {}

        #make sure not a DM call
        if event.guild == None:
            return
        guild_id = str(event.state.guild_id)
        guild_member = event.guild.get_member(event.state.user)

        #plugin enabled
        if not guild_enabled(guild_id):
            return

        #see if guild has been set up
        if guild_id not in custom_roles:
            return

        #make sure bot has manage roles permission
        if not Bot.has_perm(self.bot.client, event.guild, "manage_roles"):
            return

        #check to see if the channel is NoneType
        if event.state.channel_id != None:
            old_count = config.old_count
            new_count = len(event.state.guild.voice_states)
            channel_id = str(event.state.channel_id)

            ### verification level checking
            verify_level = event.state.guild.verification_level
            join_time = guild_member.joined_at
            current_time = datetime.utcnow()

            #actually has a verification level
            if verify_level > 0:
                give_role = False

                #low
                if verify_level == 1:
                    wait_time = 0

                #medium
                elif verify_level == 2:
                    wait_time = 5 #5 minute time restriction

                #high (tableflip) & extreme (double tableflip)
                elif verify_level >= 3: #or 4
                    wait_time = 10 #10 minute time restriction
                
                #get timedelta objects
                time_delta = timedelta(minutes=wait_time)
                time_difference = join_time - current_time
                
                #check the differences
                if time_difference > time_delta:
                    give_role = True


            ### logic checking for chat joining/leaving
            
            #joining a voice channel
            if new_count > old_count:
                
                #is allowed to get role
                if give_role:

                    #channel has custom mapping:
                    if channel_id in custom_roles[guild_id]:

                        #mapping isn't none
                        if custom_roles[guild_id][channel_id] == None:
                            return
                        
                        #assign role ID
                        role_id = custom_roles[guild_id][channel_id]
                        
                        #member doesn't have role?
                        if role_id not in guild_member.roles:
                            role_list[role_id] = "add"
                    
                    #default mappings
                    else:

                        #default isn't none
                        if custom_roles[guild_id]["default"] == None:
                            return

                        #assign role ID
                        role_id = custom_roles[guild_id]["default"]

                        #user doesn't have role
                        if role_id not in guild_member.roles:
                            role_list[role_id] = "add"

                    #add roles as needed
                    Role.multi(guild_member, bot_member, role_list)

            #moving voice channels
            elif new_count == old_count:
                current_role = None

                #is allowed to get roles
                if give_role:

                    #channel has custom mapping:
                    if channel_id in custom_roles[guild_id]:

                        #mapping isn't none
                        if custom_roles[guild_id][channel_id] != None:
                        
                            #assign role ID
                            role_id = custom_roles[guild_id][channel_id]
                            
                            #member doesn't have role?
                            if role_id not in guild_member.roles:
                                role_list[str(role_id)] = "add"
                            current_role = role_id
                    
                    #default mappings
                    else:

                        #default isn't none
                        if custom_roles[guild_id]["default"] != None:

                            #assign role ID
                            role_id = custom_roles[guild_id]["default"]

                            #user doesn't have role
                            if role_id not in guild_member.roles:
                                role_list[str(role_id)] = "add"
                            current_role = role_id

                #filter through role to find roles to remove
                for channel in custom_roles[guild_id]:
                    role_id = custom_roles[guild_id][channel]

                    #ensure we aren't removing the role w just added
                    if role_id != current_role:

                        #make sure the role isn't none
                        if role_id != None:

                            #make sure user has role
                            if role_id in guild_member.roles:

                                #add role removal to list
                                role_list[str(role_id)] = "remove"

                #add/remove roles as needed
                Role.multi(guild_member, bot_member, role_list)

        #user left the channel
        else:
            
            #filter through custom channels
            for channel in custom_roles[guild_id]:
                role_id = custom_roles[guild_id][channel]

                #does member have role
                if role_id in guild_member.roles:
                    role_list[str(role_id)] = "remove"
            
            #remove roles
            Role.multi(guild_member, bot_member, role_list)










    @Plugin.listen("ChannelDelete")
    def channel_delete(self, event):
        
        #ensure the channel is in a guild
        if event.channel.guild:

            #plugin enabled
            if not guild_enabled(str(event.guild.id)):
                return

            #ensure the channel is a voice channel
            if event.channel.type == 2:
                channel_id = str(event.channel.id)
                guild_id = str(event.channel.guild.id)
                data = PluginConfig.load("voiceless_role_mappings")

                #check if the channel had a mapping
                if channel_id in data[guild_id]:

                    #remove channel from mappings
                    data[guild_id].pop(channel_id)
                    PluginConfig.write(data, "voiceless_role_mappings")










    @Plugin.command("setup", group="voiceless")
    def setup_guild(self, event):
        #make sure its in a guild
        if event.guild == None:
            return

        #check to see if user has the proper permissions
        if not User.has_perm(event.member, "manage_channels"):
            return event.msg.reply(VoicelessRoles.invalid_perms)

        guild_id = str(event.guild.id)

        #plugin enabled
        if not guild_enabled(str(event.guild.id)):
            return event.msg.reply(VoicelessRoles.not_enabled.format(
                plugin_name,
                plugin_UUID
            ))

        #load config
        data = PluginConfig.load("voiceless_role_mappings")

        #check if guild is already set up
        if guild_id in data:
            return event.msg.reply(VoicelessRoles.already_setup)

        #add the guild to the config
        data[str(event.guild.id)] = {}
        PluginConfig.write(data, "voiceless_role_mappings")

        #acknowledge
        return event.msg.reply(VoicelessRoles.guild_setup)










    @Plugin.command("set", group="voiceless")
    def add_mapping(self, event):

        #make sure its in a guild
        if event.guild == None:
            return event.reply(VoicelessRoles.no_DMs)
        guild_id = str(event.guild.id)

        #check to see if user has the proper permissions
        if not User.has_perm(event.member, "manage_channels"):
            return event.msg.reply(VoicelessRoles.invalid_perms)
        
        #plugin enabled
            if not guild_enabled(str(event.guild.id)):
                return event.msg.reply(VoicelessRoles.not_enabled.format(
                    plugin_name,
                    plugin_UUID
                ))

        data = PluginConfig.load("voiceless_role_mappings")
        #check to make sure guild has been setup
        if guild_id not in data:
            return event.msg.reply(VoicelessRoles.not_setup)

        #argument checking
        if len(event.args) < 2:
            return event.msg.reply(VoicelessRoles.nea)


        ## CHANNEL SEARCHING
        channel_list = event.guild.channels
        #gave us an ID
        if event.args[0].lower().startswith("id:"):
            channel_id = int(event.args[0][3:])

            #search for channel
            channel_result = find_channel(channel_list, ID=channel_id)
        
        #gave us a name
        else:

            #search for channel
            channel_result = find_channel(channel_list, name=event.args[0])


        #check for any channel related errors
        if channel_result == "NameError":
            return event.msg.reply(VoicelessRoles.channel_name_error)
        elif channel_result == "NoMatch":
            return event.msg.reply(VoicelessRoles.channel_not_found)

        ## -----------------


        ## ROLE SEARCHING
        #didn't mention a role
        if not len(event.msg.mention_roles):
            role_list = event.guild.roles

            #gave us an ID
            if event.args[1].lower().startswith("id:"):
                
                role_id = event.args[1][3:]

                #search for role
                role_result = find_role(role_list, ID=role_id)

            #gave us a name
            else:
                
                #search for role
                role_result = find_role(role_list, name=event.args[1])

        #mentioned a role
        else:
            role_result = event.msg.mention_roles[0]

        #check for any role related errors
        if role_result == "NameError":
            return event.msg.reply(VoicelessRoles.role_name_error)
        elif role_result == "NoMatch":
            return event.msg.reply(VoicelessRoles.role_not_found)

        ## --------------


        ## Logic Checking for Response
        #set default to none
        if ((channel_result == "default") and (role_result == None)):
            response = VoicelessRoles.removed_default
        
        #set default to a role
        elif ((channel_result == "default") and (role_result != None)):
            response = VoicelessRoles.updated_default.format(role_result)

        #update channel to None
        elif ((channel_result in data[guild_id]) and (role_result == None)):
            response = VoicelessRoles.removed_channel_role.format(channel_result)

        #update channel to role
        elif ((channel_result in data[guild_id]) and (role_result != None)):
            response = VoicelessRoles.updated_channel.format(channel_result,
                                                             role_result)

        #create mapping to None
        elif ((channel_result not in data[guild_id]) and (role_result == None)):
            response = VoicelessRoles.create_channel_none.format(channel_result)

        #create mapping to role
        elif ((channel_result not in data[guild_id]) and (role_result != None)):
            response = VoicelessRoles.create_channel_role.format(channel_result,
                                                                 role_result)

        ## ---------------------------

        try:
            #update configuration
            data[guild_id][channel_result] = role_result
            PluginConfig.write(data, "voiceless_role_mappings")

            #acknowledge
            event.msg.reply(response)
        
        #catch the error
        except:
            #acknowledge error
            event.msg.reply(VoicelessRoles.error)










    @Plugin.command("delete", group="voiceless", aliases=["remove", "reset"])
    def remove_mapping(self, event):

        #make sure its in a guild
        if event.guild == None:
            return event.reply(VoicelessRoles.no_DMs)
        guild_id = str(event.guild.id)

        #check to see if user has the proper permissions
        if not User.has_perm(event.member, "manage_channels"):
            return event.msg.reply(VoicelessRoles.invalid_perms)
        
        #plugin enabled
        if not guild_enabled(str(event.guild.id)):
            return event.msg.reply(VoicelessRoles.not_enabled.format(
                plugin_name,
                plugin_UUID
            ))

        data = PluginConfig.load("voiceless_role_mappings")
        #check to make sure guild has been setup
        if guild_id not in data:
            return event.msg.reply(VoicelessRoles.not_setup)

        #argument checking
        if len(event.args) < 1:
            return event.msg.reply(VoicelessRoles.nea)


        ## CHANNEL SEARCHING
        channel_list = event.guild.channels
        #gave us an ID
        if event.args[0].lower().startswith("id:"):
            channel_id = int(event.args[0][3:])

            #search for channel
            channel_result = find_channel(channel_list, ID=channel_id)
        
        #gave us a name
        else:

            #error if trying to remove default
            if name == "-default":
                return event.msg.reply(no_remove_default)

            #search for channel
            channel_result = find_channel(channel_list, name=event.args[0])


        #check for any channel related errors
        if channel_result == "NameError":
            return event.msg.reply(VoicelessRoles.channel_name_error)
        elif channel_result == "NoMatch":
            return event.msg.reply(VoicelessRoles.channel_not_found)

        ## -----------------

        if channel_result not in data:
            return event.msg.reply(VoicelessRoles.channel_mapping_not_exist)

        data[guild_id].pop(channel_result)
        return event.msg.reply(VoicelessRoles.removed_channel_mapping.format(
            channel_result
        ))