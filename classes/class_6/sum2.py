n = 13
sum = 0

while n > 0:
    print(f"{sum} = {sum} + {n}")
    sum = sum+n
    # print(f"{n}")
    n=n-1

print(sum)

# 1th -> sum =3, n=2
# 2nd -> sum=3+2, n=1
# 3rd -> sum = 5 + 1 , n=0

