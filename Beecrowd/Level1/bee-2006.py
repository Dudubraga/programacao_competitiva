tea = int(input())
a, b, c, d, e = map(int, input().split())
correct = 0

if a == tea:
    correct += 1
if b == tea:
     correct += 1
if c == tea:
     correct += 1
if d == tea:
     correct += 1
if e == tea:
     correct += 1
print(correct)

# 2006 - Identifying Tea
# https://www.beecrowd.com.br/judge/en/problems/view/2006