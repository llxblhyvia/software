# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 10:33:58 2020

@author: Administrator
"""

from tkinter import *
import tkinter.font
from functools import partial
import math
import numpy as np
import io  
from PIL import Image, ImageTk  
 
def resize(w, h, w_box, h_box, pil_image):  
  ''' 
  resize a pil_image object so it will fit into 
  a box of size w_box times h_box, but retain aspect ratio 
  对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例 
  '''  
  f1 = 1.0*w_box/w # 1.0 forces float division in Python2  
  f2 = 1.0*h_box/h  
  factor = min([f1, f2])  
  #print(f1, f2, factor) # test  
  # use best down-sizing filter  
  width = int(w*factor)  
  height = int(h*factor)  
  return pil_image.resize((width, height), Image.ANTIALIAS)  

def gpa():
    root = Toplevel()
    root.title('gpa提升计算器')
    root.minsize(400, 600)    
    root.resizable(0, 0) 

    def makeitbyyourself():
        by =0.2
    
        xueqijihuaxiuxi0 = Label(root,text = '''大一上学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        xueqijihuaxiuxi0.place(relx = 0.11,rely = by)
    
        termscore0 = Entry(root,width = 5)
        termscore0.place(relx = 0.63,rely = by)
        zitermscore01 = Label(root,text = '''学分''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore01.place(relx = 0.72,rely = by)
        by+=0.04
        zitermscore0 = Label(root,text = '''GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore0.place(relx = 0.11,rely = by)
        
        termgpa0 = Entry(root,width = 5)
        termgpa0.place(relx = 0.48,rely = by)
        
        by +=0.04
    
        xueqijihuaxiuxi1 = Label(root,text = '''大一下学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        xueqijihuaxiuxi1.place(relx = 0.11,rely = by)
    
        termscore1 = Entry(root,width = 5)
        termscore1.place(relx = 0.63,rely = by)
        zitermscore11 = Label(root,text = '''学分''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore11.place(relx = 0.72,rely = by)
        by+=0.04
        zitermscore1 = Label(root,text = '''GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore1.place(relx = 0.11,rely = by)
        
        termgpa1 = Entry(root,width = 5)
        termgpa1.place(relx = 0.48,rely = by)
        
        by +=0.04
    
        #entry 0.06
        xueqijihuaxiuxi2 = Label(root,text = '''大二上学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        xueqijihuaxiuxi2.place(relx = 0.11,rely = by)
        #label 一个字 0.0166
        termscore2 = Entry(root,width = 5)
        termscore2.place(relx = 0.63,rely = by)
        zitermscore21 = Label(root,text = '''学分''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore21.place(relx = 0.72,rely = by)
        by+=0.04
        zitermscore2 = Label(root,text = '''GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore2.place(relx = 0.11,rely = by)
        
        termgpa2 = Entry(root,width = 5)
        termgpa2.place(relx = 0.48,rely = by)
        
        by +=0.04
        
        #entry 0.0
        xueqijihuaxiuxi3 = Label(root,text = '''大二下学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        xueqijihuaxiuxi3.place(relx = 0.11,rely = by)
        #label 一个字 0.0166
        termscore3 = Entry(root,width = 5)
        termscore3.place(relx = 0.63,rely = by)
        zitermscore31 = Label(root,text = '''学分''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore31.place(relx = 0.72,rely = by)
        by+=0.04
        zitermscore3 = Label(root,text = '''GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore3.place(relx = 0.11,rely = by)
        
        termgpa3 = Entry(root,width = 5)
        termgpa3.place(relx = 0.48,rely = by)
         
        by +=0.04
    
        xueqijihuaxiuxi4 = Label(root,text = '''大三上学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        xueqijihuaxiuxi4.place(relx = 0.11,rely = by)
        #label 一个字 0.0166
        termscore4= Entry(root,width = 5)
        termscore4.place(relx = 0.63,rely = by)
        zitermscore41 = Label(root,text = '''学分''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore41.place(relx = 0.72,rely = by)
        by+=0.04
        zitermscore4 = Label(root,text = '''GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore4.place(relx = 0.11,rely = by)
        
        termgpa4 = Entry(root,width = 5)
        termgpa4.place(relx = 0.48,rely = by)
        by +=0.04
        
        #entry 0.06
        xueqijihuaxiuxi5 = Label(root,text = '''大三下学期已经/计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        xueqijihuaxiuxi5.place(relx = 0.11,rely = by)
        #label 一个字 0.0166
        termscore5 = Entry(root,width = 5)
        termscore5.place(relx = 0.63,rely = by)
        zitermscore51 = Label(root,text = '''学分''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore51.place(relx = 0.72,rely = by)
        by+=0.04
        zitermscore5 = Label(root,text = '''GPA已经/计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
        zitermscore5.place(relx = 0.11,rely = by)
        
        termgpa5 = Entry(root,width = 5)
        termgpa5.place(relx = 0.48,rely = by)
        
        by+=0.055
        
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
        
        textzuizhongdegpa = Text(root,width = 5)
        textzuizhongdegpa.place(relx = 0.55,rely=by+0.005,relwidth = 0.08,relheight = 0.035)
    
        
        
    def wegenerateit():
        
        by = 0.2
        qingshurudangqiangpa = Message(root,text = '''请输入：当前GPA''',bg = '#F0F8FF',font = ('仿宋',10,'bold'),fg = '#000080',width = 500,relief =FLAT)
        #message没有height
        qingshurudangqiangpa.place(relx = 0.08,rely = by)
        
        dangqiangpa = Entry(root,width = 7)
        dangqiangpa.place(relx = 0.42,rely = by)
        by+=0.04
        wenzicurrxuefenshu = Message(root,text = '''现修习学分数\n（0~180的整数）''',bg = '#F0F8FF',font = ('仿宋',10,'bold'),fg = '#000080',width = 500,relief =FLAT)
        wenzicurrxuefenshu.place(relx = 0.08,rely = by)
        
        currxuefenshu = Entry(root,width = 7)
        currxuefenshu.place(relx = 0.42,rely = by+0.005)
        
        by+=0.06
        
        wenzileftterms = Message(root,text = ''' 还剩学期数\n(1~5的整数)''',bg = '#F0F8FF',font = ('仿宋',10,'bold'),fg = '#000080',width = 500,relief =FLAT)
        wenzileftterms.place(relx = 0.08,rely = by)
        
        var2 = IntVar()
        entryleftterms = Entry(root,width = 7)
        entryleftterms.place(relx = 0.42,rely = by)
    
    
        by +=0.055
        
        shurumubiaogpa= Label(root,text = '''请输入目标GPA:''',bg = '#F0F8FF',font = ('仿宋',11,'bold'),fg = '#000080',relief =FLAT)
        shurumubiaogpa.place(relx = 0.08,rely = by)
        
        mubiaogpa = Entry(root,width = 7)
        mubiaogpa.place(relx = 0.42,rely = by)
        
    
        by+=0.04
        #换行+0.04
        
        labelxuanzemoshi= Label(root,text = '''选择想要的模式（每学期模式相同噢）''',bg = '#F0F8FF',font = ('仿宋',11,'bold'),fg = '#000080',relief =FLAT)
        labelxuanzemoshi.place(relx = 0.08,rely = by)
        
        by+=0.04
        
        var = IntVar()
        rabuttonmucheasy = Radiobutton(root,text="愿意修大量甚至溢出学分，每学期绩点要求稍低（默认每学期修30分)",fg = '#191970',variable=var,value=0)
        rabuttonmucheasy.place(relx = 0.02,rely = by)
        by+=0.04
        shurumubiaogpa= Label(root,text = '''能接受每学期学的最高分数为''',fg = '#191970',relief =FLAT)
        shurumubiaogpa.place(relx = 0.08,rely = by)
        zuigaofenshu = Entry(root,width = 7)
        zuigaofenshu.place(relx = 0.6,rely = by)    
        
        by+=0.05
        rabuttonlittlehard = Radiobutton(root,text="愿意接受每学期达到较高绩点,选课数较少（默认每学期绩点达到3.8)",fg = '#191970',variable=var,value=1)
        rabuttonlittlehard.place(relx = 0.02,rely = by)
        by+=0.04
        shurumubiaogpa= Label(root,text = '''能接受每学期应达到的最高绩点为''',fg = '#191970',relief =FLAT)
        shurumubiaogpa.place(relx = 0.08,rely = by)
    
        zuigaojidian = Entry(root,width = 7)
        zuigaojidian.place(relx = 0.6,rely = by)
    
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
                if i == 0:
                    s = "！输入违法，请重新输入，学分数不可以为零"
                    otherinfo.insert(END,s)
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
                    maxgpa = 3.80
                    
                i = maxgpa
                
                if i <= targetgpa:
                    s = "每学期要达到的GPA要高于目标GPA才能达成目标噢~"
                    otherinfo.insert(END,s)
    
                x = (targetgpa*currscore-currtotal)/(leftterms*(i-targetgpa))
                
                #将学分数向上取整
                x = math.ceil(x)
                if x>30 or x<0:
                    s = "很抱歉，无法达到目标GPA"
                    otherinfo.insert(END,s)
                else:
                    yingxiuscore.insert(END,x)
                    yingdadaojidian.insert(END,i)
        
        
        by+=0.05
    
        letsgenerate = Button(root,text = '''生成计划''',command = func2,bg = '#4169E1',font = ('仿宋',12,'bold'),fg = '#F8F8FF')
        letsgenerate.place(relx = 0.08,rely = by)
        
        by+=0.055
        
        labelyinggaixiuscore= Label(root,text = '''您需要在接下来每学期修习学分数为：''',bg = '#FFFF00',font = ('仿宋',11,'bold'),fg = '#191970',relief =FLAT)
        labelyinggaixiuscore.place(relx = 0.08,rely = by)
        
        yingxiuscore = Text(root)
        yingxiuscore.place(relx = 0.8,rely=by,relwidth = 0.1,relheight = 0.04)
        
        by+=0.045
        
        labelyinggaidadaodejidian= Label(root,text = '''每学期绩点应达到''',bg = '#FFFF00',font = ('仿宋',11,'bold'),fg = '#191970',relief =FLAT)
        labelyinggaidadaodejidian.place(relx = 0.08,rely = by)
        
        yingdadaojidian = Text(root)
        yingdadaojidian.place(relx = 0.8,rely=by,relwidth = 0.1,relheight = 0.04)
        
        by+=0.045
        
        otherinfo = Text(root,font = ('仿宋',11,'bold'),fg = '#DC143C')
        otherinfo.place(relx = 0.08,rely=by,relwidth = 0.8,relheight = 0.2)
        
    
    biaoti =Label(root,text = 'GPA提升神器',bg = '#4169E1',font = ('仿宋',16,'bold'),fg = '#F8F8FF',width = 20,height = 2,relief =FLAT)
    biaoti.place(relx = 0.32,rely = 0.01, relheight = 0.05, relwidth = 0.36)
    
    row1minwidth = 0.035 #单位小长度
    beginningy = 0.06 #y的起始位置
    
    beginningy+=0.01
    #空隙 0.01
    
    qingxuanzetishi =Label(root,text = ''' 请选择自己制定学习计划然后查看最终GPA\n或设定目标由我们为您生成学习计划''',font = ('仿宋',12),fg = '#000080',relief =FLAT)
    qingxuanzetishi.place(relx = 0.1,rely = beginningy, relheight = 0.06)
    
    beginningy+=0.07
    
    buttonmakeitbyyourself = Button(root, text='自己制定计划', command=makeitbyyourself,bg = '#6495ED',font = ('仿宋',12,'bold'),fg = '#F8F8FF')
    buttonmakeitbyyourself.place(relx = 0.17,rely = beginningy)
    
    buttonwegenerateit = Button(root, text='我们为你生成', command=wegenerateit,bg = '#6495ED',font = ('仿宋',12,'bold'),fg = '#F8F8FF')
    buttonwegenerateit.place(relx = 0.52,rely = beginningy)


    
def fundamentalcal():
    root = Toplevel()
    root.title("计算器")
    root.minsize(400, 600)      # 窗口大小400*600
    root.resizable(0, 0) 
    
    def get_input(entry, argu):
        entry.insert(END, argu)

        
        
    def backspace(entry):
        input_len = len(entry.get())
        entry.delete(input_len - 1)

    def clear(entry):
        entry.delete(0, END)

    def calc(entry):
        input = entry.get()
        output = str(eval(input.strip()))
        clear(entry)
        entry.insert(END, output)

    def sin_an(entry):    #num为角度
        input = entry.get()
        num = float(input.strip())
        temp = math.sin(num*math.pi/180)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)

    def sin_rad(entry):    #num为弧度
        input = entry.get()
        num = float(input.strip())
        temp = math.sin(num)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)
        
    def log_a(entry):
        input = entry.get()
        num = float(input.strip())
        temp = math.log(num,math.e)
        a = round(temp,10)
        clear(entry)
        entry.insert(END,a)

    def cos_an(entry):    #num为角度
        input = entry.get()
        num = float(input.strip())
        temp = math.cos(num*math.pi/180)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)

    def cos_rad(entry):    #num为弧度
        input = entry.get()
        num = float(input.strip())
        temp = math.cos(num)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)

    def tan_an(entry):    #num为角度
        input = entry.get()
        num = float(input.strip())
        temp = math.tan(num*math.pi/180)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)

    def tan_rad(entry):    #num为弧度
        input = entry.get()
        num = float(input.strip())
        temp = math.tan(num)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)
    
 
        

    entry_font = tkinter.font.Font(size=30)
    entry = Entry(root, justify="right", font=entry_font)
    entry.place(x=0, y=0, width=400, height=110)

    button_font = tkinter.font.Font(size=18, weight=tkinter.font.BOLD)

    # 1
    a = 0
    b = 110
    button13 = Button(root,text='.', command=lambda: get_input(entry, '.'),font=(13),bg = '#FFEBCD',relief =FLAT)
    button13.place(x=a, y=b, width=100, height=70)

    button15 = Button(root, text='退格', bg='#FFEBCD',font=(13),command=lambda: backspace(entry),relief =FLAT)
    button15.place(x=a+100, y=b, width=100, height=70)

    button16 = Button(root, text='C', bg='#FFEBCD',font=(13),command=lambda : clear(entry),relief =FLAT)
    button16.place(x=a+200, y=b, width=100, height=70)

    button10 = Button(root,text='+', bg='#FFEBCD',font=(13),command=lambda: get_input(entry, '+'),relief =FLAT)
    button10.place(x=a+300, y=b, width=100, height=70)
    
    
    # 2
    a = 0
    b+=70
    button7 = Button(root,text='7', bg = '#FFDEAD',font=(13),command=lambda: get_input(entry, '7'),relief =FLAT)
    button7.place(x=a, y=b, width=100, height=70)

    button8 = Button(root,text='8', bg = '#FFDEAD',font=(13),command=lambda: get_input(entry, '8'),relief =FLAT)
    button8.place(x=a+100, y=b, width=100, height=70)
    
    button9 = Button(root,text='9', bg = '#FFDEAD',font=(13),command=lambda: get_input(entry, '9'),relief =FLAT)
    button9.place(x=a+200, y=b, width=100, height=70)
    
    button11 =Button(root,text='-', bg = '#FFDEAD',font=(13), command=lambda: get_input(entry, '-'),relief =FLAT)
    button11.place(x=a+300, y=b, width=100, height=70)
    
    
    # 3
    a = 0
    b+=70
    button4 = Button(root,text='4',bg = '#F4A460', font=(13),command=lambda: get_input(entry, '4'),relief =FLAT)
    button4.place(x=a, y=b, width=100, height=70)

    button5 = Button(root,text='5', bg = '#F4A460',font=(13),command=lambda: get_input(entry, '5'),relief =FLAT)
    button5.place(x=a+100, y=b, width=100, height=70)

    button6 = Button(root,text='6',bg = '#F4A460', font=(13),command=lambda: get_input(entry, '6'),relief =FLAT)
    button6.place(x=a+200, y=b, width=100, height=70)
    
    button12 = Button(root,text='*', bg = '#F4A460',font=(13),command=lambda: get_input(entry, '*'),relief =FLAT)
    button12.place(x=a+300, y=b, width=100, height=70)
    
    
    #4
    a = 0
    b+=70
    button1 = Button(root,text='1', bg = '#FFA500',font=(13),command=lambda: get_input(entry, '1'),relief =FLAT)
    button1.place(x=a, y=b, width=100, height=70)

    button2 = Button(root,text='2', bg = '#FFA500',font=(13),command=lambda: get_input(entry, '2'),relief =FLAT)
    button2.place(x=a+100, y=b, width=100, height=70)

    button3 = Button(root,text='3', bg = '#FFA500', font=(13),command=lambda: get_input(entry, '3'),relief =FLAT)
    button3.place(x=a+200, y=b, width=100, height=70)

    button14 = Button(root, text='/', bg='#FFA500',font=(13),command=lambda: get_input(entry, '/'),relief =FLAT)
    button14.place(x=a+300, y=b, width=100, height=70)
    
    def help():
        root2 = Toplevel()
        root2.title("帮助")
        root2.minsize(400,20)
        helpimage = Text(root2,font = ('微软雅黑',12))
        w = '指数功能：\n请先输入底数再点击指数再在后面输入指数\nln功能：\n请先输入真数再点击ln键\nsin cos tan等六个三角函数功能：\n请先输入弧度或角度再点击计算器相应按键'
        helpimage.insert(END,w)
        helpimage.place(relx = 0,rely = 0)
        btClose=Button(root2,text='返回计算器主界面',command=root2.destroy)
        btClose.place(relx=0.7,rely=0.7)
        
    #5
    a = 0
    b+=70
    button0 = Button(root,text='0',bg='#FF8C00', font=(13),command=lambda: get_input(entry, '0'),relief =FLAT)
    button0.place(x=a, y=b, width=100, height=70)

    button17 = Button(root, text='=', bg='#FF8C00',font=(13),command=lambda: calc(entry),relief =FLAT)
    button17.place(x=a+100, y=b, width=100, height=70)
    
    button25 = Button(root, text='帮助', bg='#FF8C00',font=(13),command=help,relief =FLAT)
    button25.place(x=a+200, y=b, width=200, height=70)
    
    #6
    a = 0
    b+=70
    button18 = Button(root, text='sin\n(角度制)', bg='#CD853F',font=(13),command=lambda : sin_an(entry),relief =FLAT)
    button18.place(x=a, y=b, width=100, height=70)
    
    button20 = Button(root, text='cos\n(角度制)', bg='#CD853F',font=(13),command=lambda : cos_an(entry),relief =FLAT)
    button20.place(x=a+100, y=b, width=100, height=70)
    
    button22 = Button(root, text='tan\n(角度制)', bg='#CD853F',font=(13),command=lambda : tan_an(entry),relief =FLAT)
    button22.place(x=a+200, y=b, width=100, height=70)

    button12 = Button(root,text='指数', bg='#CD853F',font=(13),command=lambda: get_input(entry, '**'),relief =FLAT)
    button12.place(x=a+300, y=b, width=100, height=70)
    
    #7
    a = 0
    b+=70
    button19 = Button(root, text='sin\n(弧度制)', bg= '#8B4513',font=(13),command=lambda : sin_rad(entry),relief =FLAT)
    button19.place(x=a, y=b, width=100, height=70)

    button21 = Button(root, text='cos\n(弧度制)', bg= '#8B4513',font=(13),command=lambda : cos_rad(entry),relief =FLAT)
    button21.place(x=a+100, y=b, width=100, height=70)

    button23 = Button(root, text='tan\n(弧度制)', bg= '#8B4513',font=(13),command=lambda : tan_rad(entry),relief =FLAT)
    button23.place(x=a+200, y=b, width=100, height=70)

        
    button24 = Button(root, text='ln', bg= '#8B4513',font=(13),command=lambda: log_a(entry),relief =FLAT)
    button24.place(x=a+300, y=b, width=100, height=70)
    
def fin():
    root4 = Toplevel()
    root4.title('金融计算器')
    root4.minsize(220,300)


    def fin1():
        root41 = Toplevel()
        root41.title('求将来资金总值')
        frame = Frame(root41)

        Label(root41, text = '参数名称').grid(row = 0, column = 0)
        Label(root41, text = '值').grid(row = 0, column = 1)
        Label(root41, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root41, text = 'nper年数').grid(row = 2, column = 0)
        Label(root41, text = 'pmt月供').grid(row = 3, column = 0)
        Label(root41, text = 'pv现在资金总额').grid(row = 4, column = 0)

        e1 = Entry(root41)
        e2 = Entry(root41)
        e3 = Entry(root41)
        e4 = Entry(root41)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e4.grid(row=4, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root41, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Future_Value():    #利率可以是数值or矩阵
            a = np.fv(eval(e1.get()), eval(e2.get()), eval(e3.get()), eval(e4.get()))
            a = 0 - a
            v1.set(a)

        Button(root41, text='将来资金总值', width=10, command = Future_Value).grid(row=5, column=0, sticky=W, padx=10, pady=5)

    def fin2():
        root42 = Toplevel()
        root42.title('求现在需投资资金总额')
        frame = Frame(root42)

        Label(root42, text = '参数名称').grid(row = 0, column = 0)
        Label(root42, text = '值').grid(row = 0, column = 1)
        Label(root42, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root42, text = 'nper年数').grid(row = 2, column = 0)
        Label(root42, text = 'pmt月供').grid(row = 3, column = 0)
        Label(root42, text = 'fv期望资金总额').grid(row = 4, column = 0)

        e1 = Entry(root42)
        e2 = Entry(root42)
        e3 = Entry(root42)
        e4 = Entry(root42)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e4.grid(row=4, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root42, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Present_Value():
            a = np.pv(eval(e1.get()), eval(e2.get()), eval(e3.get()), eval(e4.get()))
            a = 0 - a
            v1.set(a)

        Button(root42, text='求现在需投资资金总额', width=10, command = Present_Value).grid(row=5, column=0, sticky=W, padx=10, pady=5)

    def fin3():
        root43 = Toplevel()
        root43.title('求每月利润')
        frame = Frame(root43)

        Label(root43, text = '参数名称').grid(row = 0, column = 0)
        Label(root43, text = '值').grid(row = 0, column = 1)
        Label(root43, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root43, text = 'nper年数').grid(row = 2, column = 0)
        Label(root43, text = 'pv现在资金总额').grid(row = 4, column = 0)

        e1 = Entry(root43)
        e2 = Entry(root43)
        e3 = Entry(root43)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root43, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Payment():
            a = np.pmt(eval(e1.get()), eval(e2.get()), eval(e3.get()))
            a = 0 - a
            v1.set(a)

        Button(root43, text='每月利润', width=10, command = Payment).grid(row=5, column=0, sticky=W, padx=10, pady=5)


    def fin45():
        root445 = Toplevel()
        root445.title('求月供本金、利息')
        frame = Frame(root445)

        Label(root445, text = '参数名称').grid(row = 0, column = 0)
        Label(root445, text = '值').grid(row = 0, column = 1)
        Label(root445, text = 'rate欠款利率(小数)').grid(row = 1, column = 0)
        Label(root445, text = 'nper总期数').grid(row = 2, column = 0)
        Label(root445, text = 'pv现在欠款总额').grid(row = 3, column = 0)
        Label(root445, text = 'per第n个偿还期').grid(row = 4, column = 0)

        e1 = Entry(root445)
        e2 = Entry(root445)
        e3 = Entry(root445)
        e4 = Entry(root445)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e4.grid(row=4, column=1, padx=10, pady=5)

        v1 = StringVar()
        e5 = Entry(root445, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        v2 = StringVar()
        e6 = Entry(root445, width=10, textvariable=v2, state='readonly').grid(row=6, column=1)


        def Payment_Principal():    #求月供中的本金,per表示在第几个偿还期
            a = np.ppmt(eval(e1.get()), eval(e2.get()), eval(e3.get()), eval(e4.get()))
            a = 0 - a
            v1.set(a)

        def Payment_Interest():     #要求同上
            a = np.ipmt(eval(e1.get()), eval(e2.get()), eval(e3.get()), eval(e4.get()))
            a = 0 - a
            v2.set(a)

        Button(root445, text='求月供本金', width=10, command = Payment_Principal).grid(row=5, column=0, sticky=W, padx=10, pady=5)
        Button(root445, text='求月供利息', width=10, command = Payment_Interest).grid(row=6, column=0, sticky=W, padx=10, pady=5)    


    def fin67():
        root467 = Toplevel()
        root467.title('求净现值、内部回报率')
        frame = Frame(root467)

        Label(root467, text = '参数名称').grid(row = 0, column = 0)
        Label(root467, text = '值').grid(row = 0, column = 1)
        Label(root467, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root467, text = '每日现金(输入一组数)').grid(row = 2, column = 0)

        e1 = Entry(root467)
        e2 = Entry(root467)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)

        v1 = StringVar()
        e5 = Entry(root467, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        v2 = StringVar()
        e6 = Entry(root467, width=10, textvariable=v2, state='readonly').grid(row=6, column=1)

        def Net_pv():    #values是一个array
            a = np.npv(eval(e1.get()), eval(e2.get()))
            v1.set(a)

        def Internal_Rate_Return():    #要求同上
            a = np.irr(eval(e2.get()))
            v2.set(a)                                                                           


        Button(root467, text='求净现值', width=10, command = Net_pv).grid(row=5, column=0, sticky=W, padx=10, pady=5)
        Button(root467, text='求内部回报率', width=10, command = Internal_Rate_Return).grid(row=6, column=0, sticky=W, padx=10, pady=5)    

    def fin8():
        root48 = Toplevel()
        root48.title('求偿还年数')
        frame = Frame(root48)

        Label(root48, text = '参数名称').grid(row = 0, column = 0)
        Label(root48, text = '值').grid(row = 0, column = 1)
        Label(root48, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root48, text = 'pmt月供').grid(row = 2, column = 0)
        Label(root48, text = 'pv现在欠款总额').grid(row = 3, column = 0)

        e1 = Entry(root48)
        e2 = Entry(root48)
        e3 = Entry(root48)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root48, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Year_nper():
            a = np.nper(float(e1.get())), eval(e2.get()), eval(e3.get())
            a = int(a) + 1
            v1.set(a)

        Button(root48, text='求偿还年数', width=10, command = Year_nper).grid(row=5, column=0, sticky=W, padx=10, pady=5)


    
    Button1 = Button(root4, text='将来资金总值', bg = '#FFE4E1',font=('宋体',12),command = fin1,relief =FLAT).place(x=0,y=0,width=110,height=100)
    Button2 = Button(root4, text='现在需投资\n资金总额',  bg = '#FFE4E1',font=('宋体',12),command = fin2,relief =FLAT).place(x=110,y=0,width=110,height=100)
    Button3 = Button(root4, text='每月利润', bg = '#F08080', font=('宋体',12),command = fin3,relief =FLAT).place(x=0,y=100,width=110,height=100)
    Button4 = Button(root4, text='月供本金、\n利息', bg = '#F08080',font=('宋体',12),command = fin45,relief =FLAT).place(x=110,y=100,width=110,height=100)    
    Button5 = Button(root4, text='净现值、\n内部回报率',bg = '#FA8072',font=('宋体',12), command = fin67,relief =FLAT).place(x=0,y=200,width=110,height=100)    
    Button6 = Button(root4, text='偿还年数', bg = '#FA8072',font=('宋体',12),command = fin8,relief =FLAT).place(x=110,y=200,width=110,height=100)      

wd = Tk()
wd.title('冲冲冲计算器')
wd.geometry('900x480')

#期望图像显示的大小  
w_box = 480
h_box = 90
  
# open as a PIL image object  
#以一个PIL图像对象打开  
pil_image = Image.open(r'C:/Users/Administrator/Desktop/calculator/bigtitle.png')  

#获取图像的原始大小  
w, h = pil_image.size  

#缩放图像让它保持比例，同时限制在一个矩形框范围内  
pil_image_resized = resize(w, h, w_box, h_box, pil_image)  

# 把PIL图像对象转变为Tkinter的PhotoImage对象  
tk_image = ImageTk.PhotoImage(pil_image_resized)  

bigtitle = Label(wd,image=tk_image, width=w_box, height=h_box)
bigtitle.place(relx = 0.08,rely = 0,relwidth = 0.84)

w_box2 = 200
h_box2 = 300

fund_pil_image = Image.open(r'C:/Users/Administrator/Desktop/calculator/fundamentalcal.png')  
 
fund_w, fund_h =fund_pil_image.size  

fund_pil_image_resized = resize(fund_w, fund_h, w_box2, h_box2, fund_pil_image)  

fund_tk_image = ImageTk.PhotoImage(fund_pil_image_resized) 
 
gpa_pil_image = Image.open(r'C:/Users/Administrator/Desktop/calculator/gpa.png')  
 
gpa_w, gpa_h =gpa_pil_image.size  

gpa_pil_image_resized = resize(gpa_w, gpa_h, w_box2, h_box2, gpa_pil_image)  

gpa_tk_image = ImageTk.PhotoImage(gpa_pil_image_resized)  

fin_pil_image = Image.open(r'C:/Users/Administrator/Desktop/calculator/fin.png')  
 
fin_w, fin_h =fin_pil_image.size  

fin_pil_image_resized = resize(fin_w, fin_h, w_box2, h_box2, fin_pil_image)  

fin_tk_image = ImageTk.PhotoImage(fin_pil_image_resized)  

bigtitle = Label(wd,image=tk_image, width=w_box, height=h_box)
bigtitle.place(relx = 0.08,rely = 0,relwidth = 0.84)
Button_fundamentalcal = Button(wd, image = fund_tk_image , width=w_box2, height = h_box2, command = fundamentalcal)
Button_fundamentalcal.place(x = 20,y = 110)
Button_gpa = Button(wd, image = gpa_tk_image , width=w_box2, height = h_box2, command = gpa)
Button_gpa.place(x = 245,y=110)
Button_fin = Button(wd, image = fin_tk_image , width=w_box2, height = h_box2, command = fin)
Button_fin.place(x = 470,y=110)

label_funda = Label(wd,text = '基本计算器',font = ('仿宋',14,'bold'))
label_funda.place(x = 20,y = 430,relwidth = 0.2,relheight = 0.05)

label_funda = Label(wd,text = 'GPA提升神器',font = ('仿宋',14,'bold'))
label_funda.place(x = 245,y = 430,relwidth = 0.2,relheight = 0.05)

label_funda = Label(wd,text = '金融计算器',font = ('仿宋',14,'bold'))
label_funda.place(x = 480,y = 430,relwidth = 0.2,relheight = 0.05)


mainloop()