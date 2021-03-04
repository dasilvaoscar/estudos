import asyncio
import aiohttp
import time


websites = """https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/￼

 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/
 https://oscarsilvaofficial.herokuapp.com/"""


async def get(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                resp = await response.read()
                print("Successfully got url {} with response of length {}.".format(url, len(resp)))
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


async def main(urls, amount):
    ret = await asyncio.gather(*[get(url) for url in urls])
    print("Finalized all. ret is a list of len {} outputs.".format(len(ret)))


urls = websites.split("\n")
amount = len(urls)

start = time.time()
asyncio.run(main(urls, amount))
end = time.time()

print("Took {} seconds to pull {} websites.".format(end - start, amount))