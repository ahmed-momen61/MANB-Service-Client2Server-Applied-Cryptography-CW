import socket
import sys
from manb_crypto_engine import custom_unpad, des_decrypt

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

KEY = b'MANB2026'
HOST = '127.0.0.1'
PORT = 5000
BLOCK_SIZE = 8

def parse_transaction(plaintext):
    # parse payload format
    details = {
        "FROM": "Unknown",
        "TO": "Unknown",
        "AMT": "0 EGP",
        "FEE": "20 EGP"
    }
    parts = plaintext.split("|")
    for part in parts:
        if part.startswith("FROM:"):
            details["FROM"] = part.split(":", 1)[1]
        elif part.startswith("TO:"):
            details["TO"] = part.split(":", 1)[1]
        elif part.startswith("AMT:"):
            details["AMT"] = part.split(":", 1)[1]
        elif part.startswith("FEE:"):
            details["FEE"] = part.split(":", 1)[1]
    return details

def process_client_connection(conn, addr):
    ciphertext = conn.recv(2048)
    if not ciphertext:
        conn.close()
        return

    try:
        decrypted_padded = des_decrypt(ciphertext, KEY)
        plaintext_bytes = custom_unpad(decrypted_padded, BLOCK_SIZE)
        plaintext = plaintext_bytes.decode('utf-8')
    except Exception as error:
        print(RED + f"[!] Transaction processing error: {error}" + RESET)
        conn.close()
        return

    txn = parse_transaction(plaintext)

    receipt_width = 58
    print(GREEN + "=" * receipt_width + RESET)
    print(BOLD + GREEN + "        MASR ALEXANDRIA NATIONAL BANK (MANB)              " + RESET)
    print(BOLD + GREEN + "              CENTRAL MAINFRAME ENGINE                    " + RESET)
    print(GREEN + "=" * receipt_width + RESET)
    print(f"Source Account         : {txn['FROM']}")
    print(f"Recipient Account      : {txn['TO']}")
    print(f"Transfer Amount        : {txn['AMT']}")
    print(f"Service & Stamp Fees   : {txn['FEE']} (\"Mafeesh Haga Bebalash\")")
    print(f"Transaction Status     : {BOLD}{GREEN}APPROVED [PROCESSED BY MAINFRAME]{RESET}")
    print(GREEN + "=" * receipt_width + RESET + "\n")

    conn.close()
    sys.stdout.flush()

def run_mainframe():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    # 1s timeout so ctrl+c works immediately on windows
    server_socket.settimeout(1.0)

    print(CYAN + "==========================================================" + RESET)
    print(BOLD + CYAN + "     MANB CENTRAL MAINFRAME - TRANSACTION PROCESSOR       " + RESET)
    print(CYAN + "                  El-Ataba, Cairo, Egypt           " + RESET)
    print(CYAN + "==========================================================" + RESET)
    print(f"Server online on {HOST}:{PORT}")
    print("Ready to process incoming client transactions...")
    print(YELLOW + "Press Ctrl + C to safely shut down the mainframe.\n" + RESET)
    sys.stdout.flush()

    try:
        while True:
            try:
                conn, addr = server_socket.accept()
            except socket.timeout:
                continue

            conn.settimeout(None)
            process_client_connection(conn, addr)

    except KeyboardInterrupt:
        print(YELLOW + "\n[!] Shutdown signal (Ctrl + C) received." + RESET)
        print(GREEN + "[+] Closing listening socket and freeing port 5000..." + RESET)
        print(BOLD + GREEN + "[+] MANB Central Mainframe safely shut down." + RESET + "\n")
    finally:
        server_socket.close()

if __name__ == '__main__':
    run_mainframe()
