#  Write a Python script to check if a given key already exists in a dictionary. 

d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(d)
key=int(input("enter the key to check if it is present in the dictionary or not:"))
if key in d:
    print("key is present in the dictionary")
else:
    print("key is not present in the dictionary")