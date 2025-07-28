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

@bot.command(name="dna")
async def dna(ctx):
    try:
        file = discord.File("GetZenith_DNA_ID.zip", filename="GetZenith_DNA_ID.zip")
        logo = discord.File("logo.png", filename="logo.png")

        embed = discord.Embed(
            title="🧬 How to Read Your DNA ID",
            description=(
                "**Follow these steps to get your unique DNA ID:**\n\n"
                "📥 **Tool Download**\n"
                "Click the file below to download the GetZenith DNA Reader Tool.\n\n"
                "🔢 **When you see the message:**\n"
                "`Found  DNA:  0x38FA0F21B3D7C12`\n\n"
                "📩 **What to do next:**\n"
                "Send the code in a **GetZenith ticket** and we'll generate your firmware!"
            ),
            color=0x00ff00
        )

        embed.set_thumbnail(url="attachment://logo.png")
        await ctx.send(embed=embed, files=[file, logo])

    except Exception as e:
        await ctx.send(f"❌ Errore durante l'invio del file DNA: `{e}`")

if __name__ == "__main__":
    keep_alive()  # Avvia il server Flask
    TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
