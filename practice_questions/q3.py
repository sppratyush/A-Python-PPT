t = (1, "hello", 3.5, 7, "world", 10)

nums = [x for x in t if isinstance(x, (int, float))]
print("Numeric values:", nums)

try:
    t[0] = 100
except TypeError as e:
    print("Error:", e)

t2 = ("new", 99)
print("Concatenated tuple:", t + t2)