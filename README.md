# Project 5: Image Edge Detection

As part of the project we have implemented edge detection of an image using sobel's algorithm. We have implemented sobel algorithm in python with 4 different approaches: sequential(single threaded), sequential with caching, parallel(multithreaded), parallel with caching.

## Sobel Edge Detection
Edges in an images are the combination of points where there is a sudden change in pixel's intensity. Sobel's algorithm works on detecting 2 kinds if edges: horizantal and vertical.
For horizantal edges, The input image is convolved with horizantal mask: [[1, 2, 1], [0, 0, 0], [-1, -2, -1]] and for vertical edges, the input image is convolved with vertical mask: [[1, 0, -1], [2, 0, -2], [1, 0, -1]]. Once the image is processed in horizantal and vertical directions, we can add the magnitude of corresponding pixels to generate the final edge detected image.


## Implementations

### Sequential
#### Theoretical concept
In this approach we used a single thread to perform convolution of each 3*3 subarray of input image with horizantal and vertical masks. 

#### Code organization
The file named **sobel** located in main directory is implemented using the afore-mentioned approach.

#### How to run it
 `python3 sobel.py <relative image path of the images located in /images/input folder>`
 `python3 sobel.py i_1.jpeg`

### Sequential with cache advantage
#### Theoretical concept
In this approach we used a single thread to perform convolution of each 3*3 subarray of input image with horizantal and vertical masks. Also, we used python's inbuilt cache module to cache the sub computations of convolution.

#### Code organization
The file named **sobelcache** located in main directory is implemented using the afore-mentioned approach.

#### How to run it
 `python3 sobelcache.py <relative path of the images located in /images/input folder> <ouput image name, stored in /images/output folder>`
 `python3 sobelcache.py i_1.jpeg o_1.jpeg`


### Multithreading with pymp
#### Theoretical concept
In this approach we used mutlithreading using pymp where the parallelisation is done for convolving each 3*3 subarray of input image with horizantal and vertical masks. 

#### Code organization
The file named **sobelparallel** located in main directory is implemented using the afore-mentioned approach.

#### How to run it
 `python3 sobelparallel.py <relative path of the images located in /images/input folder> <ouput image name, stored in /images/output folder>`
 `python3 sobelparallel.py i_1.jpeg o_1.jpeg`


 ### Multithreading with pymp and cache advantage
#### Theoretical concept
In this approach we used mutlithreading using pymp where the parallelisation is done for convolving each 3*3 subarray of input image with horizantal and vertical masks. Also, we used python's inbuilt cache module to cache the sub computations of convolution.

#### Code organization
The file named **sobelparallelcache** located in main directory is implemented using the afore-mentioned approach.

#### How to run it
 `python3 sobelparallelcache.py <relative path of the images located in /images/input folder> <ouput image name, stored in /images/output folder>`
 `python3 sobelparallelcache.py i_1.jpeg o_1.jpeg`


## Metrics and tests
The tests were performed on Macbook M1 Air (8GB Ram, ARM arch) with 8 cores.

Execution time is used as a metric to evaluate the performance of these 4 approaches. Run `python3 performance.py` to find the execution times of each of the 4 approaches for various input sizes.

The following table shows the execution times of 4 approaches for various input image sizes, the number of threads for multithreaded programns were fixed to be 8.


|Image size(px)|	sequential |	sequential(cache) |	parallel | parallel(cache) |
| ------ | ------ | ------ | ------ | ------ |
|200 * 200	| 0.18193 |	0.17923 | 0.450148 | 0.31006 |
|300 * 300	| 0.40265 |	0.401669	| 0.38508 |	0.36704	|
|400 * 400	| 0.714027	| 0.70395	| 0.48833	| 0.449406	|
|500 * 500	| 1.12169 |	1.11464	| 0.57009	| 0.62474	|
|600 * 600	| 0.23437 |	0.22831	| 0.33637	| 0.31655	|
|800 * 800|0.22549 |0.21619 |0.31930 |0.31291 |
|900 * 900|0.22528 |0.21854 |0.31352 | 0.31723 |
|1000 * 687|3.07390 |	3.01972 |1.258894 | 1.071236 |
|1000 * 1000|4.59277 |4.21300 |1.84132 | 1.66837 |
|1600 * 1000|7.29160  |7.18333  |2.20366 |2.17059 |
|2200 * 1500|15.66130 |15.40999 |4.35557 |4.29441 |
|2560 * 1460|16.85646 |16.56266  |4.77750 |4.80002 |

![Execution Time Vs Size](images/plot.png?raw=true "Title")


## Outputs
![Screenshot of the sample input](images/input/i_3.jpeg?raw=true "Title")
![Screenshot of the sample output](images/output/o_3.jpeg?raw=true "Title")



## Findings and Interpretations
- For lower input sizes, sequential and parallel programs have comparable execution times. As the input size increases we can notice the higher speed up for multithreaded programs.
- With caching, we have seen slightly lower execution times(negligible difference). This is because of the lower kernel size, in this algorithm we used 3*3 matrix, so each sub computation of convolution is only used thrice. 
