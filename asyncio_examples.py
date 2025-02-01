import asyncio
import random

async def add(a, b):
 return a + b

# add(1, 1) # <coroutine object add at 0x77344e554e80>
asyncio.run(add(1, 1))



async def db_get():
  await asyncio.sleep(0.5)
  return random.randint(1,10)

asyncio.run(db_get())



async def process_data():
  # Najpierw trzeba poczekać na pierwszy wynik, potem na drugi:
  a = await db_get()
  b = await db_get()
  return a * b

asyncio.run(process_data())


async def process_data_faster():
  # Czekanie na dwa db_get odbywa się równolegle
  a, b = await asyncio.gather(db_get(), db_get())
  return a * b

asyncio.run(process_data_faster())



loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.gather(db_get(), db_get()))



def some_function_with_callback(callback):
  retult = 123  # result of some calculation
  if asyncio.iscoroutinefunction(callback):
    asyncio.run(callback(retult))
  else:
    callback(retult)
