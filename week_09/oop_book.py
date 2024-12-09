class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        while True:
            book_name = input("กรอกชื่อหนังสือ (หรือพิมพ์ 'exit' เพื่อหยุด): ")
            if book_name == "exit":
                break
            else:
                nameauthor = input(f"กรอกชื่อคนแต่งของหนังสือ '{book_name}': ")
                pages = int(input(f"กรอกจำนวนหน้าของหนังสือ '{book_name}': "))
                price = float(input(f"กรอกราคาของหนังสือ '{book_name}': "))

            self.books.append({
                "book_name": book_name,
                "author": nameauthor,
                "pages": pages,
                "price": price
            })
            print(f"เพิ่มหนังสือ '{book_name}' เรียบร้อยแล้ว")

    def show_book(self):
        print("\nรายการหนังสือทั้งหมด:")
        for book in self.books:
            print(f"- ชื่อ: {book['book_name']}, ชื่อคนแต่ง: {book['author']}, จำนวนหน้า: {book['pages']}, ราคา: {book['price']} บาท")
    def find_book(self):
        while True:
            search_name = input("กรอกชื่อหนังสือที่ต้องการค้นหา (หรือพิมพ์ 'exit' เพื่อหยุด): ")
            print(f"\nค้นหาหนังสือที่ตรงกับคำค้นหา '{search_name}':")
            if search_name == 'exit':
                break
            for book in self.books:
                if book['book_name'] == search_name:
                    print(f'พบหนังสือ {search_name}')
                    print(f'ชื่อผู้แต่ง: {book["author"]}')
                    print(f'จำนวนหน้า: {book["pages"]} หน้า')
                    print(f'ราคา: {book["price"]} บาท')
book1 = Library()
book1.add_book()
book1.show_book()
book1.find_book() 