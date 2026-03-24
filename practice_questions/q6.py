t = (5, 12, "hello", 3, 25, 8)

lst = list(t)
lst = [x for x in lst if not (isinstance(x, int) and x < 10)]

t_new = tuple(lst)
print("Updated tuple:", t_new)