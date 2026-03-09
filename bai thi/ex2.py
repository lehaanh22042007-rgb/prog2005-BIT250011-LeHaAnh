#bai 2
a = []
c = []
d = []
for i in range(112):
    if i>16:
        if i%2==1:
            a.append(i)
            a.sort()
            for b in range(i):
                if b > 0 and i % b == 0:
                    c.append(b)
                if len(c)==2:
                    d.append(i)
                    c =[]
print("cac so nguyen to la:",d)
print("cac so le la",a)
