import tkinter as tk

# 1. Khởi tạo cửa sổ gốc
root = tk.Tk()
root.title("Ứng dụng đầu tiên của tam - UHL")
root.geometry("500x500")

# 2. Tạo thành phần hiển thị văn bản (Label)
nhan_chao = tk.Label(root, text="Chào mừng Trần Văn Tâm!")
nhan_chao.pack(pady=50) # Đưa nhãn vào cửa sổ và tạo khoảng cách lề

# 3. Duy trì cửa sổ (Vòng lặp chính)
root.mainloop()