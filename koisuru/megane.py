def find_middle_number():
    N = int(input())
    numbers = list(map(int, input().split()))

    numbers.sort(reverse=True)  
    middle_index = (N + 1) // 2  

    return str(numbers[middle_index - 1])  


result = find_middle_number()
print(result)
