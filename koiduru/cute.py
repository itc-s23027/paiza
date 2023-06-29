def distribute_candies():
    n, m = map(int, input().split())

    if m % n == 0:
        return "ok"
    else:
        return "ng"


result = distribute_candies()
print(result)
