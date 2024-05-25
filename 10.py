a = [42, 69, 322, 13, 0, 99, 5, 9, 8, 7, 6, 5]
b = 0
c = 0
while True:
    c = a[b]
    b += 1
    if c < 0:
        print(c)
        break
    elif len(a) <= b:
        print("список кончился(")
        break
    else:
        continue