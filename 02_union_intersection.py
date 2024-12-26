s1={1,45,6,78}
s2={7,8,1,78}

print(s1.union(s2)) #{1, 6, 7, 8, 45, 78}
print(s1.intersection(s2)) #{1, 78}
print(s1.difference(s2)) #{45, 6}
print(s2.difference(s1)) #{8, 7}

s= set()
print(type(s)) # empty set