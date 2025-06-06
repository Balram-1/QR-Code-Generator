import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import qrcode
from PIL import Image, ImageTk

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 QR Code Generator")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.config(bg="#121212")

        self.fg_color = "#ffffff"
        self.bg_color = "#000000"
        self.qr_image = None

        self.build_ui()

    def build_ui(self):
        title = tk.Label(self.root, text="QR Code Generator", fg="#00ffae", bg="#121212",
                         font=("Helvetica", 20, "bold"))
        title.pack(pady=10)

        self.input_text = tk.Text(self.root, height=6, width=50, bg="#1e1e1e", fg="#ffffff",
                                  insertbackground="white", font=("Courier", 12))
        self.input_text.pack(pady=10)
        

        color_frame = tk.Frame(self.root, bg="#121212")
        color_frame.pack(pady=5)

        tk.Button(color_frame, text="Foreground Color", command=self.pick_fg_color,
                  bg="#333", fg="#fff").pack(side=tk.LEFT, padx=10)
        tk.Button(color_frame, text="Background Color", command=self.pick_bg_color,
                  bg="#333", fg="#fff").pack(side=tk.LEFT, padx=10)

        tk.Button(self.root, text="Generate QR Code", command=self.generate_qr,
                  bg="#00ffae", fg="#000", font=("Arial", 12, "bold"), width=20).pack(pady=15)

        self.qr_preview_label = tk.Label(self.root, bg="#121212")
        self.qr_preview_label.pack(pady=10)

        tk.Button(self.root, text="Save QR Code", command=self.save_qr,
                  bg="#444", fg="#fff", font=("Arial", 11), width=15).pack(pady=5)

    def pick_fg_color(self):
        color = colorchooser.askcolor(title="Choose Foreground Color")
        if color[1]:
       
            messagebox.showinfo("Saved", f"QR Code saved to:\n{file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
