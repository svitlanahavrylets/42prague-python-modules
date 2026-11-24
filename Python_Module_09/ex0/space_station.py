from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional
import json


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        is_operational=True,
        notes="All systems nominal",
    )
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")
    print(f"Crew: {valid_station.crew_size}")
    print(f"Power: {valid_station.power_level}")
    print(f"Oxygen: {valid_station.oxygen_level}")
    status = "Operational" if valid_station.is_operational else "Offline"
    print(f"Status: {status}\n")


    try:
        with open("generated_data/space_stations.json", "r") as f:
            data = json.load(f)
            if data and isinstance(data, list):
                station_from_file = SpaceStation.model_validate(data[0])
                print(f"Loaded from generated JSON: {station_from_file.name}")
    except (FileNotFoundError, IndexError, ValidationError):
        pass


    print("========================================")
    print("Expected validation error:")

    try:
        SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="All systems nominal",
        )
    except ValidationError as ex:
        print(ex.errors()[0]['msg'])


if __name__ == "__main__":
    main()
