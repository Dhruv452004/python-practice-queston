# dict kya h?
- Python mein dict (dictionary) hoti hai, jo ek tarah ka data structure hai. Ye key-value pairs mein data store karti hai, jaise ek dictionary mein shabdon ke meanings hote hain.

## syntax
     # Ek simple dictionary
       student = {
      "name": "Rahul",
      "age": 21,
      "city": "Delhi"
    }
    # Values ko access karna
      print(student["name"])  # Output: Rahul
      print(student["age"])   # Output: 21

## Key Points:
- Keys: Unique hote hain (jaise "name", "age").
- Values: Keys se linked data hote hain (jaise "Rahul", 21).

- Mutable: Aap dictionary ke data ko update ya change kar sakte ho.


# dict ke methods

## 1. clear()
- Dictionary ko saaf (empty) kar deta hai.

- Example:

      student = {"name": "Amit", "age": 20}
      student.clear()
      print(student)  # Output: {}


## 2. copy()
- Dictionary ki ek copy banata hai.

-Example:

      student = {"name": "Amit", "age": 20}
      new_student = student.copy()
      print(new_student)  # Output: {'name': 'Amit', 'age': 20}



## 3. fromkeys()
- Nayi dictionary banata hai ek list of keys aur ek common value ke saath.

- Example:

      
      keys = ["name", "age", "city"]
      
      default_dict = dict.fromkeys(keys, "unknown")
      
      print(default_dict)  # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}



## 4. get(key)
- Key ka value return karta hai; agar key na mile to default value de sakte ho.

- Example:

      student = {"name": "Amit", "age": 20}
      
      print(student.get("name"))       # Output: Amit
      
      print(student.get("city", "N/A"))  # Output: N/A



## 5. items()
- Dictionary ke key-value pairs ko ek list of tuples mein return karta hai.

- Example:

      student = {"name": "Amit", "age": 20}
      
      print(student.items())  # Output: dict_items([('name', 'Amit'), ('age', 20)])


## 6. keys()
- Sirf keys ka list return karta hai.

- Example:

      student = {"name": "Amit", "age": 20}
      
      print(student.keys())  # Output: dict_keys(['name', 'age'])


## 7. values()
- Sirf values ka list return karta hai.

- Example:

      student = {"name": "Amit", "age": 20}
      
      print(student.values())  # Output: dict_values(['Amit', 20])



## 8. pop(key)
- Di gayi key ka value return karta hai aur us key-value pair ko dictionary se delete kar deta hai.

- Example:

      student = {"name": "Amit", "age": 20}
     
      age = student.pop("age")
      
      print(age)        # Output: 20
      
      print(student)    # Output: {'name': 'Amit'}




## 9. popitem()
- Last key-value pair ko remove karke return karta hai (Python 3.7+ ke liye).

- Example:

      student = {"name": "Amit", "age": 20}
      
      item = student.popitem()
      
      print(item)       # Output: ('age', 20)
      
      print(student)    # Output: {'name': 'Amit'}



## 10. setdefault(key, default)
- Agar key exist karti hai, to uska value return karta hai; agar nahi karti, to default value set karke return karta hai.

- Example:

      student = {"name": "Amit"}
      
      city = student.setdefault("city", "Delhi")
      
      print(city)       # Output: Delhi
      
      print(student)    # Output: {'name': 'Amit', 'city': 'Delhi'}




## 11. update()
- Ek dictionary ke key-value pairs ko doosri dictionary ke saath merge ya update karta hai.

- Example"

        student = {"name": "Amit", "age": 20}
       
        extra_info = {"city": "Delhi", "course": "Python"}
      
        student.update(extra_info)
        
        print(student)  
       
        # Output: {'name': 'Amit', 'age': 20, 'city': 'Delhi', 'course': 'Python'}



