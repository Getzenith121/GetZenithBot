import discord
import os
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

app = Flask('')

@app.route('/')
def home():
    return "Bot attivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@client.event
async def on_ready():
    print(f"✅ Bot connesso come {client.user}")

@client.event
async def on_message(message):
    print(f"Messaggio ricevuto: {message.content}")

    if message.author == client.user:
        return

    if message.content.lower() == "!ping":
        await message.channel.send("🏓 Pong!")

    if message.content.lower().strip() == "!paypal":
        await message.channel.send("💳 PayPal: @ZenithDMADMA (Friends and family)")

@bot.command()
async def dna(ctx):
    try:
        await ctx.send(file=discord.File('dna_id_.mp4'))
    except Exception as e:
        await ctx.send(f"Errore nell'inviare il video: {e}")

if __name__ == "__main__":
    keep_alive()  # Avvia il server Flask (obbligatorio per Render)
    TOKEN = os.getenv("DISCORD_TOKEN")  # Prende il token da Render
    client.run(TOKEN)

