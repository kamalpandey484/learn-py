#Strings
string1 = "string"
string2 = "string 2"

print(string1[1])

#multiline string
string3 = """
This is a string
with multiple lines
"""

print("Multiline string:", string3)

for char in string1:
  print(char)


#string::
name = "kamal pandey"
print(name[0:5])
print(len(name))

name1 = "kamal"
print('len--', name1[-4:-2])

#string methods
print(name.upper())
print(name.lower())
print(name.strip("y"))
print(name.replace(" ", "-"))
print(name.split(" "))
print(name.capitalize())
print(name.count("a"))
print(name.endswith("y"))
print(name.find("t"))
print(name.islower())
print(name.title())
