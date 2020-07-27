#Discord linkBot

import config
from discord.ext import commands
import urllib
from urllib import request
from urllib.parse import quote
import re, os, sys
#cd C:\python\discord\bots\parsbot


bot = commands.Bot(command_prefix = '$')

# print message when bot ready to work
@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))


# pars link on youtube
def findyoutube(x):
	mas = []
	sq = 'http://www.youtube.com/results?search_query='+quote(x)
	doc = urllib.request.urlopen(sq).read().decode('cp1251', errors = 'ignore')
	match = re.findall("\\?v\\=(.+?)\"", doc)
	if not (match is None):
		for li in match:
			if (len(li)<25):
				mas.append(li)
	mas = dict(zip(mas,mas)).values()
	mas2 = []
	for y in mas: mas2.append('http://www.youtube.com/watch?v='+y)
	return mas2[:1]



@bot.command()
async def ytb(ctx, arg):
	await ctx.send(findyoutube(arg))


@bot.command()
async def hlp(ctx):
	await ctx.send('Для поиска любого видео ютуба введите: $ytb "название видео"(ковычки обязательно)')


@bot.command()
async def ping(ctx):
	await ctx.send('pong')

token = os.environ.get('TOKEN')
		
if __name__ == '__main__':
	bot.run(token)
