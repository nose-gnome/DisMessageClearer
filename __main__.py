from os import environ
from dotenv import load_dotenv
from discord import Client
from datetime import datetime, timedelta, timezone
from  asyncio import sleep as asleep

load_dotenv()

# Press the green button in the gutter to run the script.
client = Client()


async def auto_clear():
    channel = client.get_channel(int(environ['CHANNEL']))

    while True:
        msg = []
        time = datetime.utcnow() - timedelta(hours=environ['HOURS'], minutes=environ['MINUTES'], days=environ['DAYS'])
        await channel.purge(before=time)
        await asleep(int(environ['REFRESH']))

@client.event
async def on_ready():
    print("Logged in")
    client.loop.create_task(auto_clear())


if __name__ == '__main__':
    client.run(environ['TOKEN'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
