# ==================== PHÂN TÍCH ====================

# display_patients(patient_list)
# Input : List bệnh nhân
# Output: Không return
# Chức năng: Hiển thị danh sách bệnh nhân

# validate_gender(gender_input)
# Input : Chuỗi giới tính
# Output: True / False
# Chức năng: Kiểm tra giới tính hợp lệ

# find_patient_index(patient_list, patient_id)
# Input : List bệnh nhân, mã bệnh nhân
# Output: index hoặc -1
# Chức năng: Tìm vị trí bệnh nhân trong list

# add_patient(patient_list)
# Input : List bệnh nhân
# Output: Không return
# Chức năng: Thêm bệnh nhân mới

# update_diagnosis(patient_list)
# Input : List bệnh nhân
# Output: Không return
# Chức năng: Cập nhật chẩn đoán bệnh

# search_by_disease(patient_list)
# Input : List bệnh nhân
# Output: Không return
# Chức năng: Tìm kiếm bệnh nhân theo tên bệnh

# String dùng để lưu:
# mã BN, tên BN, giới tính, chẩn đoán

# List dùng để lưu:
# danh sách bệnh nhân và thông tin từng bệnh nhân

# Khi truyền patient_list vào hàm,
# Python truyền tham chiếu (reference),
# nên thay đổi trong hàm sẽ ảnh hưởng list gốc.

# Danh sách bệnh nhân ban đầu
patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]


def display_patients(patient_list):
    """
    Hiển thị danh sách bệnh nhân
    """

    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return

    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")

    for index, patient in enumerate(patient_list, start=1):
        print(
            f"{index}. Mã: {patient[0]} | "
            f"Tên: {patient[1]} | "
            f"Giới tính: {patient[2]} | "
            f"Bệnh: {patient[3]}"
        )


def validate_gender(gender_input):
    """
    Kiểm tra giới tính hợp lệ
    """

    gender_input = gender_input.strip().lower()

    if gender_input == "nam" or gender_input == "nu":
        return True

    return False


def find_patient_index(patient_list, patient_id):
    """
    Tìm index bệnh nhân theo mã
    """

    patient_id = patient_id.strip().upper()

    for index, patient in enumerate(patient_list):

        if patient[0] == patient_id:
            return index

    return -1


def add_patient(patient_list):
    """
    Thêm bệnh nhân mới
    """

    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    # Nhập mã bệnh nhân
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    # Kiểm tra trùng mã
    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    # Nhập tên bệnh nhân
    patient_name = input("Nhập tên bệnh nhân: ").strip().title()

    if len(patient_name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    # Nhập giới tính
    while True:

        gender = input("Nhập giới tính Nam/Nu: ").strip().lower()

        if validate_gender(gender):
            gender = gender.capitalize()
            break

        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    # Nhập chẩn đoán bệnh
    diagnosis = input("Nhập chẩn đoán bệnh: ").strip().capitalize()

    # Tạo list bệnh nhân mới
    new_patient = [
        patient_id,
        patient_name,
        gender,
        diagnosis
    ]

    # Thêm vào danh sách
    patient_list.append(new_patient)

    print("Tiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list):
    """
    Cập nhật chẩn đoán bệnh
    """

    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    patient_index = find_patient_index(patient_list, patient_id)

    if patient_index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id}!")
        return

    print(f"Tìm thấy bệnh nhân: {patient_list[patient_index][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[patient_index][3]}")

    new_diagnosis = input("Nhập chẩn đoán mới: ").strip().capitalize()

    if len(new_diagnosis) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    # Cập nhật chẩn đoán
    patient_list[patient_index][3] = new_diagnosis

    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list):
    """
    Tìm kiếm bệnh nhân theo tên bệnh
    """

    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    keyword = input("Nhập từ khóa tên bệnh: ").strip()

    if len(keyword) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return

    print("Kết quả tìm kiếm:")

    count = 0

    for index, patient in enumerate(patient_list, start=1):

        if keyword.lower() in patient[3].lower():

            count += 1

            print(
                f"{count}. Mã: {patient[0]} | "
                f"Tên: {patient[1]} | "
                f"Giới tính: {patient[2]} | "
                f"Bệnh: {patient[3]}"
            )

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(f"\nCó tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")


# Chương trình chính
while True:

    print("""
===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====
1. Hiển thị danh sách bệnh nhân
2. Tiếp nhận bệnh nhân mới
3. Cập nhật chẩn đoán bệnh theo mã BN
4. Tìm kiếm và thống kê theo tên bệnh
5. Thoát chương trình
===========================================
""")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    # Validate menu
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
        continue

    choice = int(choice)

    if choice == 1:
        display_patients(patients)

    elif choice == 2:
        add_patient(patients)

    elif choice == 3:
        update_diagnosis(patients)

    elif choice == 4:
        search_by_disease(patients)

    elif choice == 5:
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")