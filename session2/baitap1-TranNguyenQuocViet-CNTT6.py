

"""
- PHÂN TÍCH LỖI
Khi test với heart_rate = 135, chương trình đọc từ trên xuống và kiểm tra điều kiện if heart_rate > 100 đầu tiên. 
Vì 135 > 100 là đúng, nó in luôn ra YELLOW rồi thoát hẳn.

Lý do là cấu trúc if-elif-else chỉ chạy khối lệnh của điều kiện đúng đầu tiên mà nó gặp, 
sau đó bỏ qua toàn bộ phần bên dưới.

Vì bất kỳ nhịp tim nào > 120 thì cũng đã > 100, nên chương trình luôn bị kẹt ở điều kiện YELLOW. 
Nó sẽ không bao giờ chạy xuống được nhánh kiểm tra RED.
"""


# PHẦN SỬA CODE
print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))


if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")
