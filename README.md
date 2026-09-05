# 🛡️ CYBERPASS GENERATOR

### *Enterprise-grade desktop password generation utility with cryptographic entropy enforcement.*

<div align="left">

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/GUI-Tkinter-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![Security Engine](https://img.shields.io/badge/Security-CSPRNG-red?style=for-the-badge&logo=1password&logoColor=white)]()
[![Entropy Source](https://img.shields.io/badge/Entropy-OS_Kernel-darkgreen?style=for-the-badge&logo=linux&logoColor=white)]()

[![OS Windows](https://img.shields.io/badge/OS-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)]()
[![OS Linux](https://img.shields.io/badge/OS-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)]()
[![OS macOS](https://img.shields.io/badge/OS-macOS-000000?style=for-the-badge&logo=apple&logoColor=white)]()

[![Dependencies](https://img.shields.io/badge/Dependencies-Zero_External-brightgreen?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Author](https://img.shields.io/badge/Author-void--syntax-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/void-syntax)

</div>

---

## ⚡ Technical Overview

**CyberPass Generator** is a lightweight desktop security tool engineered to synthesize high-entropy, cryptographically safe passwords. Designed to overcome the vulnerabilities of standard pseudo-random number generators (PRNGs)—such as Python's default `random` module (Mersenne Twister)—CyberPass leverages kernel-level cryptographic primitives to ensure resistance against pattern prediction, dictionary compilation, and automated brute-force attacks.

Featuring a streamlined graphical user interface constructed via `tkinter`, CyberPass operates with zero external dependencies, delivering rapid execution and full cross-platform compatibility out of the box.

---

## 🚀 Key Features

* **🎲 True Cryptographic Entropy:** Utilizes Python’s `secrets` module, tapping directly into OS-level entropy pools (`/dev/urandom` on Unix-like systems or `CryptGenRandom` on Windows).
* **🎛️ Granular Pool Customization:** Allows precise character set configuration across uppercase/lowercase ASCII characters, numerical digits (`0-9`), and special punctuation symbols.
* **🔒 Read-Only Memory Buffer:** Enforces strict `readonly` widget state management to eliminate accidental keypress mutations, text field overrides, or partial inline deletions.
* **📋 Native System Clipboard Hook:** Interfacing directly with the system clipboard for immediate single-click password transfer.
* **🛡️ Defensive Input Sanitization:** Integrated exception handling and range bounds verification (restricting password lengths strictly between 8 and 100 characters).
* **⚡ Zero External Dependencies:** Built entirely using core Python standard libraries, eliminating `pip` installation overhead.

---

## 🔒 Security & Architecture Comparison

| Security Domain | Standard Implementations | **CyberPass Generator** |
| :--- | :--- | :--- |
| **Entropy Engine** | `random` module (Deterministic PRNG) | **`secrets` module (Hardware CSPRNG)** |
| **Predictability** | Vulnerable to state recovery attacks | **Cryptographically strong & non-deterministic** |
| **Buffer Integrity** | Standard editable `Entry` widgets | **Locked `readonly` State Management** |
| **Input Validation** | Unhandled TypeErrors & runtime crashes | **Try-Except Range Enforcement** |

---

## 💻 System Requirements & Dependencies

* **Runtime Environment:** Python 3.8+
* **Standard Modules:** `secrets`, `string`, `tkinter`, `tkinter.messagebox`
* **Supported Platforms:** Linux (X11/Wayland), Windows 10/11, macOS

---

## ⚡ Installation & Execution

### 1. Repository Clone
```bash
git clone [https://github.com/void-syntax/cyberpass-generator.git](https://github.com/void-syntax/cyberpass-generator.git)
cd cyberpass-generator
```

### 2. Launch Application (GUI)
```bash
python generator.py
```

### 3. Launch Prototype (CLI)
```bash
python prototype.py
```

### 4. Binary Compilation (Optional)
To package the utility into a standalone, single-file binary executable:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole generator.py
```
The compiled executable will be stored inside the generated `dist/` directory.

---

## 📂 Project Structure

```text
cyberpass-generator/
│
├── generator.py     # Core application logic & Tkinter interface
├── prototype.py     # Terminal-based CLI execution prototype
├── README.md        # Project documentation
└── .gitignore       # Git version control exclusion rules
```

---

## 👨‍💻 Author

**void-syntax**  
GitHub: [https://github.com/void-syntax](https://github.com/void-syntax)