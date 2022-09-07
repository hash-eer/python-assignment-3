#  Write a Python program to extend a list without append.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
list=[]
list1=[10, 20, 30]
print("present list of values",list1)
n=int(input("enter the size of the list you want insert"))
for i in range(0,n):
    print("enetr the",i+1,"th number")
    k=int(input())
    list.append(k)


list1[:0]=list

print(list1)