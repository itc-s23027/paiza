N = int(input())

def check_luckiness(N):
    if N % 7 == 0:
        return "lucky"
    else:
        return "unlucky"

result = check_luckiness(N)
print(result)

~                         
