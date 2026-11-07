# initial permutation
IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# final permutation (inverse of ip)
FP_TABLE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# expansion box: 32 bits -> 48 bits
E_BOX = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# permutation box: 32 bits -> 32 bits
P_BOX = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# pc-1 drops parity bits (64 -> 56 bits)
PC1_TABLE = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# pc-2 selects 48 bits for round subkey
PC2_TABLE = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# left shift schedule per round
KEY_SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# s-boxes s1 to s8
S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

def bytes_to_bits(data):
    bits = []
    for byte in data:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    return bits

def bits_to_bytes(bits):
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte_val = 0
        for bit in bits[i:i + 8]:
            byte_val = (byte_val << 1) | bit
        byte_array.append(byte_val)
    return bytes(byte_array)

def permute(bits, table):
    # map 1-indexed table positions to 0-indexed list
    return [bits[pos - 1] for pos in table]

def xor_bits(a, b):
    return [bit_a ^ bit_b for bit_a, bit_b in zip(a, b)]

def circular_left_shift(bits, shift_count):
    return bits[shift_count:] + bits[:shift_count]

def generate_subkeys(key_8bytes):
    if len(key_8bytes) != 8:
        raise ValueError("DES key must be exactly 8 bytes (64 bits).")

    # pc-1 drops parity bits to 56 bits
    key_bits = bytes_to_bits(key_8bytes)
    permuted_key = permute(key_bits, PC1_TABLE)

    # split into two 28-bit halves
    c = permuted_key[:28]
    d = permuted_key[28:]

    # 16 rounds of shifts + pc-2 compression to 48-bit subkeys
    subkeys = []
    for shift in KEY_SHIFT_SCHEDULE:
        c = circular_left_shift(c, shift)
        d = circular_left_shift(d, shift)
        round_subkey = permute(c + d, PC2_TABLE)
        subkeys.append(round_subkey)

    return subkeys

def feistel_function(r_bits, subkey_48bits):
    # expand 32 bits to 48
    expanded_r = permute(r_bits, E_BOX)
    xored = xor_bits(expanded_r, subkey_48bits)

    # 8 s-boxes: outer 2 bits give row, inner 4 bits give col
    s_box_output = []
    for i in range(8):
        chunk = xored[i * 6 : (i + 1) * 6]
        row = (chunk[0] << 1) | chunk[5]
        col = (chunk[1] << 3) | (chunk[2] << 2) | (chunk[3] << 1) | chunk[4]
        val = S_BOXES[i][row][col]
        s_box_output.extend([(val >> 3) & 1, (val >> 2) & 1, (val >> 1) & 1, val & 1])

    # final p-box permutation
    return permute(s_box_output, P_BOX)

def des_block_process(block_8bytes, subkeys):
    block_bits = bytes_to_bits(block_8bytes)

    # initial permutation & split to 32-bit halves
    permuted_block = permute(block_bits, IP_TABLE)
    left = permuted_block[:32]
    right = permuted_block[32:]

    # 16 feistel rounds
    for subkey in subkeys:
        next_left = right
        f_result = feistel_function(right, subkey)
        next_right = xor_bits(left, f_result)
        left, right = next_left, next_right

    # 32-bit swap at round 16 (r16 + l16) & final inverse permutation
    pre_output = right + left
    cipher_bits = permute(pre_output, FP_TABLE)
    return bits_to_bytes(cipher_bits)

def custom_pad(data_bytes, block_size=8):
    # pkcs7 pad to multiple of 8 bytes
    padding_len = block_size - (len(data_bytes) % block_size)
    if padding_len == 0:
        padding_len = block_size
    return data_bytes + bytes([padding_len] * padding_len)

def custom_unpad(padded_bytes, block_size=8):
    if len(padded_bytes) == 0 or len(padded_bytes) % block_size != 0:
        raise ValueError("Invalid padded data length.")

    # check padding bytes match length
    padding_len = padded_bytes[-1]
    if padding_len < 1 or padding_len > block_size:
        raise ValueError("Invalid PKCS#7 padding byte.")

    if padded_bytes[-padding_len:] != bytes([padding_len] * padding_len):
        raise ValueError("Corrupted PKCS#7 padding.")

    return padded_bytes[:-padding_len]

def des_encrypt(plaintext_bytes, key_8bytes):
    if len(plaintext_bytes) % 8 != 0:
        raise ValueError("Plaintext length must be a multiple of 8 bytes.")

    subkeys = generate_subkeys(key_8bytes)
    chunks = []
    for i in range(0, len(plaintext_bytes), 8):
        chunks.append(des_block_process(plaintext_bytes[i:i + 8], subkeys))
    return b"".join(chunks)

def des_decrypt(ciphertext_bytes, key_8bytes):
    if len(ciphertext_bytes) % 8 != 0:
        raise ValueError("Ciphertext length must be a multiple of 8 bytes.")

    subkeys = generate_subkeys(key_8bytes)
    # feistel decryption uses subkeys in reverse order (k16 to k1)
    reversed_subkeys = list(reversed(subkeys))
    chunks = []
    for i in range(0, len(ciphertext_bytes), 8):
        chunks.append(des_block_process(ciphertext_bytes[i:i + 8], reversed_subkeys))
    return b"".join(chunks)
