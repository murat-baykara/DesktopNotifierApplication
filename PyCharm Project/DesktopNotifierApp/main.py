import asyncio
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

async def main():
    await notifier.send(title="Hello Murat!", message="My dear wife is the most beautiful in the world!")

asyncio.run(main())
