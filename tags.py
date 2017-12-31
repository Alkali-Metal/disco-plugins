import os

from data.response import Tags
from data.types.bot.guild_config import GuildConfig

from disco.bot import Plugin



class CustomTags(Plugin):
    
    #!tags add <name> <response...>
    @Plugin.command("add", group="tag", aliases=["create", "new"])
    def add_tag(self, event):
        
        if len(event.args) >= 2:
            if event.msg.guild == None:
                return event.msg.reply(Tags.guild_mandatory)
            
            data = GuildConfig.load(guild_id, force_guild=True)
            need_write = False
            
            if "tags:options" not in data.keys():
                data["tags:options"] = {"is_global": False,
                                        "allow_global": True,
                                        "manage_roles": []}
                need_write = True
            if "tags:data" not in data.keys():
                data["tags:data"] = {}
                need_write = True
            
            if need_write:
                GuildConfig.write(data)
                data = GuildConfig.load(guild_id, force_guild=True)
            
            #TODO: Implement the rest of tag stuff.


class Tag:
    def get_list(local_id):
        tag_list = {}
        for config in os.listdir("data/guilds/"):
            config_id, config_format = config.split(".")
            data = GuildConfig.load(config_id)
            if config_id == local_id:
                for tag in data["tags:data"]:
                    for alias in data["tags:data"][tag]["aliases"]:
                        tag_list[tag] = data["tags:data"][tag]
                    tag_list[tag] = data["tags:data"][tag]
            else:
                if data["tags:options"]["global"]:
                    if data["tags:options"]["are_global"]:
                        for tag in data["tags:data"]:
                            for alias in data["tags:data"][tag]["aliases"]:
                                tag_list[tag] = data["tags:data"][tag]
                            tag_list[tag] = data["tags:data"][tag]
            return tag_list
                        
                    
    
    
    def get(tag_name):
        data = GuildConfig.load(guild_id, force_guild=True)
        if tag_name in data["tags:data"]:
            return data["tags:data"][tag_name]
        else:
            return None
    
    
    def exists(tag_name):
        data = GuildConfig.load(guild_id, force_guild=True)
        