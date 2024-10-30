print("กรอกคะแนน ")
score = int(input("โปรดกรอกคะแนนของคุณ : "))
if score > 100 :
    print ("กรุณากรอกไม่เกิน 100  ")
elif score >=80 :
    print ("คุณได้เกรด 4 ") 
elif score >=75 :
    print ("คุณได้เกรด 3.5 ")
elif score >=70 :
    print ("คุณได้เกรด 3 ")
elif score >=65 :
    print ("คุณได้เกรด 2.5 ")
elif score >=60 :
    print ("คุณได้เกรด 2 ")
elif score >=55 :
    print ("คุณได้เกรด 1.5 ")
elif score >=50 :
    print ("คุณได้เกรด 1 ")
elif score <0 :
    print ("กรุณากรอกมากกว่า 0 ")
else :
    score <50 
    print ("คุณสอบไม่ผ่าน ")
    print ("คุณอยากสอบแก้ไหม ")
    choice = input("พิ้มพ์ Y หรือ N \n")
    if choice == 'Y' :
        print("สอบแก้ผ่าน")
        print(f"คะแนนที่ขาด {50-score} คะแนน")
    elif choice == 'N' :
        print("สอบแก้ไม่ผ่าน")
    else :
        print('ป้อน Y หรือ N เท่านั้น')

