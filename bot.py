import tkinter as tk
import qrcode

# Create a function to generate the QR code
def generate_qr_code():
    # Get the URL from the user
    url = url_entry.get()
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    # Create a tkinter PhotoImage object from the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img_tk = tk.PhotoImage(master=qr_frame, data=img.tobytes())
    # Display the QR code in the tkinter window
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# Create the tkinter window
window = tk.Tk()
window.title("QR Code Generator")

# Create a frame for the URL entry and button
url_frame = tk.Frame(master=window, padx=10, pady=10)
url_frame.pack(fill=tk.X)

# Add a label and entry for the URL
url_label = tk.Label(master=url_frame, text="URL:")
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(master=url_frame)
url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Add a button to generate the QR code
generate_button = tk.Button(master=window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create a frame for the QR code image
qr_frame = tk.Frame(master=window, padx=10, pady=10)
qr_frame.pack()

# Add a label to display the QR code image
qr_label = tk.Label(master=qr_frame)
qr_label.pack()

# Run the tkinter event loop
window.mainloop()
