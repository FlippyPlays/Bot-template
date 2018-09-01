# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot. I added "randint" because python natively has few advanced features, but there are libraries you can add that adds these features.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
from random import randint

#REMEMBER TO INSTALL DISCORD LIBRARY USING "PIP INSTALL DISCORD"^^^^ OR THEY WON'T WORK.

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="", command_prefix="|", pm_help = True) #pm_help is whether or not the |help command will be PMd to the user or written in chat.
# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted. or flippy :3
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('You are owning Flippy\'s slave') #This is just messages that run in the console, won't appear on Discord. The bots name is defined on the dev page of Discord website.
	print('Enslaved by Flippy')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	return await client.change_presence(game=discord.Game(name='Flippy\'s orders', type=2)) #This is the status, the "playing VRChat" thingy. Type 0 is playing, type 1 is streaming, type 2 is watching and type 4 is listening to, play around with it :3

# This is a basic example of a call and response command. You tell it do "this" and it does it.

@client.command(pass_context=True, brief='Pokes the bot.', description='SPokes the slave to check if it is still alive.') #brief is the details you read in |help, description is the detail you read in |help poke. 
async def poke(ctx): #async def *command*(ctx) is basic template to a response command, ctx means context, not sure it's exact purpose but most commands require it. I believe ctx is used to get information about the command, so a |ping @user would get information about the @user.
	await client.say("Ow, that really hurt~") #The bot will say this in the chat

@client.command(brief='Flips a coin.', description='Flips a coin revealing heads or tails.')
async def coinflip():
	cflip = randint(1, 2) #Upon using this command it will choose a "random" number between 1 and 2, then display a different text message based on it
	if cflip == 1: #"if x == 1" basically asks the bot, is x 2, if yes, do the command, if no, ignore the next line(s).
		await client.say("The coin landed on heads~")
	elif cflip == 2:
		await client.say("The coin landed on tails~")

@client.command(brief='Rolls the dice.', description='Rolls a dice, giving a random number between 1 and 6.')
async def dice():
	await client.say("You rolled " + str(randint(1, 6)) + "~")#this will find a random number between 1 and 6, but the number is defined as str(number), which means it is not a value, but an object, which means the bot will say the number.

@client.command(pass_context=True, brief='Gives your or someone elses profile picture.', description='Gives the profile picture, with url, of you or the user you write after the command. Does not require @mention. cAsE sEnSiTiVe')
async def pfp(ctx, user:discord.User=None): #Due to ctx, if you were to type |pfp @Flippy it would set the discord.User=Flippy, if nothing is said, the discord.User remains as None. If user = None it will print out the pfp of the person typing the command. If user is someone defined, it will print their pfp.
    if user is None:
        user=ctx.message.author
    await client.say(str(user) + "\'s avatar is this: " + user.avatar_url)#A "\" is used because ' is used in python coding, but having a \ in front of something means Python will ignore the "command" and print it out instead.
	
@client.command(pass_context=True, brief='Sends you a mention ping.', description='Makes the bot send you an @ ping.')
async def pingme(ctx):
	await client.say("Nya~ " + "{0.mention}".format(ctx.message.author))

