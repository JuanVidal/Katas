def odd2(L):
    L1 = [i%2 for i in L]
    L2 = [i for i in L if i!=0]
    if sum(L1) == 1: return L1.index(1)
    if len(L2) == 1: return L.index(L2[0])
    try:
        return L.index(-1)
    except ValueError:
        L2 = [i//2 if i%2 else 0 for i in L]
        if sum(map(abs,L2)): return odd2(L2)
        else: return odd2([i//2 for i in L])

def oddest(a):
    return a[0] if len(a) == 1 else a[odd2(a)]

#A = oddest([1, 2, 3, 4, 5, 6, 8, 9, 10])
A = oddest([47, -33,2, 44, 6, -19, 15, 1109, 201, -1114])
print(A)
