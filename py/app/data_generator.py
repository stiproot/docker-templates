import random
from typing import Union, Optional


class DataGenerator:
    def generate(
        self,
        min: Optional[int] = 1,
        max: Optional[int] = 100,
        total: Optional[int] = 100,
    ) -> list[dict[str, int]]:
        return [{"id": random.randint(min, max)} for _ in range(total)]
