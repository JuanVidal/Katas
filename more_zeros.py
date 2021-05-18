def more_zeros(s):
    s = "".join(dict.fromkeys(s)) # Getting rid of the duplicates in order
    s2 = [bin(ord(i))[2:] for i in s]
    s2 = [len(i)>2*i.count('1') for i in s2]
    return [i for j, i in enumerate(s) if s2[j]]

print(more_zeros("DIGEST"))
