A,B,C = map(int,input().split())

if A == B or B == C or C == A or A == B+C or B == A+C or C == A+B:
  print("S")
else:
  print("N")