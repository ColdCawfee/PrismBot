import hikari
import lightbulb
from googletrans import Translator

bot = lightbulb.BotApp(token="") #replace with your token here
translator = Translator()

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Bot ready!")


@bot.listen(hikari.GuildMessageCreateEvent)
async def log(ctx):
    with open("log.txt", 'w') as f:
        f.write(str(ctx.content))


@bot.command
@lightbulb.option("text", "Text to translate.", type=str)
@lightbulb.command("translate", "Mass translate a sentence.")
@lightbulb.implements(lightbulb.SlashCommand)
async def translate(ctx):
    word = ctx.options.text
    await ctx.respond("Translating... This could take a bit.")
    await ctx.respond(f"Original phrase: {word}")
    masstrans = translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(word, dest="af").text, dest="ht").text, dest="ha").text, dest="haw").text, dest="iw").text, dest="hi").text, dest="hmn").text, dest="hu").text, dest="is").text, dest="ig").text, dest="id").text, dest="ga").text, dest="it").text, dest="ja").text, dest="jw").text, dest="kn").text, dest="kk").text, dest="km").text, dest="ko").text, dest="ku").text, dest="ky").text, dest="lo").text, dest="la").text, dest="lv").text, dest="lt").text, dest="lb").text, dest="mk").text, dest="mg").text, dest="ms").text, dest="ml").text, dest="mt").text, dest="mi").text, dest="mr").text, dest="mn").text, dest="my").text, dest="ne").text, dest="no").text, dest="or").text, dest="ps").text, dest="fa").text, dest="pl").text, dest="pl").text, dest="pt").text, dest="pa").text, dest="pa").text, dest="ro").text, dest="ru").text, dest="sm").text, dest="gd").text, dest="sr").text, dest="st").text, dest="sn").text, dest="sd").text, dest="si").text, dest="sk").text, dest="sl").text, dest="so").text, dest="es").text, dest="su").text, dest="sw").text, dest="sv").text, dest="tg").text, dest="ta").text, dest="te").text, dest="th").text, dest="tr").text, dest="uk").text, dest="ur").text, dest="uz").text, dest="vi").text, dest="cy").text, dest="xh").text, dest="yi").text, dest="yo").text, dest="en").text
    await ctx.respond(f"Translated response: {masstrans}")

bot.run(
    activity=hikari.Activity(name="with words.", type=hikari.ActivityType.PLAYING),
    ignore_session_start_limit=True,
    check_for_updates=True,
    status=hikari.Status.ONLINE,
    coroutine_tracking_depth=20,
    propagate_interrupts=True
)
