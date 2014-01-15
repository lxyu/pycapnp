import addressbook_pb2 as addressbook


def writeAddressBook():
    addressBook = addressbook.AddressBook()

    alice = addressBook.person.add()
    alice.id = 123
    alice.name = 'Alice'
    alice.email = 'alice@example.com'
    alicePhones = [alice.phone.add()]
    alicePhones[0].number = "555-1212"
    alicePhones[0].type = addressbook.Person.MOBILE

    bob = addressBook.person.add()
    bob.id = 456
    bob.name = 'Bob'
    bob.email = 'bob@example.com'
    bobPhones = [bob.phone.add(), bob.phone.add()]
    bobPhones[0].number = "555-4567"
    bobPhones[0].type = addressbook.Person.HOME
    bobPhones[1].number = "555-7654"
    bobPhones[1].type = addressbook.Person.WORK

    message_string = addressBook.SerializeToString()
    return message_string


def printAddressBook(message_string):
    addressBook = addressbook.AddressBook()
    addressBook.ParseFromString(message_string)


if __name__ == '__main__':
    import time
    t1 = time.time()
    for i in range(10000):
        message_string = writeAddressBook()
        printAddressBook(message_string)
    t2 = time.time()
    print(t2-t1)
