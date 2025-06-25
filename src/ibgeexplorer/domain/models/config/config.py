from dataclasses import dataclass
from typing import Type, TypeVar

T = TypeVar("T", bound="Settings")


@dataclass
class Settings:
    api: str

    @classmethod
    def from_json(cls: Type[T], data: dict) -> T:
        return cls(api=data["api"])
