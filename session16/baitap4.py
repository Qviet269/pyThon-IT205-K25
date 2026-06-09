# ==================== PHÂN TÍCH ====================

# Hàm: display_records(records)
# Input : records (List chứa các chuỗi hồ sơ)
# Output: Không return
# Xử lý:
# - Duyệt từng hồ sơ
# - split("-") để tách dữ liệu
# - In ra màn hình

# Hàm: find_patient_index(records, patient_id)
# Input : records, mã bệnh nhân
# Output: index hoặc -1
# Xử lý:
# - Duyệt danh sách
# - split("-") lấy mã BN
# - So sánh với patient_id
# - Nếu trùng return index
# - Không có return -1

# Hàm: add_patient(records)
# Input : records
# Output: Không return
# Xử lý:
# - Nhập thông tin bệnh nhân
# - Chuẩn hóa chuỗi bằng:
#   strip(), upper(), title(), capitalize()
# - replace("-", " ")
# - Kiểm tra trùng mã
# - Kiểm tra năm sinh hợp lệ
# - join() ghép dữ liệu thành chuỗi
# - append() thêm vào list

# Hàm: update_diagnosis(records)
# Input : records
# Output: Không return
# Xử lý:
# - Nhập mã BN
# - Tìm vị trí bệnh nhân
# - split() tách chuỗi
# - Cập nhật chẩn đoán mới
# - join() ghép lại chuỗi
# - Gán đè vào records[index]

# Hàm: generate_age_report(records)
# Input : records
# Output: Không return
# Xử lý:
# - Duyệt danh sách
# - Tách năm sinh
# - Tính tuổi
# - Phân loại:
#   <16 : Trẻ em
#   16-60 : Trưởng thành
#   >60 : Người cao tuổi

from datetime import datetime

# Danh sách hồ sơ bệnh án
patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


# Hiển thị danh sách bệnh nhân
def display_records(records):

    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN ---------------------------")

    for index, record in enumerate(records, start=1):

        data = record.split("-")

        print(
            f"{index}. [{data[0]}] {data[1]} | "
            f"Năm sinh: {data[2]} | "
            f"Chẩn đoán: {data[3]}"
        )

    print("--------------------------------------------------")


# Tìm vị trí bệnh nhân theo mã
def find_patient_index(records, patient_id):

    patient_id = patient_id.strip().upper()

    for index, record in enumerate(records):

        data = record.split("-")

        if data[0] == patient_id:
            return index

    return -1


# Thêm bệnh nhân mới
def add_patient(records):

    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    # Nhập mã bệnh nhân
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    # Kiểm tra trùng mã
    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    # Nhập tên bệnh nhân
    patient_name = input("Nhập tên bệnh nhân: ")
    patient_name = patient_name.strip().replace("-", " ").title()

    # Nhập năm sinh
    current_year = datetime.now().year

    while True:

        birth_year = input("Nhập năm sinh: ").strip()

        if birth_year.isdigit():

            birth_year_int = int(birth_year)

            if 1900 <= birth_year_int <= current_year:
                break

        print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")

    # Nhập chẩn đoán
    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = diagnosis.strip().replace("-", " ").capitalize()

    # Ghép dữ liệu thành chuỗi
    new_record = "-".join([
        patient_id,
        patient_name,
        birth_year,
        diagnosis
    ])

    # Thêm vào danh sách
    records.append(new_record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu được lưu là:")
    print(new_record)


# Cập nhật chẩn đoán
def update_diagnosis(records):

    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    patient_index = find_patient_index(records, patient_id)

    if patient_index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    # Tách dữ liệu
    data = records[patient_index].split("-")

    print(f"\nTìm thấy bệnh nhân: {data[1]}")
    print(f"Chẩn đoán hiện tại: {data[3]}")

    # Nhập chẩn đoán mới
    new_diagnosis = input("Nhập chẩn đoán mới: ")
    new_diagnosis = new_diagnosis.strip().replace("-", " ").capitalize()

    # Cập nhật chẩn đoán
    data[3] = new_diagnosis

    # Ghép lại chuỗi
    updated_record = "-".join(data)

    # Gán đè vào danh sách
    records[patient_index] = updated_record

    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(updated_record)


# Báo cáo độ tuổi
def generate_age_report(records):

    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")

    current_year = datetime.now().year

    child = 0
    adult = 0
    elderly = 0

    for record in records:

        data = record.split("-")

        age = current_year - int(data[2])

        if age < 16:
            child += 1

        elif 16 <= age <= 60:
            adult += 1

        else:
            elderly += 1

    print(f"Trẻ em: {child} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


# Chương trình chính
while True:

    print("""
===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====
1. Xem danh sách hồ sơ bệnh án
2. Thêm hồ sơ bệnh nhân mới
3. Cập nhật chẩn đoán theo Mã BN
4. Báo cáo phân loại theo độ tuổi
5. Thoát chương trình
==================================================
""")

    choice = input("Chọn chức năng (1-5): ").strip()

    # Validate menu
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    if choice == 1:
        display_records(patient_records)

    elif choice == 2:
        add_patient(patient_records)

    elif choice == 3:
        update_diagnosis(patient_records)

    elif choice == 4:
        generate_age_report(patient_records)

    elif choice == 5:
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ!")