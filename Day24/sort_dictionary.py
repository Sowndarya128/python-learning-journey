student = {
    "Prajwal" : 90,
    "Ramesh" : 88,
    "Suresh" : 99
}
sorted_marks = sorted(student.items(), key=lambda x : x[1])
print(sorted_marks)