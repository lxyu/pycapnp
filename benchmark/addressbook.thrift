enum PhoneType {
    MOBILE,
    HOME,
    WORK,
}

struct PhoneNumber {
    1: required string number,
    2: optional PhoneType type,
}

struct Person {
    1: required i32 id,
    2: required string name,
    3: required string email,
    4: required list<PhoneNumber> phones,
}

struct AddressBook {
    1: required list<Person> people,
}
