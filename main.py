import cv2
import pytesseract
import click
import os
import glob 

@click.command()
@click.argument("folder_path", type=click.Path(exists=True), required=True)
@click.argument("output_path", type=click.Path(exists=False), required=False)
# @click.option("-s", "--seg", prompt="Enter segmentation True/False", help="True/False for segmentation")
# @click.option("-l", "--lang", prompt="Enter files language", help="The language of the files")
def ocr_file(folder_path: str, output_path: str, s: bool=False):

    output_path = folder_path.split(os.sep)[-1]
    print(output_path)
    output_path = "ocr_output" + os.sep + output_path
    os.makedirs(output_path, exist_ok = True)
    
    files = [name for name in glob.glob(folder_path + os.sep + '*.jpg')]
    
    for f in files:
        img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        img = cv2.medianBlur(img,5)
        img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
        
        res = pytesseract.image_to_string(img, lang='deu')
        text_file = open(output_path + os.sep + f.split(os.sep)[-1][:-3] + 'txt', "w", encoding="utf-8")
        text_file.write(res)
    
if __name__ == "__main__":
    ocr_file()