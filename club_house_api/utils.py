import aiohttp 
import aiofiles
import asyncio
from club_house_api import ClubHouse, ClubHouseApiMethod
from typing import Optional, Any, Callable

async def file_sender(file_name:Optional[str]=None):
    async with aiofiles.open(file_name, 'rb') as f:
        chunk = await f.read(64 * 1024)
        while chunk:
            yield chunk
            chunk = await f.read(64 * 1024)

class MockedClient():
    def __init__(self, return_value: Optional[Any] = None, callback: Optional[Callable] = None):
        super().__init__()
        self.return_value = return_value
        self.callback = callback or (lambda data: None)

    async def method(self, request:str, args:Optional[list], values:Optional[dict]):
        return self.return_value or self.callback(locals())


def with_mocked_api(return_value: Any):
    """ 
    Just changes http standard api client to mocked client which returns return_value
    """
    def decorator(func: Any):
        async def wrapper(*args, **kwargs):
            cl = ClubHouse("token", 'v3') 
            api = cl.get_api()
            api._clubhouse = MockedClient(return_value)
            return await func(*args, **kwargs, ch_api=api)
        return wrapper
    return decorator
