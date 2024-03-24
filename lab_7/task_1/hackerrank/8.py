n = int(input())
student_marks = {}

for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    
query_name = input()

if query_name in student_marks:
    avg_score = sum(student_marks[query_name])/3
    print("{:.2f}".format(avg_score)) #printing 2 digits after decimal point