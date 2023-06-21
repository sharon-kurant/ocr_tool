# Welcome to the Deep Catalog OCR tool

This tool uses the power of Tesseract and is complemented by *Automatic Page Segmentation (coming soon)*, and *Automatic Language Detection (coming sooner)*.

To use this tool follow the installation process:
- Download Tesseract:
  - [For MacOS](https://tesseract-ocr.github.io/tessdoc/Installation.html)
  - [For Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- During the installation process select the required Additional script data, and Langauge data
- Finish installation by clicking next until the end
- Add Tesseract to the *PATH*

Next, download this code, there are two options:
- Use `git clone`
- Download it as a zip, and extract it to its folder

Next, open the Terminal in the code location and run `pip install -r requirements.txt`

## Now you are ready to use the Deep Catalog OCR tool

To do so, while in the Terminal inside the folder:
`python main.py [folder_absolute_path] -l [language (optional)]`

Parameters:
- `folder_absolute_path` = folder with images for OCR
- `--lang` = heb/deu/eng/yid

After running the previous line of code, a new folder inside `ocr_output` will be created, and its content will be the OCR txt files for each image in `folder_absolute_path` 



