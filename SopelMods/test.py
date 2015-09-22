timings = [1.2, 1.5, 1.3, 1.5]
print reduce(lambda a, b: a + b, timings, 0.0) / len(timings)

