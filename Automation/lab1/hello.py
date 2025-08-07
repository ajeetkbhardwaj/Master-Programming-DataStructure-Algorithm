import asyncio
def greet(name):
    return f"Hello, {name}!"

async def hello_asynch():
    await asyncio.sleep(1)
    print('Hello, World!')

async def test():
    print("Starting")
    await asyncio.sleep(1)
    print("ending")
