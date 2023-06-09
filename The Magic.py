import cv2
import numpy as np
image = cv2.imread("input/magic.tif", cv2.IMREAD_GRAYSCALE)

# # 1. 5*5 _0.04
# kernel = np.array([[0.04 , 0.04 , 0.04, 0.04, 0.04],
#                    [0.04 , 0.04 , 0.04, 0.04, 0.04],
#                    [0.04 , 0.04 , 0.04, 0.04, 0.04],
#                    [0.04 , 0.04 , 0.04, 0.04, 0.04],
#                    [0.04 , 0.04 , 0.04, 0.04, 0.04]])

# 2. 5*5 _ 1.0
# kernel = np.array([[1.0 , 1.0 , 1.0, 1.0, 1.0],
#                    [1.0 , 1.0 , 1.0, 1.0, 1.0],
#                    [1.0 , 1.0 , 1.0, 1.0, 1.0],
#                    [1.0 , 1.0 , 1.0, 1.0, 1.0],
#                    [1.0 , 1.0 , 1.0, 1.0, 1.0]])

# 3. 5*5 _ 5.0
# kernel = np.array([[5.0 , 5.0 , 5.0, 5.0, 5.0],
#                    [5.0 , 5.0 , 5.0, 5.0, 5.0],
#                    [5.0 , 5.0 , 5.0, 5.0, 5.0],
#                    [5.0 , 5.0 , 5.0, 5.0, 5.0],
#                    [5.0 , 5.0 , 5.0, 5.0, 5.0]])

# # 4. 3*3 _ 0.04
# kernel = np.array([[0.04, 0.04, 0.04],
#                    [0.04, 0.04, 0.04],
#                    [0.04, 0.04, 0.04]])

# # 5. 3*3 _ 1.0
# kernel = np.array([[1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0]])

# # 6. 3*3 _ 5.0
kernel = np.array([[5.0, 5.0, 5.0],
                   [5.0, 5.0, 5.0],
                   [5.0, 5.0, 5.0]])

result = cv2.filter2D(image, -1, kernel)
cv2.imwrite("output/magic6.jpg", result)
