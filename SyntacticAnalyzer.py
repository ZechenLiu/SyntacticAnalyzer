import re
#匹配ID
patternID=re.compile(r'(^[a-zA-Z])(([a-zA-Z0-9]*)$)')
#匹配数字
patternNUM=re.compile(r'(^[0-9])(([0-9]*)$)')
#运算符
rwopt=['+','-','*','/']
#<表达式>递归分析程序
def expression(ls):
    ls+=string
    token=''
    for i in ls:
        token+=i
        # print(token)#输出表达式
        if token[-1] in rwopt:
            token=token[:-1]
            if patternID.match(token) or patternNUM.match(token):
                token=''
            else:
                print('error,'+ch[1]+' 使用了错误的运算符！')
                exit()
        elif token[-1] == " ":
            token=token[:-1]
            #运算符或:=后是；号或其他符号，判断错误(例如：x:=;或x+#或x:=#)
            if token == '':
                print('error,'+ch[1]+' 表达式错误')
                exit()
            #运算符后是<项>，判断正确
            elif patternID.match(token) or patternNUM.match(token):
                pass
            else:
                print('error,'+ch[1]+' 表达式错误')
                exit()
#<赋值语句>递归分析程序
def statement(ls):
    ls=ls+string
    token=''
    #由于语法规定<赋值语句> → ID：＝<表达式>，则<语句>中若不含:=,则判断错误
    if ':=' not in ls:
        print('error，'+ch[1]+' 赋值出现错误！')
        exit()
    for i in ls:
        token+=i
        # print(token)
        if token[-2:] == ":=":
            token=token[:-2]
            if patternID.match(token):
                token=''
            else:
                print('error，'+ch[1]+' ID错误！')
                exit()
        #分析:=后所接成分是否为<表达式>
        elif token[-1]==" ":
            token=token[:-1]
            expression(token)
    ls=''
    return ls
#<程序>递归下降分析程序,<程序> → begin<语句串>end
def lrparser(ls):
    token=''
    for i in ls:
        token += i
        if token[-1] == " ":
            token = token[:-1]
            if token == '':
                pass
            #若<语句串>中含有begin，则判断错误
            elif token == 'begin':
                print('error，程序中begin只能出现在开头！')
                exit()
            else:
                if ch==['begin','end']:
                    ch.append(token)
                    if ch[-1]=='#':
                        print('success')
                        exit()
                else:
                    ch.append(token)
                    # print(ch)
                    if token!='end':
                        #程序间不加;号，判断错误
                        if ch[-2] != 'begin':
                            token1=token
                            ch.remove(token1)
                            print('error,'+ch[1]+'后未加;号')
                            exit()
                        else:
                            #不写end直接写#，判断错误
                            if token=='#':
                                ch.remove(token)
                                print('error')
                                exit()
                            #end前最后一条语句是程序
                            else:
                                statement(token)
                    elif token=='end':
                        ch.pop(1)
                        # print(ch)
                token=''
        elif token == '':
            pass
        elif token[-1] ==';':
            token=token[:-1]
            token1 = token
            ch.append(token)
            # print(ch)#观察入栈语句顺序
            #程序间不加;号，判断错误
            if ch[-2]!='begin':
                print('error,'+ch[1]+'后未加引号')
                exit()
            else:
                token=statement(token)
                ch.remove(token1)
while True:
    ls=input("输入单词串，以“#”结束：")
    if ls[-1]!='#':
        print('输入字符串没有以“#”结尾，请重新输入！')
    else:
        break
string=' '
ls+=string
token=''
ch=[]
ls1=''
for i in ls:
    token+=i
    if token[-1]==" ":
        token=token[:-1]
        if token=='begin':
            ch.append(token)
            token=''
            ls1=ls[ls.index(i):]+string
            lrparser(ls1)
            break
        else:
            print('error，程序未以begin开头')
            break
    elif token=='':
        pass

