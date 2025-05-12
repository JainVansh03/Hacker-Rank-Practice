        
if __name__ == '__main__':
    list1 = list()
    for _ in range(int(input())):
        name = input()
        score = input()
        list1.append([name,score])
        
    grades = [score for name,score in list1]
    unique_score = []
    for score in grades:
        if score not in unique_score:
            unique_score.append(score)
    
    unique_score.sort()
    second_lowest = unique_score[1]
    
    names = []
    
    for name, score in list1:
        if score == second_lowest:
            names.append(name)
            
    names.sort()
    
    for name in names:
        print(name) 
            

            

            

            

            
