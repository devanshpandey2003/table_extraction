from paddleocr import PaddleOCR
from PIL import Image, ImageEnhance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def load_and_crop_image(image_path):
    image = Image.open(image_path)
    cropped_image = image.crop((27.33, 304.94, 318.15, 623.19))
    return cropped_image

def display_cropped_image(cropped_image):
    plt.imshow(cropped_image)
    plt.axis('off')
    plt.title("Cropped Image")
    plt.show()

def filter_red_text(image):
    image_array = np.array(image)
    red_mask = (image_array[:, :, 0] > 150) & (image_array[:, :, 1] < 100) & (image_array[:, :, 2] < 100)
    red_text_image = np.zeros_like(image_array)
    red_text_image[red_mask] = image_array[red_mask]
    return Image.fromarray(red_text_image)

def preprocess_image(image):
    preprocessed_image = image.convert('L')
    enhancer = ImageEnhance.Contrast(preprocessed_image)
    preprocessed_image = enhancer.enhance(2)
    return preprocessed_image

def extract_text_paddle_ocr(image):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    image_array = np.array(image)
    result = ocr.ocr(image_array, cls=True)

    if result is None or len(result) == 0:
        print("No text detected.")
        return ""

    extracted_text = ""
    for line in result:
        for word_info in line:
            extracted_text += word_info[1][0] + " "
    
    return extracted_text.strip()

def write_to_excel(extracted_text):
    data = [
        [1, "", "", "", "", "", ""],
        [2, "", "", "", "", "", ""],
        [3, "", "", "", "", "", ""],
        [4, "", "", "", "", "", ""],
        [5, "", "", "", "", "", ""],
        [6, "", "", "", "", "", ""],
        [7, "", "", "", "", "", ""],
        [8, "", "", "", "", "", ""],
        ["GRAND TOTAL", "", "", "", "", "", ""],
        ["OUT OF", "", "", "", "", "", ""]
    ]
    
    data[0][1] = extracted_text
    df = pd.DataFrame(data, columns=["Q.No", "a", "b", "c", "d", "e", "Total"])
    excel_file = "output_table.xlsx"
    df.to_excel(excel_file, index=False)
    print(f"Data written to Excel file: {excel_file}")

def main():
    image_path = "image.png"
    cropped_image = load_and_crop_image(image_path)
    display_cropped_image(cropped_image)
    red_text_image = filter_red_text(cropped_image)
    preprocessed_image = preprocess_image(red_text_image)
    preprocessed_image.save("cropped_image.png")
    extracted_text = extract_text_paddle_ocr(preprocessed_image)
    print(f"Extracted Text: {extracted_text}")
    write_to_excel(extracted_text)

if __name__ == "__main__":
    main()
