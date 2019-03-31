import sys
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_wave(x, path = './wave.png'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path)

def plot_ak(a, path = './freq.png'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path)

def CosineTrans(x, B):
    # TODO
    # implement cosine transform
    a = np.dot(np.linalg.inv(B), x)
    return a

def InvCosineTrans(a, B):
    # TODO
    # implement inverse cosine transform
    x = np.dot(B, a)
    return x

def gen_basis(N):
    # TODO
    K = N
    B = np.zeros(shape=(N, K))
    for k in range(K):
        for n in range(N):
            if k == 0:
                B[n, k] = 1 / np.sqrt(N)
            else:
                B[n, k] = np.sqrt(2 / N) * np.cos((n + 0.5) * k * np.pi / N)
    return B

def main(signal_path, case):

    x = np.loadtxt(signal_path)
    N = len(x)

    print("plot input signal")
    plot_wave(x, path = './{}_wave.png'.format(case))

    print("generate signal basis B")
    B = gen_basis(N)

    print("calculate basis frequency a")
    a = CosineTrans(x, B)

    print("plot basis frequency a")
    plot_ak(a, path = './{}_freq.png'.format(case))

    if case == "test":
        mask = np.where(a > 5)[0]
        for m in mask:
            a_temp = np.array([a[index] if index==m else 0 for index in range(len(a))])
            x_hat = InvCosineTrans(a_temp, B)

            print("plot particular signal")
            plot_wave(x_hat, path = './{}_wave_{}.png'.format(case, m))
    elif case == "homework":
        mask = np.where(a > 5)[0]
        
        a_f1 = np.array([a[index] if index==mask[0] else 0 for index in range(len(a))])
        f1 = InvCosineTrans(a_f1, B)

        a_f3 = np.array([a[index] if index==mask[2] else 0 for index in range(len(a))])
        f3 = InvCosineTrans(a_f3, B)

        print("plot particular signal")
        plot_wave(f1, path = './{}_wave_{}.png'.format(case, mask[0]))
        plot_wave(f3, path = './{}_wave_{}.png'.format(case, mask[2]))

if __name__ == '__main__':

    signal_path = "test.txt" # "r06944045.txt"
    case = "test" # homework
    main(signal_path, case)


