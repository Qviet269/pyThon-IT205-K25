"""
(1) PHÂN TÍCH LỖI:
1. Loại biến: Biến total_points ở dòng 2 là biến toàn cục (Global) vì nó được khai báo ở ngoài cùng của file, không nằm trong bất kỳ hàm nào.
2. Nguyên nhân lỗi UnboundLocalError: Trong hàm có câu lệnh gán 'total_points = ...'. Python tự động coi total_points là biến cục bộ (Local). 
Khi thực hiện phép tính 'total_points + points_earned', Python tìm giá trị của biến cục bộ này nhưng nó chưa được định nghĩa trước đó, 
dẫn đến lỗi sử dụng biến trước khi gán.
3. Nếu chỉ đọc biến: Chương trình KHÔNG bị lỗi. 
Nếu chỉ dùng câu lệnh print(total_points) trong hàm, Python sẽ tự tìm ra biến toàn cục bên ngoài để đọc dữ liệu.
4. Cách sửa 1 (Dùng từ khóa): Dùng từ khóa 'global' để khai báo trong hàm. 
Câu lệnh: global total_points.
5. Cách sửa 2 (Pure Function): Hàm nên nhận tham số và dùng lệnh 'return' để trả về tổng điểm mới sau khi cộng dồn.
"""

# Sửa lỗi
total_points = 100

def add_reward_points(points_earned):
    global total_points

    total_points = total_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")
    return total_points


add_reward_points(50)

print("Tổng điểm hiện tại của khách hàng:", total_points)
