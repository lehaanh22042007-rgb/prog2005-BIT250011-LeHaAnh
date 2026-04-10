#bài 5
books = [("Triết học Mác-Lênin", 49000),]
tong = 49000
with open("books.txt", "w", encoding="utf-8") as f:
    for name, price in books:
        f.write(f"{name};{price}\n")
        tong += price
    f.write(f"Tong;{tong}")