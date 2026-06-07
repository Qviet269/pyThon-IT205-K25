student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

def menu ():
    print("""
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====
1. Xem bảng điểm và học lực
2. Cập nhật điểm thi sinh viên
3. Báo cáo thống kê (Đỗ/Trượt)
4. Tìm sinh viên Thủ khoa
5. Thoát chương trình
======================================================
""")

def get_rank(avg_score):

    if avg_score >= 8.0:
        return "Giỏi"
    elif avg_score >6.5:
        return "Khá"
    elif avg_score >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def validate_score(score_input):
    try:
        score = float(score_input)
        return 0 <= score <= 10
    except ValueError:
        return False
    
def input_validated_score(prompt):
    while True:
        input_score = input(prompt)
        if validate_score(input_score):
            return float(input_score)
        print("Điểm số không hợp lệ!")

def find_student_by_id(records, student_id):
    for i, s in enumerate(records):
        if student_id == s["student_id"]:
            return s
    return None


def display_grades(records):
    if len(records) == 0:
        print("Danh sách đang rỗng!")
    else:
        print("--- BẢNG ĐIỂM SINH VIÊN ---")
    
        for i , s in enumerate(records,1):
            avg = ( s["math"] + s["physics"] + s["chemistry"] ) / 3
            print(f"{i}. [{s['student_id']}] {s['name']:<15}| Toán: {s['math']:^5}| Lý: {s['physics']:^5}| Hóa: {s['chemistry']:^5}| ĐTB: {avg:.2f} - {get_rank(avg)}")

def update_student_score(records):
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    student = find_student_by_id(records, student_id)

    if not student:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
    else:
        print("Chọn môn học (1-Toán, 2-Lý, 3-Hóa):")
        subject_choice = input("Lựa chọn của bạn: ").strip()

        if subject_choice == "1":
            new_score = input_validated_score("Nhập điểm Toán mới: ")
            student["math"] = new_score
            print(f">> Đã cập nhật điểm Toán của sinh viên '{student['name']}' thành {new_score}.")
        elif subject_choice == "2":
            new_score = input_validated_score("Nhập điểm Lý mới: ")
            student["physics"] = new_score
            print(f">> Đã cập nhật điểm Lý của sinh viên '{student['name']}' thành {new_score}.")
        elif subject_choice == "3":
            new_score = input_validated_score("Nhập điểm Hóa mới: ")
            student["chemistry"] = new_score
            print(f">> Đã cập nhật điểm Hóa của sinh viên '{student['name']}' thành {new_score}.")
        else:
            print("Môn học lựa chọn không hợp lệ!")

    

def generate_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)
    passed_count = 0
    failed_count = 0

    for s in records:
        avg = (s["math"] + s["physics"] + s["chemistry"]) / 3
        if avg >= 5.0:
            passed_count += 1
        else:
            failed_count += 1

    passed_percentage = (passed_count / total_students) * 100
    failed_percentage = (failed_count / total_students) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {passed_count} sinh viên (Chiếm {passed_percentage:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {failed_count} sinh viên (Chiếm {failed_percentage:.2f}%)")

def find_valedictorian(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    valedictorian = records[0]
    max_avg = (valedictorian["math"] + valedictorian["physics"] + valedictorian["chemistry"]) / 3

    for s in records[1:]:
        current_avg = (s["math"] + s["physics"] + s["chemistry"]) / 3
        if current_avg > max_avg:
            max_avg = current_avg
            valedictorian = s

    print("\n--- VINH DANH THỦ KHOA ---")
    print(f" Sinh viên: {valedictorian['name']} (Mã: {valedictorian['student_id']})")
    print(f" Điểm Trung Bình: {max_avg:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")
def main ():
    while True:

        menu()
        choice = input("chọn chức năng (1-5): ")

        match choice:
            case "1":
                display_grades(student_records)
            case "2":
                update_student_score(student_records)
            case "3":
                generate_report(student_records)
            case "4":
                find_valedictorian(student_records)
            case "5":
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break
            case _:
                print("Lỗi, lựa chọn không hợp lệ!")
main ()