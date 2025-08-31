a1 = {1,2,3,4,5,5,5,5}
a2 = {1,2,3,4,5,8,9}
print(type(a1), type(a2))
print(a1)
print(a1==a2)

print(a1.issubset(a2))
print(a1.intersection(a2))
print(a1.union(a2))