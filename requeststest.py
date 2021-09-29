import requests,pandas,json
from jsonpath import jsonpath
import base64
import pprint
url='https://aip.baidubce.com/oauth/2.0/token'
data={'grant_type':'client_credentials',
      'client_id':'9AxMLZFA21ebaZwM9HpzGBfR',
      'client_secret':'PcudgPsb3G1I0kG8PfYHMS0d697xAMUI'
      }
"""res=requests.request('post',url,data=data)"""
res=requests.post(url,data=data).json()
#获取token值
token=jsonpath(res,'access_token')[0]
"""print(token)"""
def invoice_message(image_path) -> str:
    #image转base64
    #image_path='D:\\123.jpg'
    with open(image_path,'rb') as f:
        image_base64=base64.b64encode(f.read())

    url='https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice'
    data={'image':image_base64,
    'access_token':token
    }
    res=requests.post(url,data=data).json()
    #获取发票号码
    InvoiceNum=jsonpath(res,'$..InvoiceNum')
    #获取发票代码
    InvoiceCode=jsonpath(res,'$..InvoiceCode')
    #获取发票日期
    InvoiceDate=jsonpath(res,'$..InvoiceDate')
    #获取金额
    TotalAmount=jsonpath(res,'$..TotalAmount')
    return (InvoiceNum,InvoiceCode,InvoiceDate,TotalAmount)
    
