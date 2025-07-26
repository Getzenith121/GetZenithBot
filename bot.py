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
    dna_code = "0x38F4A0F21B3D7C12"  # Puoi sostituirlo con quello reale

    embed = discord.Embed(
        title="🔬 How to Read Your DNA ID",
        description="Follow these steps to get your unique DNA ID:",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="📌 Steps:",
        value=(
            "1️⃣ Connect the 75T board via USB/JTAG (CH347)\n"
            "2️⃣ Install the CH347 driver if prompted\n"
            "3️⃣ Open the GetZenith 75T DNA Reader tool\n"
            "4️⃣ Wait a few seconds"
        ),
        inline=False
    )

    embed.add_field(
        name="🔎 When you see the message:",
        value=f"```Found DNA:  {dna_code}```",
        inline=False
    )

    embed.add_field(
        name="📋 What to do next:",
        value="Copy the code and send it in your **GetZenith ticket**\n🔐 We'll generate firmware tied to your unique board ID.",
        inline=False
    )

    embed.add_field(
        name="🎥 Video Tutorial",
        value="[Click here to watch the video](https://www.youtube.com/watch?v=gl-eL0z3Bmc)",
        inline=False
    )

    embed.set_footer(text="GetZenith Team • All rights reserved")
    embed.set_author(name="GetZenith", icon_url="attachment://logo.png")

    file = discord.File("logo.png", filename="logo.png")
    await ctx.send(file=file, embed=embed)

if __name__ == "__main__":
    keep_alive()  # Avvia il server Flask
    TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
