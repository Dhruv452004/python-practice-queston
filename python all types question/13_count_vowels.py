'''

Question 13: "Count_Vowels"
Tumhe ek string diya gaya hai. Tumhe ek function banani hai jo is string mein vowels (a, e, i, o, u) ki count kare aur return kare.
aur jo vowels string mein mile h use vowel_list mein store kro.

string = "Loha badmosh"

'''


string = "Loha badmosh"

def vowels():
    vowel_list = []
    count = 0   
    for i in string:
        if(i in "aeiouAEIOU"):
            count += 1
            vowel_list.append(i)
    return vowel_list, count

total_vowels, total_count = vowels()
print(f"string mein ye {total_vowels} vowels mile hai \n aur inka total count ye hai {total_count}")