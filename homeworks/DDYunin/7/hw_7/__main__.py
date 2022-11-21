import aiohttp
import asyncio
import time
import httpx
from hw_7.parser import start_parsing

# _url = 'https://jsonplaceholder.typicode.com/users/{0}'

# async def get_response(url: str):
#     async with httpx.AsyncClient() as client:
#         resp = await client.get(url)
#         print(resp.json())
#         print()
#         resp.raise_for_status()
#         return resp

# async def main():
#     await start_parsing()
    # result = await asyncio.gather(*[
    #     get_response(_url.format(number))
    #     for number in list(range(1, 10))
    # ])
    
    # for index in result:
    #     print(index)

# if __name__ == '__main__':
#     start = time.monotonic()
#     loop = asyncio.new_event_loop()
#     loop.run_until_complete(main())
#     loop.close()
#     print('It took', time.monotonic() - start)