import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("ฟอร์มสมัครงาน (รายละเอียดครบ)")
window.geometry("1920x1080")

# ========== ส่วนหัว =============
title = tk.Label(window, text="ฟอร์มสมัครงาน", font=("TH Sarabun New", 28))
title.pack(pady=10)

frame = tk.Frame(window)
frame.pack(pady=10)

# ========== ข้อมูลส่วนตัว ==========
section1 = tk.Label(frame, text="ข้อมูลส่วนตัว", font=("TH Sarabun New", 20, "bold"))
section1.grid(row=0, column=0, sticky="w", pady=10)

# ชื่อ-สกุล
tk.Label(frame, text="ชื่อ-สกุล", font=("TH Sarabun New", 20)).grid(row=1, column=0, sticky="w")
entry_name = tk.Entry(frame, width=40)
entry_name.grid(row=1, column=1, padx=10, pady=5)

# อายุ
tk.Label(frame, text="อายุ", font=("TH Sarabun New", 20)).grid(row=2, column=0, sticky="w")
entry_age = tk.Entry(frame, width=20)
entry_age.grid(row=2, column=1, sticky="w", padx=10, pady=5)

# วันเดือนปีเกิด
tk.Label(frame, text="วันเดือนปีเกิด (DD/MM/YYYY)", font=("TH Sarabun New", 20)).grid(row=3, column=0, sticky="w")
entry_birth = tk.Entry(frame, width=25)
entry_birth.grid(row=3, column=1, sticky="w", padx=10, pady=5)

# เพศ
tk.Label(frame, text="เพศ", font=("TH Sarabun New", 20)).grid(row=4, column=0, sticky="w")
gender_var = tk.StringVar()
tk.Radiobutton(frame, text="ชาย", variable=gender_var, value="ชาย").grid(row=4, column=1, sticky="w")
tk.Radiobutton(frame, text="หญิง", variable=gender_var, value="หญิง").grid(row=4, column=1, padx=60, sticky="w")
tk.Radiobutton(frame, text="LGPTQ", variable=gender_var, value="อื่นๆ").grid(row=4, column=1, padx=120, sticky="w")

# อีเมล
tk.Label(frame, text="อีเมล", font=("TH Sarabun New", 20)).grid(row=5, column=0, sticky="w")
entry_email = tk.Entry(frame, width=40)
entry_email.grid(row=5, column=1, padx=10, pady=5)

# เบอร์โทร
tk.Label(frame, text="เบอร์โทร", font=("TH Sarabun New", 20)).grid(row=6, column=0, sticky="w")
entry_phone = tk.Entry(frame, width=40)
entry_phone.grid(row=6, column=1, padx=10, pady=5)

# ที่อยู่
tk.Label(frame, text="ที่อยู่", font=("TH Sarabun New", 20)).grid(row=7, column=0, sticky="nw")
entry_address = tk.Text(frame, width=45, height=4)
entry_address.grid(row=7, column=1, padx=10, pady=5)

# ========== ข้อมูลการศึกษา ==========
section2 = tk.Label(frame, text="ข้อมูลการศึกษา", font=("TH Sarabun New", 20, "bold"))
section2.grid(row=8, column=0, sticky="w", pady=20)

# ระดับการศึกษา
tk.Label(frame, text="ระดับการศึกษา", font=("TH Sarabun New", 20)).grid(row=9, column=0, sticky="w")
edu_level = ttk.Combobox(frame, values=["มัธยม", "ปวช", "ปวส", "ปริญญาตรี", "ปริญญาโท", "อื่นๆ"], width=37)
edu_level.grid(row=9, column=1, padx=10, pady=5)

# สาขาวิชา
tk.Label(frame, text="สาขาวิชา", font=("TH Sarabun New", 20)).grid(row=10, column=0, sticky="w")
entry_major = tk.Entry(frame, width=40)
entry_major.grid(row=10, column=1, padx=10, pady=5)

# ========== ประสบการณ์ทำงาน ==========
section3 = tk.Label(frame, text="ประสบการณ์ทำงาน", font=("TH Sarabun New", 20, "bold"))
section3.grid(row=11, column=0, sticky="w", pady=20)

tk.Label(frame, text="รายละเอียด", font=("TH Sarabun New", 20)).grid(row=12, column=0, sticky="nw")
entry_exp = tk.Text(frame, width=45, height=5)
entry_exp.grid(row=12, column=1, padx=10, pady=5)

# ========== ทักษะพิเศษ / ความสามารถ ==========
section4 = tk.Label(frame, text="ทักษะพิเศษ / ความสามารถ", font=("TH Sarabun New", 20, "bold"))
section4.grid(row=13, column=0, sticky="w", pady=20)

entry_skill = tk.Text(frame, width=45, height=5)
entry_skill.grid(row=13, column=1, padx=10, pady=5)

# ปุ่มบันทึก
submit_btn = tk.Button(window, text="บันทึกข้อมูลของคุณลงในประวัติฟอร์ม", font=("TH Sarabun New", 20), width=30, bg="#4CAF50", fg="white")
submit_btn.pack(pady=20)

window.mainloop()
