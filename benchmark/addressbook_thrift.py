from thriftpy.thrift import TPayload, TType


class PhoneType(object):
    MOBILE = 0
    HOME = 1
    WORK = 2

    _VALUES_TO_NAMES = {
        0: "MOBILE",
        1: "HOME",
        2: "WORK",
    }

    _NAMES_TO_VALUES = {
        "MOBILE": 0,
        "HOME": 1,
        "WORK": 2,
    }


class PhoneNumber(TPayload):
    thrift_spec = {
        1: (TType.STRING, 'number', None, None),
        2: (TType.I32, 'type', None, None),
    }

    def __init__(self, number=None, type=None,):
        self.number = number
        self.type = type


class Person(TPayload):
    thrift_spec = {
        1: (TType.I32, 'id', None, None),
        2: (TType.STRING, 'name', None, None),
        3: (TType.STRING, 'email', None, None),
        4: (TType.LIST, 'phones',
            (TType.STRUCT, (PhoneNumber, PhoneNumber.thrift_spec)), None),
    }

    def __init__(self, id=None, name=None, email=None, phones=None,):
        self.id = id
        self.name = name
        self.email = email
        self.phones = phones


class AddressBook(TPayload):
    thrift_spec = {
        1: (TType.LIST, 'people',
            (TType.STRUCT, (Person, Person.thrift_spec)), None),
    }

    def __init__(self, people=None,):
        self.people = people
