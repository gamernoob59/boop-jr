import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#import dice images
dice1='assets/dice/dice1.jpg'
dice2='assets/dice/dice2.jpg'
dice3='assets/dice/dice3.jpg'
dice4='assets/dice/dice4.jpg'
dice5='assets/dice/dice5.jpg'
dice6='assets/dice/dice6.jpg'
#import teky images, boy this is long
#but this makes the list which contains these smallers and readable
t1='assets/teky/teki.png'
t2='assets/teky/teki_riches.png'
t3='assets/teky/teky_bed_break.png'
t4='assets/teky/teky_blush.png'
t5='assets/teky/teky_celebration.png'
t6='assets/teky/teky_derp.png'
t7='assets/teky/teky_eyes.png'
t8='assets/teky/teky_hackusation.png'
t9='assets/teky/teky_mad.png'
t10='assets/teky/teky_nervous.png'
t11='assets/teky/teky_pensive.png'
t12='assets/teky/teky_sus_eyes.png'
t13='assets/teky/teky_thumbsup.gif'
t14='assets/teky/teky_void.png'
t15='assets/teky/teky_wink.png'
t16='assets/teky/tekyposter.png'

@client.event
async def on_message(message):
    prefix = '&'
    b='b'

    if message.author == client.user:
        return
    #lists server commands
    if message.content.startswith(prefix+'help'):
        await message.channel.send("`Commands \nboopjr \nhypixel-game \nrolldice \nteky`")
    #random sutff
    if message.content.startswith('hello BoopJr'):
        await message.channel.send('Hello!')

    if message.content.startswith('Hello BoopJr'):
        await message.channel.send('Hello!')

    if message.content.startswith('hello boopjr'):
            await message.channel.send('Hello!')
    #image test
    if message.content.startswith(prefix+'boopjr'):
      with open('toucan-bird-image.jpg', 'rb') as f:
        picture = discord.File(f)
      await message.channel.send(file=picture)
    #list hypixel game to play
    if message.content.startswith(prefix+'hypixel-game'):
        hypixelgames=["BedWars","SkyWars","Murder Mystery","Duels","The Pit","SkyBlock","QuakeCraft","TNT Games","Warlords","UHC"]
        await message.channel.send(random.choice(hypixelgames))
    #rolls a dice
    if message.content.startswith(prefix+'rolldice'):
        die=[dice1,dice2,dice3,dice4,dice5,dice6]
        with open(random.choice(die), 'rb') as g:
            dicepicture = discord.File(g)
        await message.channel.send(file=dicepicture)
    #sends a random teky emote
    if message.content.startswith(prefix+'teky'):
        teky_emotes=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16]
        with open(random.choice(teky_emotes), 'rb') as h:
            tekyemoji = discord.File(h)
        await message.channel.send(file=tekyemoji)



client.run('OTAxODQ1MjM5NjM4MTM0ODk1.YXVy1A.hJ8CjCSWgf2ytx2POxrRcUWQ4ko')