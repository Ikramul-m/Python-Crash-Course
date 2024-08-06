message = "Hello Python World"
print(message)

message = "Hello Python crash course world"
# print(message.title())
# print(message.upper())
# print(message.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
message = "Hello, " + full_name.title() + "!"
print(message)

print("\tPython")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favourate_language = 'Python '
print(favourate_language.rstrip())

favourate_language = ' Python '
print(favourate_language.lstrip())

message = "One of Python's strengths is its diverse community."
# message = 'One of Python's strengths is its diverse community.'
print(message)

a = 2 + 3
print(a)
a = 3 - 2
print(a)
a = 3 * 2
print(a)
a = 3 / 2
print(a)
a = 3 ** 2
print(a)
a = 3 ** 3
print(a)
a = 10 ** 6
print(a)

a = 2 + 3 * 4
print(a)

a = (2 + 3) * 4
print(a)

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)



bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1].title())
print(bicycles[-2].title())
print(bicycles[-3].title())

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append("pulsur")
motorcycles.append("yamaha")
motorcycles.append("ktm")
print(motorcycles)

del motorcycles[0]
print(motorcycles)
motorcycles.pop()
print(motorcycles)