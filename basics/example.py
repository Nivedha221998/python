def f(a, L=None):
    if L is None:
        L = []
        print("none")
    L.append(a)
    return L
print(f(1))