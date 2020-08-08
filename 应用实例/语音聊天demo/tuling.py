import requests
import json

truing_api_key = 'e0cd6225d7eb45d6824334715f8f31fc'
api_url = 'http://openapi.tuling123.com/openapi/api/v2'
hearders = {'Content-Type':'application/json;charset=UTF-8'}
def Tuling(text_words=""):
    req = {
        'reqType': 0,
        'perception':{
            'inputText':{
                'text':text_words
            },
            'selfInfo':{
                'location':{
                    'city':'北京',
                    'province': '北京',
                    'street':'西大街'
                }
            }
        },
        'userInfo':{
            'apiKey': truing_api_key,
            'userId':"Nieson"
        }
    }
    req['perception']['inputText']['text'] = text_words
    response = requests.request("post",api_url,json= req, headers = hearders)
    response_dict = json.loads(response.text)
    print(response_dict)
    result = response_dict['results'][0]['values']['text']
    print("AI Robot said", result)
    return result

if __name__ == '__main__':
    string = '你好，美女，可以交个朋友吗？'
    Tuling(string)