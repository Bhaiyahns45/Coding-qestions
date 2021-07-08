# Input

input_string= "bhaiya hari narayan singh"

# Output

output_string = "singh narayan hari bhaiya"

# Code

    
    
    input_string=input()
    
    #change the string to list using split() function
    s=input_string.split()
    
    ans=[]
    
    #append to ans in reverse order
    for i in range(len(s)-1,-1,-1):
        ans.append(s[i])
    
    #convert list into string using .''join() function
    output_string=' '.join(ans)
    
    print(output_string)
    
    
    
