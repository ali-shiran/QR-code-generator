import qrcode
import uuid
import platform
import subprocess
import os


def receiver() -> str :

    url = input("Please enter the URL you would like to generate QR code for: ").strip()

    return url

def data_file_path(filename: str) -> str :

    script_dir = os.path.dirname(__file__)

    file_path = os.path.join(script_dir, filename)

    return file_path

def check_existence(filename: str) -> bool :

    file_path = data_file_path(filename)

    file_existence = os.path.exists(file_path)

    return file_existence

def name_manager() -> str :

    unique_id = uuid.uuid4().hex[:8]

    return f"qr_{unique_id}.png"

def qr_generator(data: str, filepath: str) -> None :

    qr = qrcode.QRCode(version = 1, box_size = 10, border = 2)

    qr.add_data(data)

    qr.make(fit = True)

    img = qr.make_image(fill_color = 'black', back_color = 'white')

    img.save(filepath)

    return

def image_opener(filepath: str) -> None :

    try :

        if platform.system() == 'Windows' :

            os.startfile(filepath)

        elif platform.system() == 'Darwin' :

            subprocess.call(('open', filepath))

        else :

            subprocess.call(('xdg-open', filepath))

    except Exception as e :

        print(f"Could not open image automatically: {e}")

def main() :

    url = receiver()

    filename = name_manager()

    file_path = data_file_path(filename)

    qr_generator(url, file_path)

    image_opener(file_path)


if __name__ == "__main__" :

    main()
