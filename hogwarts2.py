students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
#using lists to match keys and values
#not ideal if we have many strings and many lists

#let's try a dictionary instead

students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
}
#look up key and get back the value
print(students["Hermione"])

for student in students:
    print(student)

#iterate through the students.... can we print out both key and value?

for student in students:
    print(student, students[student])

#let's make it cleaner

for student in students:
    print(student, students[student], sep=", ")
    #when you use a for loop with dictionary, you get to choose what the individual
    #variable is! Iterates over keys rather than index numbers like a list


#let's increase the data

