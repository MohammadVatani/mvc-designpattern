from router import Router
import config as c
import os
import importlib

router = Router()

def load_apps():
    app_names =  os.listdir(c.appsDirectory)
    app_names = [ x for x in app_names if x not in ["__init__.py", "__pycache__"]]
    print(app_names)
    for app in app_names:
        module = importlib.import_module(f'{c.appsDirectory}.{app}')
        for key,value in module.router.routes.items():
            route_object = {
                "route":key,
                **value
            }
            router.add_route(route_object)
            

    
load_apps()

letter = {'SuperVision': {'UnderSupervision': 0, 'AdditionalInfo': '', 'Reasons': []}, 'TracingNo': 864583, 'Symbol': 'وکبهمن', 'CompanyName': 'مدیریت سرمایه گذاری کوثر بهمن', 'UnderSupervision': 0, 'Title': 'گزارش فعالیت ماهانه دوره ۱ ماهه منتهی به ۱۴۰۰/۱۲/۲۹', 'LetterCode': 'ن-۳۱', 'SentDateTime': '۱۴۰۱/۰۱/۰۲ ۱۶:۰۰:۲۶', 'PublishDateTime': '۱۴۰۱/۰۱/۰۲ ۱۶:۰۰:۲۶', 'HasHtml': True, 'IsEstimate': False, 'Url': '/Reports/Decision.aspx?LetterSerial=gNsjPbspoFfcRTuttDuQ1g%3D%3D&rt=2&let=8&ct=0&ft=-1', 'HasExcel': 
True, 'HasPdf': True, 'HasXbrl': False, 'HasAttachment': False, 'AttachmentUrl': '', 'PdfUrl': 'DownloadFile.aspx?hs=gNsjPbspoFfcRTuttDuQ1g%3d%3d&ft=1005&let=8', 'ExcelUrl': 'https://excel.codal.ir/service/Excel/GetAll/gNsjPbspoFfcRTuttDuQ1g%3d%3d/0', 
'XbrlUrl': '', 'TedanUrl': 'http://www.tedan.ir'}


router.letter_handler(letter)