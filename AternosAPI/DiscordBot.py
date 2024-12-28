from typing import Optional
import disnake
from disnake.ext import commands
import ApiAternos

token = 'MTMyMjUxMzkwNDkyODE2MTgwMg.GEwwPb.e9ZNadT3JevTBzCA20j90-XFvIKsp0y3wXdoPY'
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents, test_guilds=[1322201462054584380])

class Server(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Start", style=disnake.ButtonStyle.green, emoji="🎉")
    async def st(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        self.value = True
        self.stop()






@bot.event
async def on_ready():
    print(f"Bot {bot.user} запущен!")

@bot.command()
async def ButtonServer(ctx):
    print("1")
    view = Server()
    await ctx.message.delete()
    await ctx.author.send("Нажмите на кнопку чтобы запустить сервер", view=view)
    await view.wait()

    if view.value:
        print("server started!")
        ApiAternos.ServerStarted()

@bot.command()
async def ServerInfo(ctx):
    print("2")
    await ctx.message.delete()
    data = ApiAternos.info()
    for i in data:
        await ctx.author.send(i)

bot.run(token)