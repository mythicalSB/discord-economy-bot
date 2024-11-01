import os

def load_commands(bot):
    for file in os.listdir("Commands"):
        if file.endswith(".py"):
            bot.load_extension(f"Commands.{file[:-3]}")
