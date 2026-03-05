#.sort() → method for lists only, sorts in place.
#sorted() → built-in function, works on any iterable, returns new sorted list.
# .sort is only used when working with List || Other items are sorted using sorted function which will create a new sorted List

names = ["kuldeep","dave","henry","Cavil","chico","leo"]

sorted_names = sorted(names)  # sorted(names,reverse=True) -> Will sort the list in a reverse order

for i in sorted_names:
    print(i)

# List of tuples:-

students = [("Kuldeep","A",50),
            ("Dave","F",40),
            ("Henry","B",18),
            ("Cavil","E",60),
            ("Chico","D",11)]

def grades(x):
    return x[2]

#students.sort(key=grades)            # Python looks at each tuple and passes it to the function you gave in key — here, that’s grade.
students.sort(key=lambda x : x[2])

for i in students:
    print(i)

# Tuple of tuples
Studentss = (("Kuldeep","A",50),
            ("Dave","F",40),
            ("Henry","B",18),
            ("Cavil","E",60),
            ("Chico","D",11))

age = lambda x : x[1]
sorted_Students = sorted(Studentss,key=age)

    