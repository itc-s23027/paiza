def progress_status():
    s = int(input())
    t = int(input())

    progress = "-" * s
    progress = progress[: t - 1] + "+" + progress[t:]

    return progress


result = progress_status()
print(result)
