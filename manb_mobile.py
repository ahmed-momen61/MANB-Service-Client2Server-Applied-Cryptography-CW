import socket
import hashlib
from manb_crypto_engine import custom_pad, des_encrypt

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

# sha256 hash of pin 2026
PIN_HASH = hashlib.sha256(b"2026").hexdigest()

def authenticate_user():
    print(BOLD + "\n--- CLIENT AUTHENTICATION ---" + RESET)
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        pin_input = input(f"Enter 4-digit banking PIN (Attempt {attempt}/{max_attempts}): ").strip()
        hashed_attempt = hashlib.sha256(pin_input.encode('utf-8')).hexdigest()

        if hashed_attempt == PIN_HASH:
            print(GREEN + "[+] PIN verified. Welcome, MANB Valued Customer." + RESET)
            return True
        else:
            remaining = max_attempts - attempt
            if remaining > 0:
                print(YELLOW + f"[-] Incorrect PIN. {remaining} attempt(s) remaining." + RESET)
            else:
                print(RED + "\n[!] SECURITY ALERT: 3 consecutive invalid attempts." + RESET)
                print(RED + "[!] Account locked. Please visit El-Ataba branch with your National ID." + RESET)
                return False
    return False

def select_account(accounts):
    print(BOLD + "\n[ SELECT SOURCE ACCOUNT ]" + RESET)
    while True:
        print(CYAN + f"[1] Masr-Alex Current Account (Acc: {accounts['1']['acc_num']}) | Balance: {accounts['1']['balance']:,.2f} EGP" + RESET)
        print(CYAN + f"[2] El-Ataba VIP Saving Account (Acc: {accounts['2']['acc_num']}) | Balance: {accounts['2']['balance']:,.2f} EGP" + RESET)

        choice = input("\nSelect source account (1 or 2): ").strip()
        if choice == "2":
            print(RED + BOLD + "\nu better not dear to use this account" + RESET)
            print(YELLOW + "[-] Account 20020020 is unavailable due to an outstanding negative balance (-1,250.00 EGP).\n" + RESET)
            continue
        elif choice == "1":
            return "1"
        else:
            print(RED + "[!] Invalid option. Please enter 1 or 2.\n" + RESET)

def get_transfer_details(account_info):
    print(BOLD + "\n[ TRANSFER DETAILS ]" + RESET)
    print(f"Available Balance: {GREEN}{account_info['balance']:,.2f} EGP{RESET}")

    while True:
        recipient = input("Enter Recipient Account Number: ").strip()
        if recipient:
            break
        print(RED + "[!] Recipient account number cannot be empty." + RESET)

    service_fee = 15
    tax_fee = 5
    total_fee = service_fee + tax_fee

    while True:
        amount_input = input("Enter Transfer Amount in EGP: ").strip()
        try:
            amount = float(amount_input)
            if amount <= 0:
                print(RED + "[!] Transfer amount must be positive." + RESET)
                continue
        except ValueError:
            print(RED + "[!] Please enter a valid numerical amount." + RESET)
            continue

        # check if amount exceeds balance
        if amount > account_info["balance"]:
            print(RED + f"\n[!] You only have {account_info['balance']:,.2f} EGP in your account." + RESET)
            retry = input("Would you like to enter a different amount? (y/n): ").strip().lower()
            if retry != 'y':
                return None, None
            continue

        # check if amount + 20 egp fee exceeds balance
        total_needed = amount + total_fee
        if total_needed > account_info["balance"]:
            max_allowed = account_info["balance"] - total_fee
            print(RED + f"\n[!] Cannot transfer {amount:,.2f} EGP. 20 EGP fee is required (\"Mafeesh Haga Bebalash\")." + RESET)
            print(YELLOW + f"[-] Maximum amount you can transfer: {max_allowed:,.2f} EGP." + RESET)
            retry = input("Would you like to enter a different amount? (y/n): ").strip().lower()
            if retry != 'y':
                return None, None
            continue

        return recipient, amount

