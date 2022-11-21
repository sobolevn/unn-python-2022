import httpx
import asyncio
from loguru import logger

async def func(index):
	logger.debug("connect: {0}".format(index))
	async with httpx.AsyncClient() as client:
		http = await client.get('https://www.example.com/');
		logger.debug("sucsess: {0}".format(index))

	return "ok"+str(index);

async def main():
	q = asyncio.Queue()

	task_list = []
	for i in range(10):
		task = asyncio.create_task(func(i))
		task_list.append(task)

	await q.join()
	await asyncio.gather(*task_list,return_exceptions=True)

	return list(i.result() for i in task_list)

async def main2():

	rezult = await asyncio.gather(*[func(i) for i in range(10)],return_exceptions=True)

	print(rezult)
	print(rezult)

async def fuck():
	await main2()
	return 1
	#main()

print(asyncio.run(fuck()))

'''async def my_sleep():
	print("my sleep start")
	await asyncio.sleep(2)
	print("my sleep end")

async def main():
	print("sleep now")
	await my_sleep();
	print("Ok, wake up")

asyncio.run(main())'''


'''
async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.com/')
        print(response)

asyncio.run(main())'''