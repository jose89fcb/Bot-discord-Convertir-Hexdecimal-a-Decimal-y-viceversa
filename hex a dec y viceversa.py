import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help




@bot.command()
async def hexadecimal(ctx, *, numero):
   entero = (int(numero))
   hexadecimal = hex(entero)
   hexadecimal = format(entero,"0x")
   
   embed = discord.Embed(title="Hexadecimal", description=f"{hexadecimal}", color=discord.Colour.random())
   await ctx.send(embed=embed)
   
 ###

@bot.command()
async def decimal(ctx, *, numero):
    NumeroHEX = f"{numero}"
    NumHEX = int(NumeroHEX,16)
    hex(NumHEX)
   
    embed = discord.Embed(title="Decimal", description=f"{NumHEX}", color=discord.Colour.random())
    await ctx.send(embed=embed)
   





bot.run("")