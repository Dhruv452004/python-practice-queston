'''
Sum of Even Numbers
Problem: Calculate the sum of even numbers up to a given number n.
aur total sum bhi de

'''

numbers = int(input("number daal: "))
sum_of_even_numbers = 0
total_sum = 0

for number in range(1, numbers+1): # jese 10 dala tho ye 1 se 10 tk even find krega fir total sum dega 
    if(number % 2 == 0):
        print(f"ye {number} tho even hai")
        sum_of_even_numbers += 1
        total_sum += number


print(f"\nsum of even number is: {sum_of_even_numbers}")
print(f"\n total sum of even number is: {total_sum}")