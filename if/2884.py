# 알람 시계
h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
else:
    a = m - 45 + 60
    h -= 1
    if h == -1:
        h = 23
        print(h, a)
    else:
        print(h, a)

'''time = h * 60 + m - 45
print(time//60%24, time%60)'''
