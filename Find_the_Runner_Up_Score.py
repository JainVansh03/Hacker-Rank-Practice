if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    max_sum = max(arr)
    arr.remove(max_sum)
    print(max(arr))
