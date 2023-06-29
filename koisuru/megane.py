def find_middle_number():
    N = int(input())
    numbers = list(map(int, input().split()))

    numbers.sort(reverse=True)  # 大きい順に並び替える
    middle_index = (N + 1) // 2  # 真ん中のインデックスを計算

    return str(numbers[middle_index - 1])  # インデックスは0から始まるため1を引く


result = find_middle_number()
print(result)
