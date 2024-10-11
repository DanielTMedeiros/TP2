import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    urls = [
        'https://api.jikan.moe/v4/anime/7', 
        'https://api.jikan.moe/v4/anime/91',  
        'https://api.jikan.moe/v4/anime/24' 
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(f"Nome: {result['data']['title']}")
            print(f"Episódios: {result['data']['episodes']}")
            print(f"Status: {result['data']['status']}")
            print(f"Nota: {result['data']['score']}\n")

if __name__ == "__main__":
    asyncio.run(main())
