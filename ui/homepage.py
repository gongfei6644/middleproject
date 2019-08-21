import tkinter, math, os
from tkinter import StringVar
from middle_project.common.entry_display_tool import *
from middle_project.ui.private_chat import PrivateChat

# from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk


class HomePage(tkinter.Tk):
    def __init__(self, get_username, get_friends_list):
        super().__init__()

        self.get_username = get_username
        self.get_friends_list = get_friends_list

        self.title("CQ")
        self.resizable(width=False, height=False)  # 窗口大小不可变
        self.geometry('%dx%d+%d+%d' % (350, 650, 650, 30))  # 设置窗口大小 和位置
        self['background'] = '#76B2ED'

        self.path = StringVar()
        self.current_path = os.path.abspath(__file__)  # 获取当前文件路径
        # 拼接
        self.path = os.path.join(os.path.abspath(os.path.dirname(self.current_path) + os.path.sep + ".."),
                                 'static', 'image', 'homepage')

        self.head_portrait_img = Image.open(os.path.join(self.path, 'head_QQ96px.png'))
        self.head_portrait_img = ImageTk.PhotoImage(self.head_portrait_img)

        self.head_portrait_minimg = Image.open(os.path.join(self.path, 'head_QQ48px.png'))
        self.head_portrait_minimg = ImageTk.PhotoImage(self.head_portrait_minimg)

        self.status_img = Image.open(os.path.join(self.path, 'status1.png'))
        self.status_img = ImageTk.PhotoImage(self.status_img)

        self.chat_img = Image.open(os.path.join(self.path, 'Chat.png'))
        self.chat_img = ImageTk.PhotoImage(self.chat_img)

        self.friends_img = Image.open(os.path.join(self.path, 'friends.png'))
        self.friends_img = ImageTk.PhotoImage(self.friends_img)

        self.group_img = Image.open(os.path.join(self.path, 'group.png'))
        self.group_img = ImageTk.PhotoImage(self.group_img)

        self.foot_more_img = Image.open(os.path.join(self.path, 'foot_more.png'))
        self.foot_more_img = ImageTk.PhotoImage(self.foot_more_img)

        self.foot_add_friends_img = Image.open(os.path.join(self.path, 'foot_add_friends.png'))
        self.foot_add_friends_img = ImageTk.PhotoImage(self.foot_add_friends_img)

        self.username = StringVar()
        self.username.set(self.get_username)
        self.personalized_signature = StringVar()
        self.personalized_signature.set("风华是一种流砂,苍老是一段年华")
        self.search_focus_num = 0
        self.search_value = StringVar()
        # self.search.set("输入您要搜索的好友")

        self.get_friends_list = ["张三", "李四", "王五", "赵旭老师",
                                 "祁老师", "蒙蒙老师", "吕泽老师", "王丹波老师"]  # 好友列表
        self.friends_dict = {}

        self.cleatepage()

    def cleatepage(self):

        self.page = tkinter.Frame(self, bg="#76B2ED")  # 创建Frame
        self.page.pack(expand=True)

        self.canvas = tkinter.Canvas(self, width=400, height=420, scrollregion=
        (0, 0, 520, 62 * len(self.get_friends_list)), bg='#76B2ED')  # 创建canvas
        # canvas.place(x=0, y=190)  # 放置canvas的位置
        self.canvas.pack(expand=True)

        self.content_page = tkinter.Frame(self.canvas, bg="#76B2ED", width=430, height=430)
        # self.content_page.place(width=340, height=400)
        self.content_page.pack(expand=True)
        self.vbar = tkinter.Scrollbar(self.canvas, orient='vertical', bg='#A2CBF5')  # 竖直滚动条
        self.vbar.place(x=335, width=15, height=430)
        self.vbar.configure(command=self.canvas.yview)

        # hbar = tkinter.Scrollbar(canvas, orient='horizontal')  # 水平滚动条
        # hbar.place(x=0, y=165, width=180, height=20)
        # hbar.configure(command=canvas.xview)
        # canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)  # 设置
        self.canvas.config(yscrollcommand=self.vbar.set)  # 设置
        self.canvas.create_window((200, 30 * len(self.get_friends_list)), window=self.content_page)  # create_window

        self.foot = tkinter.Frame(self, width=430, height=50, bg='#F2F7F4')
        self.foot.pack(expand=True)

        # tkinter.Label(self.page,text="CQ",bg="#76B2ED",font=('黑体',20),fg='blue')\
        #     .grid(row=0,column=0,columnspan=2,stick='wn')
        self.head = tkinter.Label(self.page, image=self.head_portrait_img, width=96,
                                  height=96, text=self.path, borderwidth=0, bg="#76B2ED")

        self.head.grid(row=1, column=0, rowspan=2, columnspan=2)

        tkinter.Label(self.page, textvariable=self.username, bg="#76B2ED", font=('宋体', 15)) \
            .grid(row=1, column=2, stick='sw')
        tkinter.Label(self.page, image=self.status_img, bg="#76B2ED", borderwidth=0, width=16, height=16) \
            .grid(row=1, column=3, stick='sw', pady=7)
        tkinter.Entry(self.page, textvariable=self.personalized_signature, width=23, font=("宋体", 12),
                      bd=0, bg="#76B2ED", borderwidth=0).grid(row=2, column=2, columnspan=4, stick='SW')
        # tkinter.Label(self.page,text='',bg="#76B2ED").grid(row=3)

        self.search = tkinter.Entry(self.page, textvariable=self.search_value, width=26, bd=0,
                                    font=("宋体", 15), validate='focus', validatecommand=self.search_display)
        self.search.insert(0, '输入您要搜索的好友')
        self.search.grid(row=3, column=0, columnspan=6, pady=10)

        # tkinter.Label(self.page, text='',bg="#76B2ED").grid(row=5)
        self.chat_index = tkinter.Label(self.page, image=self.chat_img, bg="#76B2ED")
        self.chat_index.grid(row=4, column=0, columnspan=2, stick="w", padx=38, pady=5)

        self.friends_all_index = tkinter.Label(self.page, image=self.friends_img, bg="#76B2ED")
        self.friends_all_index.grid(row=4, column=2, columnspan=2, stick="w", padx=46)

        self.group_index = tkinter.Label(self.page, image=self.group_img, bg="#76B2ED", )
        self.group_index.grid(row=4, column=4, columnspan=2, stick="w")

        self.friends_index_page(0)

    def friends_index_page(self,event):

        for i in range(len(self.get_friends_list)):
            tkinter.Label(self.content_page, image=self.head_portrait_minimg, bg="#76B2ED") \
                .grid(row=5 + i, column=0, stick='w', pady=5)

            self.friends_dict[self.get_friends_list[i]] = tkinter.Label(self.content_page,
                                                                        text='', bg="#76B2ED", borderwidth=0, width=12)
            self.friends_dict[self.get_friends_list[i]]['text'] = self.get_friends_list[i]

            self.friends_dict[self.get_friends_list[i]].grid(row=5 + i, column=1, stick='E', pady=3)

            tkinter.Label(self.content_page, text='', width=33, borderwidth=0, bg="#76B2ED") \
                .grid(row=5 + i, column=2)
        self.foot_page()

    def foot_page(self):
        self.foot_more_func = tkinter.Label(self.foot, image=self.foot_more_img)
        self.foot_more_func.grid(row=0, stick='w', padx=10)

        self.foot_add_friend=tkinter.Label(self.foot, image=self.foot_add_friends_img)
        self.foot_add_friend.grid(row=0, column=1, stick='w')
        tkinter.Label(self.foot, text='', width=36, bg='#F2F7F4').grid(row=0, column=2)

        self.event_monitor()

    def event_monitor(self):
        """事件监控"""
        self.head.bind("<Button-1>", self.head_portrait_change)
        self.chat_index.bind("<Button-1>",self.chat_index_page)
        self.friends_all_index.bind("<Button-1>",self.friends_index_page)
        self.group_index.bind("<Button-1>",self.group_index_page)
        for friend_name, elem in self.friends_dict.items():
            elem.bind("<Double-Button-1>",
                      self.handler_adaptor(self.private_chat, user_name=self.get_username, friend_name=friend_name))

        self.foot_more_func.bind("<Button-1>",self.foot_more_page)
        self.foot_add_friend.bind("<Button-1>",self.foot_add_friend_page)


    def handler_adaptor(self, function, **kwargs):
        """聊天事件处理函数适配器"""
        return lambda event, function=function, kwargs=kwargs: function(event, **kwargs)

    def head_portrait_change(self, event):
        print("更换头像")
        # path_=askopenfilename()
        # self.path.set(path_)
        img = Image.open(os.path.join(self.path, 'head.png'))
        img = ImageTk.PhotoImage(img)
        # self.head_portrait_img= img
        self.head['image'] = img

    def private_chat(self, event, user_name, friend_name):
        PrivateChat(user_name, friend_name)

    def search_display(self):
        default_value = '输入您要搜索的好友'
        entry_display_tool(self.search_focus_num, self.search,
                           self.search_value, default_value)
        self.search_focus_num += 1
        return True

    def chat_index_page(self,event):
        pass

    def group_index_page(self,event):
        pass

    def foot_more_page(self,event):
        pass

    def foot_add_friend_page(self,event):
        pass


root = HomePage("zs", ['sd', "dsd"])

root.mainloop()
