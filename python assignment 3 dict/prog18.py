# Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

l = [{},{},{}] # this list is generated elsewhere...
all_empty = True
for i in l:
  if i:
    all_empty = False

print (all_empty)