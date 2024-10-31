import asyncio

async def start_strongman(name, power):
    num_balls = 5
    print(f'Силач {name} начал соревнования.')
    for i_ball in range(1, 1 + num_balls):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i_ball}')
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    t1 = asyncio.create_task(start_strongman('Pasha', 3))
    t2 = asyncio.create_task(start_strongman('Denis', 4))
    t3 = asyncio.create_task(start_strongman('Apollon', 5))
    await t1
    await t2
    await t3

asyncio.run(start_tournament())



