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
    root.geometry('200x300')

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

    entry_font = tkinter.font.Font(size=12)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, sticky=N+W+S+E, padx=5,  pady=5)

    button_font = tkinter.font.Font(size=10, weight=tkinter.font.BOLD)
    button_bg = '#D5E0EE'
    button_active_bg = '#E5E35B'

    myButton = partial(Button, root, bg=button_bg, padx=10, pady=3, activebackground = button_active_bg)

    button7 = myButton(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=1, column=0, pady=5)

    button8 = myButton(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=1, column=1, pady=5)

    button9 = myButton(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=1, column=2, pady=5)

    button10 = myButton(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=1, column=3, pady=5)

    button4 = myButton(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=2, column=0, pady=5)

    button5 = myButton(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=2, column=1, pady=5)

    button6 = myButton(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=2, column=2, pady=5)

    button11 = myButton(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=2, column=3, pady=5)

    button1 = myButton(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=3, column=0, pady=5)

    button2 = myButton(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=3, column=1, pady=5)

    button3 = myButton(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=3, column=2, pady=5)

    button12 = myButton(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=3, column=3, pady=5)

    button0 = myButton(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=4, column=0, columnspan=2, padx=3, pady=5, sticky=N+S+E+W)

    button13 = myButton(text='.', command=lambda: get_input(entry, '.'))
    button13.grid(row=4, column=2, pady=5)

    button14 = Button(root, text='/', bg=button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '/'))
    button14.grid(row=4, column=3, pady=5)

    button15 = Button(root, text='<-', bg=button_bg, padx=10, pady=3,
                      command=lambda: backspace(entry), activebackground=button_active_bg)
    button15.grid(row=5, column=0, pady=5)

    button16 = Button(root, text='C', bg=button_bg, padx=10, pady=3,
                      command=lambda : clear(entry), activebackground=button_active_bg)
    button16.grid(row=5, column=1, pady=5)

    button17 = Button(root, text='=', bg=button_bg, padx=10, pady=3,
                      command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=2, columnspan=2, padx=3, pady=5, sticky=N+S+E+W)

    button18 = Button(root, text='sin', bg=button_bg, padx=10, pady=3,
                      command=lambda : sin_an(entry), activebackground=button_active_bg)
    button18.grid(row=1, column=4, pady=5)
    
    button19 = Button(root, text='sinh', bg=button_bg, padx=10, pady=3,
                      command=lambda : sin_rad(entry), activebackground=button_active_bg)
    button19.grid(row=1, column=5, pady=5)
    
    button20 = Button(root, text='cos', bg=button_bg, padx=10, pady=3,
                      command=lambda : cos_an(entry), activebackground=button_active_bg)
    button20.grid(row=2, column=4, pady=5)
    
    button21 = Button(root, text='cosh', bg=button_bg, padx=10, pady=3,
                      command=lambda : cos_rad(entry), activebackground=button_active_bg)
    button21.grid(row=2, column=5, pady=5)
    
    button22 = Button(root, text='tan', bg=button_bg, padx=10, pady=3,
                      command=lambda : tan_an(entry), activebackground=button_active_bg)
    button22.grid(row=3, column=4, pady=5)
    
    button23 = Button(root, text='tanh', bg=button_bg, padx=10, pady=3,
                      command=lambda : tan_rad(entry), activebackground=button_active_bg)
    button23.grid(row=3, column=5, pady=5)
    
    button12 = myButton(text='指数', command=lambda: get_input(entry, '**'))
    button12.grid(row=4, column=4, pady=5)
    
    button23 = Button(root, text='对数', bg=button_bg, padx=10, pady=3,
                      command=lambda : log(entry), activebackground=button_active_bg)
    button23.grid(row=4, column=5, pady=5)
    
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

fund_pil_image = Image.open(r'C:/Users/Administrator/Desktop/calculator/daffa.png')  
 
fund_w, fund_h =fund_pil_image.size  

fund_pil_image_resized = resize(fund_w, fund_h, w_box2, h_box2, fund_pil_image)  

fund_tk_image = ImageTk.PhotoImage(fund_pil_image_resized) 
 
gpa_pil_image = Image.open(r'C:/Users/Administrator/Desktop/calculator/gpa.png')  
 
gpa_w, gpa_h =gpa_pil_image.size  

gpa_pil_image_resized = resize(gpa_w, gpa_h, w_box2, h_box2, gpa_pil_image)  

gpa_tk_image = ImageTk.PhotoImage(gpa_pil_image_resized)  

bigtitle = Label(wd,image=tk_image, width=w_box, height=h_box)
bigtitle.place(relx = 0.08,rely = 0,relwidth = 0.84)
Button_fundamentalcal = Button(wd, image = fund_tk_image , width=w_box2, height = h_box2, command = fundamentalcal)
Button_fundamentalcal.place(x = 20,y = 110)
Button_gpa = Button(wd, image = gpa_tk_image , width=w_box2, height = h_box2, command = gpa)
Button_gpa.place(x = 240,y=110)




mainloop()