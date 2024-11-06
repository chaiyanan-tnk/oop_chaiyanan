import random
win = 0 
lose = 0
allow = 0
while True :
 a = random.choice(['ค้อน', 'กรรไกร', 'กระดาษ'])
 print("เลือก ค้อน กรรไกร หรือ กระดาษ")
 b = input("คุณเลือก: ")  

 print(f"สุ้ม: {a}")
 print(f"คุณเลือก: {b}")

 if a == b:
    print("ผลลัพธ์คือ เสมอ!")
    allow += 1
 elif (a == 'ค้อน' and b == 'กรรไกร') :
    print("ผลลัพธ์คือ คุณแพ้!") 
    lose += 1
 elif (a == 'กรรไกร' and b == 'กระดาษ') :
    print("ผลลัพธ์คือ คุณแพ้!") 
    lose += 1
 elif (a == 'กระดาษ' and b == 'ค้อน'):
    print("ผลลัพธ์คือ คุณแพ้!")
    lose += 1
 elif (a == 'กระดาษ' and b == 'กรรไกร'):   
    print("ผลลัพธ์คือ คุณชนะ!")
    win += 1
 elif (a == 'กรรไกร' and b == 'ค้อน'):
    print("ผลลัพธ์คือ คุณชนะ!")
    win += 1
 elif (a == 'ค้อน' and b == 'กระดาษ'):
    print("ผลลัพธ์คือ คุณชนะ!")  
    win += 1
 elif b == 'หยุด':
    print("ออกแล้ว")  
    print(f'ผลลัพธ์การ ชนะ : {win} \nผลลัพธ์การ แพ้ : {lose} \nผลลัพธ์การ เสมอ {lose}')
    break
 else:
    print("กรุณาเลือกให้ถูกต้อง (ค้อน, กรรไกร, หรือ กระดาษ)")