def confirm_and_deduct(account_info, amount):
    service_fee = 15
    tax_fee = 5
    total_fee = service_fee + tax_fee
    total_deducted = amount + total_fee

    # safety check: ensure balance is strictly sufficient
    if total_deducted > account_info["balance"]:
        print(RED + f"\n[!] Transaction denied: insufficient funds ({account_info['balance']:,.2f} EGP available)." + RESET)
        return False, total_fee

    print(BOLD + "\n[ TRANSACTION SUMMARY ]" + RESET)
    print(f"Transfer Amount    : {amount:,.2f} EGP")
    print(f"Service Charge     : {service_fee} EGP")
    print(f"Stamp & Tax Fees   : {tax_fee} EGP")
    print(YELLOW + '[!] Notice: 15 EGP service fee + 5 EGP tax & misc ("Mafeesh Haga Bebalash") will be deducted.' + RESET)
    print(BOLD + f"[*] Total Amount to Deduct: {total_deducted:,.2f} EGP" + RESET)

    decision = input("\nConfirm transaction? (y/n): ").strip().lower()
    if decision != "y":
        print(YELLOW + "[-] Transaction cancelled by user. No funds deducted." + RESET)
        return False, total_fee

    # deduct transfer + fee
    account_info["balance"] -= total_deducted
    print(GREEN + f"[+] Transaction confirmed." + RESET)
    print(GREEN + f"[+] Updated Remaining Balance: {account_info['balance']:,.2f} EGP" + RESET)
    return True, total_fee

def transmit_transaction(from_acc, to_acc, amount, fee):
    amount_clean = int(amount) if amount.is_integer() else amount
    plaintext_string = f"TXN|FROM:{from_acc}|TO:{to_acc}|AMT:{amount_clean}EGP|FEE:{fee}EGP"

    # pad to 8 bytes and encrypt with des
    plaintext_bytes = plaintext_string.encode('utf-8')
    padded_bytes = custom_pad(plaintext_bytes, BLOCK_SIZE)
    ciphertext = des_encrypt(padded_bytes, KEY)

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        client_socket.sendall(ciphertext)
        client_socket.close()
        print(GREEN + "[+] Transaction submitted to MANB Mainframe successfully." + RESET)
    except Exception as error:
        print(RED + f"[!] Connection error: {error}" + RESET)
        print(YELLOW + "[-] Ensure MANB Mainframe server is active and accessible." + RESET)

def run_mobile_app():
    print(GREEN + "==========================================================" + RESET)
    print(BOLD + GREEN + "       MASR ALEXANDRIA NATIONAL BANK (MANB)               " + RESET)
    print(BOLD + GREEN + "           MOBILE BANKING APPLICATION (v2.6)              " + RESET)
    print(GREEN + "                  El-Ataba, Cairo                 " + RESET)
    print(GREEN + "==========================================================" + RESET)

    if not authenticate_user():
        return

    accounts = {
        "1": {
            "acc_num": "10010010",
            "name": "Masr-Alex Current Account",
            "balance": 45000.0,
            "is_active": True
        },
        "2": {
            "acc_num": "20020020",
            "name": "El-Ataba VIP Saving Account",
            "balance": -1250.0,
            "is_active": False
        }
    }

    while True:
        selected_key = select_account(accounts)
        selected_acc = accounts[selected_key]

        to_acc, amount = get_transfer_details(selected_acc)
        if to_acc is None or amount is None:
            print(YELLOW + "\n[-] Transaction aborted." + RESET)
        else:
            confirmed, fee = confirm_and_deduct(selected_acc, amount)
            if confirmed:
                transmit_transaction(selected_acc["acc_num"], to_acc, amount, fee)

        print("\n" + CYAN + "-" * 58 + RESET)
        another = input(BOLD + "Transaction Done! Do you need to do any other transactions? (y/n): " + RESET).strip().lower()
        if another != 'y':
            print(GREEN + "\n==========================================================" + RESET)
            print(BOLD + GREEN + "Thank you for using MANB (Masr Alexandria National Bank)." + RESET)
            print(BOLD + GREEN + "Session Ended." + RESET)
            print(GREEN + "==========================================================" + RESET)
            break
        print(CYAN + "\n[+] Returning to main menu..." + RESET)

if __name__ == '__main__':
    run_mobile_app()
