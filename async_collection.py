import asyncio
import aiohttp
from scraper.collect_data import DataCollection


async def get_site_content(link, session):
    async with session.get(link) as resp:
        page_html = await resp.read()

    site_content_list = await DataCollection(page_html).collect_job_details()
    return site_content_list



# asynchronicznie przejdż przez linki zbierając dane
async def get_all_site_content(links):
    actions = []
    offer_data = []

    try:
        async with aiohttp.ClientSession() as session:
            for link in links:
                actions.append(asyncio.ensure_future(get_site_content(link, session)))
            offer_res = await asyncio.gather(*actions)

            for data in offer_res:
                offer_data.append(data)

        return offer_data

    except Exception as err:
        print(f"An error ocurred: {err}")


