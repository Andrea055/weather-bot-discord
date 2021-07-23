import requests
import json
import os
import discord
from discord.ext import commands
from discord.ext.commands import bot


client = commands.Bot(command_prefix='.')    #define bot prefix



@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

@client.command()                                       # wide command and processing 
async def weather(ctx, *, arg):
    os.remove("ciro.json")
    location=arg
    api="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+ location +"?unitGroup=metric&key=VISUALCROSSINGAPIKEY"
    r=requests.get(api)
    open('ciro.json', 'wb').write(r.content)
    json1open=open('ciro.json')
    json1=(json1open.read())
    printdate= json.loads(json1)
    location=arg
    for i in printdate['days']:
        await ctx.send(':timer:Orario: {} :thermometer:Temperatura: {} :cloud_rain:Precipitazione: {} Probabilità di precipitazioni: {} :cloud_snow:Neve: {} :wind_blowing_face:Velocità del vento: {}'.format(i['datetime'], i['temp'],i['precip'],i['precipprob'],i['snow'],i['windspeed']))

client.run('TOKENDISCORDBOT')
