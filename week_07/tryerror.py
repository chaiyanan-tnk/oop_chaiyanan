try:
    num = int(input("ยอดสั่งซื้อ : "))
    if num == 0 :
        raise ZeroDivisionError 
    elif num < 0 :
        raise Exception
    sum = num * 0.2
    sum1 = num * 0.1
    if num >= 5000:
        print(f"ส่วนลดทั้งหมด {sum} บาท")
        print(f'ยอดที่ต้องจ่าย {num-sum} บาท')
    elif num >= 2000:
        print(f"ส่วนลดทั้งหมด {sum1} บาท")
        print(f'ยอดที่ต้องจ่าย {num-sum1} บาท')
    else : 
        print (f'คุณไม่ได้รับส่วนลด \nยอดที่ต้องจ่ายคือ {num} บาท')
except ValueError:
    print('กรอกตัวเลขเท่านั้น')
except ZeroDivisionError :
    print('ห้ามใส่ 0 ')
except:
    print('ห้ามใส่เลขติดลบ')