#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing
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


def proc_name(proc: DataProcessor) -> str:
    name: str = type(proc).__name__
    return name


def proc_label(proc: DataProcessor) -> str:
    name: str = type(proc).__name__
    res: str = ""
    is_first = True
    for c in name:
        if (not is_first) and c.upper() == c:
            res += " "
        res += c
        is_first = False
    return res


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.processed: dict[str, int] = {}
        self.initial_len: dict[str, int] = {}
        self.total_data: int = 0

    def register_processor(self, proc: DataProcessor) -> None:
        try:
            self.processors.append(proc)
        except Exception as err:
            print(f"Error: {err}")

    def process_stream(self, stream: list[typing.Any]) -> None:
        if len(self.processors) > 0:
            for proc in self.processors:
                self.processed[proc_name(proc)] = 0
                self.initial_len[proc_name(proc)] = 0

        for item in stream:
            if isinstance(item, list):
                self.total_data += len(item)
            else:
                self.total_data += 1

        if self.total_data <= 0:
            return

        try:
            for item in stream:
                handled = False
                for proc in self.processors:
                    if proc.validate(item):
                        handled = True
                        proc.ingest(item)
                        if isinstance(item, list):
                            self.processed[proc_name(proc)] += len(item)
                        else:
                            self.processed[proc_name(proc)] += 1
                if not handled:
                    print(("DataStream error - "
                           "Can't process element in stream: "
                           f"{item}"))
            for proc in self.processors:
                self.initial_len[proc_name(proc)] = len(proc.storage)
        except Exception as err:
            print(f"{err}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if self.total_data <= 0:
            print("No processor found, no data")
            return

        for proc in self.processors:
            print(
                (f"{proc_label(proc)}: "
                 f"total {self.initial_len[proc_name(proc)]} items processed, "
                 f"remaining {len(proc.storage)} on processor")
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")

    batch: list[Any] = ['Hello world', [3.14, -1, 2.71],
                        [{'log_level': 'WARNING',
                         ' log_message': 'Telnet access! Use ssh instead'},
                        {'log_level': 'INFO',
                         'log_message': 'User wil is connected'}], 42,
                        ['Hi', 'five']]

    print("Initialize Data Stream...")
    stream: DataStream = DataStream()

    stream.print_processors_stats()
    print()

    print("Registering Numeric Processor\n")
    stream.register_processor(NumericProcessor())

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print()
    print("Registering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print()
    print(("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1"))
    for proc in stream.processors:
        n = 0
        if isinstance(proc, NumericProcessor):
            n = 3
        if isinstance(proc, TextProcessor):
            n = 2
        if isinstance(proc, LogProcessor):
            n = 1
        extracts(proc, n, "Extracted", False)
    stream.print_processors_stats()
