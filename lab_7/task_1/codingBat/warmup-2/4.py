def front_times(str, n):
    l = len(str)
    if l < 3:
        return str * n
    else:
        return str[0:3] * n