def my_function():
    print("Hello from My Function!")

def my_function_with_args(username, greeting):
    print("Welcome %s! %s" % (username, greeting))  

def calculate_age(birth_year, current_year):
    return current_year - birth_year

# Print a simple greeting
my_function()

# Welcome the user
my_function_with_args("Amydillo", "Happy Friday!")

# Display age of user
age = calculate_age(2002, 2021)
print("You are %d years old." % age)

# Classes and Objects -----------------------------------------
class Vehicle:
    name = ""
    color = ""
    kind = "car"
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Amy"
car1.color = "red"
car1.kind = "Mini Cooper"
car1.value = 35000.00

car2 = Vehicle()
car2.name = "Erin"
car2.color = "Silver"
car2.kind = "Porsche"
car2.value = 60000.00

print(car1.description())
print(car2.description())

# Dictionaries -----------------------------------------
phonebook = {
    "Amy" : 1111111111,
    "Erin" : 2222222222
}
del phonebook["Amy"] # or phonebook.pop("Amy")
print(phonebook)