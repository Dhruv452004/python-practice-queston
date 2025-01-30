'''
*  
**  
***  
****  
***** 

'''



def pattern(n):
    if(n == 0):
        return 0
    pattern(n-1)
    print("*" * n )
    

pattern(5)




'''

*****
****
***
**
*

upr vala code hi mene likha bs print ko upr krdia aur ye reverse ho jayga
'''

print("nice")

def pattern(n):
    if(n == 0):
        return 0
    print("*" * n )
    pattern(n-1)
    

pattern(5)