def count_cat_occurrences(S):
    count = 0

    for i in range(len(S) - 2):
        if S[i : i + 3] == "cat":
            count += 1

    return count


S = input().strip()
result = count_cat_occurrences(S)
print(result)
