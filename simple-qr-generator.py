import qrcode

# Function to generate QR code
def generate_qr_code(data, file_name, size):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(file_name)

# Prompt the user for URL and output file name
url = input("Enter the URL for the QR code: ")
output_file = input("Enter the output file name (without extension): ")
output_file += ".png"  # Append ".png" extension

# Prompt the user for the size of the QR code
size = int(input("Enter the size of the QR code (in pixels): "))

# Generate the QR code
generate_qr_code(url, output_file, size)
print(f"QR code generated and saved as {output_file}.")
