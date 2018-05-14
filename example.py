import asyncio
import aiohttp

from pyfamilyhublocal import FamilyHubCam

async def main():
    async with aiohttp.ClientSession() as session:
        api = FamilyHubCam('192.168.1.14', loop, session)
        image = await api.async_get_cam_image()

        with open("camtest.jpeg", "wb") as f:
                    f.write(image)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
