from phone_book import Book, json

contact_book = Book(r"C:\Users\vishnu vardhan\PycharmProjects\pythonProject\AddressBook/book.json")
while True:
    option = int(input("Enter Choice:\n1.Display Contacts\n2.Add Contacts\n3.Update Contacts\n4.Delete Contacts\n5.Search Contacts"
                       "\n6.Exit \n"))
    if option == 1:
        contact_book.display_contacts()
    if option == 2:
        contact_book.add_contacts()
    if option == 3:
        contact_book.update_contacts()
    if option == 4:
        contact_book.delete_contacts()
    if option == 5:
        contact_book.search_Contacts()
    if option == 6:
        break

contact_list = []
for data in contact_book.person_list:
    dict1 = {"First Name": data.firstName, "LastName": data.lastName , "MobileNumber": data.mobileNumber, "State": data.State , "City": data.City, "Pincode": data.Pincode  }
    contact_list.append(dict1)


with open(r"C:\Users\vishnu vardhan\PycharmProjects\pythonProject\AddressBook/book.json", 'w') as out_file:
    json.dump(contact_list, out_file)