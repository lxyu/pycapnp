enum PhoneType {
    MOBILE,
    HOME,
    WORK,
}

struct PhoneNumber {
    1: optional string number,
    2: optional PhoneType type,
}

struct Person {
    1: optional i32 id,
    2: optional string name,
    3: optional string email,
    4: optional list<PhoneNumber> phones,
}

struct AddressBook {
    1: optional list<Person> people,
}
