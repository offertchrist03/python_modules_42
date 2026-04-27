#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.rank: int = 0
        self.storage: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def _store(self, data: Any) -> None:
        if not data:
            return
        new_data: tuple[int, str] = (self.rank, str(data))
        self.storage.append(new_data)
        self.rank += 1

    def output(self) -> tuple[int, str]:
        oldest: tuple[int, str] = self.storage.pop(0)
        return oldest


NumericType = int | float
NumericProcessorType = int | float | list[int] | list[float]


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, (int, float)):
                return True
            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, (int, float)):
                        raise Exception()
                return True
            return False
        except Exception:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


TextProcessorType = str | list[str]


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, str):
                return True
            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, str):
                        raise Exception()
                return True
            return False
        except Exception:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper text data")
        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


LogProcessorType = dict[str, str] | list[dict[str, str]]


def is_dict_str(data: Any) -> bool:
    try:
        if not isinstance(data, dict):
            return False
        for item in data.keys():
            if not isinstance(item, str):
                return False
        for item in data.values():
            if not isinstance(item, str):
                return False
        return True
    except Exception:
        return False


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, dict):
                return is_dict_str(data)
            if isinstance(data, list):
                for item in data:
                    return is_dict_str(item)
            return False
        except Exception:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper log data")
        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


def extracts(
        instance: DataProcessor,
        n: int,
        label: str,
        visible: bool = True) -> None:
    try:
        if visible:
            print(f"Extracting {n} values...")
        if isinstance(instance, LogProcessor):
            for _ in range(n):
                extracted: tuple[int, str] = instance.output()
                data: list[str] = extracted[1][1:-1].split(",")
                if visible:
                    print(
                        (f"{label} {extracted[0]}: "
                         f"{data[0].split(": ")[1][1:-1]}: "
                         f"{data[1].split(": ")[1][1:-1]}")
                    )
        else:
            for _ in range(n):
                extracted = instance.output()
                if visible:
                    print(f"{label} {extracted[0]}: {extracted[1]}")
    except Exception as err:
        print(f"Error : {err}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ==\n")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    try:
        print(f"Trying to validate input '42': {numeric.validate(42)}")
        print(f"Trying to validate input 'hello': {numeric.validate('hello')}")
    except Exception as err:
        print(f"Error : {err}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except Exception as err:
        print(err)

    print("Processing data: [1, 2, 3, 4, 5]")
    try:
        numeric.ingest([1, 2, 3, 4, 5])
        extracts(numeric, 3, "Numeric value")
    except Exception as err:
        print(err)
    print()

    print("Testing Text Processor...")
    text = TextProcessor()
    try:
        print(f"Trying to validate input '42': {text.validate(42)}")
    except Exception as err:
        print(f"Error : {err}")

    print("Processing data: ['Hello', 'Nexus', 'World']")
    try:
        text.ingest(['Hello', 'Nexus', 'World'])
        extracts(text, 1, "Text value")
    except Exception as err:
        print(err)
    print()

    print("Testing Log Processor...")
    log = LogProcessor()
    try:
        print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
        print(
            ("Trying to validate input '{0: \"warning\"}': "
             f"{log.validate({0: "warning"})}")
        )
        print(
            ("Trying to validate input '{\"info\": 42}': "
             f"{log.validate({"info": 42})}")
        )
        print(
            ("Trying to validate input '{\"info\": \"warning\"}': "
             f"{log.validate({"info": "warning"})}")
        )
    except Exception as err:
        print(f"Error: {err}")

    try:
        log.ingest(
            [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
             {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
        )
        extracts(log, 2, "Log entry")
    except Exception as err:
        print(err)
