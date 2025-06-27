from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу
	def __init__(self, value):
          super().__init__(value)
          if self.value.isdigit() and len(self.value) == 10:
              return
          
          raise ValueError('The info is not correct. Please provide correct phone number')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        for obj_phone in self.phones:
            if obj_phone.value == phone:
                self.phones.remove(obj_phone)
                return
        raise ValueError('Number not found') 
    
    def edit_phone(self, old_phone, new_phone):
        for i, obj_phone in enumerate(self.phones):
            if obj_phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError('Number not found')
            
    def find_phone(self, phone):
        for obj_phone in self.phones:
            if obj_phone.value == phone:
                return obj_phone
        return None
    
    
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
        
    def delete(self, name):
        self.data.pop(name)
            
    def __str__(self) -> str:
        return '\n'.join(str(record) for record in self.data.values())

# book = AddressBook()
# alex = Record('Alex')
# alex.add_phone('1231231231')
# print(alex.phones)
# #alex.remove_phone('1231231231')
# #print(alex.phones)
# #alex.find_phone('12312312311')

# book.add_record(alex)

# #print(book.find('Alex'))
# #book.delete('Alex')
# #print(book.find('Alex'))

# #print(book)
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
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
