def calculate_steps():
    M, N = map(int, input().split())

    total_steps = M - N
    if total_steps <= 0:
        return 0
    else:
        return total_steps


result = calculate_steps()
print(result)
