import abc


class Meta(type):
    @property
    def spam(cls):
        return 'Spam property of %r' % cls

    def eggs(self):
        return 'Eggs method of %r' % self


class Some(object, metaclass=Meta):
        def __init__(self):
            self.spam = 3

        def eggs(self):
            print("Eggs")


class Spam(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self):
        raise NotImplemented


class Eggs(Spam):
    def run(self):
        pass


class CustomList(abc.ABC):
    'This class implements a list like interface'
    pass



if __name__ == "__main__":
    some = Some()
    print(some.spam)
    print(some.eggs())
    print(Some.spam)
    f=Eggs()
    CustomList.register(list)
    ls = CustomList()
    print(issubclass(list, CustomList))
    print(dir(CustomList))



