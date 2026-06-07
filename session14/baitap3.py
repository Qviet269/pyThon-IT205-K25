students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def menu():
    print("""
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
    1. Hiển thị danh sách sinh viên
    2. Thêm học viên mới
    3. Cập nhật điểm thi theo mã học viên
    4. Đánh giá học lức của toàn bộ học viên
    5. Thoát chương trinh
""")

def  validate_score(score_input):
    try:
        score = float(score_input)
        return 0 <= score <= 10
    except ValueError:
        return False

def input_validate_score(prompt):
    while True:
        score = input(prompt)

        if validate_score(score):
            return float(score)
        
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    
def find_student_by_id(student_list, student_id):
    for i, s in enumerate(student_list):
        if student_id == s["student_id"]:
            return s
    return None
    

def display_student(student_list):

    if len(student_list) == 0:
        print("Danh sách sinh viên hiện đang trống")
    else:
        for i, v in enumerate(student_list,1):
            print(f"{i}. Mã: {v["student_id"]:^7}| Tên:{v["name"]:^15}| Toán:{v["math_score"]:^10}| Anh:{v["english_score"]:^10}")

def add_student(student_list):

    while True:
        student_id = input("Nhập Mã Học Viên: ").strip().upper()
        if student_id == "":
            print("ID không được để trống")
            continue

        if find_student_by_id(student_list , student_id):
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác")
            continue
        break

    while True:
        name = input("Nhập tên học viên: ").title()
        if name == "":
            print("Tên không được để trống")
        else:
            break
        

    math_score = input_validate_score("Nhập điểm toán: ")
    english_score = input_validate_score("Nhập điểm anh: ")

    student_list.append({
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    })
    print("Đã Thêm thành công!")

def update_score(student_list):
    while True:
        update_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
        students = find_student_by_id(student_list, update_id)
        if not find_student_by_id(student_list, update_id):
            print(f"Không tìm thấy Mã học viên {update_id}")
        else:
            students["math_score"] = input_validate_score("Nhập điểm toán: ")
            students["english_score"] = input_validate_score("Nhập điểm anh: ")
            print("Cập nhật thành công!")

            return


def  get_rank(average_score):
    if   average_score > 8:
        return "Giỏi"
    elif average_score > 6.5:
        return "Khá"
    elif average_score > 5:
        return "Trung bình"
    else:
        return "Yếu"   
     

def  evaluate_students(student_list):
    for i, s in enumerate(student_list):
        avg = (s["math_score"] + s["english_score"]) / 2
        print(f"Mã: {s["student_id"]:^10}| tên: {s["name"]:^20}| DTB: {avg:^5}| Xếp loại: {get_rank(avg):^10}")
def main():

    while True:
        menu()

        choice = input("Mời bạn nhập lựa chọn (1-5): ")

        match choice:
            case "1":
                display_student(students)
            case "2":
                add_student(students)
                
            case "3":
                update_score(students)
            case "4":
                evaluate_students(students)
            case "5":
                print("Thoát chương trình!")
                break
            case _:
                print("Lựa chọn của bạn không hợp lệ!")

main()
