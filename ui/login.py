import tkinter, re

from tkinter import StringVar
from common.entry_display_tool import *
from tkinter.messagebox import *

from ui.register import RegisterPage
from ui.homepage import *

# from client.clientmanager import ClientManager
from PIL import Image, ImageTk


class LoginPage(tkinter.Tk):
    def __init__(self):  # , master=None
        super().__init__()
        # self.root = master  # 定义内部变量root
        self.title("CQ")
        self.resizable(width=False, height=False)  # 窗口大小不可变
        # self.overrideredirect(1)  #去掉菜单栏，但无法移动窗口
        # self.iconbitmap("20190530225657.ico")   #加窗口图标
        self['background'] = '#52AAE5'  # 窗口背景色

        self.geometry('%dx%d+%d+%d' % (550, 385, 650, 200))  # 设置窗口大小 和位置
        self.username_focus_num = 0
        self.username_value = StringVar()
        # self.username.set(r"请输入CQ号")

        self.password_focus_num = 0
        self.password_value = StringVar()
        # self.password.set(r"请输入密码")
        self.create_page()

    def create_page(self):
        self.page = tkinter.Frame(self, bg='#52AAE5')  # 创建Frame
        self.page.pack(expand=True)

        # tkinter.Label(self.page,height=1).grid(row=0, stick='W')
        tkinter.Label(self.page, text="用户登录", bg='#52AAE5', font=("宋体", 20)).grid(row=1, stick='W')
        tkinter.Button(self.page, text="用户注册", bg='#52AAE5', font=("宋体", 10), borderwidth=0, width=4,
                       activebackground="#52AAE5", command=self.register_request).grid(row=2, column=1, stick='E')

        tkinter.Label(self.page, bg='#52AAE5').grid(row=2, stick='W')
        tkinter.Label(self.page, text='账户:', bg='#52AAE5', font=("宋体", 20)).grid(row=3, stick='W', pady=10)
        self.username = tkinter.Entry(self.page, textvariable=self.username_value, width=27, font=25, bd=0,
                                      fg='#767676',
                                      validate='focus', validatecommand=self.user_name_display)
        self.username.insert(0, "请输入CQ号")
        self.username.grid(row=3, column=1, stick='E')

        tkinter.Label(self.page, text='密码:', bg='#52AAE5', font=("宋体", 20)).grid(row=4, stick='W', pady=10)
        self.password = tkinter.Entry(self.page, textvariable=self.password_value, width=27, font=25, bd=0,
                                      fg='#767676', validate='focus', validatecommand=self.password_display)
        self.password.insert(0, '请输入密码')
        self.password.grid(row=4, column=1, stick='E')

        tkinter.Checkbutton(self.page, text="记住密码", bg='#52AAE5', font=("宋体", 10), borderwidth=0, width=6,
                            activebackground="#52AAE5").grid(row=5, column=1, stick='w')
        tkinter.Button(self.page, text="找回密码", bg='#52AAE5', font=("宋体", 10), borderwidth=0, width=5,
                       activebackground="#52AAE5").grid(row=5, column=1, stick='e')

        tkinter.Label(self.page, bg='#52AAE5').grid(row=6, stick='W')
        tkinter.Button(self.page, text='安全登录', font=("宋体", 20), width=13, activebackground="#52AAE5",
                       bg='#52AAE5', command=self.login_check) \
            .grid(row=6, column=1, stick='W', pady=10)
        # tkinter.Button(self.page, text='退出', command=self.page.quit).grid(row=7, column=1, stick='E')

    def login_check(self):
        name = self.username.get()
        password = self.password.get()
        # if name == "zs" and password=='123':
        #     print("登录成功")
        # else:
        #     print("账号密码错误")

        # ClientManager().login(name, password)

    def login_result(self, result=False, user_name='', friend_list=[]):
        if result:
            self.destroy()
            root = HomePage(user_name, friend_list)
            root.mainloop()
        else:
            return


            # if result:
            #     self.destroy()
            #     root = HomePage(name,["张三","李四","王五","赵旭老师",
            #                 "祁老师","蒙蒙老师","吕泽老师","王丹波老师"])
            #     root.mainloop()

    def register_request(self):
        self.destroy()
        root = RegisterPage()
        root.mainloop()

    def user_name_display(self):
        # if self.username_focus_num % 2 == 0:
        #     if self.username_value.get() == '请输入CQ号':
        #         self.username.delete(0, "end")
        # else:
        #     if self.username_value.get() == '':
        #         self.username.insert(10, '请输入CQ号')
        default_value = '请输入CQ号'
        entry_display_tool(self.username_focus_num, self.username,
                           self.username_value, default_value)
        self.username_focus_num += 1
        return True

    def password_display(self):

        # if self.password_focus_num %2 == 0:
        #     self.password['show'] = "*"
        #     if self.password_value.get()== '请输入密码':
        #         self.password.delete(0, "end")
        # else:
        #     if self.password_value.get()=='':
        #         self.password['show']=''
        #         self.password.insert(10,'请输入密码')
        default_value = '请输入密码'
        entry_display_tool(self.password_focus_num, self.password,
                           self.password_value, default_value, 1)
        self.password_focus_num += 1
        return True
