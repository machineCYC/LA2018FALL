import util as u
import numpy as np


def map_symbol_2_index(symbol):
    '''
    Input:
    symbol: str

    Return:
    int
    '''
    dic = {
        "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9,
        "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19,
        "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25, "_":26, ".":27, ",":28, "?":29,
        "!":30
    }
    return dic.get(symbol)

def map_index_2_symbol(index):
    '''
    Input:
    index: int

    Return:
    str
    '''
    dic = {
        0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J",
        10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T",
        20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z", 26:"_", 27:".", 28:",", 29:"?",
        30:"!"
    }
    return dic.get(index)

def convert_text_2_matrix(text):
    '''
    Input:
    text: str

    Return:
    matrix: numpy array
    '''
    matrix = []
    for t in text:
        matrix.append(map_symbol_2_index(t))
    
    matrix = np.array(matrix).reshape(3, -1)
    return matrix

def convert_matrix_2_text(matrix):
    '''
    Input:
    matrix: numpy array

    Return:
    text: str
    '''
    text = ""
    for i in matrix.flatten():
        text += map_index_2_symbol(i)
    return text

def decode_stage(cipher_text, decode_matrix):
    '''
    Input:
    cipher_text: str
    decode_matrix: numpy array

    Return:
    plain_text: str
    '''
    cipher_matrix = convert_text_2_matrix(cipher_text)

    plain_matrix = np.dot(decode_matrix, cipher_matrix)
    plain_matrix = np.mod(plain_matrix, 31)

    plain_text = convert_matrix_2_text(plain_matrix)

    return plain_text

if __name__ == "__main__":

    cipher_text = "WPK_FJEIIXZ.OQFPM_"
    key = "4 9 -2 3 5 7 1 -6 11"
    plain_text_ans = "THI  S_I S_A N_A PPL E.."
    
    encode_matrix = np.fromstring(key, dtype=int, sep=" ").reshape(3, 3)
    decode_matrix = u.inv_key(encode_matrix)
    plain_text = decode_stage(cipher_text, decode_matrix)
    print(plain_text)

