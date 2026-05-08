#!/usr/bin/env python3

from pydantic import BaseModel, Field, PastDatetime, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: PastDatetime | str = Field()
    is_operational: bool = Field()
    notes: str = Field(default="", max_length=200)

    def display_status(self) -> None:
        try:
            print("Valid station created:")
            print(f"ID : {self.station_id}")
            print(f"Name : {self.name}")
            print(f"Crew : {self.crew_size} people")
            print(f"Power : {self.power_level}%")
            print(f"Oxygen : {self.oxygen_level}%")
            print(f"Status : {"Operational"
                              if self.is_operational
                              else "Not operational"}")
            if self.notes:
                print(f"Notes : {self.notes}")
        except Exception as err:
            print(f"Exception Error: {err}")


def main() -> None:
    print("Space Station Data Validation")
    print(f"{"=" * 40}")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2023-10-15T08:30:00",
            is_operational=True,
            notes="")
        station.display_status()
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            field = error['loc'][0]
            msg = error['msg']
            print(f"{field}: {msg}")
    except Exception as err:
        print(f"Exception Error: {err}")

    print()
    print(f"{"=" * 40}")
    try:
        failed_station = SpaceStation(
            station_id="SS-HA",
            name="Dark Void",
            crew_size=50,
            power_level=100.0,
            oxygen_level=50.0,
            last_maintenance="2026-01-01T00:00:00",
            is_operational=False
        )
        failed_station.display_status()
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            msg = error['msg']
            print(f"{msg}")
    except Exception as err:
        print(f"Exception Error: {err}")


if __name__ == "__main__":
    main()
