#bài 1
a= "d:\\music\\muabui.mp3"
def product(a):
    arr = a.split('\\')
    print(arr[2])
def nhac(a):
    arr = a.split('\\')
    ab = arr[2].split('.')
    print(ab[0])
product(a)
nhac(a)
