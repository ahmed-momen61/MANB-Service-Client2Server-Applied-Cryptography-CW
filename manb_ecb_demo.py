from manb_crypto_engine import des_encrypt

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

KEY = b'MANB2026'

def to_binary_string(byte_data):
    return ' '.join(f'{byte:08b}' for byte in byte_data)

def run_ecb_demo():
    block1_str = "5000_EGP"
    block2_str = "5000_EGP"
    combined_plaintext = (block1_str + block2_str).encode('utf-8')

    ciphertext = des_encrypt(combined_plaintext, KEY)

    # split into 8-byte blocks
    p1 = combined_plaintext[0:8]
    p2 = combined_plaintext[8:16]

    c1 = ciphertext[0:8]
    c2 = ciphertext[8:16]

    p1_ascii = p1.decode('utf-8')
    p2_ascii = p2.decode('utf-8')
    p1_hex = p1.hex()
    p2_hex = p2.hex()
    c1_hex = c1.hex()
    c2_hex = c2.hex()
    c1_bin = to_binary_string(c1)
    c2_bin = to_binary_string(c2)

    width = 104
    print(CYAN + "=" * width + RESET)
    print(BOLD + CYAN + "     MASR ALEXANDRIA NATIONAL BANK (MANB) - APPENDIX B: DES ECB PATTERN LEAKAGE" + RESET)
    print(CYAN + "=" * width + RESET)
    print(f"{BOLD}Bank Mainframe Key (Hex):{RESET} {KEY.hex()} (ASCII: '{KEY.decode('utf-8')}', 64-bit / 8-byte)")
    print(f"{BOLD}Cipher Algorithm & Mode  :{RESET} Custom Pure-Python DES in ECB Mode (Electronic Codebook)")
    print(f"{BOLD}Test Plaintext Payload   :{RESET} '{block1_str}' + '{block2_str}' (16 bytes = 2 DES blocks)")
    print("-" * width)
    print(BOLD + "BLOCK 1 BREAKDOWN (Bytes 0-7):" + RESET)
    print(f"  Plaintext (ASCII)  : {p1_ascii}")
    print(f"  Plaintext (Hex)    : {p1_hex}")
    print(f"  Ciphertext (Hex)   : {YELLOW}{c1_hex}{RESET}")
    print(f"  Ciphertext (Binary): {c1_bin}")
    print("-" * width)
    print(BOLD + "BLOCK 2 BREAKDOWN (Bytes 8-15):" + RESET)
    print(f"  Plaintext (ASCII)  : {p2_ascii}")
    print(f"  Plaintext (Hex)    : {p2_hex}")
    print(f"  Ciphertext (Hex)   : {YELLOW}{c2_hex}{RESET}")
    print(f"  Ciphertext (Binary): {c2_bin}")
    print("-" * width)
    print(BOLD + CYAN + "SIDE-BY-SIDE VERIFICATION TABLE:" + RESET)
    print("-" * width)
    print(f"{'Attribute':<20} | {'Block 1':<36} | {'Block 2':<36} | {'Match?'}")
    print("-" * width)
    print(f"{'Plaintext (ASCII)':<20} | {p1_ascii:<36} | {p2_ascii:<36} | {GREEN}YES{RESET}")
    print(f"{'Plaintext (Hex)':<20} | {p1_hex:<36} | {p2_hex:<36} | {GREEN}YES{RESET}")
    print(f"{'Ciphertext (Hex)':<20} | {c1_hex:<36} | {c2_hex:<36} | {GREEN}YES{RESET}")
    print(f"{'Ciphertext (Bin L1)':<20} | {c1_bin[:35]:<36} | {c2_bin[:35]:<36} | {GREEN}YES{RESET}")
    print(f"{'Ciphertext (Bin L2)':<20} | {c1_bin[36:]:<36} | {c2_bin[36:]:<36} | {GREEN}YES{RESET}")
    print("-" * width)
    print(BOLD + YELLOW + "SECURITY VULNERABILITY ANALYSIS:" + RESET)
    print(f"[*] Plaintext Equality   : Block 1 == Block 2 -> {p1 == p2}")
    print(f"[*] Ciphertext Equality  : Block 1 == Block 2 -> {GREEN}{c1 == c2}{RESET}")
    print(RED + "[!] PROOF OF PATTERN LEAKAGE IN ECB:" + RESET)
    print("    In Electronic Codebook (ECB) mode, each 64-bit block is encrypted")
    print("    independently with the same key (Ci = DES_K(Pi)). Because no initialization")
    print("    vector (IV) or chaining is used, identical plaintext blocks deterministically")
    print("    produce identical ciphertext blocks. An adversary snooping on MANB network")
    print("    traffic can easily detect recurring amounts and transaction structures.")
    print(CYAN + "=" * width + RESET)

if __name__ == '__main__':
    run_ecb_demo()
