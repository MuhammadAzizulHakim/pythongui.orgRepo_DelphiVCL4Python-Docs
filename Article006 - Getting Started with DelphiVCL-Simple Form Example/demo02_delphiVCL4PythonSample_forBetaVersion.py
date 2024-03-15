from DelphiVCL import *

class MainForm(Form):
    def __init__(self, Owner):
        self.Caption = "A VCL Form..."
        self.SetBounds(10, 10, 340, 410)
        self.lblHello = Label(self)
        self.lblHello.SetProps(Parent=self, Caption="Please Input Your Lists")
        self.lblHello.SetBounds(10,10,100,24)
        self.edit1 = Edit(self)
        self.edit1.SetProps(Parent=self, Top=30, Left=10, Width=200, Height=24)
        self.button1 = Button(self)
        self.button1.SetProps(Parent=self, Caption="Add", OnClick=self.Button1Click)
        self.button1.SetBounds(220,29,90,24)
        self.lb1 = ListBox(self)
        self.lb1.SetProps(Parent=self)
        self.lb1.SetBounds(10,60,300,300)
        
    def Button1Click(self, Sender):
        self.lb1.Items.Add(self.edit1.Text)

def main():
    Application.Initialize()
    Application.Title = "My DelphiVCL4Python App"
    f = MainForm(Application)
    f.Show()
    FreeConsole()
    Application.Run()
main()
