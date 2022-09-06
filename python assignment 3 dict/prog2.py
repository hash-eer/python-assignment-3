# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

d={0:10,1:20}
print("the dictionary which is alredy present here is",d)
key1=int(input("enetr the key to insert into dictionary"))
value1=int(input("enetr the  value to insert into dictionary"))
d.update({key1:value1})
print("updated dictionary is :",d)