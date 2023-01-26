import cv2
import numpy as np
import matplotlib.pyplot as plt

def check_benford(image):
    # read the image
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # get the image shape
    rows, cols = img.shape

    # create an array to count the number of pixels with a given first digit
    count = [0] * 10

    for r in range(rows):
        for c in range(cols):
            # get the intensity value of the pixel
            intensity = img[r][c]
            # get the first digit of the intensity value
            first_digit = int(str(intensity)[0])
            count[first_digit] += 1

    # calculate the proportion of pixels with a given first digit
    total_pixels = rows * cols
    proportions = [c/total_pixels for c in count]

    # calculate the expected proportion according to Benford's law
    expected_proportions = [np.log10(1 + 1/i) for i in range(1, 10)]

    # calculate the deviation from the expected proportion
    deviations = [abs(p - e) for p, e in zip(proportions, expected_proportions)]

    # print the results
    for i in range(1, 10):
        print(f"{i}: {proportions[i]:.4f} (expected: {expected_proportions[i-1]:.4f}, deviation: {deviations[i-1]:.4f})")
    proportions.pop(0)
    print(proportions)
    plt.bar(range(1, 10), proportions)
    plt.show()
    plt.bar(range(1, 10), deviations)
    plt.show()

check_benford("image.jpg")
