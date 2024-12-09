class Student :
    def __init__(self, name, id, age):
        self.ชื่อ = name
        self.เลข = id
        self.อายุ = age
        self.grade = {}

    def Update(self):
        Update = int(input("ใส่คะแนน : "))
        choice = input('กรุณาเลือกวิชาที่จะกรอกคะแนน \n มีวิชาดังนี้ Thai , Maths , English , Science , Society : ')
        grade = self.Grades(Update)
        if choice == "Thai":
           self.grade["Thai"] = grade
        elif choice ==  "Maths":
            self.grade["Maths"] = grade
        elif choice ==  "Science":
            self.grade["Science"] = grade
        elif choice ==  "Society":
            self.grade["Society"] = grade
    def Grades(self,Update):  
        if Update >= 80 :
            return 4
        elif Update >= 70:
            return 3
        elif Update >= 60:
            return 2
        elif Update >= 50:
            return 1
        else :
            return 0
student1 = Student("นานา", 6001, 12)
student2 = Student("บีม", 6002, 13)
student1.Update()
print(student1.grade)