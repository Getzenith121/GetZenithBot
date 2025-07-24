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

@bot.command()
async def dna(ctx):
    await ctx.send(
        "**🧬 Come leggere la tua DNA ID**\n\n"
        "Segui questi passaggi per ottenere il tuo DNA ID univoco:\n\n"
        "1️⃣ **Collega la scheda 75T via USB/JTAG (CH347)**\n"
        "2️⃣ **Installa i driver CH347 se richiesto**\n"
        "3️⃣ **Apri il tool GetZenith 75T DNA Reader**\n"
        "4️⃣ **Attendi qualche secondo**\n\n"
        "Quando compare la scritta:\n"
        "```yaml\nFound DNA: 0x38F4A0F21B3D7C12\n```\n"
        "📋 Copia quel codice e invialo nel ticket a **GetZenith**\n"
        "🔐 Ti genereremo il firmware legato al tuo ID univoco di scheda"
    )

    await ctx.send(file=discord.File("dna_id_.mp4"))  # Assicurati che il video sia nella cartella del bot

if __name__ == "__main__":
    keep_alive()  # Avvia il server Flask
    TOKEN = os.getenv("DISCORD_TOKEN")  # Prende il token da variabile ambiente su Render
    bot.run(TOKEN)

