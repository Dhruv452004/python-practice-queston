'''
Question:
Tumhe 12 ka table print karna hai, lekin agar result even number 
ho toh usko "Even" print karna hai aur agar odd number ho toh "Odd" 
print karna hai. Matlab, output kuch aisa dikhna chahiye:


12 x 1 = 12 - Even
12 x 2 = 24 - Even
12 x 3 = 36 - Even
...
Hint:

Tum if-else statement ka use kar sakte ho, jisme check karna hoga ki result even hai ya odd.
'''



for twelve in range(1, 11):
    result = 3 * twelve
    # print(f"3 x {twelve} = {result}")
    if result % 2 == 0:
     print(f"3 x {twelve} = {result} - Even")
    
    else:
        print(f"3 x {twelve} = {result} - Odd")