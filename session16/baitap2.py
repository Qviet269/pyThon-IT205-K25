# Khi gán:
# new_prescription = old_prescription
# thì cả 2 biến cùng trỏ tới một List trong bộ nhớ.
# Vì vậy append() sẽ làm thay đổi luôn List gốc.

# Để tạo bản sao độc lập của List có thể dùng:
# old_prescription.copy()
# old_prescription[:]

# String là immutable nên replace() không sửa chuỗi gốc,
# mà trả về chuỗi mới.

# Muốn cập nhật phần tử trong List phải gán lại:
# new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")


# Đơn thuốc hôm qua
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Hàm cập nhật đơn thuốc mới
def update_prescription(old_prescription):

    # Tạo bản sao độc lập
    new_prescription = old_prescription.copy()

    # Đổi tên thuốc
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")

    # Thêm thuốc mới
    new_prescription.append("Oresol")

    return new_prescription


# Đơn thuốc hôm nay
today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)