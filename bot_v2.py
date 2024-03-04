from collections import UserDict

# base class for forming records 
class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    def get_name(self):
        self.name = name
        return self.name
		
class Phone(Field):

    # return only valid phones with 10 digits else exception
    def check_phone(self):

        if self.value.isdigit()	and len(self.value) == 10:
            return self.value
        else:
            raise ValueError("Phone number is invalid")        

class Record:
    def __init__(self, name):
        self.name = Name(name) # store instance in attr
        self.phones = [] # could be more than 1 phone for each name

    def add_phone(self, phone):
        phone_checked = Phone(phone).check_phone()
        self.phones.append(phone_checked) # adding valid Phone instance to the list of phones
         
    def edit_phone(self,old_value,new_value):
        old_phone = Phone(old_value).check_phone()
        new_phone = Phone(new_value).check_phone()

        if old_phone in self.phones:
            i = self.phones.index(old_phone) # replace old_number with new_phone
            self.phones[i] = new_phone
            return self.phones
        else:
            raise ValueError("Phone number for a change not found")

    def remove_phone(self, phone):

        try:
            checked_phone = Phone(phone).check_phone()
            self.phones.remove(checked_phone)

        except Exception as e:
            return print(f'Error: {e}')

    def find_phone(self, phone):
        checked_phone = Phone(phone).check_phone()   

        if checked_phone in self.phones:
            return checked_phone
        else:
            raise ValueError("Phone number not found")   

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):

    def __init__(self):
        self.data = {} # empty dict for initialization
  
    def add_record(self, record):
        self.data[record.name.value] = record # expand dictionary with name of user as a key and instance of Record for user as a value

    def find(self, name):
        if name in self.data:
           return self.data[name] # get instance of Record for user if found by name

    def delete(self, name):
        if name in self.data: # delete instance of Record for user if found by name
            del self.data[name]

# Залишила для подальших перевірок цей шматок з домашки =>
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
book.delete("Jane")            
    
for name, record in book.data.items():
    print(record)