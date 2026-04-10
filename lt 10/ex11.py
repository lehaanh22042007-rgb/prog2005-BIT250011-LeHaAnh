# Bài 11
while True:
    print("1-10 chọn bài, 0 thoát")
    choice = int(input())
    if choice == 0:
        break
    elif choice == 1:
        p = input()
        print(p.split("\\")[-1])
    elif choice == 2:
        s = input()
        c = input()
        print(s.count(c))
    elif choice == 3:
        def f(n):
            if n <= 1:
                return 1
            return n * f(n - 1)
        print(f(int(input())))