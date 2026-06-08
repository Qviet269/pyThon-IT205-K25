inventory_stock = 100
total_revenue = 0.0

def validate (prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Dữ liệu nhập vào phải lớn hơn 0")
            else:
                return value
        except:
            print("Bạn nhập không phải số")


def add_stock(amount):
    global inventory_stock
    
    print(f"Đã nhập thành công {amount} sản phẩm")
    inventory_stock += amount
    print(f"Tồn kho hiện tại: {inventory_stock}")

def process_sale(quantity):
    global inventory_stock

    if inventory_stock < quantity:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}")
        return False
    return True

def  calculate_final_price(quantity, price):
    total = quantity * price
    discount = 0

    if total >= 1000:
        discount = total * 0.1

    after_discount = total - discount
    vat = after_discount * 0.08

    final_total = after_discount + vat

    return total, discount, vat, final_total

def  print_report():
    """
    Hàm hiển thị báo cáo tổng quan của cửa hàng.
    Bao gồm:
    - Tồn kho hiện tại
    - Tổng doanh thu
    """
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock}")
    print(f"Tổng doanh thu: {total_revenue}")

def menu():
    print("""
========== TECHSTORE MANAGEMENT SYSTEM ==========
    1. Nhập thêm hàng vào kho
    2. Bán hàng (Tính toán hóa đơn)
    3. Xem báo cáo tổng quan
    4. Thoát chương trình
=================================================
""")
    
def main():
    global inventory_stock
    global total_revenue
    while True:
        menu()
        choice = input("Chọn chức năng (1-4): ").strip()

        match choice:
            case "1":
                print("-----Nhập hàng----")
                amount = validate ("Nhập số lượng hàng muốn thêm")
                add_stock(amount)
            case "2":
                print("---- Bán Hàng -----")
                while True:
                    quantity = validate("Nhập số lượng mua: ")           
                    if not process_sale(quantity):
                        print("vui lòng nhập lại!")
                    else:
                        break
                price = validate("Nhập đơn giá ($): ")
                inventory_stock -= quantity
                total, discount, vat, final_total = calculate_final_price(quantity, price)
                total_revenue += final_total
                print("-> Hóa đơn chi tiết: ")
                print(f"Số lượng: {quantity} | Đơn giá: ${price}")
                print(f"tạm tính: ${total}")
                print(f"Giảm giá (10%): ${discount}")
                print(f"Thuế VAT (8%): ${vat}")
                print(f"Tổng thanh toán: ${final_total}")
                print("Đã bán thành công!")
                
            case "3":
                print_report()
            case "4":
                print("Đã thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

main()
