#  Write a Python program to extend a list without append.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
list=[10, 20, 30]

list[:0]=[40, 50, 60]

print(list)