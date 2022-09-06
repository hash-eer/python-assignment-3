#Write a Python program to remove duplicates from Dictionary.

d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60,1:30,2:10}
result={}

for key,value in d.items():
    if value not in result.values():
        result[key] = value
        
print(result) 