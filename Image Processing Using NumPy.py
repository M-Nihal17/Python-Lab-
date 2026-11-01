import numpy as np

img = np.array([[10, 50, 100, 150],
                [20, 60, 110, 160],
                [30, 70, 120, 170],
                [40, 80, 130, 180]])

print("Original Image:\n", img)

# Reshaping
print("Reshaped:\n", img.reshape(2, 8))
print("Flattened:\n", img.flatten())

# Slicing
print("Centre Region:\n", img[1:3, 1:3])
print("First Row:", img[0])
print("Last Column:", img[:, -1])

# Brightness Adjustment
print("Bright Image:\n", np.clip(img + 100, 0, 255))
print("Dark Image:\n", np.clip(img - 50, 0, 255))

# Matrix Multiplication
flip = np.fliplr(np.eye(4, dtype=int))
print("Horizontal Flip:\n", img @ flip)
print("Vertical Flip:\n", flip @ img)