from delphivcl import *

class MainForm(Form):

    def __init__(self, Owner):
        self.Caption = "Components Overview Sample"
        self.Name = "BaseForm"
        self.SetBounds(10, 10, 700, 650)
        #
        pnlMain = CreateComponent('TPanel',Owner)
        pnlMain.SetProps(Parent=self, Caption="",align = "alClient", Name = "MainPanel")

        # page control creation
        pgConMain = PageControl(pnlMain)
        pgConMain.Name = "MyPageControl"
        pgConMain.Parent = pnlMain
        pgConMain.Align = "alClient"

        # Tabsheet one
        pgOne = TabSheet(pnlMain)
        pgOne.PageControl = pgConMain
        pgOne.Caption = "StandardControls"

       # label Creation
        lblHello = CreateComponent('TLabel',pgOne)
        lblHello.Parent = pgOne
        lblHello.Caption = 'FirstName'
        lblHello.Name = 'Name'
        lblHello.Left = 20
        lblHello.Top = 14
        lblHello.Width = 121
        lblHello.Height = 30

        # Edit box creation
        edtHello = CreateComponent('TEdit',pgOne)
        edtHello.Parent = pgOne
        edtHello.Text = 'Jim'
        edtHello.Name = 'edtFirstName'
        edtHello.Left = 145
        edtHello.Top = 14
        edtHello.Width = 121
        edtHello.Height = 30

        chkSingle = CheckBox(self)
        chkSingle.Parent = pgOne
        chkSingle.Caption = 'Single ?'
        chkSingle.Alignment = 'taLeftJustify'
        chkSingle.SetBounds(20, 44, 141, 30)

        # label Creation
        lblCountry = CreateComponent('TLabel',pgOne)
        lblCountry.SetProps(Parent=pgOne,Caption='Country')
        lblCountry.SetBounds(20,88,121,30)

        #listbox
        lboxCountry = ListBox(pgOne)
        lboxCountry.SetProps(Parent=pgOne)
        lboxCountry.SetBounds(145,88,121,60)
        lboxCountry.Items.Add('RUSSIA')
        lboxCountry.Items.Add('USA')
        lboxCountry.Items.Add('INDIA')
        lboxCountry.Items.Add('AUSTRALIA')

         # label Creation
        lblDateOfIssue = CreateComponent('TLabel',pgOne)
        lblDateOfIssue.SetProps(Parent=pgOne,Caption='Date Of Birth')
        lblDateOfIssue.SetBounds(20,162,121,30)

        dtpDateofIssue = CreateComponent('TDateTimePicker',pgOne)
        dtpDateofIssue.SetProps(Parent=pgOne)
        dtpDateofIssue.SetBounds(145,162,121,30)

        # label Creation
        lblCity = CreateComponent('TLabel',pgOne)
        lblCity.SetProps(Parent=pgOne,Caption='City')
        lblCity.SetBounds(20,206,121,30)

        #Combobox
        cbxCity = ComboBox(pgOne)
        cbxCity.SetProps(Parent=pgOne,Name='ComboBox')
        cbxCity.SetBounds(145,206,121,60)
        cbxCity.Items.Add('New York')
        cbxCity.Items.Add('Sydney')
        cbxCity.Items.Add('Banglore')
        cbxCity.Items.Add('Tokyo')

        def ChangeHandler(sender):
            memoEvent.Lines.Add('changed')

        cbxCity.OnChange = ChangeHandler

        # Radiogroup Creation
        rbgRadioBox = RadioGroup(pgOne)
        rbgRadioBox.SetProps(Parent=pgOne,Caption='Gender')
        rbgRadioBox.SetBounds(20,250,242,90)
        rbgRadioBox.Items.Add('Male')
        rbgRadioBox.Items.Add('Female')

        #Button
        btnOK = Button(pgOne)
        btnOK.SetProps(Parent=pgOne,Caption = 'Submit',Name = 'btnOK')
        btnOK.SetBounds(145,540,60,30)

        #Memo
        memoEvent = Memo(pgOne)
        memoEvent.SetProps(Parent=pgOne)
        memoEvent.SetBounds(300,14,350,300)

        def ClickHandler(Sender):
         memoEvent.Lines.Add(Sender.Name + ' clicked')

        btnOK.OnClick = ClickHandler


        # Tabsheet two
        pgTwo = TabSheet(pnlMain)
        pgTwo.PageControl = pgConMain
        pgTwo.Caption = "Ext controls"

        shpRectangle = Shape(pgTwo)
        shpRectangle.SetProps(Parent=pgTwo,Shape = 'stRectangle')
        shpRectangle.SetBounds(140,14,400,200)

        clbSelect = ColorBox(pgTwo)
        clbSelect.SetProps(Parent=pgTwo)
        clbSelect.SetBounds(20,14,100,30)
        def ColorChangeHandler(Sender):
          shpRectangle.Brush.Color = clbSelect.Selected


        clbSelect.Onchange = ColorChangeHandler

        grdTest = DrawGrid(pgTwo)
        grdTest.Parent = pgTwo
        grdTest.SetBounds(20, 220, 520, 180)


        def grdTestDrawCell(Sender, Col, Row, Rect, State):
          if gdSelected in State:
            Sender.Canvas.Brush.Color = clBlue # 0x00ff0000 # blue
            Sender.Canvas.TextRect(Rect, Rect.Left+2, Rect.Top+2, "%d @ %d" % (Col, Row))

        def grdTestSelectCell(Sender, Col, Row, CanSelect):
            if Col == 2 and Row == 2:
              CanSelect.Value = False

        grdTest.OnDrawCell = grdTestDrawCell
        grdTest.OnSelectCell = grdTestSelectCell



        self.OnClose = self.MainFormClose

    def MainFormClose(self, Sender, Action):
        Action.Value = caFree

    def btnOKClick(self, Sender):
        btnOK.Caption = "Clicked"


def main():
    Application.Initialize()
    Application.Title = "MyDelphiApp"
    f = MainForm(Application)
    f.Show()
    FreeConsole()
    Application.Run()
    Application.Destroy()

main()