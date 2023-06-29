def check_movie_seats():
    s, n = map(int, input().split())

    if s >= n:
        return "OK"
    else:
        return "NG"


result = check_movie_seats()
print(result)
