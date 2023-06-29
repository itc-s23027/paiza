def calculate_total_cost(n, p, m, q):
    # サインを書くために必要な色紙の枚数を計算
    total_papers = n

    # サインを書くために必要なペンの本数を計算
    required_pens = n // m
    if n % m != 0:
        required_pens += 1

    # 必要な色紙の費用とペンの費用を計算
    paper_cost = total_papers * p
    pen_cost = required_pens * q

    # 全体の費用を計算
    total_cost = paper_cost + pen_cost

    return total_cost


# 入力を受け取る
n, p = map(int, input().split())
m, q = map(int, input().split())

# 全てのファンにサインを書くために必要な費用を計算する
result = calculate_total_cost(n, p, m, q)

# 結果を出力する
print(result)
