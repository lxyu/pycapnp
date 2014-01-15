import capnp
import addressbook_capnp as addressbook


def writeAddressBook():
    addressBook = addressbook.AddressBook.new_message()
    people = addressBook.init_resizable_list('people')

    alice = people.add()
    alice.id = 123
    alice.name = 'Alice'
    alice.email = 'alice@example.com'
    alicePhones = alice.init('phones', 1)
    alicePhones[0].number = "555-1212"
    alicePhones[0].type = 'mobile'

    bob = people.add()
    bob.id = 456
    bob.name = 'Bob'
    bob.email = 'bob@example.com'
    bobPhones = bob.init('phones', 2)
    bobPhones[0].number = "555-4567"
    bobPhones[0].type = 'home'
    bobPhones[1].number = "555-7654"
    bobPhones[1].type = 'work'

    people.finish()
    msg_bytes = addressBook.to_bytes()
    return msg_bytes


def printAddressBook(msg_bytes):
    addressBook = addressbook.AddressBook.from_bytes(msg_bytes)


if __name__ == '__main__':
    import time
    t1 = time.time()
    for i in range(10000):
        msg_bytes = writeAddressBook()
        printAddressBook(msg_bytes)
    t2 = time.time()
    print(t2-t1)
