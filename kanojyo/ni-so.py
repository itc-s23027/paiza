n = int(input())
m = int(input())

stripe = ""

for i in range(m):
    if i % (2 * n) < n:
        stripe += "R"
    else:
        stripe += "W"

print(stripe)
