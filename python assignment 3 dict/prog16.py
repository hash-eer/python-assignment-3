# Write a Python program to find the highest 3 values in a dictionary.
from collections import Counter

my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
k = Counter(my_dict)
print(k)
# Finding 3 highest values
high = k.most_common(3)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in high:
   print(i[0]," :",i[1]," ")