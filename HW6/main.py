from PIL import Image

import numpy as np
import matplotlib.pyplot as plt


def compress_svd(img, k):
    w, h, c = img.shape
    img_compress = np.zeros(shape=(w, h, c))
    for channel in range(3):
        img_channel = img[:, :, channel].reshape(w, h)
        u, s, v_T = np.linalg.svd(img_channel)

        if channel == 0:
            # print R channel rank
            print("R channel rank:{}".format(len(s!=0)))
            print("R channel rank:{}".format(cal_matrix_rank(img_channel)))

        s[k:] = 0
        s_matrix = np.zeros(shape=(w, h), dtype=float)
        for j in range(len(s)):
            s_matrix[j:j+1, j:j+1] = s[j]
        img_channel_compress = np.dot(np.dot(u, s_matrix), v_T)

        img_channel_compress -= img_channel_compress.min()
        img_channel_compress /= img_channel_compress.max()
        img_channel_compress *= 225
        img_compress[:, :, channel] = img_channel_compress
    return img_compress.astype(np.uint8)

def cal_compress_error(img, img_compress):
    original = img.ravel().astype(float)
    compress = img_compress.ravel().astype(float)
    error = np.linalg.norm(original - compress) / len(original)
    return error

def plot_curve(k_list, compress_error_list, path):
    plt.plot(k_list, compress_error_list, 'b', marker='.')

    plt.xlabel('K')
    plt.ylabel('approxomation error')
    plt.savefig(path)

def cal_matrix_rank(mat):
    rank = np.linalg.matrix_rank(mat)
    return rank

def main():
    # 2880, 1620
    img_path = './snow_man.jpeg'
    img = Image.open(img_path)
    # RGB
    # img.size
    # img.show()
    img = np.array(img)

    compress_error_list = []
    k_list = [1, 5, 50, 150, 400, 1050, 1289]
    for k in k_list:
        img_compress = compress_svd(img, k)
        compress_error = cal_compress_error(img, img_compress)
        compress_error_list.append(compress_error)
        print("k:{0}, compress error:{1}".format(k, compress_error))
        img_s = Image.fromarray(img_compress)
        img_s.save("./compress_{}.jpeg".format(k))

    plot_curve(k_list, compress_error_list, path='./plot_curve.png')

def plot_G_channel_by_5_k():
    '''
    This is for question 3
    '''
    img_path = './snow_man.jpeg'
    img = Image.open(img_path)
    img = np.array(img)

    w, h, c = img.shape
    img_G_channel = img[:, :, 1].reshape(w, h) # RGB, choose 1
    u, s, v_T = np.linalg.svd(img_G_channel)

    compress_img_sum = np.zeros(shape=(w, h), dtype=float)
    for r in range(5):
        s_matrix = np.zeros(shape=(w, h), dtype=float)
        s_matrix[r:r+1, r:r+1] = s[r]
        compress_img = np.dot(np.dot(u, s_matrix), v_T)
        compress_img_sum += compress_img

        compress_img -= compress_img.min()
        compress_img /= compress_img.max()
        compress_img *= 225
        compress_img = compress_img.astype(np.uint8)

        img_s = Image.fromarray(compress_img)
        img_s.save("./compress_A{}R.jpeg".format(r+1))

    compress_img_sum -= compress_img_sum.min()
    compress_img_sum /= compress_img_sum.max()
    compress_img_sum *= 225
    compress_img_sum = compress_img_sum.astype(np.uint8)
    img_s = Image.fromarray(compress_img_sum)
    img_s.save("./compress_ATop5R.jpeg")

if __name__ == '__main__':
    main()
    plot_G_channel_by_5_k()