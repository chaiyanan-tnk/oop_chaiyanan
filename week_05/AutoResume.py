box = {'nickname':'  ','stdid':'  ','hobby':' ','color':' '}
num = int(input("จำนวนที่จะป้อน : "))
for i in range(1,num+1):
     print(f'กรอกคนที่ { i } ')
     box['nickname'] = str(input("กรุณากรอกชื่อเล่น : "))
     box['stdid'] = int(input("กรุณากรอกเลขที่ : "))
     box['hobby'] = str(input("กรุณากรอกงานอดิเรก : "))
     box['color'] = str(input("กรุณากรอกสีที่ชอบ : "))
     print(f'ข้อมูลคนที่ {i}\n{box} ')
     print('-----------------------------------------------')