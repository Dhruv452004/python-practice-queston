'''
Movie Ticket Pricing

Problem: Movie tickets are priced based on age: 200rs for adults (18+), 100rs for children. Everyone gets a 20rs discount on Wednesday.


Adult (18+): Ticket price is 200rs.
Child (<18): Ticket price is 100rs.
Wednesday: Sabhi ko 20rs discount milega.

'''


age = int(input("Kitne saal ka he be tu ?: "))
day = input("aaj konsa din he vo bta: ").strip().lower()

#.strip() ye faltu space ko hta deta hai and .lower() jese kisi user ne WeDnesday, Wednesday ese kuch bhi likha tho ye use lower case mein kar dega tani wednesday

if(age >= 18):
    price = 200

else:
    price = 100


# discount mein original price show krne k liye price ko store krenge

before_discount_price = price

# ab bari h discount denge agr day wednesday hua tho
if(day == "wednesday"):
    price -= 20 # ye short trika h price = price - 20 ko likhne ka apki mrji h kese apko likhna h
    print(f"mubarakh ho aaj wednesday hai aur wednesday ke din hum custumer ko 20rs ka discount dete h {before_discount_price} - 20Rs")
else:
    print("apko discount nahi milega")


print(f"\nThe ticket price  is: {price}Rs")