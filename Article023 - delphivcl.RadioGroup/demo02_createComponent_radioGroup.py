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

    	# Radiogroup Creation
        rbgRadioBox = RadioGroup(pgOne)
        rbgRadioBox.SetProps(Parent=pgOne,Caption='Gender')
        rbgRadioBox.SetBounds(20,50,242,90)
        rbgRadioBox.Items.Add('Male')
        rbgRadioBox.Items.Add('Female')


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
