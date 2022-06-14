appsDirectory = "apps"


# import requests

# def get_announcement_Letters(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "application/json; charset=utf-8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
#     return requests.get(url, headers=headers, timeout=2.5).json()['Letters']

# def get_target_source_page(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
#     return requests.get(url, headers=headers, timeout=2.5).text


# a= get_announcement_Letters("https://search.codal.ir/api/search/v2/q?&Audited=true&AuditorRef=-1&Category=-1&Childs=true&CompanyState=-1&CompanyType=-1&Consolidatable=true&IsNotAudited=false&Length=-1&LetterType=-1&Mains=true&NotAudited=true&NotConsolidatable=true&PageNumber=1&Publisher=false&TracingNo=-1&search=false")

# print(a[0])