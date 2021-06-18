print("This line will be printed")

# Variables and Types -----------------------------------------
x = 1
if x == 1:
    print("x is 1")

print("Goodbye World")

myfloat = float(7)
print(myfloat)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
print(hello + " " + world)

a,b = 3, 4
print(a, b)

# Lists -----------------------------------------
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])

names = ["John", "Eric", "Bob"]
second_name = names[1]
print("The second name in the list is " + second_name)

# Operators -----------------------------------------
remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

lots_of_hellos = "hello " * 10
print(lots_of_hellos)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
all_numbers = even + odd
print(all_numbers)
length_even = len(even)
print(length_even)

print([1, 2, 3] * 3)

# String Formatting -----------------------------------------
name = "Amy"
age = 19
print("Hello %s!" % name)
print("%s is %d years old!" % (name, age))

print("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello"
print(format_string + " %s %s. Your current balance is %.2f" % (data[0], data[1], data[2]))

# String Operations -----------------------------------------
string = "Hello World!"
print(len(string))
print(string.index("o"))
print(string.count("o"))
print(string[::-1])

couple_words = string.split(" ")
print(couple_words[0])

# Conditions -----------------------------------------
x = 1
print(x == 2)
print(x == 3)
print(x < 3)

if x == 2:
    print("x is two")
else:
    print("x is not two")    

if name == "Amy" and age == 19:
    print("Your name is Amy and you are 19 years old.")

if name == "Amy" or "Erin":
    print("Your name is either Amy or Erin.")

if name in ["Amy", "Erin"]:
    print("Your name is either Amy or Erin.")

print(not False)

# Loops -----------------------------------------
for x in range(5):
    print(x)
for x in range(3,6):
    print(x)
for x in range(3,8,2):
    print(x)        

count = 0
while count < 5:
    print(count)
    count += 2