if __name__ == "__main__":
    students_marks = {}
    for _ in range(int(input())):
        name, *line = input().split()
        score = list(map(float,line))
        students_marks[name] = score
    
    query_name = input()
    
    if query_name in students_marks:
        result = sum(students_marks[query_name])/len(students_marks[query_name])
    
    print(f"{result:.2f}")
        
