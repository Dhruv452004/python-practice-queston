'''

Bank Account:
Ek simple bank account bana ke usme deposit, withdraw aur balance check karne ki functionality implement karo.
Balance = 5000

'''
balance = 5000

def check_balance():
    print(f"apka bank balance hai {balance}")

def deposite(amount):
    global balance
    balance += amount
    print(f"Aapne {amount} rs deposit kiye. Naya balance: {balance} rs")

def withdraw(amount):
    global balance

    if(amount > balance):
        print(f"bhai bank mein itna paisa nahi hai")
    else:
        balance -= amount
        print(f"Aapne {amount} rs withdraw kiye. Naya balance: {balance} rs")

def bank_account():
    print("ye number daal ye check krne k liye \nbalance:1 \ndeposite:2 \nwithdraw:3")
    try:
        user = int(input("enter 1 or 2 or 3: "))
        print(f"current bank balance {balance}")
        if(user == 1):
            return check_balance()
        elif(user == 2):
            amount = int(input("Kitna deposit karna hai: "))
            deposite(amount)
        elif(user == 3):
            amount = int(input("Kitna withdraw karna hai: "))
            withdraw(amount)
        else:
            print("bhai jo number diye vo daal bhai (1 or 2 or 3)")
    except ValueError:
        print("karu guddi laal")

bank_account()