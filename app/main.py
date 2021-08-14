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
                    if float(stat) > 1:
                        open('first.svg', 'w').write(open('first.svg').read().replace('>Name</tspan>','>'+ playerName + '</tspan>'))
                        #svg2png(bytestring=open('first.svg', 'w').read(),write_to='first.png')
                        #data = io.BytesIO(await resp.read())
                        await message.channel.send(file=discord.File('./first.png'))
                except ValueError:
                     print("not Int")
                     
        stats[playerName] = playerStatistics
        
    if message.content == '!BNDT':
        response = stats
        await message.channel.send(response)

client.run(TOKEN)