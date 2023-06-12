from censys import certificates
import json

# تعیین API ID و سریال شماره در کنسیس
UID = "YOUR_CENSYS_UID"
SECRET = "YOUR_CENSYS_SECRET"

# اتصال به API
certs = certificates.CensysCertificates(api_id=UID, api_secret=SECRET)

# تعیین پارامتر جستجو
query = "google.com"  # جستجو برای دامنه Google
fields = ["parsed.subject", "parsed.names"]

# انجام جستجو
search_results = certs.search(query, fields=fields)

# ذخیره نتایج به صورت url، ip و پورت
for search_result in search_results:
    for name in search_result["parsed.names"]:
        if '.' not in name:
            continue
        url = "https://" + name
        for address in search_result["parsed.ip_addresses"]:
            for port in search_result["parsed.port"]:
                print(url, address, port)
