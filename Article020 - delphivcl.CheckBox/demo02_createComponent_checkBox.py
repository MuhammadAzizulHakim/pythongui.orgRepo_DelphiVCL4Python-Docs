from delphivcl import *
 
# Create a Class to build a basic Form
class MainForm(Form):
    def __init__(self, Owner):
        self.Caption = "Introduction to VCL Components"
        self.Name = "BaseForm"
        self.SetBounds(10, 10, 500, 450)
 
        # Create a Main Panel component
        pnlMain = CreateComponent('TPanel',Owner)
        pnlMain.SetProps(Parent=self, Caption="",align = "alClient", Name = "MainPanel")
 
        # Page control creation
        pgConMain = PageControl(pnlMain)
        pgConMain.Name = "MyPageControl"
        pgConMain.Parent = pnlMain
        pgConMain.Align = "alClient"
 
        # Tabsheet one
        pgOne = TabSheet(pnlMain)
        pgOne.PageControl = pgConMain
        pgOne.Caption = "Tab 1"
 
        # Tabsheet two
        pgTwo = TabSheet(pnlMain)
        pgTwo.PageControl = pgConMain
        pgTwo.Caption = "Tab 2"
 
        # Label Creation
        lblHello = CreateComponent('TLabel',pgOne)
        lblHello.Parent = pgOne
        lblHello.Caption = 'FirstName'
        lblHello.Name = 'Name'
        # Set the positions
        lblHello.Left = 20
        lblHello.Top = 14
        lblHello.Width = 121
        lblHello.Height = 30
 
        # Edit box creation
        edtHello = CreateComponent('TEdit',pgOne)
        edtHello.Parent = pgOne
        edtHello.Text = 'Arthur'
        edtHello.Name = 'edtFirstName'
        # Set the positions and dimensions
        edtHello.Left = 145
        edtHello.Top = 14
        edtHello.Width = 121
        edtHello.Height = 30
 
        # Check box creation
        chkSingle = CheckBox(self)
        chkSingle.Parent = pgOne
        chkSingle.Caption = 'Single ?'
        chkSingle.Alignment = 'taLeftJustify'
        chkSingle.SetBounds(20, 44, 141, 30)
 
# Initialize your application
def main():
    Application.Initialize()
    Application.Title = "MyDelphiApp"
    f = MainForm(Application)
    f.Show()
    FreeConsole()
    Application.Run()
    Application.Destroy()
 
main()
