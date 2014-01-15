from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

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
    transport = TTransport.TMemoryBuffer()
    protocol = TBinaryProtocol.TBinaryProtocolAccelerated(transport)
    addressBook.write(protocol)
    message_string = transport.getvalue()
    return message_string


def printAddressBook(message_string):
    addressBook = addressbook.AddressBook()
    transport = TTransport.TMemoryBuffer(message_string)
    protocol = TBinaryProtocol.TBinaryProtocolAccelerated(transport)
    addressBook.read(protocol)


if __name__ == '__main__':
    import time
    t1 = time.time()
    for i in range(10000):
        message_string = writeAddressBook()
        printAddressBook(message_string)
    t2 = time.time()
    print(t2-t1)
