"""

(1) PHÂN TÍCH LỖI:
1. Gán sai tham số: Giá trị 15000 đang bị gán cho discount. 
Giá trị 0.1 đang bị gán cho shipping_fee.
2. Sai lệch công thức: Phép nhân trở thành 100000 * 15000 = 1,500,000,000. 
Tổng tiền bị biến thành: 100000 - 1500000000 + 0.1, dẫn đến kết quả âm -1499999999.9.
3. Lỗi TypeError: Do hàm không có lệnh return nên biến order_total nhận giá trị mặc định là None. 
Hệ thống không thể cộng NoneType với int (None + 5000).
4. Giá trị của order_total: Mang giá trị None vì hàm chỉ dùng print() để hiển thị chứ không trả dữ liệu về cho biến nhận.
5. Khác biệt giữa print và return: print() chỉ hiển thị dữ liệu lên màn hình, không thể dùng tính toán tiếp. 
return xuất dữ liệu ra khỏi hàm, cho phép lưu vào biến và tái sử dụng.
6. Cách sửa đổi hàm: Thay thế dòng lệnh print() trong hàm bằng return total để trả về giá trị sau khi tính toán.

"""
# Sửa code
def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total

order_total = calculate_final_price(price = 100000,shipping_fee = 15000,discount = 0.1)

final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)