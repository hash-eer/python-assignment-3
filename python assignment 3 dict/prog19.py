#  Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

list=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
result=[]

for i in list:
    if i not in result:
        result.append(i)
        
print(result)