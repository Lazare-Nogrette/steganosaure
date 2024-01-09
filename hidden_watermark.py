import cv2
import os


def lsb1_stegano(image_path, message):
    image_array = cv2.imread(image_path)
    image_array = image_array - image_array%2
    binary_message = ''.join(format(ord(carac), '08b') for carac in message)

    if len(binary_message)> image_array.size:
        raise Exception("taille supérieur au nombre de pixel de l'image")
    
    nb_rows, nb_cols, nb_canals = image_array.shape
    index_binary_message = 0

    for index_row in range(nb_rows):
        for index_col in range(nb_cols):
            for index_canal in range(nb_canals):
                if index_binary_message < len(binary_message):
                    image_array[index_row, index_col, index_canal] += int(binary_message[index_binary_message])
                else:
                    break
            
    #cv2.imshow("grace", image_array)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    cv2.imwrite("watermarked_image.png", image_array)
    #plt.imshow(image_array%2*255)
    #plt.show()

if __name__ == "__main__":
    lsb1_stegano("grace.webp", "hello")






















