from unittest import mock


class Foo:
    @property
    def bar(self):
        return "bar"


with mock.patch("__main__.Foo.bar", new_callable=mock.PropertyMock(return_value="barbar")) as foo_mock:
    foo = Foo()
    print(foo.bar)


print(foo.bar)

