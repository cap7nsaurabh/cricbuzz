import urllib2 as u2
from bs4 import BeautifulSoup as bs
from Tkinter import *
import time
def red2(url2,root):
     req=u2.urlopen(url2)
     soup=bs(req,'html.parser')  
     s=soup.find('div',class_="cb-min-bat-rw")
     li=s.find_all('span')
     tt=Text(root,height=3,width=30)
     pr1= "score: "+str(li[0].get_text())+'\n'
     pr2="CRR: "+str(li[3].get_text())
     tt.insert(END,pr1)
     tt.insert(END,pr2)
     tt.pack()
     start=time.time()
     elapsed=0
     while elapsed<10:
         elapsed=time.time()-start
         time.sleep(1)
     red2(url2,root)
def red():
    root1=Tk()
    Label(root1,text="url: ").grid(row=0)
    e=Entry(root1)
    e.grid(row=0,column=1)
    def pros(ent=e,roo=root1):
        global url2
        url2=str(e.get())
    b1=Button(root1,text='submit',command=pros).grid(row=2 ,column=0,sticky=W,pady=4)
    b2=Button(root1,text='done',command=root1.destroy).grid(row=2,column=1,sticky=W,pady=4)
    root1.mainloop()
    root=Tk()
    tt=Text(root,height=3,width=40)
    i=0
    while 1:
        req=u2.urlopen(url2)
        soup=bs(req,'html.parser')  
        s=soup.find('div',class_="cb-min-bat-rw")
        li=s.find_all('span')
        pr1= "score: "+str(li[0].get_text())+'\n'
        pr2="CRR: "+str(li[3].get_text())
        tt.delete('1.0',END)
        tt.insert(END,pr1)
        tt.insert(END,pr2)
        tt.pack()    
        root.update_idletasks()
        root.update()
        i=i+1
        time.sleep(10)
    tt.pack()
    root.mainloop()
red()
