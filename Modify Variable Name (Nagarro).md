# Write a program to convert a C++ variable name into Java variable and vice-versa

## 1) C++ to Java

input1= 'this_is_a_variable"

output1= "thisIsAVariable"

input2="modify_variableName"

output2="modifyVariableName"



## 2) Java to C++

input= "thisIsAVariable"

output= "this_is_a_variable"

# Code

    input_string=input()

    def cplus_to_java(s):

        ans=''
        c=0

        for i in s:
            if i!='_' and c==0:
                ans += i
            elif i=='_':
                c=1
            else:
                ans+=i.upper()
                c=0

        return ans

    def java_to_cplus(s):

        ans=''
        for i in s:
            if i.isupper()!=True:
                ans+=i
            elif i.isupper()==True:
                ans+='_'+i.lower()

        return ans


    if '_' in input_string:

        print(cplus_to_java(input_string))
    else:
        print(java_to_cplus(input_string))
