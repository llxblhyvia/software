# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:26:51 2020

@author: Administrator
"""

from tkinter import *

def makeitbyyourself():
    by =0.238
    
    mibycurrgpa = currgpa
    mibycurrscore = currscore
    mibyleftterms = leftterms
    
    
    ps1 = Label(root,text = '''填写示例:大二上''',font = ('微软雅黑',9),relief =FLAT)
    ps1.place(relx = 0.08,rely = by-0.04)
    
    daji1 = Entry(root,width = 7)
    daji1.place(relx = 0.1,rely = by)
    
    #entry 0.06
    xueqijihuaxiuxi1 = Label(root,text = '''学期计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi1.place(relx = 0.15,rely = by)
    #label 一个字 0.0166
    termscore1 = Entry(root,width = 7)
    termscore1.place(relx = 0.25,rely = by)
    
    zitermscore1 = Label(root,text = '''学分，GPA计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore1.place(relx = 0.31,rely = by)
    
    termgpa1 = Entry(root,width = 7)
    termgpa1.place(relx = 0.44,rely = by)
    
    ps2 = Label(root,text = '''请还剩几学期就填写几学期的计划''',font = ('微软雅黑',9),relief =FLAT)
    ps2.place(relx = 0.5,rely = by)
     
    by +=0.04
    
    daji2 = Entry(root,width = 7)
    daji2.place(relx = 0.1,rely = by)
    
    #entry 0.06
    xueqijihuaxiuxi2 = Label(root,text = '''学期计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi2.place(relx = 0.15,rely = by)
    #label 一个字 0.0166
    termscore2 = Entry(root,width = 7)
    termscore2.place(relx = 0.25,rely = by)
    
    zitermscore2 = Label(root,text = '''学分，GPA计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore2.place(relx = 0.31,rely = by)
    
    termgpa2 = Entry(root,width = 7)
    termgpa2.place(relx = 0.44,rely = by)
    
    by +=0.04
    
    daji3 = Entry(root,width = 7)
    daji3.place(relx = 0.1,rely = by)
    
    #entry 0.06
    xueqijihuaxiuxi3 = Label(root,text = '''学期计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi3.place(relx = 0.15,rely = by)
    #label 一个字 0.0166
    termscore3 = Entry(root,width = 7)
    termscore3.place(relx = 0.25,rely = by)
    
    zitermscore3 = Label(root,text = '''学分，GPA计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore3.place(relx = 0.31,rely = by)
    
    termgpa3 = Entry(root,width = 7)
    termgpa3.place(relx = 0.44,rely = by)
     
    by +=0.04
    
    daji4 = Entry(root,width = 7)
    daji4.place(relx = 0.1,rely = by)
    
    #entry 0.06
    xueqijihuaxiuxi4 = Label(root,text = '''学期计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi4.place(relx = 0.15,rely = by)
    #label 一个字 0.0166
    termscore4 = Entry(root,width = 7)
    termscore4.place(relx = 0.25,rely = by)
    
    zitermscore4 = Label(root,text = '''学分，GPA计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore4.place(relx = 0.31,rely = by)
    
    termgpa4 = Entry(root,width = 7)
    termgpa4.place(relx = 0.44,rely = by)
    
    by +=0.04
    
    daji5 = Entry(root,width = 7)
    daji5.place(relx = 0.1,rely = by)
    
    #entry 0.06
    xueqijihuaxiuxi5 = Label(root,text = '''学期计划修习''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    xueqijihuaxiuxi5.place(relx = 0.15,rely = by)
    #label 一个字 0.0166
    termscore5 = Entry(root,width = 7)
    termscore5.place(relx = 0.25,rely = by)
    
    zitermscore5 = Label(root,text = '''学分，GPA计划达到''',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    zitermscore5.place(relx = 0.31,rely = by)
    
    termgpa5 = Entry(root,width = 7)
    termgpa5.place(relx = 0.44,rely = by)
    
    
    
def wegenerateit():
   
    by =0.238
    
    wgicurrgpa = currgpa
    wgicurrscore = currscore
    wgileftterms = leftterms
    
    daji = Entry(root,width = 7)
    daji.place(relx = 0.1,rely = by)
    
    shurumubiaogpa= Label(root,text = '''请输入目标GPA:''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    shurumubiaogpa.place(relx = 0.08,rely = by)
    
    mubiaogpa = Entry(root,width = 7)
    mubiaogpa.place(relx = 0.196,rely = by)
    
    by+=0.04
    #换行+0.04
    labelxuanzemoshi= Label(root,text = '''选择想要的模式（每学期模式相同噢）''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',relief =FLAT)
    labelxuanzemoshi.place(relx = 0.08,rely = by)
    
    def model():
      dic = {0:'甲',1:'乙',2:'丙'}
      s = "您选了" + dic.get(var.get()) + "项"
      lb.config(text = s)
    
    by+=0.04
    
    var = IntVar()
    rabuttonmucheasy = Radiobutton(root,text="愿意修大量甚至溢出学分，每学期绩点要求稍低（默认每学期修30分）   能接受每学期学的最高分数为",fg = '#191970',variable=var,value=0,command=model)
    rabuttonmucheasy.place(relx = 0.08,rely = by)

    rabuttonlittlehard = Radiobutton(root,text="愿意接受每学期达到较高绩点，选修课程数较少（默认每学期绩点达到3.8）   能接收每学期应达到的最高绩点为",fg = '#191970',variable=var,value=1,command=model)
    rabuttonlittlehard.place(relx = 0.08,rely = by+0.05)
    
    zuigaofenshu = Entry(root,width = 7)
    zuigaofenshu.place(relx = 0.56,rely = by)
    
    zuigaojidian = Entry(root,width = 7)
    zuigaojidian.place(relx = 0.6,rely = by+0.05)
    
    by+=0.05
    by+=0.05
    labelyinggaixiuscore= Label(root,text = '''您需要在接下来每学期修''',bg = '#FFFF00',font = ('仿宋',12,'bold'),fg = '#191970',relief =FLAT)
    labelyinggaixiuscore.place(relx = 0.08,rely = by)
    
    yingxiuscore = Text(root)
    yingxiuscore.place(relx = 0.243,rely=by,relwidth = 0.05,relheight = 0.04)
    
    labelyinggaidadaodejidian= Label(root,text = '''学分，每学期绩点应达到''',bg = '#FFFF00',font = ('仿宋',12,'bold'),fg = '#191970',relief =FLAT)
    labelyinggaidadaodejidian.place(relx = 0.3,rely = by)
    
    yingxiuscore = Text(root)
    yingxiuscore.place(relx = 0.465,rely=by,relwidth = 0.05,relheight = 0.04)
    
    print(by)
    

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

qingshurudangqiangpa = Message(root,text = '''请输入：  当前GPA''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',width = 500,relief =FLAT)
#message没有height
qingshurudangqiangpa.place(relx = row1minwidth,rely = beginningy)

dangqiangpa = Entry(root,width = 7)
dangqiangpa.place(relx = 0.17,rely = beginningy)
'''得到当前gpa数值存放在currgpa中'''
currgpa = dangqiangpa.get()

wenzicurrxuefenshu = Message(root,text = '''现修习学分数\n（0~180的整数）''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',width = 500,relief =FLAT)
wenzicurrxuefenshu.place(relx = 0.26,rely = beginningy)

currxuefenshu = Entry(root,width = 7)
currxuefenshu.place(relx = 0.4,rely = beginningy)
'''得到当前修的学分存放在currscore中'''
currscore = currxuefenshu.get()

wenzileftterms = Message(root,text = ''' 还剩学期数\n(1~5的整数)''',bg = '#F0F8FF',font = ('仿宋',12,'bold'),fg = '#000080',width = 500,relief =FLAT)
wenzileftterms.place(relx = 0.47,rely = beginningy)

entryleftterms = Entry(root,width = 7)
entryleftterms.place(relx = 0.57,rely = beginningy)
'''得到还剩的学期数存放在leftterms中'''
leftterms = entryleftterms.get()

beginningy+=0.065
#两行12号字的message 0.055+0.01

qingxuanzetishi =Label(root,text = ''' 请选择自己制定学习计划然后查看最终GPA或设定目标由我们为您生成学习计划''',font = ('仿宋',14),fg = '#000080',relief =FLAT)
qingxuanzetishi.place(relx = 0.2,rely = beginningy, relheight = 0.035)

beginningy+=0.038

buttonmakeitbyyourself = Button(root, text='自己制定计划', command=makeitbyyourself,bg = '#6495ED',font = ('仿宋',12,'bold'),fg = '#F8F8FF')
buttonmakeitbyyourself.place(relx = 0.25,rely = beginningy)

buttonwegenerateit = Button(root, text='我们为你生成', command=wegenerateit,bg = '#6495ED',font = ('仿宋',12,'bold'),fg = '#F8F8FF')
buttonwegenerateit.place(relx = 0.5,rely = beginningy)

    

root.mainloop()
