import os

import discord
from dotenv import load_dotenv

from bs4 import BeautifulSoup

import requests

import xml.dom.minidom

#from cairosvg import svg2png

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

        
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '!luckycharms' in message.content:
        embed=discord.Embed(title="Tier 1 BNDT", url="https://dashleague.games/teams/bndt/", description="", color=0x1CEEEE)
        embed.set_thumbnail(url="https://github.com/AndreasInk/HyperDashDiscordBot/blob/main/lucky.jpg?raw=true")
        #embed.add_field(name="BNDT " + playerName, value=statType + ": " + stat, inline=False)
        await message.channel.send(embed=embed)
    if '!RP' in message.content:
        print(1)
        team_url = 'https://dashleague.games/players/' + message.content.replace("!RP ", "").lower()
        page = requests.get(team_url)
        soup = BeautifulSoup(page.content, "html.parser")
        #players = soup.find_all("div", class_="player__tag")
        stats = {}

        playerStats = soup.find_all("div", class_="stats__stat")
        
        playerStatistics = {}
        
        for playerStat in playerStats:
            
            statType = playerStat.find("span").text.strip()
            stat = playerStat.text.strip().replace(statType, "").replace("\n", "").replace("        ", "")
            playerStatistics[statType]  = stat
            #soup = BeautifulSoup(page.content, "html.parser")
            
            playerRank = 0
            if statType == "K/D":
                
                #if int(stat) > 0.8:
                #    open('third.svg', 'w').write(open('third.svg').read().replace('>TEXT TO CHANGE</tspan>','>What I meant to write</tspan>'))
                #    await message.channel.send(file=discord.File('third.svg'))
                #if int(stat) > 0.9:
                #    open('second.svg', 'w').write(open('second.svg').read().replace('>TEXT TO CHANGE</tspan>','>What I meant to write</tspan>'))
                #    await message.channel.send(file=discord.File('second.svg'))
                
                    print(stat)
                    
                    #open('first.svg', 'w').write(open('first.svg').read().replace('>Name</tspan>','>'+ playerName + '</tspan>'))
                    #svg2png(bytestring=open('first.svg', 'w').read(),write_to='first.png')
                    #data = io.BytesIO(await resp.read())
                    embed=discord.Embed(title="", url="https://dashleague.games/teams/bndt/", description="", color=0x1CEEEE)
                    embed.set_thumbnail(url="https://github.com/AndreasInk/HyperDashDiscordBot/blob/main/trophy.png?raw=true")
                    embed.add_field(name="BNDT " + message.content.replace("!RP", ""), value=statType + ": " + stat, inline=False)
                    await message.channel.send(embed=embed)
                    # await message.channel.send(file=discord.File('./first.png'))
                
    if message.content == '!rank':
        team_url = 'https://dashleague.games/teams/bndt/'
        page = requests.get(team_url)
        soup = BeautifulSoup(page.content, "html.parser")
        players = soup.find_all("div", class_="player__tag")
        stats = {}
        for player in players:
            playerName = player.find(class_='player__tag--name').text
            playerPage = requests.get("https://dashleague.games/players/" + playerName)
            soup = BeautifulSoup(playerPage.content, "html.parser")
            playerStats = soup.find_all("div", class_="stats__stat")
           
            playerStatistics = {}
            
            for playerStat in playerStats:
                
                statType = playerStat.find("span").text.strip()
                stat = playerStat.text.strip().replace(statType, "").replace("\n", "").replace("        ", "")
                playerStatistics[statType]  = stat
                soup = BeautifulSoup(page.content, "html.parser")
                
                playerRank = 0
                if statType == "K/D":
                    
                    #if int(stat) > 0.8:
                    #    open('third.svg', 'w').write(open('third.svg').read().replace('>TEXT TO CHANGE</tspan>','>What I meant to write</tspan>'))
                    #    await message.channel.send(file=discord.File('third.svg'))
                    #if int(stat) > 0.9:
                    #    open('second.svg', 'w').write(open('second.svg').read().replace('>TEXT TO CHANGE</tspan>','>What I meant to write</tspan>'))
                    #    await message.channel.send(file=discord.File('second.svg'))
                    try: 
                        print(stat)
                       
                        #open('first.svg', 'w').write(open('first.svg').read().replace('>Name</tspan>','>'+ playerName + '</tspan>'))
                        #svg2png(bytestring=open('first.svg', 'w').read(),write_to='first.png')
                        #data = io.BytesIO(await resp.read())
                        embed=discord.Embed(title="Tier 1 BNDT", url="https://dashleague.games/teams/bndt/", description="", color=0x1CEEEE)
                        embed.set_thumbnail(url="https://github.com/AndreasInk/HyperDashDiscordBot/blob/main/trophy.png?raw=true")
                        embed.add_field(name="BNDT " + playerName, value=statType + ": " + stat, inline=False)
                        await message.channel.send(embed=embed)
                        # await message.channel.send(file=discord.File('./first.png'))
                    except ValueError:
                        print("not float")
        playerRow = soup.find_all("table")
               
                # await message.channel.send(games)
        points = {}
        numberOfMatches = {}
        playerNames = []
        # for row in playerRow:
        #     playerName = row.find("td", class_="name").text.strip()
        #     score = row.find("td", class_="score").text.strip()
        #     playerNames.append(playerName)
        #     try:
        #         points[playerName] = float(points[playerName]) + float(score)
        #         numberOfMatches[playerName] = float(numberOfMatches[playerName]) + 1
               
        #     except:
        #         points[playerName] = float(score)
        #         numberOfMatches[playerName] = 1
                 
        
        #stats[playerName] = playerStatistics/numberOfMatches[playerName]
        removeDuplicateNames = []
        #[removeDuplicateNames.append(x) for x in playerNames if x not in removeDuplicateNames]
        list_set = set(playerNames)
     # convert the set to the list
        unique_list = (list(list_set))
    
        for playerName in unique_list:
            print(playerName)
            if float(float(points[playerName]/float(numberOfMatches[playerName]))) > float(13000):
                embed=discord.Embed(title="Tier 1 BNDT", url="https://dashleague.games/teams/bndt/", description="", color=0x1CEEEE)
                embed.set_thumbnail(url="https://github.com/AndreasInk/HyperDashDiscordBot/blob/main/trophy.png?raw=true")
                
                if "BNDT" in playerName:
                    embed.add_field(name=playerName, value="Points" + ": " + str(float(float(points[playerName]/float(numberOfMatches[playerName])))), inline=False)
                    await message.channel.send(embed=embed)

            
    #if message.content == '!rank':
        #response = stats
       # await message.channel.send(response)

client.run(TOKEN)