# main.py
import os
import discord
from files import Board
from dotenv import load_dotenv

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

    if message.content == '$print':
        board = Board.Board()
        print_board = board.print_board()
        await message.channel.send(print_board)


client.run(TOKEN)

