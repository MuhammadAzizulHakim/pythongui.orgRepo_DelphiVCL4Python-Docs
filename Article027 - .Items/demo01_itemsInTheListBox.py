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

        # label Creation
        lblCountry = CreateComponent('TLabel',pgOne)
        lblCountry.SetProps(Parent=pgOne,Caption='Country')
        lblCountry.SetBounds(20,88,121,30)

        # Items in list box
        lboxCountry = ListBox(pgOne)
        lboxCountry.SetProps(Parent=pgOne)
        lboxCountry.SetBounds(145,88,121,60)
        lboxCountry.Items.Add('RUSSIA')
        lboxCountry.Items.Add('USA')
        lboxCountry.Items.Add('INDIA')
        lboxCountry.Items.Add('AUSTRALIA')

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