import tkinter, os, math, re
from tkinter import StringVar,IntVar
from PIL import Image, ImageTk


class PrivateChat(tkinter.Toplevel):
    def __init__(self, user_name, friend_name):
        super().__init__()
        self.user_name = user_name
        self.friend_name = friend_name
        # self.friend_name = StringVar()
        # self.friend_name.set("ss")

        self.title("CQ")
        self.resizable(width=False, height=False)  # 窗口大小不可变
        self.geometry('%dx%d+%d+%d' % (550, 510, 650, 30))  # 设置窗口大小 和位置
        self['background'] = '#76B2ED'

        current_path = os.path.abspath(__file__)  # 获取当前文件路径
        path = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),
                            'static', 'image', 'private_chat')

        self.friend_head_img = Image.open(os.path.join(path, 'head_QQ48px.png'))
        self.friend_head_img = ImageTk.PhotoImage(self.friend_head_img)

        self.tool_picture_img = Image.open(os.path.join(path, 'pictures_24px.png'))
        self.tool_picture_img = ImageTk.PhotoImage(self.tool_picture_img)

        self.tool_expression_img = Image.open(os.path.join(path, 'CQ_expression_24px.png'))
        self.tool_expression_img = ImageTk.PhotoImage(self.tool_expression_img)

        self.input_text = StringVar()

        self.message_num = 0  # 消息数量

        self.a =1


        self.createpage()

    def createpage(self):
        self.page = tkinter.Frame(self, bg='#76B2ED')
        self.page.pack(expand=True)


        self.text_page = tkinter.Text(self,bg='white',bd=0,width=78,height=17,font=('宋体',11),state='disable')
        self.vbar = tkinter.Scrollbar(self.text_page, orient='vertical', bg='#ccc')  # 竖直滚动条
        self.text_page['yscrollcommand'] = self.vbar.set

        self.text_page.pack(side="top",pady=3)
        self.vbar.configure(command=self.text_page.yview)
        self.vbar.place(x=531, width=15, height=310)


        self.tool_page = tkinter.Frame(self, bg='#76B2ED')
        self.tool_page.pack()

        self.input_page = tkinter.Frame(self, bg='#76B2ED')
        self.input_page.pack()

        # hbar = tkinter.Scrollbar(canvas, orient='horizontal')  # 水平滚动条
        # hbar.place(x=0, y=165, width=180, height=20)
        # hbar.configure(command=canvas.xview)
        # canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)  # 设置


        tkinter.Label(self.page, image=self.friend_head_img, width=48, height=48) \
            .grid(row=0)
        self.friend = tkinter.Label(self.page, text='', bg='#76B2ED', width=8, height=3)
        self.friend['text'] = self.friend_name
        self.friend.grid(row=0, column=1, stick='sw')
        tkinter.Label(self.page, text='', bg='#76B2ED', width=61, height=3) \
            .grid(row=0, column=2, stick='sw')

        tkinter.Label(self.tool_page, image=self.tool_picture_img, width=27, height=23) \
            .grid(row=0, padx=3)
        tkinter.Label(self.tool_page, image=self.tool_expression_img, width=27, height=23) \
            .grid(row=0, column=1)
        tkinter.Label(self.tool_page, text='', width=68, height=1, bg='#76B2ED') \
            .grid(row=0, column=2)

        self.text = tkinter.Text(self.input_page, width=77, height=5)

        self.text.grid(row=0)
        self.send = tkinter.Label(self.input_page, text='发送', width=5, height=1, bg='#ccc', fg='#111')
        self.send.grid(row=1, stick='E')

        self.event_monitor()

    def event_monitor(self):

        # self.send.bind('<Button-1>', self.chat_text)
        self.send.bind('<Button-1>', self.test)

    def test(self,event):
        self.chat_text(event,name="测试",message='测试测试测试测试测试测试测试测试测试测试测试',flag=0)

        #
        self.bind('<Return>', self.chat_text)

    def chat_text(self, event, name='', message='', flag=1):
        # for i in range(self.message_num):
        #
        #     tkinter.Label(self.text_page, image=self.friend_head_img, bg="white") \
        #         .grid(row=5+i, column=0, stick='w', pady=5)
        #     tkinter.Label(self.text_page, textvariable=self.friend_name, bg="white", borderwidth=0,
        #                    width=12).grid(row=5+i, column=1, stick='E', pady=3)
        #     tkinter.Label(self.text_page, text='', width=50, borderwidth=0, bg="white")\
        #                   .grid(row=5+i, column=2,padx=10)

        if flag:
            self.message = self.text.get('1.0', 'end')
            self.message = re.findall(r'[^(\n)]', self.message)
            self.message = ''.join(self.message)
            # print(self.message)
            if len(self.message) > 0:

                self.text_page['state']='normal'
                self.empty01=tkinter.Label(self.text_page,text='',bg='white',width=68-len(self.user_name))
                self.text_page.window_create('%d.0'%(self.a),window=self.empty01)
                self.text_user_name = tkinter.Label(self.text_page,text='',bg='white')
                self.text_user_name['text']=self.user_name
                self.text_page.window_create('%d.1'%(self.a), window=self.text_user_name)

                self.text_page.image_create('end',image=self.friend_head_img)
                self.text_page.insert('end','\n')

                self.empty02 = tkinter.Label(self.text_page, text='', width=50,bg='white')
                self.text_page.window_create('%d.0'%(self.a+1), window=self.empty02)
                self.text_message = tkinter.Label(self.text_page,text='',bg='#B4F5D6',wraplength=150,justify='left')
                self.text_message['text']=self.message
                self.text_page.window_create('%d.1'%(self.a+1), window=self.text_message)
                self.text_page.insert('end','\n')

                self.text_page.see('end')
                self.a +=2
                self.text.delete('1.0', 'end')
                self.text_page['state'] = 'disable'

        else:

            self.text_page['state'] = 'normal'
            self.text_page.image_create('end', image=self.friend_head_img)

            self.text_friend_name = tkinter.Label(self.text_page, text='', bg='white')
            self.text_friend_name['text'] = self.friend_name
            self.text_page.window_create('%d.1' % (self.a), window=self.text_friend_name)
            self.text_page.insert('end', '\n')

            self.empty02 = tkinter.Label(self.text_page, text='', width=3,bg='white')
            self.text_page.window_create('%d.0' % (self.a + 1), window=self.empty02)
            self.text_message = tkinter.Label(self.text_page, text='', bg='#B4F5D6', wraplength=150, justify='left')
            self.text_message['text'] = message
            self.text_page.window_create('%d.1' % (self.a + 1), window=self.text_message)
            self.text_page.insert('end', '\n')

            self.text_page.see('end')
            self.a += 2
            self.text_page['state'] = 'disable'


root = PrivateChat("zs", "ls")
root.mainloop()
