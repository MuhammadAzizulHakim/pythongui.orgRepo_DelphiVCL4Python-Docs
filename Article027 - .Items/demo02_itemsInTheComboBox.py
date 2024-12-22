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
        lblCity = CreateComponent('TLabel',pgOne)
        lblCity.SetProps(Parent=pgOne,Caption='City')
        lblCity.SetBounds(20,206,121,30)

        # Combo box
        cbxCity = ComboBox(pgOne)
        cbxCity.SetProps(Parent=pgOne,Name='ComboBox')
        cbxCity.SetBounds(145,206,121,60)
        cbxCity.Items.Add('New York')
        cbxCity.Items.Add('Sydney')
        cbxCity.Items.Add('Banglore')
        cbxCity.Items.Add('Tokyo')

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