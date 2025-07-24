import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# Flask server per tenere attivo il bot su Render o simili
app = Flask('')

@app.route('/')
def home():
    return "Bot attivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Imposta il prefisso dei comandi e gli intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connesso come {bot.user}")

# Comando ping
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Comando paypal
@bot.command()
async def paypal(ctx):
    await ctx.send("💳 PayPal: @ZenithDMADMA (Friends and family)")

# Comando dna che manda un video
@bot.command()
async def dna(ctx):
    video_path = "dna_id_.mp4"  # Assicurati che il file sia nella stessa cartella di bot.py
    await ctx.send(file=discord.File(video_path))

if __name__ == "__main__":
    keep_alive()  # Avvia il server Flask
    TOKEN = os.getenv("DISCORD_TOKEN")  # Prende il token da variabile ambiente su Render
    bot.run(TOKEN)

