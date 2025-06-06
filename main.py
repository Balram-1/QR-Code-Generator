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
            self.fg_color = color[1]

    def pick_bg_color(self):
        color = colorchooser.askcolor(title="Choose Background Color")
        if color[1]:
            self.bg_color = color[1]

    def generate_qr(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter some text to generate QR.")
            return

        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.fg_color, back_color=self.bg_color).convert("RGB")

        self.qr_image = img

        img_resized = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img_resized)
        self.qr_preview_label.config(image=img_tk)
        self.qr_preview_label.image = img_tk

    def save_qr(self):
        if not self.qr_image:
            messagebox.showwarning("No QR", "Generate a QR code first.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg")])
        if file_path:
            self.qr_image.save(file_path)
            messagebox.showinfo("Saved", f"QR Code saved to:\n{file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
