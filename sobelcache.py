from functools import cache
import numpy as np
import math
import cv2
import datetime

class SobelCache:
    def __init__(self, image_path, output_path):
        self.image = cv2.imread(image_path)
        self.kernel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        self.kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        self.detected_image = np.zeros(self.image.shape)
        self.output_path = output_path

    def convert_to_grey(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    
    @cache
    def edge_detector(self):
        self.convert_to_grey()
        kernel_size = self.kernel_x.shape[0]//2
        self.image = np.pad(self.image, pad_width= ([kernel_size, ], [kernel_size, ]), mode= 'constant', constant_values= (0, 0))

        for i in range(kernel_size, self.image.shape[0] - kernel_size):
            for j in range(kernel_size, self.image.shape[1] - kernel_size):
                x = self.image[i - kernel_size: i + kernel_size + 1, j - kernel_size: j + kernel_size + 1]
                x = x.flatten() * self.kernel_x.flatten()
                sum_x = x.sum()

                y = self.image[i - kernel_size: i + kernel_size + 1, j - kernel_size: j + kernel_size + 1]
                y = y.flatten() * self.kernel_y.flatten()
                sum_y = y.sum()

                self.detected_image[i - kernel_size][j - kernel_size] = math.sqrt(sum_x**2 + sum_y**2)
        cv2.imwrite(self.output_path, self.detected_image)

if __name__ == "__main__":
    input_path = 'images/input/' + sys.argv[1]
    output_path = 'images/output/' + sys.argv[2]
    start_time = datetime.datetime.now()
    sobel = SobelCache(input_path, output_path)
    sobel.edge_detector()
    end_time = datetime.datetime.now()
    print(f'Execution time: {end_time - start_time} sec.')