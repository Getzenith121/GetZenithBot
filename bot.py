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
    embed = discord.Embed(
        title="📖 Come leggere la tua DNA ID",
        description=(
            "Segui questi passaggi per ottenere il tuo DNA ID univoco:\n\n"
            "1️⃣ **Collega la scheda 75T via USB/JTAG (CH347)**\n"
            "2️⃣ **Installa i driver CH347 se richiesto**\n"
            "3️⃣ **Apri il tool GetZenith 75T DNA Reader**\n"
            "4️⃣ **Attendi qualche secondo**\n\n"
            "Quando compare la scritta:\n"
            "```yaml\n"
            "Found DNA: 0x38F4A0F21B3D7C12\n"
            "```\n"
            "📋 Copia quel codice e invialo nel ticket a GetZenith\n"
            "🔐 Ti genereremo il firmware legato al tuo ID univoco di scheda"
        ),
        color=0x2ecc71
    )
    embed.set_thumbnail(url="https://i.imgur.com/AJdW69A.png")  # Esempio thumbnail
    embed.add_field(
        name="🎥 Video tutorial",
        value="[Guarda il video su YouTube](https://www.youtube.com/watch?v=tuo_video_link)",
        inline=False
    )
    embed.set_footer(text="GetZenith Team", icon_url="https://i.imgur.com/8w0f6pS.png")  # Icona footer

    await ctx.send(embed=embed)

if __name__ == "__main__":
    keep_alive()  # Avvia il server Flask
    TOKEN = os.getenv("DISCORD_TOKEN")  # Prende il token da variabile ambiente su Render
    bot.run(TOKEN)

