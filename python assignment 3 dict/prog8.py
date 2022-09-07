#Write a Python program to sum all the items in a dictionary.
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 'a', 6: 60,'a':20}



list=[]
for key in d.keys():
    key=str(key)
    

    
    if key.isdigit()==True:
        list.append(int(key))
for value in d.values():
    value=str(value)
    if value.isdigit()==True:
        list.append(int(value))
print(sum(list))


