def eye_exam():
    pass_count = 0

    for _ in range(5):
        d, e = input().split()

        if d == e:
            pass_count += 1

    if pass_count >= 3:
        return "OK"
    else:
        return "NG"


result = eye_exam()
print(result)
