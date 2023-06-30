def choose_energy_drink(c1, p1, c2, p2):
    cp_ratio1 = c1 / p1  
    cp_ratio2 = c2 / p2  

    if cp_ratio1 > cp_ratio2:
        return 1  
    else:
        return 2  


c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())


result = choose_energy_drink(c1, p1, c2, p2)
print(result)
