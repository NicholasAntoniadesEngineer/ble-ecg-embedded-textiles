"""
Notifications
-------------
Example showing how to add notifications to a characteristic and handle the responses.
Updated on 2019-07-03 by hbldh <henrik.blidh@gmail.com>
"""

import sys
import asyncio
import platform

from bleak import BleakClient


# you can change these to match your device or override them from the command line
#CHARACTERISTIC_UUID = "18424398-7cbc-11e9-8f9e-2a86e4085a59"
CHARACTERISTIC_UUID = "15005991-B131-3396-014C-664C9867B917"
ADDRESS = (
    "CC:86:EC:65:E4:E9"
)


def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    print("{0}: {1}".format(sender, data))


async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")

        await client.start_notify(char_uuid, notification_handler)
        await asyncio.sleep(5.0)
        await client.stop_notify(char_uuid)


if __name__ == "__main__":
    asyncio.run(
        main(
            sys.argv[1] if len(sys.argv) > 1 else ADDRESS,
            sys.argv[2] if len(sys.argv) > 2 else CHARACTERISTIC_UUID,
        )
    )

