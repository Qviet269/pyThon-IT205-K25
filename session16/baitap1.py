# String trong Python là immutable (bất biến),
# nên strip() và title() không thay đổi chuỗi gốc,
# mà trả về một chuỗi mới.

# Muốn lưu kết quả sau khi xử lý chuỗi,
# cần gán lại vào biến:
# raw_diagnosis = raw_diagnosis.strip().title()

# extend() khi nhận String sẽ tách từng ký tự
# và thêm từng ký tự vào list.

# Để thêm nguyên chuỗi vào list,
# cần dùng append() thay vì extend().


# Danh sách chẩn đoán hiện tại
patient_diagnoses = ["Sốt Xuất Huyết"]

# Hàm chuẩn hóa và thêm chẩn đoán
def add_diagnosis(raw_diagnosis, current_list):

    # Chuẩn hóa chuỗi
    raw_diagnosis = raw_diagnosis.strip().title()

    # Thêm nguyên chuỗi vào list
    current_list.append(raw_diagnosis)

    return current_list


# Chẩn đoán mới nhập vào
new_diagnosis = "  viEm phE QUan  "

# Cập nhật hồ sơ bệnh án
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)