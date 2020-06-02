def get():
    for a in range(10):
        yield a


c = list(get())

print(c)
