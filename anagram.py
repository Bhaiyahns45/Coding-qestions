
#An anagram of a string is another string that contains the same characters,
# only the order of characters can be different.
# For example, “abcd” and “dabc” are an anagram of each other.


print("enter the 1st string:")
s1=input()

print("enter the 2nd string:")
s2=input()


if sorted(s1)==sorted(s2):
    print("yes")
else:
    print("no")
























# inertion sort
#
# def insertion_sort(a,ln):
#
#     for i in range(1,ln):
#         temp=a[i]
#
#         j=i-1
#
#         while j!=-1 and temp<a[j]:
#             a[j+1]=a[j]
#             j-=1
#
#         a[j+1]=temp
#
#     return a
#
#
# print(insertion_sort(a,ln))























# selection sort
# for i in range(ln):
#     loc=i
#     for j in range(i+1,ln):
#         if a[loc]>a[j]:
#             loc=j
#
#     if loc!=i:
#         temp=a[i]
#         a[i]=a[loc]
#         a[loc]=temp
#
# print(a)































#bubble sort
# for i in range(ln-1):
#
#     flag=0
#     for j in range(ln-i-1):
#         if a[j]>a[j+1]:
#             flag=1
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp
#
#     if flag==0:
#         print(i)
#         break
#
# print(a)

