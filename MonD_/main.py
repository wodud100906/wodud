import discord, pytz, sqlite3
from discord import app_commands, Interaction
from datetime import datetime
from config import config

class MyClient(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        await tree.sync(guild= discord.Object(id=config.config('guild')))
        print("사전예약, mond0o0")

client = MyClient(intents = discord.Intents.all())
tree = app_commands.CommandTree(client)

@tree.command(guild=discord.Object(id=config.config('guild')), name="사전예약")
async def 사전예약(interaction: Interaction):
    embed = discord.Embed(timestamp=datetime.now(pytz.timezone('UTC')), title='사전예약', description=f'{interaction.user.name}님이 사전예약을 했습니다.', color=0x80b4ff)
    embed.set_thumbnail(url=interaction.user.display_avatar)
    await interaction.user.add_roles(interaction.guild.get_role(config.config('role')))
    await interaction.response.send_message(embed=embed)

client.run(config.config('token'))