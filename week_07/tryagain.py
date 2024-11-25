sum = 0

while True:
 try:
    num = input('กรอกราคาสินค้า : ')

    if num == 'exit':  
            print(f"ยอดขายทั้งหมด {sum} บาท")
            break
    num = int(num)

    if num == 0 :
       raise ZeroDivisionError
    elif num < 0:
       raise Exception
    else:
        sum += num
        print (sum)
 except  ZeroDivisionError:
    print('ราคาสินค้าต้องมากกว่า 0 ') 
 except ValueError:
    print('กรอกตัวเลขเท่านั้น')
 except:
    print('ราคาสินค้าต้องไม่ติดลบ')