@client.command(pass_context=True, brief='Gives an unusual Wikipedia page.', description='Gives one out of 34 different unusual Wikipedia pages.')
async def unusualwiki(ctx):
	uw = random.randint(1,34)#Pointless command, but rolls a random number from 1 to 34 then prints out the wiki article. May be a much better way to do this command but I did it this way.
	if uw == 1:
		await client.say("https://en.wikipedia.org/wiki/Island_of_California")
	if uw == 2:
		await client.say("https://en.wikipedia.org/wiki/Monowi,_Nebraska")
	if uw == 3:
		await client.say("https://en.wikipedia.org/wiki/Sam_Kee_Building")
	if uw == 4:
		await client.say("https://en.wikipedia.org/wiki/Jewish_Autonomous_Oblast")
	if uw == 5:
		await client.say("https://en.wikipedia.org/wiki/Hell,_Norway")
	if uw == 6:
		await client.say("https://en.wikipedia.org/wiki/Llanfairpwllgwyngyll")
	if uw == 7:
		await client.say("https://en.wikipedia.org/wiki/Y,_Somme")
	if uw == 8:
		await client.say("https://en.wikipedia.org/wiki/2_%2B_2_%3D_5")
	if uw == 9:
		await client.say("https://en.wikipedia.org/wiki/Longest_word_in_English")
	if uw == 10:
		await client.say("https://en.wikipedia.org/wiki/RAS_syndrome")
	if uw == 11:
		await client.say("https://en.wikipedia.org/wiki/Naming_law_in_Sweden#Brfxxccxxmnpcccclllmmnprxvclmnckssqlbb11116")
	if uw == 12:
		await client.say("https://en.wikipedia.org/wiki/Richard_Temple-Nugent-Brydges-Chandos-Grenville,_3rd_Duke_of_Buckingham_and_Chandos")
	if uw == 13:
		await client.say("https://en.wikipedia.org/wiki/Dihydrogen_monoxide_hoax")
	if uw == 14:
		await client.say("https://en.wikipedia.org/wiki/Hot,_dust-obscured_galaxies")
	if uw == 15:
		await client.say("https://en.wikipedia.org/wiki/Tanganyika_laughter_epidemic")
	if uw == 16:
		await client.say("https://en.wikipedia.org/wiki/52-hertz_whale")
	if uw == 17:
		await client.say("https://en.wikipedia.org/wiki/Wojtek_(bear)")
	if uw == 18:
		await client.say("https://en.wikipedia.org/wiki/Antikythera_mechanism")
	if uw == 19:
		await client.say("https://en.wikipedia.org/wiki/Xianxingzhe")
	if uw == 20:
		await client.say("https://en.wikipedia.org/wiki/Bobobo-bo_Bo-bobo")
	if uw == 21:
		await client.say("https://en.wikipedia.org/wiki/Sleepify")
	if uw == 22:
		await client.say("https://en.wikipedia.org/wiki/Night_of_the_Day_of_the_Dawn")
	if uw == 23:
		await client.say("https://en.wikipedia.org/wiki/Corrupted_Blood_incident")
	if uw == 24:
		await client.say("https://en.wikipedia.org/wiki/MaDonal")
	if uw == 25:
		await client.say("https://en.wikipedia.org/wiki/2005_United_States_Grand_Prix")
	if uw == 26:
		await client.say("https://en.wikipedia.org/wiki/1916_Cumberland_vs._Georgia_Tech_football_game")
	if uw == 27:
		await client.say("https://en.wikipedia.org/wiki/United_States_v._Approximately_64,695_Pounds_of_Shark_Fins")
	if uw == 28:
		await client.say("https://en.wikipedia.org/wiki/United_States_ex_rel._Gerald_Mayo_v._Satan_and_His_Staff")
	if uw == 29:
		await client.say("https://en.wikipedia.org/wiki/Anglo-Zanzibar_War")
	if uw == 30:
		await client.say("https://en.wikipedia.org/wiki/War_Plan_Red")
	if uw == 31:
		await client.say("https://en.wikipedia.org/wiki/Tsar_Tank")
	if uw == 32:
		await client.say("https://en.wikipedia.org/wiki/How_many_angels_can_dance_on_the_head_of_a_pin")
	if uw == 33:
		await client.say("https://en.wikipedia.org/wiki/If_a_tree_falls_in_a_forest")
	if uw == 34:
		await client.say("https://en.wikipedia.org/wiki/Voulez-vous_coucher_avec_moi")

@client.command(pass_context=True, brief='Gives a Niko gif.', description='Gives a random (out of 4) gif of Niko.')
async def niko(ctx):
	niko = random.randint(1,4)
	if niko == 1:
		await client.send_file(ctx.message.channel, r"C:\\Users\\xXcla\\Desktop\\BasicBot-master\\Bot-template\\Niko1.gif")#Searches for a file on your pc based on the number it rolls. Then it sends the file to the text channel.
	if niko == 2:
		await client.send_file(ctx.message.channel, r"C:\\Users\\xXcla\\Desktop\\BasicBot-master\\Bot-template\\Niko2.gif")#ctx is likely used to make things like "ctx.nessage.channel" work, which defines which channel the command was posted in.
	if niko == 3:
		await client.send_file(ctx.message.channel, r"C:\\Users\\xXcla\\Desktop\\BasicBot-master\\Bot-template\\Niko3.gif")#Double \\ (backwards slash) is used because python uses \ in coding, so having a \ in front will ignore the function python uses \ for.
	if niko == 4:
		await client.send_file(ctx.message.channel, r"C:\\Users\\xXcla\\Desktop\\BasicBot-master\\Bot-template\\Niko4.gif")
	
client.run('NDg1MDA3NzI4NzUwNjI0NzY5.DmqX7g.e81uJvWkfhmzxeWGJxoA5RMW5AQ')#From the discord development site, after making a bot you can view the key, paste the key in here. Only 1 key per bot and only 1 bot per key.

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.




