from models.models import Sheep
from typing import Dict, List

class SheepDB:
    def __init__(self):
        self.sheep_data: Dict[int, Sheep] = {}

    def get_sheep(self, sheep_id: int) -> Sheep:
        return self.sheep_data.get(sheep_id)

    def add_sheep(self, sheep: Sheep) -> Sheep:
    # Check if the sheep ID already exists
        if sheep.id in self.sheep_data:
            raise ValueError("Sheep with this ID already exists")
    # Add the new sheep to the database
        self.sheep_data[sheep.id] = sheep
        return sheep
    def delete_sheep(self, sheep_id: int) -> bool:
    # Check if the sheep ID exists
        if sheep_id not in self.sheep_data:
            return False
    # Delete the sheep from the database
        del self.sheep_data[sheep_id]
        return True

    def get_all_sheep(self) -> List[Sheep]:
        return list(self.sheep_data.values())

    def update_sheep(self, sheep_id: int, sheep: Sheep) -> Sheep:
        # Check if the sheep ID exists
        if sheep_id not in self.sheep_data:
            return None
        # Update the sheep in the database
        self.sheep_data[sheep_id] = sheep
        return sheep

db = SheepDB()
db.sheep_data = {
    1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe"),
    2: Sheep(id=2, name="Shaun", breed="Suffolk", sex="ram"),
    3: Sheep(id=3, name="Lamb Chop", breed="Dorset", sex="ewe"),
    4: Sheep(id=4, name="Woolly", breed="Romney", sex="ram"),
    5: Sheep(id=5, name="Fluffy", breed="Hampshire", sex="ewe"),
    6: Sheep(id=6, name="Baa Baa", breed="Texel", sex="ram")
}

