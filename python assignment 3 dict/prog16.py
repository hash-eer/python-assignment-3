# Write a Python program to find the highest 3 values in a dictionary.
from heapq import nlargest
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
list=nlargest(3,d,key=d.get)
print(list)