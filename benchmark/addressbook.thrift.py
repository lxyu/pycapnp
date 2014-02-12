from thriftpy.utils import serialize, deserialize

import addressbook_thrift as addressbook


def writeAddressBook():
    alice = addressbook.Person()
    alice.id = 123
    alice.name = 'Alice'
    alice.email = 'alice@example.com'
    alice_phone = addressbook.PhoneNumber()
    alice_phone.number = '555-1212'
    alice_phone.type = addressbook.PhoneType.MOBILE
    alice.phones = [alice_phone]

    bob = addressbook.Person()
    bob.id = 456
    bob.name = 'Bob'
    bob.email = 'bob@example.com'
    bob_phone1 = addressbook.PhoneNumber()
    bob_phone1.number = '555-4567'
    bob_phone1.type = addressbook.PhoneType.HOME
    bob_phone2 = addressbook.PhoneNumber()
    bob_phone2.number = "555-7654"
    bob_phone2.type = addressbook.PhoneType.WORK
    bob.phones = [bob_phone1, bob_phone2]

    addressBook = addressbook.AddressBook()
    addressBook.people = [alice, bob]
    message_string = serialize(addressBook)
    return message_string


def printAddressBook(message_string):
    addressBook = addressbook.AddressBook()
    return deserialize(addressBook, message_string)


if __name__ == '__main__':
    import time
    t1 = time.time()
    for i in range(10000):
        message_string = writeAddressBook()
        printAddressBook(message_string)
    t2 = time.time()
    print(t2-t1)
