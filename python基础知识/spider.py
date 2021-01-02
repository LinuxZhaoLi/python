'''
爬取图片：
（1）通过 Requests 发起 HTTP 请求，获取『美女』下的部分讨论列表
（2）通过 lxml 解析抓取到的每个讨论中 HTML，获取其中所有的 img 标签相应的 src 属性
（3）通过 Requests 发起 HTTP 请求，下载 src 属性指向图片（不考虑动图）
（4）通过 AipFace 请求对图片进行人脸检测
（5）判断是否检测到人脸，并使用 『4 检测过滤条件』过滤
（6）将过滤后的图片持久化到本地文件系统，文件名为 颜值 + 作者 + 问题名 + 序号
返回第一步，继续

'''

import time
import os
import re
import requests
from lxml import etree
from aip import  AipFace

APP_ID ="xxxxxxxx"
API_KEY ="xxxxxxxxxxxxxxxxxxxxxxxx"
SECRET_KEY ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

DIR ="image"
BEAUTY_THRESHOLD =45
AUTHORIZATION ="oauth c3cef7c66a1843f8b3a9e6a1e3160e20"    # 跳过权限验证，在开发者工具复制一个，无需登录
LIMIT =5

SOURCE ="19552207"
USER_AGENT ="Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3"
REFERER ="https://www.zhihu.com/topic/%s/newest"% SOURCE
print(REFERER)
BASE_URL ="https://www.zhihu.com/api/v4/topics/%s/feeds/timeline_activity"

URL_QUERY ="?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.\
data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.\
is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.\
type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.\
is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.\
badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.\
target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.\
badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.\
target.data%5B%3F%28target.type%3Dpeople%29%5D.target.\
answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.\
type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.\
target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.\
topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.comment_count&limit="+ str(LIMIT)

def fetch_image(url):  # 发送请求
    try:
        headers ={
            "User-Agent": USER_AGENT,
            "Referer": REFERER,
            "authorization": AUTHORIZATION
            }
        s = requests.get(url, headers=headers)
    except Exception as e:
        print("fetch last activities fail. "+ url)
        raise e
    return s.content


def fetch_activities(url):
    print("第一步： 获取活动")
    try:
        headers ={
        "User-Agent": USER_AGENT,
        "Referer": REFERER,
        "authorization": AUTHORIZATION
        }
        s = requests.get(url, headers=headers)
    except Exception as e:
        print("fetch last activities fail. "+ url)
        raise e
    print("\ns.json: \n %s"% s.json())
    print("\nJson_end\n")
    return s.json()


def process_activities(datums, face_detective):
    for data in datums["data"]:
        target = data["target"]
        if"content" not in target or"question" not in target or"author" not in target:
            continue
        #解析列表中每一个元素的内容
        html = etree.HTML(target["content"])
        seq =0
        #question_url = target["question"]["url"]
        question_title = target["question"]["title"]
        author_name = target["author"]["name"]
        #author_id = target["author"]["url_token"]
        print("current answer: "+ question_title +" author: "+ author_name)
        #获取所有图片地址
        images = html.xpath("//img/@src")
        for image in images:
            if not image.startswith("http"):
                continue
            s = fetch_image(image)
        #请求人脸检测服务
            scores = face_detective(s)
            for score in scores:
                filename =("%d--"% score)+ author_name +"--"+ question_title +("--%d"% seq)+".jpg"
                filename = re.sub(r'(?u)[^-w.]','_', filename)
        #注意文件名的处理，不同平台的非法字符不一样，这里只做了简单处理，特别是 author_name / question_title 中的内容
                seq = seq +1
                with open(os.path.join(DIR, filename),"wb")as fd:
                    fd.write(s)
        #人脸检测 免费，但有 QPS 限制
                time.sleep(2)
    if not datums["paging"]["is_end"]:
        #获取后续讨论列表的请求 url
        return None #datums["paging"]["next"]
    else:
        return None


def get_valid_filename(s):  # 获取合法的文件名
    s = str(s).strip().replace(' ','_')
    return re.sub(r'(?u)[^-w.]','_', s)


def init_face_detective(app_id, api_key, secret_key):
    client =AipFace(app_id, api_key, secret_key)
    #人脸检测中，在响应中附带额外的字段。年龄 / 性别 / 颜值 / 质量
    options ={"face_fields":"age,gender,beauty,qualities"}

    def detective(image):
        r = client.detect(image, options)
    # 如果没有检测到人脸
        if r["result_num"] == 0:
            return []
        scores = []
        for face in r["result"]:
            # 人脸置信度太低
            if face["face_probability"] < 0.6:
                continue
        # 真实人脸置信度太低
            if face["qualities"]["type"]["human"] < 0.6:
                continue
                # 颜值低于阈值
            if face["beauty"] < BEAUTY_THRESHOLD:
                continue
# 性别非女性
            if face["gender"] != "female":
                continue
            scores.append(face["beauty"])
        return scores
    return detective


def init_env():     # 创建文件夹
    if not os.path.exists(DIR):
       os.makedirs(DIR)
init_env()
face_detective = init_face_detective(APP_ID, API_KEY, SECRET_KEY)
url = BASE_URL % SOURCE #+ URL_QUERY
while url is not None:
    print("current url: " + url)
    datums = fetch_activities(url)
    print(datums)
    url = process_activities(datums, face_detective)

'''
https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&fm=detail&lm=-1&hd=&latest=&copyright=&st=-1&sf=2&fmq=1604158412246_R_D&fm=detail&pv=&ic=&nc=1&z=0&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=window10%E7%94%B5%E8%84%91%E7%BE%8E%E5%A5%B3


https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=window10%E7%94%B5%E8%84%91%E7%BE%8E%E5%A5%B3&step_word=&hs=2&pn=46&spn=0&di=4840&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=312024990%2C1839024711&os=3186586042%2C3259168651&simid=80493500%2C724453309&adpicid=0&lpn=0&ln=1394&fr=&fmq=1604158412246_R_D&fm=detail&ic=&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimage.xcar.com.cn%2Fattachments%2Fa%2Fday_111122%2F2011112213_f4d819d9fc9fe4a8864e4Z0aWoO69acO.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bxvw6_z%26e3Bv54_z%26e3BvgAzdH3FkkfAzdH3Fetjopi6jw1_z%26e3Brir%3Fpt1%3D8m9dlc99%26rw2j%3Dd&gsm=d&rpstart=0&rpnum=0&islist=&querylist=&force=undefined


https://github.com/KDAB/android_openssl

'''