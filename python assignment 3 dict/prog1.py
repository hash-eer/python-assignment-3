#Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
d= {1:2,2:3,3:4,4:5}
sort=sorted(d.items(),key=operator.itemgetter(1))
print("ascending order sort",sort)
sort=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("descending order sort",sort)