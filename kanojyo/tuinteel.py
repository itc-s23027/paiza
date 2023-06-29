def choose_energy_drink(c1, p1, c2, p2):
    cp_ratio1 = c1 / p1  # ドリンク1のコストパフォーマンス
    cp_ratio2 = c2 / p2  # ドリンク2のコストパフォーマンス

    if cp_ratio1 > cp_ratio2:
        return 1  # ドリンク1のコストパフォーマンスが高い
    else:
        return 2  # ドリンク2のコストパフォーマンスが高い


c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())


result = choose_energy_drink(c1, p1, c2, p2)
print(result)
