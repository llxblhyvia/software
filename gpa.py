# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:26:51 2020

@author: Administrator
"""

from tkinter import *
import math

def makeitbyyourself():
    by =0.238
    
    #entry 0.06
    xueqijihuaxiuxi0 = Label(root,text = '''大一上学期已经修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi0.place(relx = 0.11,rely = by)
    #label 一个字 0.0166
    termscore0 = Entry(root,width = 7)
    termscore0.place(relx = 0.25,rely = by)
    
    zitermscore0 = Label(root,text = '''学分，GPA为：''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore0.place(relx = 0.31,rely = by)
    
    termgpa0 = Entry(root,width = 7)
    termgpa0.place(relx = 0.41,rely = by)
    
    by +=0.04
    
    #entry 0.06
    xueqijihuaxiuxi1 = Label(root,text = '''大一下学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi1.place(relx = 0.11,rely = by)
    #label 一个字 0.0166
    termscore1 = Entry(root,width = 7)
    termscore1.place(relx = 0.275,rely = by)
    
    zitermscore1 = Label(root,text = '''学分，GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore1.place(relx = 0.31,rely = by)
    
    termgpa1 = Entry(root,width = 7)
    termgpa1.place(relx = 0.475,rely = by)
    
    ps = Label(root,text = '''请还剩哪几学期就填写哪几学期的计划''',font = ('微软雅黑',9),relief =FLAT)
    ps.place(relx = 0.53,rely = by)
     
    by +=0.04

    #entry 0.06
    xueqijihuaxiuxi2 = Label(root,text = '''大二上学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi2.place(relx = 0.11,rely = by)
    #label 一个字 0.0166
    termscore2 = Entry(root,width = 7)
    termscore2.place(relx = 0.275,rely = by)
    
    zitermscore2 = Label(root,text = '''学分，GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore2.place(relx = 0.31,rely = by)
    
    termgpa2 = Entry(root,width = 7)
    termgpa2.place(relx = 0.475,rely = by)
    
    by +=0.04
    
    #entry 0.06
    xueqijihuaxiuxi3 = Label(root,text = '''大二下学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi3.place(relx = 0.11,rely = by)
    #label 一个字 0.0166
    termscore3 = Entry(root,width = 7)
    termscore3.place(relx = 0.275,rely = by)
    
    zitermscore3 = Label(root,text = '''学分，GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore3.place(relx = 0.31,rely = by)
    
    termgpa3 = Entry(root,width = 7)
    termgpa3.place(relx = 0.475,rely = by)
     
    by +=0.04

    #entry 0.06
    xueqijihuaxiuxi4 = Label(root,text = '''大三上学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi4.place(relx = 0.11,rely = by)
    #label 一个字 0.0166
    termscore4 = Entry(root,width = 7)
    termscore4.place(relx = 0.275,rely = by)
    
    zitermscore4 = Label(root,text = '''学分，GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore4.place(relx = 0.31,rely = by)
    
    termgpa4 = Entry(root,width = 7)
    termgpa4.place(relx = 0.475,rely = by)
    
    by +=0.04
    
    #entry 0.06
    xueqijihuaxiuxi5 = Label(root,text = '''大三下学期计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi5.place(relx = 0.11,rely = by)
    #label 一个字 0.0166
    termscore5 = Entry(root,width = 7)
    termscore5.place(relx = 0.275,rely = by)
    
    zitermscore5 = Label(root,text = '''学分，GPA计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore5.place(relx = 0.31,rely = by)
    
    termgpa5 = Entry(root,width = 7)
    termgpa5.place(relx = 0.475,rely = by)
    
    by+=0.04
    
    def func1():
        mibyts0 = int(termscore0.get())
        mibygpa0 = float(termgpa0.get())
        mibyts1 = int(termscore1.get())
        mibygpa1 = float(termgpa1.get())       
        mibyts2 = int(termscore2.get())
        mibygpa2 = float(termgpa2.get())
        mibyts3 = int(termscore3.get())
        mibygpa3 = float(termgpa3.get())
        mibyts4 = int(termscore4.get())
        mibygpa4 = float(termgpa4.get())
        mibyts5 = int(termscore5.get())
        mibygpa5 = float(termgpa5.get())
        allscores = 0
        allscores = mibyts0+mibyts1+mibyts2+mibyts3+mibyts4+mibyts5
        mibyfinalresultgpa = 0.0
        mibyfinalresultgpa = float((mibyts0*mibygpa0+mibyts1*mibygpa1+mibyts2*mibygpa2+mibyts3*mibygpa3+mibyts4*mibygpa4+mibyts5*mibygpa5)/allscores)
        #保留两位小数
        mibyfinalresultgpa = round(mibyfinalresultgpa,2)
        textzuizhongdegpa.insert(END,mibyfinalresultgpa)
    
    labelzuizhongdegpa = Button(root,command = func1,text = "您最终得到的GPA为：",bg = '#FFFF00',font = ('仿宋',12,'bold'),fg = '#191970')
    labelzuizhongdegpa.place(relx = 0.08, rely = by)
    
    textzuizhongdegpa = Text(root)
    textzuizhongdegpa.place(relx = 0.23,rely=by,relwidth = 0.05,relheight = 0.035)

    
    
def wegenerateit():
    
    by = 0.173
    qingshurudangqiangpa = Message(root,text = '''请输入：  当前GPA''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',width = 500,relief =FLAT)
    #message没有height
    qingshurudangqiangpa.place(relx = 0.08,rely = by)
    
    dangqiangpa = Entry(root,width = 7)
    dangqiangpa.place(relx = 0.22,rely = by)
    
    wenzicurrxuefenshu = Message(root,text = '''现修习学分数\n（0~180的整数）''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',width = 500,relief =FLAT)
    wenzicurrxuefenshu.place(relx = 0.28,rely = by)
    
    currxuefenshu = Entry(root,width = 7)
    currxuefenshu.place(relx = 0.42,rely = by)
    
    
    wenzileftterms = Message(root,text = ''' 还剩学期数\n(1~5的整数)''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',width = 500,relief =FLAT)
    wenzileftterms.place(relx = 0.48,rely = by)
    
    entryleftterms = Entry(root,width = 7)
    entryleftterms.place(relx = 0.59,rely = by)
    

    by =0.22
    
    shurumubiaogpa= Label(root,text = '''请输入目标GPA:''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    shurumubiaogpa.place(relx = 0.08,rely = by)
    
    mubiaogpa = Entry(root,width = 7)
    mubiaogpa.place(relx = 0.196,rely = by)
    

    by+=0.04
    #换行+0.04
    
    labelxuanzemoshi= Label(root,text = '''选择想要的模式（每学期模式相同噢）''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    labelxuanzemoshi.place(relx = 0.08,rely = by)
    
    by+=0.04
    
    var = IntVar()
    rabuttonmucheasy = Radiobutton(root,text="愿意修大量甚至溢出学分，每学期绩点要求稍低（默认每学期修30分）   能接受每学期学的最高分数为",fg = '#191970',variable=var,value=0)
    rabuttonmucheasy.place(relx = 0.08,rely = by)

    rabuttonlittlehard = Radiobutton(root,text="愿意接受每学期达到较高绩点，选修课程数较少（默认每学期绩点达到3.8）   能接收每学期应达到的最高绩点为",fg = '#191970',variable=var,value=1)
    rabuttonlittlehard.place(relx = 0.08,rely = by+0.05)
    
    zuigaofenshu = Entry(root,width = 7)
    zuigaofenshu.place(relx = 0.56,rely = by)
    
    zuigaojidian = Entry(root,width = 7)
    zuigaojidian.place(relx = 0.6,rely = by+0.05)
    
    by+=0.05
    by+=0.05
        
    def func2():
        choice = var.get()
        #得到当前gpa数值存放在currgpa中
        currgpa = dangqiangpa.get()
        if currgpa:
            currgpa = float(currgpa)
        #得到当前修的学分存放在currscore中
        currscore =currxuefenshu.get()
        if currscore:
            currscore = int(currscore)
        #求目前学分数×GPA
        currtotal = float(currscore*currgpa)

        #得到还剩的学期数存放在leftterms中
        leftterms = entryleftterms.get()
        if leftterms:
            leftterms = int(leftterms)
        #得到目标GPA存放在targetgpa中
        targetgpa = mubiaogpa.get()
        if targetgpa:
            targetgpa = float(targetgpa)
        
        if choice == 0:
            #能接受的最多分数
            maxscore = zuigaofenshu.get()
            if maxscore:
                maxscore = int(maxscore)
            else:
                maxscore = 30
            i = maxscore 
            while TRUE:
                x = float((targetgpa*(i*leftterms+currscore)-currtotal)/(i*leftterms))
                #gpa取两位小数
                x = round(x,2)
                if x>4.00:
                    s = "很抱歉，无法达到目标GPA"
                    otherinfo.insert(END,s)
                    break
                else:
                    yingxiuscore.insert(END,i)
                    yingdadaojidian.insert(END,x)
                    break
                --i
                
        if choice == 1:
            #能接受的最高绩点
            maxgpa = zuigaojidian.get()
            if maxgpa:
                maxgpa = float(maxgpa)
            else:
                maxgpa = 4.00
            i = maxgpa
            while TRUE:
                x = (targetgpa*currscore-currtotal)/(leftterms*(i-targetgpa))
                #将学分数向上取整
                x = math.ceil(x)
                if x>30:
                    s = "很抱歉，无法达到目标GPA"
                    otherinfo.insert(END,s)
                    break
                else:
                    yingxiuscore.insert(END,i)
                    yingdadaojidian.insert(END,x)
                    break
                i-=0.01
        
    letsgenerate = Button(root,text = '''生成计划''',command = func2,bg = '#4169E1',font = ('仿宋',12,'bold'),fg = '#F8F8FF')
    letsgenerate.place(relx = 0.08,rely = by)
    by+=0.05
    
    labelyinggaixiuscore= Label(root,text = '''您需要在接下来每学期修''',bg = '#FFFF00',font = ('仿宋',12,'bold'),fg = '#191970',relief =FLAT)
    labelyinggaixiuscore.place(relx = 0.08,rely = by)
    
    yingxiuscore = Text(root)
    yingxiuscore.place(relx = 0.243,rely=by,relwidth = 0.05,relheight = 0.04)
    
    labelyinggaidadaodejidian= Label(root,text = '''学分，每学期绩点应达到''',bg = '#FFFF00',font = ('仿宋',12,'bold'),fg = '#191970',relief =FLAT)
    labelyinggaidadaodejidian.place(relx = 0.3,rely = by)
    
    yingdadaojidian = Text(root)
    yingdadaojidian.place(relx = 0.465,rely=by,relwidth = 0.05,relheight = 0.04)
    
    by+=0.05
    
    otherinfo = Text(root,font = ('仿宋',14,'bold'),fg = '#DC143C')
    otherinfo.place(relx = 0.08,rely=by,relwidth = 0.3,relheight = 0.05)
    
global root
root = Tk()
root.title('gpa提升计算器')
root.geometry('480x600')

biaoti =Label(root,text = 'GPA提升神器',bg = '#4169E1',font = ('仿宋',16,'bold'),fg = '#F8F8FF',width = 20,height = 2,relief =FLAT)
biaoti.place(relx = 0.32,rely = 0.01, relheight = 0.05, relwidth = 0.36)

ps = Label(root,text = '(请全屏使用)',font = ('微软雅黑',10),relief =FLAT)
ps.place(relx = 0.7,rely = 0.03)

row1minwidth = 0.035 #单位小长度
beginningy = 0.06 #y的起始位置

beginningy+=0.01
#空隙 0.01

qingxuanzetishi =Label(root,text = ''' 请选择自己制定学习计划然后查看最终GPA或设定目标由我们为您生成学习计划''',font = ('仿宋',14),fg = '#000080',relief =FLAT)
qingxuanzetishi.place(relx = 0.2,rely = beginningy, relheight = 0.035)

beginningy+=0.038

buttonmakeitbyyourself = Button(root, text='自己制定计划', command=makeitbyyourself,bg = '#6495ED',font = ('仿宋',12,'bold'),fg = '#F8F8FF')
buttonmakeitbyyourself.place(relx = 0.25,rely = beginningy)

buttonwegenerateit = Button(root, text='我们为你生成', command=wegenerateit,bg = '#6495ED',font = ('仿宋',12,'bold'),fg = '#F8F8FF')
buttonwegenerateit.place(relx = 0.5,rely = beginningy)

root.mainloop()
