def count_substring(string, sub_string):
    start = 0
    counter = 0
    while True:
        pos = string.find(sub_string,start)
        if pos  == -1:
            break
        counter +=1
        start = pos + 1
    
    return counter
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
