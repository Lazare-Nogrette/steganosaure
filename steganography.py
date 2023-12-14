import cv2
import os

def lsb1_stegano(image_path, message):
    image_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image_array = image_array - image_array%2
    binary_message = ''.join(format(ord(carac), '08b') for carac in message)

    if len(binary_message)> image_array.size():
        raise Exception("taille supérieur au nombre de pixel de l'image")
    
    nb_rows, nb_cols = image_array.shape
    for index_row in range(nb_rows):
        for index_col in range(nb_cols):
            if index_col *nb_cols + index_col < len(binary_message):
                image_array[index_row, index_col] += int(binary_message[index_row * nb_cols + index_col])
            else:
                break
            
    cv2.imshow("grace", image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    lsb1_stegano("grace.webp", "")






















