a = int(input("ป้อนสูตรคูณ: "))
for i in range(1, 25):  
    b = a * i
    if (b / 2) % 2 != 0:
     print(f"{a} x {i} = {b}") 