# Conditional Statements kya hai?

## Python mein conditional statements ka use karke hum program ko decisions lene ke liye tayar karte hain. Yeh statements conditions ko check karte hain aur uske hisaab se alag-alag code blocks execute hote hain.

# Types of Conditional Statements in Python:
1. if statement

2. if-else statement

3. if-elif-else statement

4. Nested if statement



# Examples


1. if statement
- Yeh ek single condition ko check karta hai. Agar condition true hai, toh uska block execute hota hai.

      x = 10
      if x > 5:
         print("x is greater than 5")


2. if-else statement
- Yeh 2 conditions handle karta hai: ek true ke liye aur ek false ke liye.

      x = 10
      if x % 2 == 0:
         print("x is even")
      else:
         print("x is odd")

3. if-elif-else statement
- Yeh multiple conditions ko check karne ke liye use hota hai.

      x = 15
      if x < 10:
         print("x is less than 10")
      elif x == 10:
         print("x is equal to 10")
      else:
         print("x is greater than 10")


4. Nested if statement
- Ek if ke andar doosra if likhne ke liye use hota hai.

      x = 20
      if x > 10:
         if x % 2 == 0:
            print("x is greater than 10 and even")
         else:
            print("x is greater than 10 and odd")
   


# Important Points:
- Python mein indentation kaafi important hai. Har conditional block ke andar ka code ek level andar likha jata hai.

- Condition ke andar comparison operator
(==, !=, <, >, <=, >=) aur logical operators (and, or, not) ka use hota hai.