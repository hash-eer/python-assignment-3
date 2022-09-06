# Write a Python program to get the maximum and minimum value in a dictionary. 
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

 
# get key with min value
min_key = min(d, key=d.get)

#get the key with max value
max_key=max(d,key=d.get)


print("maximum value in the dictionary",d.get(max_key))
print("minimum value in the dictionary",d.get(min_key))

