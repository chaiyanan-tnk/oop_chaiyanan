name = str(input("โปรดกรอกชื่อและนามสกุล: "))
nickname = str(input("โปรดกรอกชื่อเล่น: "))
age = int(input("โปรดกรอกอายุ: "))
StudentID = int(input("โปรดกรอกรหัสประจำตัวนักเรียน: "))
Gradelevel = int(input("โปรดกรอกระดับชั้น: "))
height = float(input("โปรดกรอกส่วนสูง : "))
weight = float(input("โปรดกรอกน้ำหนัก : "))

print(f"\nชื่อ-นามสกุล: {name}  อายุ: {age} ปี")
print(f"รหัสประจำตัวนักเรียน: {StudentID} ระดับชั้น: {Gradelevel}")
print(f"ชื่อเล่น: {nickname}")
print(f"ส่วนสูง: {height} เซนติเมตร น้ำหนัก: {weight} กิโลกรัม")

sum = height + weight 
print(f"ส่วนสูง + น้ำหนัก = {sum}")
