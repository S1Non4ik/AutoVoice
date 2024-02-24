import disnake
from cfg.cfg import guild
from disnake.ext import commands
from cfg.cfg import *


class limit(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Limit",
                placeholder="Change limit - 1 or 3 max 99",
                custom_id="limituser",
                max_length=2
            ),
        ]
        super().__init__(
            title="New limit",
            custom_id="New_limit",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        await inter.response.send_message('Limit was change', ephemeral=True)
        try:
            for key, value in inter.text_values.items():
                await inter.user.voice.channel.edit(user_limit=value[:1024])
        except (Exception) as error:
            print(error)



class LimitButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='🙎')
    async def button(self, button: disnake.ui.Button, inter):
        try:
            await inter.response.send_modal(modal=limit())
        except Exception as ext:
            print(ext)


class CloseButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='🔒')
    async def button(self, button: disnake.ui.Button, inter):
        try:
            await inter.user.voice.channel.edit(user_limit=1)
            await inter.response.send_message('Channel was closed', ephemeral=True)
        except Exception as ext:
            print(ext)


class OpenButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='✅')
    async def button(self, button: disnake.ui.Button, inter):
        try:
            await inter.user.voice.channel.edit(user_limit=99)
            await inter.response.send_message('Channel was open', ephemeral=True)
        except Exception as ext:
            print(ext)



class VoiceMenu(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('Main Modules - VoiceMenu is Load')

    async def on_error(self, error: Exception, inter: disnake.ModalInteraction):
        await inter.response.send_message(f"An error has occurred!\n```{error}```")

    @commands.slash_command(guild_ids=[guild], description='change your voice')
    async def voicemenu(self, inter: disnake.ApplicationCommandInteraction):
        voice_channel = self.bot.get_channel(inter.user.voice.channel.id)
        user = inter.user.name.replace(f"{inter.user.name}", f"Area {inter.user.name}")
        emb = disnake.Embed(title='**VoiceBot**', description='')
        if str(user) == str(voice_channel):
            button = LimitButton(), CloseButton(), OpenButton()
            await inter.response.send_message(embed=emb,view=button)
        else:
            await inter.response.send_message('у вас нет прав')


def setup(bot: commands.Bot):
    bot.add_cog(VoiceMenu(bot))