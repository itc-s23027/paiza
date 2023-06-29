def check_cd_fit():
    n = int(input())
    m = int(input())

    total_time = 0
    fit_songs = 0

    for i in range(m):
        t = int(input())

        if total_time + t <= n * 60:
            total_time += t
            fit_songs += 1
        else:
            break

    if fit_songs == m:
        return "OK"
    else:
        return str(fit_songs)


result = check_cd_fit()
print(result)
