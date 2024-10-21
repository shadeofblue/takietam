from dataclasses import dataclass
from typing import Optional, ClassVar

@dataclass(kw_only=True)
class Singleton:
    test: Optional[str] = None

    __instance: ClassVar = None

    def __post_init__(self):
        if self.__class__.__instance:
            raise RuntimeError("Only one instance allowed")
        self.__class__.__instance = self

    @classmethod
    def get_instance(cls, *args, **kwargs) -> "Singleton":
        if not cls.__instance:
            cls(*args, **kwargs)
        return cls.__instance

s1 = Singleton.get_instance()

s2 = Singleton.get_instance()

s1.test = "foo"

print(s2.test)
