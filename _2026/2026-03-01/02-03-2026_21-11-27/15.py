def a(start, stop, step):
    if stop is None:
        start, stop = 0.0, float(start)
    start = float(start)
    stop = float(stop)
    step = float(step)
    result = []
    if step > 0:
        current = start
        while current < stop:
            result.append(current)
            current += step
            if abs(current - stop) < 0.0000000001:
                break
    else:
        current = start
        while current > stop:
            result.append(current)
            current += step
    return result
print(a(1, 14,2))
