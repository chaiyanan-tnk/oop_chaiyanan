name = str(input("โปรดกรอกชื่อและนามสกุล: "))
nickname = str(input("โปรดกรอกชื่อเล่น: "))
age = int(input("โปรดกรอกอายุ: "))
StudentID = int(input("โปรดกรอกรหัสประจำตัวนักเรียน: "))
Gradelevel = int(input("โปรดกรอกระดับชั้น: "))
height = float(input("โปรดกรอกส่วนสูง : "))
weight = float(input("โปรดกรอกน้ำหนัก : "))

print("\nชื่อ-นามสกุล: " + name + " อายุ: " + str(age) + " ปี")
print("รหัสประจำตัวนักเรียน: " + str(StudentID) + " ระดับชั้น: " + str(Gradelevel))
print("ชื่อเล่น " + nickname )
print("ส่วนสูง " + str(height) + " เซนติเมตร" + "น้ำหนัก: " + str(weight) + " กิโลกรัม" )

sum = height + weight 
print("ส้วนสูง + น้ำหนัก  = " + str(sum))