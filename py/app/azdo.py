from http_client import HttpClient


class AzdoUrlBuilder:
    def __init__(self):
        self._base_url = "https://dev.azure.com/Derivco/Software/_apis/wit/workitems/"
        self._api_version = "api-version=7.0"

    def build_get_url(self, work_item_id: int) -> str:
        return f"{self._base_url}{work_item_id}?$expand=all&{self._api_version}"


class AzdoHttpClient:
    def __init__(self):
        self.client = HttpClient()
        self.url_builder = AzdoUrlBuilder()

    async def get_work_item(self, work_item_id: int):
        url = self.url_builder.build_get_url(work_item_id)
        print(url)
        return await self.client.get(url=url)
