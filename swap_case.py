def swap_case(s):
    result =  ''
    for char in s:
        if char.islower():
            result = result + char.upper()
        elif char.isupper():
            result = result + char.lower()
        else:
            result = result + char
    
    return  result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
