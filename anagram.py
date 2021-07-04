
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


