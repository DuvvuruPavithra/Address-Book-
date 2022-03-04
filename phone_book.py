import json
from person_details import Person

class Book:
    def __init__(self, filename):
        with open(filename) as file:
            self.json_data = json.load(file)
        self.person_list = []
        for data in self.json_data:
            self.person_list.append(Person(**data))

    def display_contacts(self):
        for data in self.person_list:
            print(f"{data.firstName} \t {data.lastName} \t {data.mobileNumber}\t {data.State} \t {data.City} \t {data.pinCode}")

    def add_contacts(self):
        while True:
            contact_present, firstname = self.validate()
            if contact_present:
                print(f"{firstname.firstName} Already Exist!!")
                break
            lastname = input("Enter  Last Name:")
            mobile_number = int(input("Enter Phone Number:"))
            state = input("Enter  State:")
            city = input("Enter  City:")
            pincode = input("Enter  Pincode:")
            person = Person(firstname, lastname, mobile_number, state, city, pincode)
            self.person_list.append(person)
            return

    def delete_contacts(self):
        while True:
            contact_present, person = self.validate()
            if contact_present:
                self.person_list.remove(person)
                self.display_contacts()
                return
            print(f"{person} is not in contact list")

    def display(self, name):
        for data in self.person_list:
            if data.firstName == name:
                print(f"{data.firstName} \t {data.lastName} \t {data.mobileNumber}\t {data.State} \t {data.City} \t {data.pinCode}")
                return
        print(f"{name} is not in contact list enter the correct name")

    def validate(self):
        contact_present = False
        firstname = input("Enter First Name:")
        for data in self.person_list:
            if data.firstName == firstname:
                contact_present = True
                person = data
                return contact_present, person
        return contact_present, firstname

    def update_contacts(self):
        while True:
            contact_present, person = self.validate()
            if contact_present:
                option = int(input("What you want to update:\n1.FirstName\n2.LastName\n3.MobileNumber\n4.State\n5"
                                   ".City\n6.Pincode\n"))
                if option == 1:
                    new_name = input("Enter New First Name:")
                    lastname = person.lastName
                    mobile_number = person.mobileNumber
                    state = person.State
                    city = person.City
                    pincode = person.pinCode
                    self.person_list.remove(person)
                    temp_person = Person(new_name, lastname, mobile_number, state, city, pincode)
                    self.person_list.append(temp_person)
                    self.display(new_name)
                    return
                if option == 2:
                    new_lastname = input("Enter New Last Name:")
                    firstname = person.firstName
                    mobile_number = person.mobileNumber
                    state = person.State
                    city = person.City
                    pincode = person.pinCode
                    self.person_list.remove(person)
                    temp_person = Person( firstname, new_lastname, mobile_number, state, city, pincode)
                    self.person_list.append(temp_person)
                    self.display(new_lastname)
                    return
                if option == 3:
                    new_phone = int(input("Enter New Phone Number:"))
                    firstname = person.firstName
                    lastname = person.lastName
                    state = person.State
                    city = person.City
                    pincode = person.pinCode
                    self.person_list.remove(person)
                    temp_person = Person(firstname, lastname, new_phone, state, city, pincode)
                    self.person_list.append(temp_person)
                    self.display(new_phone)
                    return
                if option == 4:
                    new_state = input("Enter new State:")
                    firstname = person.firstName
                    lastname = person.lastName
                    mobile_number = person.mobileNumber
                    city = person.City
                    pincode = person.pinCode
                    self.person_list.remove(person)
                    temp_person = Person(firstname,lastname,mobile_number,new_state,city,pincode)
                    self.person_list.append(temp_person)
                    self.display(new_state)
                    return
                if option == 5:
                    new_city = input("Enter new City:")
                    firstname = person.firstName
                    lastname = person.lastName
                    mobile_number = person.mobileNumber
                    state = person.State
                    pincode = person.pinCode
                    self.person_list.remove(person)
                    temp_person = Person(firstname,lastname,mobile_number, state, new_city, pincode)
                    self.person_list.append(temp_person)
                    self.display(new_city)
                    return
                if option == 6:
                    new_pincode = input("Enter new Pincode:")
                    firstname = person.firstName
                    lastname = person.lastName
                    mobile_number = person.mobileNumber
                    state = person.State
                    city = person.City
                    self.person_list.remove(person)
                    temp_person = Person(firstname, lastname, mobile_number, state, city, new_pincode)
                    self.person_list.append(temp_person)
                    self.display(new_pincode)
                    return
            print(f"{person} is not in contact list")

    def search_Contacts(self):
        while True:
            contact_present, person = self.validate()
            if contact_present:
                self.person_list.index(person)
                self.display_contacts()
                return
            print(f"{person} is not in contact list")

