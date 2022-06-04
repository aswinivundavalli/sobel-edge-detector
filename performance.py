
from sobel import Sobel
from sobelparallel import SobelParallel
from sobelcache import SobelCache
from sobelparallelcache import SobelParallelCache
import time

if __name__ == "__main__":
    for i in range(1, 11):
        input_image = 'images/input/i_' + str(i) + '.jpeg'
        output_image = 'images/output/o_' + str(i) + '.jpeg'
        start_time = time.time()
        sobel = Sobel(input_image, output_image)
        sobel.edge_detector()
        end_time = time.time()
        print(f'Execution time for sequential implementation: {end_time - start_time} secs.')

        start_time = time.time()
        sobel = SobelCache(input_image, output_image)
        sobel.edge_detector()
        end_time = time.time()
        print(f'Execution time for sequetial implementation with cache advantage: {end_time - start_time} secs.')

        start_time = time.time()
        sobel = SobelParallel(input_image, output_image)
        sobel.edge_detector()
        end_time = time.time()
        print(f'Execution time for parallel implementation: {end_time - start_time} secs.')

        start_time = time.time()
        sobel = SobelParallelCache(input_image, output_image)
        sobel.edge_detector()
        end_time = time.time()
        print(f'Execution time for parallel implementation with cache advantage: {end_time - start_time} secs.')
