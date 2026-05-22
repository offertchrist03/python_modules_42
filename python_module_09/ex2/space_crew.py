#!/usr/bin/env python3

from typing import Any
from datetime import datetime
from enum import Enum
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except Exception as err:
    print(f"Error: {err}")
    print("Run: pip install pydantic")
    exit(1)


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


rank_type = Rank


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: rank_type = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_rule(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")

        leaders = [leader
                   for leader in self.crew
                   if (leader.rank == Rank.commander
                       or leader.rank == Rank.captain)]
        if not (len(self.crew) > 0 and len(leaders) > 0):
            raise ValueError("Must have at least one Commander or Captain")

        seniors = [senior
                   for senior in self.crew
                   if (senior.years_experience >= 5)]
        if (self.duration_days > 365
                and (not (len(seniors) / len(self.crew)) >= (1/2))):
            raise ValueError(("Long missions (> 365 days) "
                              "need 50% experienced crew (5+ years)"))

        inactives = [crew
                     for crew in self.crew
                     if (not crew.is_active)]
        if len(inactives) > 0:
            raise ValueError("All crew members must be active")

        return self

    def display(self) -> None:
        print("Valid mission created:")
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for crew in self.crew:
            print(f"- {crew.name} ({crew.rank.name}) - {crew.specialization}")


def parse_digit(data: Any) -> bool:
    if isinstance(data, (int, float)):
        return True
    return False


def main() -> None:
    # 12 crew members
    alice = CrewMember(member_id="C001", name="Alice", rank=Rank.commander,
                       age=40, specialization="Navigation",
                       years_experience=10)
    bob = CrewMember(member_id="C002", name="Bob", rank=Rank.captain,
                     age=35, specialization="Pilot",
                     years_experience=8)
    charlie = CrewMember(member_id="C003", name="Charlie", rank=Rank.officer,
                         age=30, specialization="Engineering",
                         years_experience=6)
    dana = CrewMember(member_id="C004", name="Dana", rank=Rank.lieutenant,
                      age=28, specialization="Science",
                      years_experience=5)
    eve = CrewMember(member_id="C005", name="Eve", rank=Rank.cadet,
                     age=25, specialization="Medical",
                     years_experience=2)
    frank = CrewMember(member_id="C006", name="Frank", rank=Rank.officer,
                       age=32, specialization="Engineering",
                       years_experience=7)
    grace = CrewMember(member_id="C007", name="Grace", rank=Rank.lieutenant,
                       age=29, specialization="Pilot",
                       years_experience=4)
    hank = CrewMember(member_id="C008", name="Hank", rank=Rank.cadet,
                      age=22, specialization="Science",
                      years_experience=1)
    ivy = CrewMember(member_id="C009", name="Ivy", rank=Rank.officer,
                     age=34, specialization="Medical",
                     years_experience=9)
    jack = CrewMember(member_id="C010", name="Jack", rank=Rank.lieutenant,
                      age=27, specialization="Navigation",
                      years_experience=3)
    kate = CrewMember(member_id="C011", name="Kate", rank=Rank.cadet,
                      age=23, specialization="Engineering",
                      years_experience=0)
    leo = CrewMember(member_id="C012", name="Leo", rank=Rank.officer,
                     age=31, specialization="Science",
                     years_experience=5)
    katy = CrewMember(member_id="C013", name="Katy", rank=Rank.officer,
                      age=28, specialization="Science",
                      years_experience=4)

    data_crew = [alice, bob, charlie, dana, eve,
                 frank, grace, hank, ivy, jack, kate, leo]

    inexperienced_crew = [eve, grace, hank, ivy, alice]

    invalid_crew = data_crew[:11] + [
        CrewMember(member_id="C013", name="Inactive",
                   rank=Rank.officer, age=29, specialization="Science",
                   years_experience=6, is_active=False)]

    # 5 missions
    missions_data = [
        # Valid mission
        {
            "mission_id": "M10001",
            "mission_name": "Mars Exploration",
            "destination": "Mars",
            "launch_date": datetime(2030, 5, 1),
            "duration_days": 400,  # long mission
            "crew": data_crew,
            "budget_millions": 5000.0
        },
        # Mission with invalid ID
        {
            "mission_id": "X20002",
            "mission_name": "Venus Expedition",
            "destination": "Venus",
            "launch_date": datetime(2031, 7, 15),
            "duration_days": 200,
            "crew": data_crew,
            "budget_millions": 3000.0
        },
        # Mission with no Captain/Commander
        {
            "mission_id": "M30003",
            "mission_name": "Jupiter Study",
            "destination": "Jupiter",
            "launch_date": datetime(2032, 3, 10),
            "duration_days": 100,
            "crew": data_crew[2:],
            "budget_millions": 4000.0
        },
        # Mission with long duration but <50% experienced crew
        {
            "mission_id": "M40004",
            "mission_name": "Saturn Survey",
            "destination": "Saturn",
            "launch_date": datetime(2033, 8, 20),
            "duration_days": 500,
            "crew": inexperienced_crew,
            "budget_millions": 6000.0
        },
        # Mission with inactive crew member
        {
            "mission_id": "M50005",
            "mission_name": "Neptune Mission",
            "destination": "Neptune",
            "launch_date": datetime(2034, 12, 5),
            "duration_days": 300,
            "crew": invalid_crew,
            "budget_millions": 7000.0
        },
        # Mission with crew > 12
        {
            "mission_id": "M",
            "mission_name": "Moon Mission" * 50,
            "destination": "Moon" * 50,
            "launch_date": datetime(2035, 12, 5),
            "duration_days": 0,
            "crew": data_crew + [katy],
            "budget_millions": 700000.0
        }
    ]

    first = True
    for data in missions_data:
        if first:
            first = False
        else:
            print()
        print("=" * 50)
        try:
            days = -1
            if isinstance(data['duration_days'], int):
                days = int(data['duration_days'])
            crew_in = []
            if isinstance(data['crew'], list):
                crew_in = [person for person in data['crew']]
            budget = -1.0
            if isinstance(data['budget_millions'], float):
                budget = float(data['budget_millions'])

            mission = SpaceMission(
                mission_id=str(data['mission_id']),
                mission_name=str(data['mission_name']),
                destination=str(data['destination']),
                launch_date=datetime.fromisoformat(str(data['launch_date'])),
                duration_days=days,
                crew=crew_in,
                budget_millions=budget
            )
            mission.display()
        except ValidationError as err:
            print("Expected validation error:")
            for error in err.errors():
                err_txt = str(error['msg'][13:]
                              if error['msg'].startswith('Value error, ')
                              else error['msg'])
                msg = f"{err_txt}"
                print(f"{msg}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    main()
