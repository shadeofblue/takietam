
class Singleton:
    dupa = {}

    def __init__(self):
        raise NotImplementedError(f"{__class__.__name__} cannot be instantiated")

    @classmethod
    def set(cls, name, value):
        cls.dupa[name] = value

    @classmethod
    def get(cls, name):
        return cls.dupa.get(name)

print(Singleton.get("aaa"))
Singleton.set("aaa", 123)
print(Singleton.get("aaa"))
Singleton.set("aaa", 333)
print(Singleton.get("aaa"))
