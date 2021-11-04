"""Python API for accessing information from Samsung FamilyHub fridges locally."""
import asyncio
import logging
import json
import io

import aiohttp
import async_timeout
from PIL import Image


_LOGGER = logging.getLogger(__name__)
_SERVER_PATH = '.krate/owner/share/scloud'
_PORT = '17654'


class FamilyHubCam(object):
    """A class for handling information from Samsung FamilyHub fridges locally."""

    def __init__(self, ip_address, loop, session):
        """Initialize the data retrieval."""
        self._loop = loop
        self._session = session
        self.host = 'http://{}:{}/{}'.format(ip_address, _PORT, _SERVER_PATH)
        self.data = {}

    async def async_get_cam_image(self):

        glazeCameraInfo = await self._get_cam_info()

        images = await self._get_images(glazeCameraInfo['GlazeURL'])
        print(images)
        pil_images = list(map(Image.open, images))

        widths, heights = zip(*(i.size for i in pil_images))
        max_width = max(widths)
        total_height = sum(heights)

        output_image = Image.new('RGB', (max_width, total_height))

        offset = 0
        for im in pil_images:
          output_image.paste(im, (0, offset))
          offset += im.size[1]

        output_image_bytes = io.BytesIO()
        output_image.save(output_image_bytes, format='JPEG')

        return output_image_bytes.getvalue()

    async def _get_cam_info (self):
        async with async_timeout.timeout(5):
            url = '{}{}'.format(self.host, '/glazeCameraInfo.txt')
            response = await self._session.get(url)

        _LOGGER.debug("Response from fridge: %s", response.status)
        data = json.loads(await response.read())
        _LOGGER.debug(data)
        return data

    async def _get_images (self, image_urls):
        camera_images = []
        for camera in image_urls:
            url = '{}{}'.format(self.host, camera)
            print('getting ' + url)
            image = await self._session.get(url)
            image_data = await image.read()
            camera_images.append(io.BytesIO(image_data))
        return camera_images
