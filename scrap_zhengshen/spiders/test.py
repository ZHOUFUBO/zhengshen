a=['b','c','d','b','c','a','a']
b=list(set(a))
print(b)
c={}.fromkeys(a).keys()
print(c)