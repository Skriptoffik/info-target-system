## ÇÈÍË Úä 

	EXCHANGE_LIMIT_RANGE = 3000

	def __init__(self):
		ui.ThinBoard.__init__(self)

		name = ui.TextLine()
		name.SetParent(self)
		name.SetDefaultFontName()
		name.SetOutline()
		name.Show()

		hpGauge = ui.Gauge()
		hpGauge.SetParent(self)
		hpGauge.MakeGauge(130, "red")
		hpGauge.Hide()

		closeButton = ui.Button()
		closeButton.SetParent(self)
		closeButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		closeButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		closeButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		closeButton.SetPosition(30, 13)

		if localeInfo.IsARABIC():
			hpGauge.SetPosition(55, 17)
			hpGauge.SetWindowHorizontalAlignLeft()
			closeButton.SetWindowHorizontalAlignLeft()
		else:
			hpGauge.SetPosition(175, 17)
			hpGauge.SetWindowHorizontalAlignRight()
			closeButton.SetWindowHorizontalAlignRight()

		closeButton.SetEvent(ui.__mem_func__(self.OnPressedCloseButton))
		closeButton.Show()

## ÖÚ ÇÓÝáåÇ


#ENABLE TARGET INFO SYSTEM_AZO ONE
		infoButton = ui.Button()
		infoButton.SetParent(self)
		infoButton.SetUpVisual("d:/ymir work/ui/pattern/q_mark_01.tga")
		infoButton.SetOverVisual("d:/ymir work/ui/pattern/q_mark_02.tga")
		infoButton.SetDownVisual("d:/ymir work/ui/pattern/q_mark_01.tga")
		
		if localeInfo.IsARABIC():
			infoButton.SetPosition(5, 13)
			infoButton.SetWindowHorizontalAlignLeft()
		else:
			infoButton.SetPosition(5, 13)
			infoButton.SetWindowHorizontalAlignRight()
			
		infoButton.SetEvent(ui.__mem_func__(self.OnPressedInfoButton))
		infoButton.Hide()
#ENABLE TARGET INFO SYSTEM_AZO ONE


## ÇÈÍË Úä

		self.name = name
		self.hpGauge = hpGauge
		self.closeButton = closeButton


## ÖÚ ÇÓÝáåÇ

#ENABLE TARGET INFO SYSTEM_AZO ONE
		self.infoButton = infoButton
#ENABLE TARGET INFO SYSTEM_AZO ONE


# ÇÈÍË Úä

	def Destroy(self):
		self.eventWhisper = None
		self.closeButton = None


## ÖÚ ÇÓÝáåÇ

#ENABLE TARGET INFO SYSTEM_AZO ONE
		self.infoButton = None
#ENABLE TARGET INFO SYSTEM_AZO ONE


## ÇÈÍË Úä

	def OnPressedCloseButton(self):
		player.ClearTarget()
		self.Close()


## ÖÚ ÇÓÝáåÇ

#ENABLE TARGET INFO SYSTEM_AZO ONE
	def OnPressedInfoButton(self):

		import uitargetinfo
		if not hasattr(self, "targetInfoDialog"):

			self.targetInfoDialog = uitargetinfo.TargetInfoBoard()

		self.targetInfoDialog.Open(self.GetTargetVID(), self.GetTargetName())
#ENABLE TARGET INFO SYSTEM_AZO ONE


## ÇÈÍË Úä

		self.name.SetPosition(0, 13)
		self.name.SetHorizontalAlignCenter()
		self.name.SetWindowHorizontalAlignCenter()
		self.hpGauge.Hide()


## ÖÚ ÇÓÝáåÇ

#ENABLE TARGET INFO SYSTEM_AZO ONE
		if self.infoButton:
			self.infoButton.Hide()
#ENABLE TARGET INFO SYSTEM_AZO ONE


## ÇÈÍË Úä

		nameFront = ""
		if -1 != level:
			nameFront += "Lv." + str(level) + " "
		if self.GRADE_NAME.has_key(grade):
			nameFront += "(" + self.GRADE_NAME[grade] + ") "

		self.SetTargetName(nameFront + name)


## ÖÚ ÇÓÝáåÇ

#ENABLE TARGET INFO SYSTEM_AZO ONE
		if level > 0:
			if self.infoButton:
				self.infoButton.Show()
#ENABLE TARGET INFO SYSTEM_AZO ONE