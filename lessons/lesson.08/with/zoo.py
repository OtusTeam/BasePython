from dataclasses import dataclass
from typing import List
from animals import Bear

@dataclass
class Zoo:

    animals: List[Bear]