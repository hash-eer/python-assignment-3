# Write a Python program to remove a key from a dictionary.
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(d)
key=int(input("enter a key to remove a key"))
if key in d:
    del d[key]
    
print("after deletion of a key new dictionary is",d)
     