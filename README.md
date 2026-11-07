# MANB - Masr Alexandria National Bank
## Applied Cryptography Coursework - Milestone 2

A pure-Python implementation of a symmetric banking tunnel between a Mobile Banking App (Client) and a Central Mainframe (Server) over TCP/IP sockets using DES in ECB mode.

Developed for **KH6037CMD Applied Cryptography** at Coventry University / The Knowledge Hub Universities (TKH).

---

### Key Features
- **Zero External Cryptography Libraries:** Both the 16-round DES cipher (NIST FIPS 46-3) and PKCS#7 padding/unpadding are implemented 100% from scratch in pure procedural Python using standard bitwise operations and permutation tables.
- **Client Application (`manb_mobile.py`):** Interactive terminal banking app featuring Layer 1 SHA-256 PIN authentication (with 3-attempt brute-force lockout), account selection with debt protection, transaction fee notices, and live balance deductions.
- **Server Mainframe (`manb_mainframe.py`):** TCP socket server listening on `127.0.0.1:5000` that decrypts incoming transaction payloads, verifies/removes PKCS#7 padding, and prints official banking receipts. Includes graceful `Ctrl + C` shutdown.
- **Appendix B Demonstration (`manb_ecb_demo.py`):** Side-by-side terminal verification proving that identical 8-byte plaintext blocks (`'5000_EGP'`) produce identical ciphertext blocks under ECB mode (Pattern Leakage).

---

### Project Structure
```text
.
├── manb_crypto_engine.py   # Pure-Python DES (16 rounds) & PKCS#7 padding engine
├── manb_mobile.py          # Mobile Banking App (Client)
├── manb_mainframe.py       # Central Mainframe Server (TCP Server)
├── manb_ecb_demo.py        # Appendix B: ECB Pattern Leakage Demonstration
├── requirements.txt        # Standard library only (no external dependencies)
└── README.md
```

---

### How to Run

No `pip install` required. Only Python 3.8+ standard library is used.

1. **Start the Central Mainframe Server:**
   ```bash
   python manb_mainframe.py
   ```

2. **Launch the Mobile Banking App (Default PIN: `2026`):**
   ```bash
   python manb_mobile.py
   ```

3. **Run the Appendix B ECB Leakage Proof:**
   ```bash
   python manb_ecb_demo.py
   ```
