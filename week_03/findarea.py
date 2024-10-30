print("คำนวณหาพื้นที่ 4 เหลี่ยมจัตุรัส")
side = int(input("ใส่ความยาวด้าน: "))
square = side * side
print("พื้นที่สี่เหลี่ยมจัตุรัส คือ", square)

print("\nคำนวณหาพื้นที่ 4 เหลี่ยมผืนผ้า")
width = int(input("ใส่ความกว้าง: "))
height = int(input("ใส่ความยาว: "))
print("พื้นที่สี่เหลี่ยมผืนผ้า คือ", width * height)

print("\nคำนวณหาพื้นที่ วงกลม")
radius = float(input("ใส่ความยาวรัศมี: "))
print(f"พื้นที่วงกลม คือ {3.14 * (radius ** 2)}")