import disnake
from cfg.cfg import guild
from disnake.ext import commands
from cfg.cfg import *


class Voice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('Main Modules - Voice is Load')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        def check(x, y, z):
            return len(channel.members) == 0
        try:
            if after.channel.id == VoiceChannel:
                channel = await member.guild.create_voice_channel(name=f'Area {member.name}', category=after.channel.category, user_limit=5)
                await channel.set_permissions(member.guild.get_role(member.guild.id),
                                              send_messages=False)
                await member.move_to(channel)
                await self.bot.wait_for('voice_state_update', check=check)
                await channel.delete()

        except Exception as ext:
            print(ext)



def setup(bot: commands.Bot):
    bot.add_cog(Voice(bot))