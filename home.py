from tkinter import *
from tkinter import messagebox


def doNothing():
    print("I do nothing")


def login():
    name = nameinput.get()
    # password = passinput.get()
    n = Label(root, text=name, font='20')
    # p = Label(root, text=password)
    messagebox.showinfo("Welcome", "Login Successful")
    frame.destroy()
    Label(root, text="Welcome!", font='20').pack()
    n.pack()
    createTable(name)


def createTable(name):
    f = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=900, height=900, bd= 0,  pady = 30, padx = 90)
    f.pack()
    height = 4
    width = 4
    # k = 0
    headings = {
        "0": "Sno.",
        "1": "Book Title",
        "2": "Book Id",
        "3": "Due Date"
    }
    for i in range(height):  # Rows
        for j in range(width):  # Columns
            bold = Label(f, text=headings[str(j)], padx=15, pady=15, font='Arial 13 bold')
            bold.grid(row=0, column=j)

    a = Entry(f)
    a.grid(row=1, column=0)
    b = Entry(f)
    b.grid(row=1, column=1)
    c = Entry(f)
    c.grid(row=1, column=2)
    d = Entry(f)
    d.grid(row=1, column=3)

    def save():

        sno = a.get()
        title = b.get()
        bookid = c.get()
        date = d.get()
        f.destroy()

        fr = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=900, height=900, bd=0, pady=30, padx=90)
        fr.pack()
        h = 4
        w = 4
        # k = 0
        head = Label(fr, text="SNo.\t\tBook Title\t   BookId\tDate", font='Arial 10 bold')
        head.grid(row=0, sticky='W')
        file = open(name+'.txt', 'a+')
        file.write("%s \t %s \t %s \t %s \n" % (sno, title, bookid, date))
        file.close()
        file = open(name+'.txt', 'r')
        data = file.readlines()
        for line in data:
            line.split('\t')
            for i in range(5):
                nos = Label(fr, text=data[i], font='Verdana')
                nos.grid(row=i+1, sticky='W')

        # for line in data:
            # y = line.split('\t')
            #nos = Label(fr, text=data, font='Verdana')
            #btitle = Label(fr, text=y[1], font='Verdana')
            #bid = Label(fr, text=y[2], font='Verdana')
            #ddate = Label(fr, text=y[3], font='Verdana')
            #nos.grid()
            # btitle.grid(column=1)
            # bid.grid(column=2)
            # ddate.grid(column=3)


# .write("%s \n %s \n %s \n" % (line1, line2, line3))
    btn = Button(f, text="Save", cursor="hand2", command=save)
    btn.grid(columnspan=4, sticky=E, padx=5, pady=5)


root = Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# toolbar
toolbar = Frame(root)
insertbtn = Button(toolbar,text="Logout", command=doNothing, cursor="hand2")
deletebtn = Button(toolbar,text="Delete", command=doNothing, cursor="hand2")
insertbtn.grid(row=0, column=w-1, sticky=E)
deletebtn.grid(row=0, column=w, sticky=E)
toolbar.pack(side=TOP, fill=X)

# main layout

heading = Label(root, text="LIBRARY MANAGEMENT SYSTEM" ,font='Verdana 30 bold')
heading.pack(padx=30, pady=30)
frame = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=900, height=900, bd= 0,  pady = 30, padx = 90)
frame.pack(side=TOP )
# image = PhotoImage(file="fb.png")
# photo = Label(frame, image=image)
# photo.grid(row=1)
l = Label(frame, text="Login!", font='Courier 21 bold')
namelabel = Label(frame, text="Username", font= "Courier 15")
passLabel = Label(frame, text="Password", font= "Courier 15")
nameinput = Entry(frame)
passinput = Entry(frame)
submitbtn = Button(frame, text="Submit", cursor="hand2", font='Courier 10', command=login)
checkbox1 = Checkbutton(frame, text="Keep me logged in")
l.grid(columnspan=3, sticky=N)
namelabel.grid(row=2,column=1 ,sticky=E)
passLabel.grid(row=4,column=1 ,sticky=E)
nameinput.grid(row=2,column=2 )
passinput.grid(row=4,column=2 )
checkbox1.grid(columnspan=3)
submitbtn.grid(row=6, column=2, sticky=E)


# ********main menu*********
mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="My Books..", command=doNothing)
submenu.add_command(label="My Reserves..", command =doNothing)
submenu.add_separator()
submenu.add_command(label="Logout", command=doNothing)

editmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Add Books",  command=doNothing)
editmenu.add_command(label="Delete Books",  command=doNothing)

# statusbar
status = Label(root, text="successfully doing nothing....", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM,  fill=X)


root.mainloop()
