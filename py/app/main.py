from fastapi import FastAPI
from data_generator import DataGenerator
from azdo import AzdoHttpClient

app = FastAPI()
data = DataGenerator()
client = AzdoHttpClient()


@app.get("/workitems/{work_item_id}")
async def read_root(work_item_id: int):
    resp = await client.get_work_item(work_item_id)
    return resp.text


# if __name__ == "__main__":

#     async def main():
#         result = await client.get_work_item(1)
#         print("Async task result:", result.text)

#     asyncio.run(main())
