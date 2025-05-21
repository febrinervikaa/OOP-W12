import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menggambar di canvas
def draw(event):
    x, y = event.x, event.y
    r = 3
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="green")

# Fungsi untuk menyimpan info sayuran
def save_info():
    name = name_entry.get()
    note = note_text.get("1.0", tk.END).strip()

    if not name or not note:
        messagebox.showwarning("Peringatan", "Nama sayuran dan catatan tidak boleh kosong!")
        return

    messagebox.showinfo("Tersimpan", f"Informasi tentang sayuran '{name}' telah disimpan!")

# Window Utama
root = tk.Tk()
root.title("Belajar Sayuran")
root.geometry("520x550")
root.configure(bg="#e0ffe0")

# FRAME ATAS: Input Nama Sayuran
top_frame = tk.Frame(root, bg="#e0ffe0")
top_frame.pack(pady=10)

name_label = tk.Label(top_frame, text="Nama Sayuran:", font=("Arial", 12), bg="#e0ffe0")
name_label.pack(side=tk.LEFT)

name_entry = tk.Entry(top_frame, width=30)
name_entry.pack(side=tk.LEFT, padx=5)

# FRAME TENGAH: Canvas Menggambar Sayuran
middle_frame = tk.Frame(root, bg="#e0ffe0")
middle_frame.pack(pady=10)

canvas_label = tk.Label(middle_frame, text="Gambar Sayuran (klik dan drag):", font=("Arial", 12), bg="#e0ffe0")
canvas_label.pack()

canvas = tk.Canvas(middle_frame, width=400, height=200, bg="white", borderwidth=2, relief="ridge")
canvas.pack()
canvas.bind("<B1-Motion>", draw)

# FRAME BAWAH: Catatan Manfaat Sayur
bottom_frame = tk.Frame(root, bg="#e0ffe0")
bottom_frame.pack(pady=10)

note_label = tk.Label(bottom_frame, text="Catatan / Manfaat Sayur:", font=("Arial", 12), bg="#e0ffe0")
note_label.pack()

note_text = tk.Text(bottom_frame, width=55, height=6)
note_text.pack()

# BUTTON SIMPAN
save_button = tk.Button(root, text="Simpan Informasi", command=save_info, bg="green", fg="white", font=("Arial", 11, "bold"))
save_button.pack(pady=15)

# Jalankan Program
root.mainloop()
