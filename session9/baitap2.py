
# 1. express_orders.insert(0, "GE100-FAST") làm thay đổi danh sách thế nào?
# -> Thêm "GE100-FAST" vào đầu danh sách (vị trí 0), đẩy tất cả phần tử cũ dịch sang phải 1 chỉ số.
# -> Danh sách thành: ["GE100-FAST", "GE101", "GE102-WRONG", "GE103-CANCEL"]

# 2. Sau khi chèn "GE100-FAST", "GE102-WRONG" nằm ở index nào?
# -> Đang nằm ở vị trí index 2.

# 3. Vì sao lệnh express_orders[1] = "GE102-UPDATED" sửa nhầm "GE101"?
# -> Vì sau khi chèn đơn hỏa tốc vào đầu, phần tử nằm ở index 1 lúc này đã trở thành "GE101".

# 4. Vì sao express_orders.pop(3) không xóa đúng đơn hàng bị hủy?
# -> Lệnh này xóa phần tử tại index 3 (là "GE104" vừa được append vào cuối trước đó),
#    trong khi đơn hàng hủy "GE103-CANCEL" thực tế đang nằm ở index 4 sau khi mảng bị dịch chuyển.

# 5. Muốn xóa đúng đơn hàng "GE103-CANCEL" bằng remove() thì viết thế nào?
# -> Nên dùng: express_orders.remove("GE103-CANCEL") (xóa trực tiếp theo giá trị chuỗi).

# 6. Phương thức pop() không truyền index sẽ lấy phần tử ở đâu?
# -> Mặc định lấy và xóa phần tử ở CUỐI danh sách.

# 7. Vì sao lệnh current_order = express_orders.pop() lấy sai đơn hàng đang giao?
# -> Do không truyền index nên hàm lấy nhầm đơn hàng cuối cùng, thay vì đơn đầu tiên cần giao.

# 8. Muốn lấy đơn hàng ĐẦU TIÊN trong danh sách ra để giao, cần viết lệnh thế nào?
# -> Cần truyền chỉ số vị trí đầu tiên: current_order = express_orders.pop(0)

# 9. Muốn chương trình cho ra kết quả đúng, cần sửa lại những dòng nào?
# -> Sửa dòng cập nhật mã: express_orders[1] chuyển thành express_orders[2]
# -> Sửa dòng xóa đơn hủy: express_orders.pop(3) chuyển thành express_orders.remove("GE103-CANCEL")
# -> Sửa dòng lấy đơn giao: express_orders.pop() chuyển thành express_orders.pop(0)

express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

express_orders.append("GE104")

express_orders.insert(0, "GE100-FAST")

express_orders[2] = "GE102-UPDATED"

express_orders.remove("GE103-CANCEL")

current_order = express_orders.pop(0)


print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)