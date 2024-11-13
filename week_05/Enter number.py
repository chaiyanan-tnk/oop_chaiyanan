box = []
num =(int(input("ต้องการป้อนทั้งหมดกี่ตัว : ")))
for i in range(1,num+1):
    q = (int(input(f'ใส่ตัวเลขที่{i} : ')))
    box.append (q)
print(f'ค่าเฉลี่ยของ {box} = {sum(box)/num}')
