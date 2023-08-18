import httpx
import asyncio
from typing import Optional


class HttpClient:
    async def get(self, url: str, headers: Optional[dict[str, str]] = None):
        hdrs: dict[str, str] = self.build_headers(headers)
        url: str = self.build_url(url)
        async with self.create_client() as client:
            return await client.get(url, headers=hdrs)

    def build_url(self, url: str) -> str:
        return url

    def build_headers(self, headers: Optional[dict[str, str]] = None) -> dict[str, str]:
        return {
            "Authorization": "Basic <<pat>>",
            # "Content-Type": "application/json",
        }

    def create_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(verify=False)
