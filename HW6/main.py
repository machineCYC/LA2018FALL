from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

# 2025, 1289
path = 'D:/Git/LA2018FALL/Linear_algbra_2018-master/Linear_algbra_2018-master/hw6/img/vegetable_english.jpg'

def compress_svd(img, k):

    h, w, c = img.shape
    img_compress = np.zeros(shape=(h, w, c))
    for channel in range(3):
        img_channel = img[:, :, channel].reshape(h, w)
        u, s, v_T = np.linalg.svd(img_channel)

        s[k:] = 0
        s_matrix = np.zeros(shape=(h, w), dtype=float)
        for j in range(len(s)):
            s_matrix[j:j+1, j:j+1] = s[j]
        img_channel_compress = np.dot(np.dot(u, s_matrix), v_T)

        img_channel_compress -= img_channel_compress.min()
        img_channel_compress /= img_channel_compress.max()
        img_channel_compress *= 225
        img_compress[:, :, channel] = img_channel_compress
    return img_compress.astype(np.uint8)

def cal_compress_ratio(img, img_compress):
    original = img.ravel().astype(float)
    compress = img_compress.ravel().astype(float)
    ratio = np.linalg.norm(original - compress) / len(original)
    return ratio

def plot_curve(k_list, compress_ratio_list, path):
    plt.plot(k_list, compress_ratio_list, 'b', marker='.')

    plt.xlabel('K')
    plt.ylabel('approxomation error')
    plt.savefig(path)

# 2880, 1620
img_path = './snow_man.jpeg'
img = Image.open(img_path)
# img.show()
img = np.array(img)

compress_ratio_list = []
k_list = [1, 5, 50, 150, 400, 1050, 1289]
for k in k_list:
    img_compress = compress_svd(img, k)
    compress_ratio = cal_compress_ratio(img, img_compress)
    compress_ratio_list.append(compress_ratio)
    print("k:{0}, compress ratio:{1}".format(k, compress_ratio))
    img_s = Image.fromarray(img_compress)
    img_s.save("./compress_{}.jpeg".format(k))

plot_curve(k_list, compress_ratio_list, path='./plot_curve.png')
print("GG")