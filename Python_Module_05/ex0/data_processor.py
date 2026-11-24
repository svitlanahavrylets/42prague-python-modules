from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data left to extract")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, int | float) and not isinstance(data, bool):
            return True

        if isinstance(data, list):
            return all(
                isinstance(x, int | float)
                and not isinstance(x, bool)
                for x in data
                )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, str(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, str(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:

        def is_valid_log(d: Any) -> bool:
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items())

        if is_valid_log(data):
            return True
        if isinstance(data, list):
            return all(is_valid_log(x) for x in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            level = d.get('log_level', 'UNKNOWN')
            message = d.get('log_message', '')
            return f"{level}: {message}"

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, format_log(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, format_log(data)))
            self._counter += 1


def data_processor():
    my_int = 42
    # my_float = 42.42
    my_str = 'Hello'
    inval_str = 'foo'
    my_data = [1, 2, 3, 4, 5]
    # my_data_float = [1, 2.5, True, "Hello"]
    my_data2 = ['Hello', 'Nexus', 'World']
    my_data3 = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
        ]
    values1 = 3
    values2 = 1
    values3 = 2
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '{my_int}': {np.validate(my_int)}")
    # print(f"Trying to validate input '{my_float}': {np.validate(my_float)}")
    print(f"Trying to validate input '{my_str}': {np.validate(my_str)}")

    print(f"Test invalid ingestion of string "
          f"'{inval_str}' without prior validation:")
    try:
        np.ingest(inval_str)
    except ValueError as e:
        print(f"Got exception: {e}")

    print(f"Processing data: {my_data}")
    np.ingest(my_data)
    print(f"Extracting {values1} values...")
    for _ in range(values1):
        rank, val = np.output()
        print(f"Numeric value {rank}: {val}")
    print()

    print("Testing Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '{my_int}': {tp.validate(my_int)}")
    # print(f"Trying to validate input '{my_float}': {tp.validate(my_float)}")

    print(f"Processing data: {my_data2}")
    tp.ingest(my_data2)
    print(f"Extracting {values2} values...")
    for _ in range(values2):
        rank, val = tp.output()
        print(f"Text value {rank}: {val}")
    print()

    print("Testing Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input '{my_int}': {lp.validate(my_int)}")
    # print(f"Trying to validate input '{my_float}': {tp.validate(my_float)}")

    print(f"Processing data: {my_data3}")
    lp.ingest(my_data3)
    print(f"Extracting {values3} values...")
    for _ in range(values3):
        rank, val = lp.output()
        print(f"Log value {rank}: {val}")


if __name__ == "__main__":
    data_processor()
