def calculate_paiza_points():
    p = int(input())

    points = p // 100  
    bonus = 0

    if p >= 1000:
        bonus = 10 

    total_points = points + bonus

    return str(total_points)


result = calculate_paiza_points()
print(result)
