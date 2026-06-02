"""
Danh sách ban đầu: ["GE001", "GE002", "GE003-CANCEL"]

1. delivery_orders.insert(0, "GE000")
-> Thêm "GE000" vào đầu danh sách. Các phần tử cũ bị dịch sang phải 1 vị trí.
-> Danh sách mới: ["GE000", "GE001", "GE002", "GE003-CANCEL"]
delivery_orders.insert(0, "GE000")

2. Sau khi chèn "GE000" vào đầu, "GE002" bị đẩy từ index 1 sang index 2.
-> Dòng lệnh dưới đây sửa sai vì chỉ số [1] lúc này đã thuộc về "GE001" chứ không còn là "GE002".
delivery_orders[1] = "GE002-UPDATED"

3. delivery_orders.remove(3) gây lỗi vì:
-> Phương thức remove() xóa phần tử theo GIÁ TRỊ (value) chứ không phải theo vị trí (index).
-> Hệ thống báo lỗi ValueError vì không tìm thấy giá trị số 3 trong danh sách chuỗi.
-> Muốn xóa "GE003-CANCEL", phải truyền đúng giá trị chuỗi: delivery_orders.remove("GE003-CANCEL")

4. Tác dụng của pop(): Xóa phần tử khỏi danh sách và TRẢ VỀ (return) chính phần tử vừa xóa đó.

5. Chương trình cũ báo lỗi NameError khi in 'transferred_order' vì:
-> Gọi hàm pop() nhưng chưa gán kết quả trả về vào biến này (biến chưa được khởi tạo).
-> Muốn lưu lại đơn hàng cuối cùng vừa lấy ra, phải viết: transferred_order = delivery_orders.pop()
"""

delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]
print('Danh sách ban đầu: ', delivery_orders)

delivery_orders.append('GE004')

delivery_orders.insert(0, 'GE000')

delivery_orders[2] = 'GE002-UPDATED'

delivery_orders.remove('GE003-CANCEL')

transferred_order = delivery_orders.pop(-1)
print('\nDanh sách đơn hàng còn lại: ',delivery_orders)
print('Đơn hàng được bàn giao: ', transferred_order)