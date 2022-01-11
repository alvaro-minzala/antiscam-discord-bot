from discord.ext import commands
from AntiScam import AntiScam

whitelist = [] # Here you add the IDs of the users allowed to bypass the AntiScam system.
logs_channel = channel # Here you need to add the ID of the channel where the logs will be sent.

bot = commands.Bot(command_prefix='>')
bot.remove_command('help') # Remove this line if you want to use the help command.

@bot.listen()
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='muted', verified_role='verified', logs_channel=logs_channel) # Here you can change the names of the roles.

bot.run('token') #change 'token' with your bot token
