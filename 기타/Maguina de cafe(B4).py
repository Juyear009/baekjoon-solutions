A = int(input())
B = int(input())
C = int(input())

t1 = 0*A + 2*B + 4*C
t2 = 2*A + 0*B + 2*C
t3 = 4*A + 2*B + 0*C

print(min(t1, t2, t3))
