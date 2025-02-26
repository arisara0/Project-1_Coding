import tkinter as tk
from tkinter import messagebox

def calculate_water_bill(consumption):
    """
    คำนวณค่าน้ำประปาสำหรับประเภทที่ 1 ที่พักอาศัย (Residence) ตามปริมาณการใช้น้ำ (ลบ.ม.)
    """
    rates = [
        (0, 10, 9.50),    # 0-10 ลบ.ม. อัตรา 9.50 บาท/ลบ.ม. แต่ไม่ต่ำกว่า 90 บาท
        (11, 30, 8.50),   # 11-30 ลบ.ม. อัตรา 8.50 บาท/ลบ.ม.
        (31, 40, 10.03),  # 31-40 ลบ.ม. อัตรา 10.03 บาท/ลบ.ม.
        (41, 50, 10.35),  # 41-50 ลบ.ม. อัตรา 10.35 บาท/ลบ.ม.
        (51, 60, 10.68),  # 51-60 ลบ.ม. อัตรา 10.68 บาท/ลบ.ม.
        (61, 70, 11.00),  # 61-70 ลบ.ม. อัตรา 11.00 บาท/ลบ.ม.
        (71, 80, 11.33),  # 71-80 ลบ.ม. อัตรา 11.33 บาท/ลบ.ม.
        (81, 90, 12.50),  # 81-90 ลบ.ม. อัตรา 12.50 บาท/ลบ.ม.
        (91, 100, 12.82), # 91-100 ลบ.ม. อัตรา 12.82 บาท/ลบ.ม.
        (101, 120, 13.15),# 101-120 ลบ.ม. อัตรา 13.15 บาท/ลบ.ม.
        (121, 160, 13.47),# 121-160 ลบ.ม. อัตรา 13.47 บาท/ลบ.ม.
        (161, 200, 13.80),# 161-200 ลบ.ม. อัตรา 13.80 บาท/ลบ.ม.
        (201, float('inf'), 14.45) # มากกว่า 200 ลบ.ม. อัตรา 14.45 บาท/ลบ.ม.
    ]

    total_cost = 0.0
    remaining_consumption = consumption

    if consumption > 0 and consumption <= 10:
        return max(90.00, consumption * 9.50)  # กรณีต่ำกว่า 10 ลบ.ม. ต้องไม่ต่ำกว่า 90 บาท

    for lower, upper, rate in rates:
        if remaining_consumption > 0:
            if remaining_consumption > upper - lower + 1:
                total_cost += (upper - lower + 1) * rate
                remaining_consumption -= (upper - lower + 1)
            else:
                total_cost += remaining_consumption * rate
                break

    return total_cost

# ฟังก์ชันที่จะเรียกเมื่อกดปุ่มคำนวณ
def calculate():
    try:
        usage = float(entry_usage.get())
        bill = calculate_water_bill(usage)
        result_label.config(text=f"ค่าน้ำที่ต้องชำระ: {bill:.2f} บาท")
    except ValueError:
        messagebox.showerror("ข้อมูลไม่ถูกต้อง", "กรุณาป้อนข้อมูลที่เป็นตัวเลข")

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("คำนวณค่าน้ำประปา")

# สร้าง Label และ Entry สำหรับป้อนข้อมูลการใช้น้ำ
label_usage = tk.Label(root, text="ป้อนปริมาณการใช้น้ำ (ลบ.ม.):")
label_usage.pack(pady=10)

entry_usage = tk.Entry(root)
entry_usage.pack(pady=5)

# สร้างปุ่มคำนวณ
calculate_button = tk.Button(root, text="คำนวณ", command=calculate)
calculate_button.pack(pady=20)

# สร้าง Label สำหรับแสดงผลลัพธ์
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# เริ่มโปรแกรม GUI
root.mainloop()
