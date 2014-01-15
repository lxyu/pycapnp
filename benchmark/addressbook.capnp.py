import capnp
import addressbook_capnp as addressbook


def writeAddressBook():
    addressBook = addressbook.AddressBook.new_message()
    people = addressBook.init('people', 2)

    alice = people[0]
    alice.id = 123
    alice.name = 'Alice'
    alice.email = 'alice@example.com'
    alicePhones = alice.init('phones', 1)
    alicePhones[0].number = "555-1212"
    alicePhones[0].type = 'mobile'

    bob = people[1]
    bob.id = 456
    bob.name = 'Bob'
    bob.email = 'bob@example.com'
    bobPhones = bob.init('phones', 2)
    bobPhones[0].number = "555-4567"
    bobPhones[0].type = 'home'
    bobPhones[1].number = "555-7654"
    bobPhones[1].type = 'work'

    msg_bytes = addressBook.to_bytes()
    return msg_bytes


def printAddressBook(msg_bytes):
    addressbook.AddressBook.from_bytes(msg_bytes)


if __name__ == '__main__':
    import time
    t1 = time.time()
    for i in range(10000):
        msg_bytes = writeAddressBook()
        printAddressBook(msg_bytes)
    t2 = time.time()
    print(t2-t1)
