# Set kya hai?

- Python mein set ek unordered collection hota hai jo unique elements ko store karta hai.

- Set ke elements unique hote hain aur isme duplicate values nahi hoti.

- Example

        num1 = {1, 2, 3}
        num2 = {3, 4, 5 }

        union = set1 | set2       # Union of two sets

        intersection = set1 & set2  # Intersection of two sets

        difference = set1 - set2   # Difference of two sets

        print("Union:", union)

        print("Intersection:", intersection)
        
        print("Difference:", difference)



# set operators 

## 1. |  (Union Operator):
- Operator: set1 | set2
- Inbuilt method: set1.union(set2)

        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        result_operator = set1 | set2  # {1, 2, 3, 4, 5}

        # use inbuilt method:
        result_method = set1.union(set2)  # {1, 2, 3, 4, 5}



## 2. & (Intersection Operator):
- Operator: set1 & set2
- Inbuilt method: set1.intersection(set2)

        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        result_operator = set1 & set2  # {3}

        # use inbuilt method:
        result_method = set1.intersection(set2)  # {3}


## 3. - (Difference Operator):
- Operator: set1 - set2
- Inbuilt method: set1.difference(set2)

        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        result_operator = set1 - set2  # {1, 2}

        # use inbuilt method: 
        result_method = set1.difference(set2)  # {1, 2}


## 4. ^ (Symmetric Difference Operator):
- Operator: set1 ^ set2
- Inbuilt method: set1.symmetric_difference(set2)

        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        result_operator = set1 ^ set2  # {1, 2, 4, 5}

        # use inbuilt method:
        result_method = set1.symmetric_difference(set2)  # {1, 2, 4, 5}


## 5. <= (Subset Operator):
- Operator: set1 <= set2
- Inbuilt method: set1.issubset(set2)

        set1 = {1, 2, 3}
        set2 = {1, 2, 3, 4, 5}
        result_operator = set1 <= set2  # True

        # use inbuilt method:
        result_method = set1.issubset(set2)  # True


## 6. >= (Superset Operator):
- Operator: set1 >= set2
- Inbuilt method: set1.issuperset(set2)

        set1 = {1, 2, 3, 4, 5}
        set2 = {1, 2, 3}
        result_operator = set1 >= set2  # True

        # use inbuilt method:
        result_method = set1.issuperset(set2)  # True


## 7. == (Equality Operator):
- Operator: set1 == set2
- Inbuilt method: set1.__eq__(set2)

        set1 = {1, 2, 3}
        set2 = {1, 2, 3}
        result_operator = set1 == set2  # True

        # use inbuilt method:
        result_method = set1.__eq__(set2)  # True


## 8. != (Inequality Operator):
- Operator: set1 != set2
- Inbuilt method: set1.__ne__(set2)

        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        result_operator = set1 != set2  # True

        # use inbuilt method:
        result_method = set1.__ne__(set2)  # True


# Summary:
- Operators jaise |, &, -, ^, <=, >=, ==, != directly likhe jaate hain.

- Unke corresponding inbuilt methods bhi hote hain jaise union(), intersection(), difference(), symmetric_difference(), issubset(), issuperset(), __eq__(), etc.

- Tum dono ka use kar sakte ho, par generally operators ko prefer kiya jata hai kyunki yeh zyada concise aur readable hote hain.



# set ke kuch important methods:

## 1. add()
- Purpose: Is method se tum ek single element ko set mein add kar sakte ho.
- Syntax: set.add(element)
- Example 

        my_set = {1, 2, 3}
        my_set.add(4)
        print(my_set)  # Output: {1, 2, 3, 4}


## 2. remove()
- Purpose: Is method se tum set se ek specific element ko remove kar sakte ho. Agar element set mein nahi hai, toh yeh KeyError raise karega.
- Syntax: set.remove(element)
- Example

        my_set = {1, 2, 3, 4}
        my_set.remove(3)
        print(my_set)  # Output: {1, 2, 4}


## 3. discard()
- Purpose: Is method se tum set se specific element ko remove kar sakte ho. Agar element set mein nahi hai, toh KeyError nahi aayega, bas koi effect nahi hoga.
- Syntax: set.discard(element)
- Conclusion:
1. Agar tumhe error chahiye, tab remove() use karo.
2. Agar safe removal chahiye bina error ke, tab discard() use karo.

- Example 
 
        my_set = {1, 2, 3, 4}
        my_set.discard(5)  # No error, even though 5 is not in the set
        print(my_set)  # Output: {1, 2, 3, 4}


## 4. clear()
- Purpose: Is method se tum poore set ko clear kar sakte ho, matlab set ko empty bana sakte ho.
- Syntax: set.clear()
- Example

        my_set = {1, 2, 3}
        my_set.clear()
        print(my_set)  # Output: set()


## 5. copy()
- Purpose: Is method se tum set ka shallow copy bana sakte ho. Matlab original set ko modify karte waqt copied set unaffected rahega.
- Syntax: set.copy()
- Example 

        my_set = {1, 2, 3}
        new_set = my_set.copy()
        print(new_set)  # Output: {1, 2, 3}



## 6. update()
- Purpose: Is method se tum ek set ko dono sets ke elements se update kar sakte ho. Yeh tumhe ek set ke saath ek aur set, list, tuple, ya koi iterable object add karne ki suvidha deta hai.
- Syntax: set.update(iterable)
- Example

        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        set1.update(set2)
        print(set1)  # Output: {1, 2, 3, 4, 5}



## 7. issubset()
- Purpose: Is method se tum check kar sakte ho ki kya ek set dusre set ka subset hai ya nahi (yaani kya pehle set ke sabhi elements doosre set mein hain).
- Syntax: set.issubset(other_set)
- Example 

        set1 = {1, 2, 3}
        set2 = {1, 2, 3, 4, 5}
        result = set1.issubset(set2)
        print(result)  # Output: True




## 8.  issuperset()
- Purpose: Is method se tum check kar sakte ho ki kya ek set dusre set ka superset hai ya nahi (yaani kya pehle set mein doosre set ke sabhi elements hain).
- Syntax: set.issuperset(other_set)
- Example 

        set1 = {1, 2, 3, 4, 5}
        set2 = {1, 2, 3}
        result = set1.issuperset(set2)
        print(result)  # Output: True


## 9. isdisjoint()
- Purpose: Is method se tum check kar sakte ho ki kya do sets ke beech koi common elements nahi hain (yaani unka intersection empty hai).
- Syntax: set.isdisjoint(other_set)
- Example

        set1 = {1, 2, 3}
        set2 = {4, 5, 6}
        result = set1.isdisjoint(set2)
        print(result)  # Output: True




# Summary:
- add(), remove(), discard(), pop(), clear(): Sets ko modify karte hain.

- copy(): Set ka shallow copy banata hai.

- update(): Set ko update karne ke liye use hota hai.

- issubset(), issuperset(), isdisjoint(): Set ke relationship ko check karte hain doosre set ke saath.

- Yeh sab methods sets ke liye kaafi useful hote hain jab tumhe sets ko manipulate ya check karna ho.