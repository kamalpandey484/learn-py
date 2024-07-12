value = int(input("Enter your age:"))
print(value);

print(value>18)
print(value<18)
print(value==18)
print(value!=18)
print(value>=18)
print(value<=18)

if(value > 18):
  gender = int(input("Enter your gender: \n 1: Male \n 2: Female \n"))
  if(gender == 1 or gender > 3):
    print("Male")
  else:
    print("Female")
  print("You can drive")
  print("Yes")
elif(value == 18):
  print("You are 18")
else:
  print("You cannot drive")
  print("No")
print("Outside if else")