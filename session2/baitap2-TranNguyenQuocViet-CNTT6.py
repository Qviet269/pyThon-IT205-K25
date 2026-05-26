
"""
Phân tích lỗi

Code sai logic ở chữ or.

Khi chạy test case (tuổi = 16, cân nặng = 55):

Tuổi: 16 >= 18 (Sai).

Cân nặng: 55 >= 50 (Đúng).

Bản chất của or (hoặc) là chỉ cần 1 vế Đúng thì nó sẽ duyệt cho qua luôn. 
Máy thấy cân nặng đạt chuẩn nên lập tức in ra "ĐỦ ĐIỀU KIỆN", 
bỏ lọt trường hợp chưa đủ tuổi.

Khác biệt là: or chỉ cần 1 vế Đúng, còn and bắt buộc cả 2 vế cùng Đúng. 
Quy định y khoa yêu cầu đáp ứng đồng thời cả tuổi và cân nặng, nên bắt buộc phải dùng and.
"""

# phần đã sữa lại code
print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra điều kiện hiến máu 
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:

    print("Result: NOT ELIGIBLE. Reason: You must be at least 18 years old AND weigh at least 50 kg.")