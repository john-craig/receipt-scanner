from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
Image.MAX_IMAGE_PIXELS = 933120000

CONFIG = r'--tessdata-dir "/usr/share/tessdata"'

PATH='./receipt.png'

#scanimage --mode gray --resolution 200 --output-file receipt.png
#tesseract receipt.png output -l eng

def read_receipt():
    image = Image.open('./receipt.png', mode='r')
    print(pytesseract.image_to_string(image))



read_receipt()
