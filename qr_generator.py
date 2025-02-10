import qrcode
import uuid

id = str(uuid.uuid4())  

def generate_qr(text, file="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(file)  

    print(f"QR Code foi gerado e salvo como {file}")

text_input = input("Enter the text or URL to generate the QR Code: ")

file_name = f"{id}-qrcode.png"

generate_qr(text_input, file_name)