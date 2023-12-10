import discord, random, os, requests
from discord.ext import commands
from settings import TOKEN
from bot_logic import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents, help_command=None)
balls = 0

@bot.command()
async def help(ctx):
    await ctx.send("# Привет!<:otter:1172454576344019004>")
    await ctx.send("Я бот борец с глобальным потеплением , а также с загрязнением нашего мира<a:redsiren:1169729235510894682> . Я могу помочь тебе верно отсортировать мусор, для этого нужно прописать команду -check и прикрепить файл, а также по команде -example пришлю как могут выглядеть такие контейнеры<a:Discord_popular_animated:1172262073481306173> . Также вы можете копить эко очки сервера✨  для этого надо прописать -get количество выброшенного вами мусора, команду -points, чтобы узнать сколько баллов вы накопили ")

@bot.command()
async def points(ctx):
    global balls
    await ctx.send(balls)

@bot.command()
async def example(ctx):
    ecom = random.choice(os.listdir("images"))
    with open(f"images\{ecom}", 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def get(ctx, count_bottles):
    global balls
    balls = balls + int(count_bottles)
    ran = random.randint(1, 2)
    if ran == 1:
        await ctx.send(f"Вы получили {count_bottles} экобалл(-а)(-ов)!")
    if ran == 2:
        await ctx.send(f"Вы получили {count_bottles} экобалл(-а)(-ов), вы большой молодец!")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            image_path = 'urimages/{file_name}'
            await attachment.save(image_path)
            await ctx.send(get_class(model_path='model\keras_model.h5', labels_path='model\labels.txt', image_path=image_path))
            os.remove(image_path)

    else:
        await ctx.send("Прикрепи картинку к сообщению!!!")

bot.run(TOKEN)