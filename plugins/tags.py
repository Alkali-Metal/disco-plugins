from data.types.bot.guild_config import GuildConfig
from data.response import Tags


from disco.bot import Plugin


class Tags(Plugin):
    @Plugin.command("remove", group="tag")
    def tag_remove(self, event):
        #argument checking
        if len(event.args) < 1:
            return event.msg.reply(Tags.nea)
        #check for global argument
        elif len(event.args) >= 2:
            tag_name = event.args[0]
            global_tag = event.args[1]
        else:
            tag_name = event.args[0]
            global_tag = False

        #load guild configuration
        if not global_tag:
            tags = GuildConfig.load(event.guild.id, force_guild=True)
        else:
            tags = GuildConfig.load("default")
