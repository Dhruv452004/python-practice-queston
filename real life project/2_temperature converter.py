'''

Temperature Converter:
Celsius se Fahrenheit aur Fahrenheit se Celsius me temperature convert karne ka program likho.

Celsius to Fahrenheit formula: F = (C * 9/5) + 32
Fahrenheit to Celsius formula: C = (F - 32) * 5/9
'''
def celsius_to_fahrenheit():
    celsius = int(input("\nCelsius to Fahrenheit ke liye temperature daalo: "))
    F = (celsius * 9/5) + 32
    return round(F, 2)

def Fahrenheit_to_Celsius():
    fahrenheit = int(input("\nFahrenheit to Celsius ke liye temperature daalo: "))
    C = (fahrenheit - 32) * 5/9
    return round(C, 2)


def main():
    print("\ncelsius to fahrenhiet ke liye 1 \n \nfahrenheit to celsius ke liye 2 enter kr: ")
    # error handle krne k liye try ka use kra h isse ye hota h ki agr koi error ayga bhi tho ye khud error dega lekin code nahi rokega
    try:
        user = int(input("\n1 or 2: "))
        if(user == 1):
            print(f"\nCelsius to Fahrenheit: {celsius_to_fahrenheit()}°F")
        elif(user == 2):
            print(f"\nFahrenheit to Celsius: {Fahrenheit_to_Celsius()}°C")
        else:
            print("Invalid choice! 1 ya 2 me se koi ek number daal.")
            return main()
    except ValueError:
        print("Invalid input!  abe vo dhakan isme se koi ek number daal (1 or 2).")
        return main()

    # dubara isko chlane k liye
    print("\nagr dubara convert krna h tho haa ya nahi likh")
    dubara = input("haa ya nahi: ").strip().lower()
    if(dubara == "haa"):
        return main()
    elif(dubara == "nahi"):
        print("\nram ram bhai milte h fir baad mein")
    else:
        print("karu guddi laal haa ya nahi mein se koi ek likhna h")
        return main()

main()
