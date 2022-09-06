#Write a Python program to sort a dictionary by key.
d={'b':'ball','c':'cat','a':'apple','d':'dog'}
new_d=sorted(d)

for key in new_d:
    print("%s:%s" % (key,d[key]))