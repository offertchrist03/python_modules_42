#!/usr/bin/env python3

from enum import Enum
from datetime import datetime
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except Exception as err:
    print(f"Error: {err}")
    print("Run: pip install pydantic")
    exit(1)


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


contact = ContactType


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: contact = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str = Field(default="", max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def id_rules(self) -> "AlienContact":
        if not self.contact_id.startswith('AC'):
            raise ValueError("Contact ID must start with \"AC\"")
        return self

    @model_validator(mode="after")
    def physical_contact_rules(self) -> "AlienContact":
        if (self.contact_type == ContactType.physical
                and (not self.is_verified)):
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode="after")
    def telepathic_contact_rules(self) -> "AlienContact":
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        return self

    @model_validator(mode="after")
    def signal_rules(self) -> "AlienContact":
        if (self.signal_strength > 7.0
                and (not self.message_received)):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self

    def display(self) -> None:
        print("Valid contact report:")
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type.name}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        print(f"Message: '{self.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")

    print('=' * 40)
    try:
        first_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-01-01"),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received='Greetings from Zeta Reticuli')
        first_contact.display()
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            msg = error['msg']
            print(f"{msg}")

    print()
    print('=' * 40)
    try:  # id error
        second_contact = AlienContact(
            contact_id="AC_2024_0018888888",
            timestamp=datetime.fromisoformat("2026-01-01"),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received='Greetings from Zeta Reticuli')
        second_contact.display()
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            err_txt = str(error['msg'][13:]
                          if error['msg'].startswith('Value error, ')
                          else error['msg'])
            msg = f"{err_txt}"
            print(f"{msg}")

    print()
    print('=' * 40)
    try:  # physical error
        second_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-01-01"),
            location="Area 51, Nevada",
            contact_type=ContactType.physical,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received='Greetings from Zeta Reticuli')
        second_contact.display()
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            err_txt = str(error['msg'][13:]
                          if error['msg'].startswith('Value error, ')
                          else error['msg'])
            msg = f"{err_txt}"
            print(f"{msg}")

    print()
    print('=' * 40)
    try:  # telepathic error
        second_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-01-01"),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received='Greetings from Zeta Reticuli')
        second_contact.display()
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            err_txt = str(error['msg'][13:]
                          if error['msg'].startswith('Value error, ')
                          else error['msg'])
            msg = f"{err_txt}"
            print(f"{msg}")

    print()
    print('=' * 40)
    try:  # signal error
        second_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-01-01"),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2)
        second_contact.display()
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            err_txt = str(error['msg'][13:]
                          if error['msg'].startswith('Value error, ')
                          else error['msg'])
            msg = f"{err_txt}"
            print(f"{msg}")


if __name__ == "__main__":
    main()
