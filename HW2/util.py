import numpy as np

# key should be a numpy array
def inv_key(key):
    det = int(round(np.linalg.det(key)))
    inv = np.linalg.inv(key)
    tem = (inv * det)
    modinv = np.mod(det ** 29, 31)
    return np.around(np.mod(tem * modinv, 31)).astype(int)
