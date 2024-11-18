import random

class Student:
    def __init__(self, name, nickname,score=0):

        self.name = name
        self.nickname = nickname
        self.score = score

    def take(self):

        self.score = random.randint(1, 10)

    def grade(self):
        if self.score >= 5:
            print(f"{self.nickname} สอบผ่าน\n------------------------------------")
        else:
            print(f"{self.nickname} สอบไม่ผ่าน\n-----------------------------------")



student1 = Student('ชัยนันท์ ยิ้มสวัสดิ์', 'ติว')
student1.take()
print(f"นาย {student1.name} ชื่อเล่น {student1.nickname} มีคะแนน: {student1.score} คะแนน")
student1.grade()

student2 = Student('วรวิทย์ ประเสริฐผล', 'ปอนด์')  
student2.take()
print(f"นาย {student2.name}  ชื่อเล่น {student2.nickname} มีคะแนน: {student2.score} คะแนน")
student2.grade()

student3 = Student('การดวงดี มีกินมา', 'ดวงดี')  
student3.take()
print(f"นาย {student3.name}  ชื่อเล่น {student3.nickname} มีคะแนน: {student3.score} คะแนน")
student3.grade()

student4 = Student('หามาสี กามาดี', 'กำมา')  
student4.take()
print(f"นาย {student4.name}  ชื่อเล่น {student4.nickname} มีคะแนน: {student4.score} คะแนน")
student4.grade()

student5 = Student('ยายำดี หาไม่มี', 'มีไหม')  
student5.take()
print(f"นาย {student5.name}  ชื่อเล่น {student5.nickname} มีคะแนน: {student5.score} คะแนน")
student5.grade()
