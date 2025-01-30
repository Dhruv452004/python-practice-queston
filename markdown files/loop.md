# Loops kya hota h ? 

## Python mein loops ek aise structure hote hain jo kisi kaam ya code ko baar-baar repeat karne ke liye use hote hain. Isse aapko manually ek hi cheez baar-baar likhne ki zarurat nahi hoti.


## Python mein do tarah ke loops commonly use hote hain:

## - For loop:----------------------------------------------
- For loop: Jab aapko kisi fixed range ya collection (list, string, tuple, etc.) ke elements ko iterate karna ho.
[
## Example 1: Ek se 5 tak numbers print karna
    for i in range(1, 6):  # range(1, 6) ka matlab hai 1 se lekar 5 tak
    print(i)
    #Output: 1 2 3 4 5 
]

## agr samaj ni aya tho idhr dekh nalle.

- range(1, 6) ek function hai jo 1 se lekar 5 tak numbers deta hai.
i har baar ek naya number le raha hai range ke andar se.

[
## Example 2: Ek list ke elements print karna
      fruits = ['apple', 'banana', 'cherry']
      for fruit in fruits:
      print(fruit)
      #Output: apple banana cherry
]

## agr samaj ni aya tho idhr dekh nalle.
- fruits ek list hai.
- for fruit in fruits ka matlab hai, list ke har element ko ek-ek karke fruit variable mein dal kar usse print karo
      


## While loop: ----------------------------------------------
- While loop: Jab tak koi condition True hai, tab tak code ko repeat karta hai.
Ye tab use hota hai jab aapko pata na ho ki loop kab rukega, lekin ek condition ke basis par usse stop karwana ho.

[
## Example 3: 1 se 5 tak numbers print karna (while loop se)

    i = 1
    while i <= 5:  # Jab tak i ki value 5 se chhoti ya barabar hai
    print(i)
    i += 1  # i ki value har baar 1 se badhao
    #Output: 1 2 3 4 5 
]

## agr samaj ni aya tho idhr dekh nalle.
- i = 1 se start hota hai.
- while i <= 5 ka matlab hai, loop tab tak chalega jab tak i ki value 5 ya usse chhoti hai.
i += 1 ka matlab hai har baar i ki value ko 1 se badhana.



# Break aur Continue Statement

## Kabhi-kabhi hume loop ko beech mein hi stop ya skip karna hota hai. Iske liye break aur continue ka use hota hai.

[
## Example 4: Break statement

    for i in range(1, 10):
    if i == 5:  # Jab i ki value 5 ho
        break   # Loop wahi stop ho jata hai
    print(i)
]

[
## Example 5: Continue statement

    for i in range(1, 6):
    if i == 3:  # Jab i ki value 3 ho
        continue  # Us iteration ko skip kar do
    print(i)
]

# Ek statement aur hoti h Pass

## Python mein agar aap ek block (e.g., loop, function, if condition, etc.) ko blank chhodte hain, toh error aayega. Lekin agar aap waha pass ka use karte hain, toh Python samajhta hai ki yeh block abhi khali hai, par ye valid hai.

    for i in range(5):
    pass  # Abhi ke liye loop mein kuch nahi


## dekho pass ka use jada tar har jga use hota h jese function, loops, if else etc. lekin Continue and Break statement ka use jada tar loops mein hota h. baki khud try kro kha kha iska use kar skte hai har chij nalle mein thodi btaunga.