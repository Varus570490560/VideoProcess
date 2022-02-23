import requests
import urllib

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "__gads=ID=79b966ca278ddd0f:T=1643106054:S=ALNI_MZMzQxTkW35RLEkPhHODyRb_nAeIw; _ga=GA1.2.814802378.1643106054; noauth=1643106060522; _fbp=fb.1.1643106063270.17137962; zdbb_fb_id=1; fpid=250a51daaf6f4816af45438be2706d56; _pubcid=896a8077-214d-4755-bc6b-84cce426dcf0; _cc_id=5f117e62fccbf9f29af3e4c66d08944b; _gaexp=GAX1.2.1aGFJQwZQuqGI9ZgmkGyaQ.19123.0; geoCC=HK; _gid=GA1.2.1580160982.1645511246; panoramaId_expiry=1646116071305; panoramaId=02d5d22dfb13a18eb50fa77759b516d53938181e044a5b09af2d7adb82b768e3; comScore=amp-rCBvNUCUt2Psl7vSjFNCuA; crid=MjUwYTUxZGFhZjZmNDgxNmFmNDU0MzhiZTI3MDZkNTZ8MDM5Y2MwMTItYjU5OS00MDM2LWJhMjItZTQyZTZmZTBhYmE3; __idcontext=eyJjb29raWVJRCI6IkRBRDczN0k0U1ZPNlVVTzZQRUpPRkNCU0JJQjNJT1c3TVBLU0dQNUJTTkVRPT09PSIsImRldmljZUlEIjoiREFENzM3STRTWkc0RzdQNUxZSTQzU0FVQ0E1Sk9MV09NVExSV001NDJKRVE9PT09IiwiaXYiOiJFWkxJU0FaS1lBN1RKTkpDVzZSMjJMNllUQT09PT09PSIsInYiOjF9; FCNEC=[[\"AKsRol9INEFhHjpd6ivA32eyeLlnolatNIM5ALkV4eIpBQouGQrgYXMQKvAa6cj0il__CRh7EwuPhwQFhB-6b8IT9IdDt4nlt1PEMLkvsZfLF5Rox1zTSYTpwkkqmq-CPlrU4-uzlWuJZQE7FLKCO3504c7JkS5aOQ==\"],null,[]]; cto_bundle=Ug4QN19yc0JneUxxZnpyeU1mZkFQR1IlMkJjbXNMYmdlSHNhaCUyQk8lMkJqdElOUUVyckRvcWZBSmFwdTNRZzgxTzZ5T3pBVjgxJTJGYThwdzF3UzJRMXFhNnNxZVZXYXdqWWtSNHY5bVdPQ0xuTEF4cGZUNnptR1lQN2d5ckpkbUtycFZCJTJGT0JOTCUyRmVJY3ZVbVNmTnVtWjVRZmtXVGNUT0ElM0QlM0Q; cto_bidid=dpt9xV9QWG1VZktKV3J5Z2FROXJPMVlTekFFRzhnOW1zcFEzbWRCMHFNdDVVOTZhZWR1VURvZm1jcFIyQk1WcWdsSUNZa0NSeG9uWVpScmY5Vks0cU4lMkJRTmMwMGFCUE1vRlZvc2JYbXRiTjBNdU5RJTNE"
}


def analysis_master():
    with open('./input/master.m3u8', 'r') as master:
        while True:
            line = master.readline()
            if not line:
                break
            if line[0] == '#':
                continue
            else:
                line = line[:len(line)-1]
                response = requests.get(url=line, headers=headers, allow_redirects=True)
                print(response.content)