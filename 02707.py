import math
n = int(input())
for i in range(n):
    a, b, c = map(float, input().split())
    if b == 0:
        b = -b
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1={x1:.5f};x2={x2:.5f}")
    elif delta == 0:
        t = (-b) / (2 * a)
        print(f"x1=x2={t:.5f}")
    else:
        d = math.sqrt(-delta) / (2 * a)
        re = (-b) / (2 * a)
        print(f"x1={re:.5f}+{d:.5f}i;x2={re:.5f}-{d:.5f}i")