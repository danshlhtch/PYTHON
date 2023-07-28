import python_weather
import asyncio
import os


async def getweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Минск')
        celsius = (weather.current.temperature - 32) / 1.8
        print(str(round(celsius)))
        local = (weather.current.kind)
        print(local)
        print(weather.nearest_area)


if __name__ == '__main__':

    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())