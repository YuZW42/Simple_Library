from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')
        
        
        MType=StringVar()
        Ref = StringVar()
        Title =StringVar()
        FirstName =StringVar()
        BookID =StringVar()
        Author=StringVar()
        DateStarted=StringVar()
        DateFinished=StringVar()
        SellingPrice=StringVar()
        DateOverDue=StringVar()
        
        
        def iReset():
            MType.set("")
            Ref.set("")
            Title.set("")
            FirstName.set("")
            BookID.set("")
            Author.set("")
            DateStarted.set("")
            DateFinished.set("")
            SellingPrice.set("")
            DateOverDue.set("")
            self.txtFrameDetail.delete("1.0",END)
            self.txtDisplayR.delete("1.0",END)
            
        def iDelete():
            iReset()
            self.txtDisplayR.delete("1.0",END)
        
        def iExit():
            iExit=tkinter.messagebox.askyesno("Book Management System","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return
        def iDisplayData():
            self.txtFrameDetail.insert(END, "\t" + MType.get()+"\t\t"+ Title.get()+"\t\t"+FirstName.get()+
            "\t\t"+BookTitle.get()+"\t\t"+DateStarted.get()+"\t\t"+DateFinished.get()+"\n")
            
        def iReceipt():
            self.txtDisplayR.insert(END, "Member Type: \t\t" + MType.get() + "\n")
        ## Frame
        MainFrame = Frame(self.root)
        MainFrame.grid()
        
        TitleFrame = Frame(MainFrame, width = 1350, padx=20, bd=20, relief = RIDGE)
        TitleFrame.pack(side=TOP)
        self.lbTitle = Label(TitleFrame, width=39, font=('arial', 40, 'bold'), text="\tLibrary Management System \t", padx = 12)
        self.lbTitle.grid()
        
        ButtonFrame = Frame(MainFrame, width = 1350, padx=20, bd=20, relief = RIDGE,height = 50)
        ButtonFrame.pack(side=BOTTOM)
        
        FrameDetail = Frame(MainFrame, width = 1350, padx=20, bd=20, relief = RIDGE,height = 100 )
        FrameDetail.pack(side=BOTTOM)
        
        DataFrame = Frame(MainFrame,width = 1300, padx=20, bd=20, relief = RIDGE,height = 400)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT = LabelFrame(DataFrame, width = 800, padx=20, bd=10, relief = RIDGE,height = 300,
                                   font=('arial', 12, 'bold'), text="Library Membership Information ")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT = LabelFrame(DataFrame, width = 450, padx=20, bd=10, relief = RIDGE,height = 300,
                                   font=('arial', 12, 'bold'), text="Book Details ")
        DataFrameRIGHT.pack(side=RIGHT)
        
        ## Widget
        self.lbMemberType = Label(DataFrameLEFT,font=('arial',12,'bold'),text = "Member Type:",padx = 2,pady=2)
        self.lbMemberType.grid (row=0, column = 0,sticky = W)
        
        self.cboMemberType = ttk.Combobox(DataFrameLEFT, font = ('arial',12,'bold') , width=23,state='readonly',textvariable=MType)
        self.cboMemberType['value'] =('','Student','Lecturer','Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid (row=0, column=1)
        
        self.lblBookID = Label(DataFrameLEFT, font = ('arial',12,'bold') , text = "BookID", padx=2,pady=2)
        self.lblBookID.grid (row=0, column = 2,sticky = W)
        self.txtBookID = Entry(DataFrameLEFT, font = ('arial',12,'bold'),width=25,textvariable=BookID)
        self.txtBookID.grid (row=0, column =3 )
        
        self.lblAuthor = Label(DataFrameLEFT, font = ('arial',12,'bold') , text = "Author", padx=2,pady=2)
        self.lblAuthor.grid (row=1, column = 0,sticky = W)
        self.txtAuthor = Entry(DataFrameLEFT, font = ('arial',12,'bold'),width=25,textvariable=Author)
        self.txtAuthor.grid (row=1, column =1 )
        
        self.lblBookTitle = Label(DataFrameLEFT, font = ('arial',12,'bold') , text = "BookTitle", padx=2,pady=2)
        self.lblBookTitle.grid (row=1, column = 2,sticky = W)
        self.txtBookTitle = Entry(DataFrameLEFT, font = ('arial',12,'bold'),width=25,textvariable=Title)
        self.txtBookTitle.grid (row=1, column =3 )
        
        self.lblTitle= Label(DataFrameLEFT, font =('arial',12,'bold'), text="Title:",padx=2,pady=2)
        self.lblTitle.grid(row=2,column=0,sticky=W)
        self.txtSellingPrice = Entry(DataFrameLEFT, font = ('arial',12,'bold'),width=25)
        self.txtSellingPrice.grid (row=2, column =1 )
        
        self.lblSellingPrice= Label(DataFrameLEFT, font = ('arial',12,'bold') , text = "SellingPrice", padx=2,pady=2)
        self.lblSellingPrice.grid (row=2, column = 2,sticky = W)
        self.txtSellingPrice = Entry(DataFrameLEFT, font = ('arial',12,'bold'),width=25,textvariable=SellingPrice)
        self.txtSellingPrice.grid (row=2, column =3 )
        
        self.lblDateStarted= Label(DataFrameLEFT, font = ('arial',12,'bold') , text = "DateStarted", padx=2,pady=2)
        self.lblDateStarted.grid (row=3, column = 0,sticky = W)
        self.txtDateStarted = Entry(DataFrameLEFT, font = ('arial',12,'bold'),width=25,textvariable=DateStarted)
        self.txtDateStarted.grid (row=3, column =1 )
        
        self.lblDateFinished= Label(DataFrameLEFT, font = ('arial',12,'bold') , text = "DateFinished", padx=2,pady=2)
        self.lblDateFinished.grid (row=3, column = 2,sticky = W)
        self.txtDateFinished = Entry(DataFrameLEFT, font = ('arial',12,'bold'),width=25,textvariable=DateFinished)
        self.txtDateFinished.grid (row=3, column =3 )
        
        self.lblFirstName= Label(DataFrameLEFT, font = ('arial',12,'bold') , text = "FirstName", padx=2,pady=2)
        self.lblFirstName.grid (row=4, column = 0,sticky = W)
        self.txtFirstName = Entry(DataFrameLEFT, font = ('arial',12,'bold'),width=25,textvariable=FirstName)
        self.txtFirstName.grid (row=4,column =1 )
        
        self.lblDateOverDue= Label(DataFrameLEFT, font = ('arial',12,'bold') , text = "DateOverDue", padx=2,pady=2)
        self.lblDateOverDue.grid (row=4, column = 2,sticky = W)
        self.txtDateOverDue = Entry(DataFrameLEFT, font = ('arial',12,'bold'),width=25,textvariable=DateOverDue)
        self.txtDateOverDue.grid (row=4,column =3 )
        
        ##Widget 
        self.txtDisplayR = Text(DataFrameRIGHT, font = ('arial',12,'bold'),width=32,height=13,padx=8,pady=20)
        self.txtDisplayR.grid (row=0,column =2 )
        
        ##List Box
        
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid (row=0,column=1,sticky='ns')
        ListOfBooks= ['Intro to Java', 'Economic 101']
        
        def selectedBook(evt):
            value=str(booklist.get(booklist.curselection()))
            w = value
            if(w == "Intro to Java"):
                BookID.set("Book Number: 01")
                iReceipt()
            
                            
            


        booklist=Listbox(DataFrameRIGHT,width=20,height=12,font = ('arial',12,'bold'))      
        booklist.bind('<<ListboxSelect>>',selectedBook)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)
        
        for items in ListOfBooks:
            booklist.insert(END,items)
            
        ##
        self.lblLabel = Label(FrameDetail, font=('arial',10,'bold'),pady=9,
        text="Book_Title \t Author \t Date_Borrowed \t  Date_Finished \t Selling_Price \t First_Name")
        
        self.lblLabel.grid(row=0,column=0)
        
        
        self.txtDisplayR = Text(FrameDetail, font = ('arial',12,'bold'),width=80, height=4,padx=2,pady=4)
        self.txtDisplayR.grid (row=1,column =0 )
        ##Button
        self.btnDisplayData=Button(ButtonFrame, text='Display Data', font = ('arial',12,'bold'),width=30, bd=4 )
        self.btnDisplayData.grid(row=0,column=0)
        
        self.btnReset=Button(ButtonFrame, text='Reset', font = ('arial',12,'bold'),width=30, bd=4, command = iReset)
        self.btnReset.grid(row=0,column=1)
        
        self.btnDelete=Button(ButtonFrame, text='Delete', font = ('arial',12,'bold'),width=30, bd=4, command = iDelete)
        self.btnDelete.grid(row=0,column=2)
        
        self.btnExit=Button(ButtonFrame, text='Exit', font = ('arial',12,'bold'),width=30, bd=4, command = iExit)
        self.btnExit.grid(row=0,column=3)
        
        
if __name__=='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()