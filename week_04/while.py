a = int(input("ป้อนสูตรคูณ: "))
i = 1  
while i < 25:  
    b = a * i
    if (b / 2) % 2 != 0:
        print(f"{a} x {i} = {b}") 
    i += 1   