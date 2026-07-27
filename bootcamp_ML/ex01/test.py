a = [1, 42, 300, 10, 59]

ts = TinyStatistician()

print(ts.mean(a))
print(ts.median(a))
print(ts.quartile(a))
print(ts.percentile(a, 10))
print(ts.percentile(a, 15))
print(ts.percentile(a, 20))
print(ts.var(a))
print(ts.std(a))