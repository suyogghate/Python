'''
Asynchronous I/O, or async for short, is a programming pattern 
that allows for high-performance I/O operations in a concurrent 
and non-blocking manner. In Python, async programming is achieved 
through the use of the asyncio module and asynchronous functions.
'''

# import asyncio

# async def my_async_function():
    # asynchronous code here
    # await asyncio.sleep(1)
    # return "Hello, Async World!"

# async def main():
#     result = await my_async_function()
#     print(result)

# async def main():
#     L = await asyncio.gather(
#             my_async_function(),
#             my_async_function(),
#             my_async_function(),
#         )
#     print(L)

# asyncio.run(main())

# ---------------------------------------------------------------

import time
import asyncio 
import requests


async def function1():
  print("func 1") 
  URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
  response = requests.get(URL)
  open("instagram.ico", "wb").write(response.content)
   
  return "Harry"
  
async def function2():
  print("func 2") 
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram2.jpg", "wb").write(response.content)
  
async def function3():
  print("func 3")
  URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram3.ico", "wb").write(response.content)

async def main():
  await function1()
  await function2()
  await function3()
  return 3
  L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
  print(L)
  # task = asyncio.create_task(function1())
  # # await function1()
  # await function2()
  # await function3()

asyncio.run(main())