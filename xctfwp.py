import requests
import re,os

url = 'https://www.xctf.org.cn/library/all/Writeup/?page=3' #xctf的writeup地址

biaoti = '<p style="margin-top:-2px">正则</p>'

biaotijianjie = '<a class="font14 hidden-xs">.*</a>'

shequname = 'xctf'

fabushijian = '<span class="font14">正则</span>'

data = requests.get(url).text

digui = ''

def b(shuju):
    try:
        zhengze = re.compile('''                                    <p style="margin-top:-2px">
                                        <span class="a-title-icon"></span>
                                            <a class="a-title font18 weight c333" target="_blank" style="white-space:nowrap;width:100%;overflow:hidden;text-overflow:ellipsis;display:inline-block;"
                                               
                                           href=".+" >
                                                .+
                                                

                                            </a>
                                    </p>
''')
        duqu = zhengze.findall(shuju)
        return duqu
    except:
        return '[]'


def j(shuju):
    try:
        zhengze = re.compile('''                                            <a class="font14 hidden-xs"
                                               
                                            >[\w \n-;\/\/\{\}\[\]\.\*\`\(\)\!\,\+\，\：\（\）\d]+''')
        duqu = zhengze.findall(shuju)
        return duqu
    except:
        return '[]'


def whattime(shuju):
    try:
        zhengze = re.compile('''                                            <span class='font14'>[\w\d \-\:\：]+</span>''')
        duqu = zhengze.findall(shuju)
        return duqu
    except:
        return '[]'

def liulaninglundianzan(shuju):
    try:
        zhengze = re.compile('''                                            <span class="pull-right cccc pad5T">[\<\>\w\d \;\-\%\&\.\"\"\n\/\=]+</span>''')
        duqu = zhengze.findall(shuju)
        return duqu
    except:
        return '[]'

def tupiandizhi(shuju):
    try:
        zhengze = re.compile('''                                           <img class="img-responsive" src="[\/\w\d\. ]+" >''')
        duqu = zhengze.findall(shuju)
        return duqu
    except:
        return '[]'

def urldizhihuoqu(shuju):
    try:
        zhengze = re.compile('''
                                            <a class="a-title font18 weight c333" target="_blank" style="white-space:nowrap;width:100%;overflow:hidden;text-overflow:ellipsis;display:inline-block;"
                                               
                                           href=".+" >''')
        duqu = zhengze.findall(shuju)
        return duqu
    except:
        return '[]'
    
def tupianbaocun(biaoti,biaotijianjie,fabushijian,liulangpinglundianzana3,tupiandizhi,urldizhiya):
    for x in range(len(biaoti)):
        if('*'in biaoti[x]):
            biaoti[x] = biaoti[x][1:]
    for x in biaoti:
        try:
            if(os.path.exists(os.getcwd()+'\\'+x)):
                pass
            else:
                os.mkdir(x)
        except:
            pass
    for t in range(len(biaoti)):
        os.chdir(biaoti[t])
        xieru = open(biaoti[t]+'.txt','w+')
        xieru.write(urldizhiya[t]+'\n')
        xieru.write(biaoti[t]+'\n')
        xieru.write(biaotijianjie[t]+'\n')
        xieru.write(fabushijian[t]+'\n')
        xieru.write(liulangpinglundianzana3[t]+'\n')
        xieru.close()
        os.chdir('../')

    #图片文件名获取
    tupainame = []
    for t in tupiandizhi:
        fege = t.split('/')
        for r in fege:
            if('jpg' in r or 'png' in r or 'jpeg' in r):
                tupainame.append(r)
            else:
                pass

    #图片下载
    for t in range(len(biaoti)):
        os.chdir(biaoti[t])
        fason = requests.get(tupiandizhi[t])
        with open(tupainame[t],'wb')as f:
            f.write(fason.content)
            f.close()
            os.chdir('../')
if __name__ == '__main__':
    data = requests.get(url).text
    digui = b(data)
    biaotidata = [] #标题 
    for x in digui:
        fege = x.split('\n')
        for t in fege:
            if('WP' in t):
                biaotidata.append(t.strip())
            elif('writeup' in t):
                if('href' in t):
                    pass
                else:
                    biaotidata.append(t.strip())
            elif('Writeup' in t):
                biaotidata.append(t.strip())
            elif('write up' in t):
                biaotidata.append(t.strip())
            else:
                pass
    digui = j(data)
    bitaotijianjie = [] #标题简介
    for x in digui:
        fenge = x.split('''                                            <a class="font14 hidden-xs"
                                               
                                            >''')
        for t in fenge:
            if(t == ''):
                pass
            else:
                bitaotijianjie.append(t.strip())
    digui = whattime(data)
    time = [] #发布时间
    for x in digui:
        fenge = x.split('</span>')
        for t in fenge:
            jixu = t.split('<span class=\'font14\'>')
            for r in jixu:
                if('-' in r):
                    time.append(r.strip())

    digui = liulaninglundianzan(data)
    liulaninglundianzan=[]#浏览量评论点赞
    zhengze2 = re.compile('\d+&nbsp;')
    hecheng = ''
    for x in digui:
        pipei = zhengze2.findall(x)
        for t in pipei:
            fege = t.split('&nbsp;')
            for r in fege:
                if(r == ''):
                    pass
                else:
                    liulaninglundianzan.append(r.strip())
    liulaninglundianzan2 = [] #浏览量评论点赞
    for x in range(len(liulaninglundianzan)):
        hecheng +=liulaninglundianzan[x]+'-'
        if(x % 3 == 0):
            liulaninglundianzan2.append(hecheng)
            hecheng = ''
    tupianzihi = []
    digui = tupiandizhi(data)
    for x in digui:
        fege = x.split('"')
        tupianzihi.append('https://www.xctf.org.cn'+fege[3])

    urldizhi = []
    digui = urldizhihuoqu(data)
    for x in digui:
        fege = x.split('"')
        urldizhi.append('https://www.xctf.org.cn'+fege[len(fege)-2])
    tupianbaocun(biaotidata,bitaotijianjie,time,liulaninglundianzan2,tupianzihi,urldizhi)
    
