import ui
import app
import net
import localeInfo
import item
import wndMgr
import grp
import chr
import nonplayer
import player
import uiToolTip

#ENABLE TARGET INFO SYSTEM_AZO ONE

class DungeonStyleDropRow(ui.Window):
	def __init__(self, width):
		ui.Window.__init__(self)
		self.width = width
		self.vnum = 0
		self.tooltipItem = None

		self.bgOut = ui.Bar()
		self.bgOut.SetParent(self)
		self.bgOut.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 1.0))
		self.bgOut.AddFlag("not_pick")
		self.bgOut.Show()

		self.bgIn = ui.Bar()
		self.bgIn.SetParent(self)
		self.bgIn.SetColor(grp.GenerateColor(0.13, 0.13, 0.13, 0.95))
		self.bgIn.AddFlag("not_pick")
		self.bgIn.Show()

		self.hover = ui.Bar()
		self.hover.SetParent(self)
		self.hover.SetColor(grp.GenerateColor(1.0, 1.0, 1.0, 0.05))
		self.hover.AddFlag("not_pick")
		self.hover.Hide()

		self.iconBg = ui.ThinBoard()
		self.iconBg.SetParent(self)
		self.iconBg.AddFlag("not_pick")
		self.iconBg.Show()

		self.icon = ui.ImageBox()
		self.icon.SetParent(self)
		self.icon.AddFlag("not_pick")
		self.icon.Show()

		self.nameText = ui.TextLine()
		self.nameText.SetParent(self)
		self.nameText.SetFontName(localeInfo.UI_DEF_FONT)
		self.nameText.SetPackedFontColor(0xFFEBEBEB)
		self.nameText.AddFlag("not_pick")
		self.nameText.Show()

		self.rarityText = ui.TextLine()
		self.rarityText.SetParent(self)
		self.rarityText.SetFontName(localeInfo.UI_DEF_FONT)
		self.rarityText.AddFlag("not_pick")
		self.rarityText.Show()

	def SetToolTip(self, tooltip):
		self.tooltipItem = tooltip

	def SetItemInfo(self, vnum, prob):
		self.vnum = vnum
		item.SelectItem(vnum)
		itemName = item.GetItemName()
		iconPath = item.GetIconImageFileName()

		try:
			gridHeight = item.GetItemSize()[1]
		except:
			gridHeight = 1

		icon_h = gridHeight * 32
		row_h = max(55, icon_h + 16)

		self.SetSize(self.width, row_h)
		self.bgOut.SetSize(self.width, row_h)
		
		self.bgIn.SetPosition(1, 1)
		self.bgIn.SetSize(self.width - 2, row_h - 2)
		self.hover.SetPosition(1, 1)
		self.hover.SetSize(self.width - 2, row_h - 2)

		self.iconBg.SetSize(32 + 8, icon_h + 8)
		self.icon.LoadImage(iconPath)

		icon_y = (row_h - icon_h) / 2
		text_y_center = row_h / 2

		if app.IsRTL():
			self.iconBg.SetPosition(self.width - 44, icon_y - 4)
			self.icon.SetPosition(self.width - 40, icon_y)

			self.nameText.SetPosition(self.width - 55, text_y_center - 12)
			self.nameText.SetWindowHorizontalAlignRight()
			self.nameText.SetHorizontalAlignRight()

			self.rarityText.SetPosition(self.width - 55, text_y_center + 5)
			self.rarityText.SetWindowHorizontalAlignRight()
			self.rarityText.SetHorizontalAlignRight()
		else:
			self.iconBg.SetPosition(6, icon_y - 4)
			self.icon.SetPosition(10, icon_y)

			self.nameText.SetPosition(55, text_y_center - 12)
			self.rarityText.SetPosition(55, text_y_center + 5)

		self.nameText.SetText(itemName)

		if prob >= 150000:
			self.rarityText.SetText(localeInfo.UITARGETINFO_RARITY_VERY_COMMON)
			self.rarityText.SetPackedFontColor(0xFFFFFFFF) 
		elif prob >= 100000:
			self.rarityText.SetText(localeInfo.UITARGETINFO_RARITY_COMMON)
			self.rarityText.SetPackedFontColor(0xFF54FF54) 
		elif prob >= 50000:
			self.rarityText.SetText(localeInfo.UITARGETINFO_RARITY_MEDIUM)
			self.rarityText.SetPackedFontColor(0xFF00BFFF) 
		elif prob >= 10000:
			self.rarityText.SetText(localeInfo.UITARGETINFO_RARITY_RARE)
			self.rarityText.SetPackedFontColor(0xFFFFD700) 
		else:
			self.rarityText.SetText(localeInfo.UITARGETINFO_RARITY_LEGENDARY)
			self.rarityText.SetPackedFontColor(0xFFFF4500) 

		return row_h


	def OnMouseOverIn(self):
		self.hover.Show()
		if self.tooltipItem:
			try:
				self.tooltipItem.SetItemToolTip(self.vnum)
			except Exception as e:
				self.tooltipItem.HideToolTip()

	def OnMouseOverOut(self):
		self.hover.Hide()
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

class TargetInfoBoard(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.vid = 0
		self.mobName = ""
		self.dropList = []
		self.dropYPos = 0
		self.statTexts = [] 
		
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()

		self.__BuildWindow()

	def __del__(self):
		if self.tooltipItem:
			del self.tooltipItem
		ui.BoardWithTitleBar.__del__(self)

	def __BuildWindow(self):
		self.SetSize(600, 480)
		self.SetCenterPosition()
		self.AddFlag("movable")
		self.AddFlag("float")
		self.SetTitleName(localeInfo.UITARGETINFO_TITLE)
		self.SetCloseEvent(self.Close)

		self.dropBoard = ui.ThinBoard()
		self.dropBoard.SetParent(self)
		self.dropBoard.SetPosition(10, 35)
		self.dropBoard.SetSize(330, 435)
		self.dropBoard.Show()

		self.dropWindow = ui.Window()
		self.dropWindow.SetParent(self.dropBoard)
		self.dropWindow.SetPosition(5, 5)
		self.dropWindow.SetSize(305, 425)
		self.dropWindow.Show()

		self.scrollBar = ui.ScrollBar()
		self.scrollBar.SetParent(self.dropBoard)
		self.scrollBar.SetPosition(312, 5)
		self.scrollBar.SetScrollBarSize(425)
		self.scrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.scrollBar.Hide()

		self.statsBoard = ui.ThinBoard()
		self.statsBoard.SetParent(self)
		self.statsBoard.SetPosition(345, 35)
		self.statsBoard.SetSize(245, 435)
		self.statsBoard.Show()

		self.__BuildStatsElements()

		self.loadingText = ui.TextLine()
		self.loadingText.SetParent(self.dropWindow)
		self.loadingText.SetFontName(localeInfo.UI_DEF_FONT)
		self.loadingText.SetPackedFontColor(0xFF888888)
		if app.IsRTL():
			self.loadingText.SetPosition(295, 20)
			self.loadingText.SetWindowHorizontalAlignRight()
			self.loadingText.SetHorizontalAlignRight()
		else:
			self.loadingText.SetPosition(15, 20)
		self.loadingText.SetText(localeInfo.UITARGETINFO_LOADING)
		self.loadingText.Show()

	def __BuildStatsElements(self):
		self.rightTitle = ui.TextLine()
		self.rightTitle.SetParent(self.statsBoard)
		self.rightTitle.SetWindowHorizontalAlignCenter()
		self.rightTitle.SetHorizontalAlignCenter()
		self.rightTitle.SetPosition(0, 12)
		self.rightTitle.SetPackedFontColor(0xFFD4AF37) 
		self.rightTitle.SetText(localeInfo.UITARGETINFO_DETAILS)
		self.rightTitle.Show()

		self.sepLine1 = ui.Line()
		self.sepLine1.SetParent(self.statsBoard)
		self.sepLine1.SetPosition(15, 32)
		self.sepLine1.SetSize(215, 0)
		self.sepLine1.SetColor(grp.GenerateColor(0.3, 0.3, 0.3, 1.0))
		self.sepLine1.Show()

		self.monsterImageBg = ui.Bar()
		self.monsterImageBg.SetParent(self.statsBoard)
		self.monsterImageBg.SetPosition(10, 42)
		self.monsterImageBg.SetSize(225, 170)
		self.monsterImageBg.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.3)) 
		self.monsterImageBg.Show()

		self.monsterImage = ui.ExpandedImageBox()
		self.monsterImage.SetParent(self.monsterImageBg)
		self.monsterImage.SetWindowHorizontalAlignCenter()
		self.monsterImage.SetWindowVerticalAlignCenter()
		self.monsterImage.Hide()

		self.noModelText = ui.TextLine()
		self.noModelText.SetParent(self.monsterImageBg)
		self.noModelText.SetWindowHorizontalAlignCenter()
		self.noModelText.SetHorizontalAlignCenter()
		self.noModelText.SetPosition(0, 75)
		self.noModelText.SetPackedFontColor(0xFF666666)
		self.noModelText.SetText(localeInfo.UITARGETINFO_SEARCHING)
		self.noModelText.Show()

		self.sepLine2 = ui.Line()
		self.sepLine2.SetParent(self.statsBoard)
		self.sepLine2.SetPosition(15, 220)
		self.sepLine2.SetSize(215, 0)
		self.sepLine2.SetColor(grp.GenerateColor(0.3, 0.3, 0.3, 1.0))
		self.sepLine2.Show()

		self.statsTextDict = {}
		
		start_y = 230
		step_y = 20

		stats_keys = ["HP", "DAMAGE", "DEFENSE", "EXP", "GOLD", "RACE_MAIN", "REGEN", "RESISTS_L1", "RESISTS_L2"]

		for i, key in enumerate(stats_keys):
			text = ui.TextLine()
			text.SetParent(self.statsBoard)
			text.SetFontName(localeInfo.UI_DEF_FONT)
			text.SetWindowHorizontalAlignCenter()
			text.SetHorizontalAlignCenter()
			text.SetPosition(0, start_y + (i * step_y))
			text.Show()
			
			self.statsTextDict[key] = text
			self.statTexts.append(text) 

	def Open(self, vid, name):
		self.vid = int(vid)
		self.mobName = name
		self.SetTitleName(localeInfo.UITARGETINFO_TITLE + ": " + name)
		self.rightTitle.SetText(name)
		
		vnum = 0
		try:
			chr.SelectInstance(self.vid)
			vnum = chr.GetRace()
		except:
			pass

		if vnum == 0:
			try:
				vnum = chr.GetRace(self.vid)
			except:
				pass

		if vnum == 0:
			try:
				target_vid = player.GetTargetVID()
				chr.SelectInstance(target_vid)
				vnum = chr.GetRace()
			except:
				pass

		try:
			image_loaded = False
			
			search_paths = [
				"d:/ymir work/ui/target/%d%s"
			]
			
			for ext in [".tga", ".png", ".jpg", ".gif"]:
				for path_format in search_paths:
					test_path = path_format % (vnum, ext)
					if app.IsExistFile(test_path):
						try:
							self.monsterImage.LoadImage(test_path)
							self.monsterImage.Show()
							self.noModelText.Hide()
							image_loaded = True
							break
						except RuntimeError:
							pass
				if image_loaded:
					break
			
			if not image_loaded:
				self.monsterImage.Hide()
				self.noModelText.SetText(localeInfo.UITARGETINFO_NO_IMAGE % vnum)
				self.noModelText.Show()
		except:
			self.monsterImage.Hide()
			self.noModelText.SetText(localeInfo.UITARGETINFO_READ_ERROR)
			self.noModelText.Show()

		for row, _, _ in self.dropList:
			row.Hide()
				
		self.dropList = []
		self.dropYPos = 0
		
		self.scrollBar.SetPos(0.0)
		self.scrollBar.Hide()
		
		self.loadingText.SetText(localeInfo.UITARGETINFO_LOADING)
		self.loadingText.Show()
		self.Show()
		
		net.SendTargetInfoLoadPacket(self.vid)

	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnScroll(self):
		pos = self.scrollBar.GetPos()
		max_scroll = max(0, self.dropYPos - 425)
		current_offset = int(pos * max_scroll)
		
		for row, baseY, rowHeight in self.dropList:
			actual_y = baseY - current_offset
			
			if actual_y < 0 or actual_y + rowHeight > 425:
				row.Hide()
			else:
				row.SetPosition(5, actual_y)
				row.Show()

	def SetStats(self, hp, dmg_min, dmg_max, defense, exp, gold_min, gold_max, regen_pct, regen_cycle, res_sword, res_twohand, res_bell, res_dagger, res_fan, res_bow):
		try:
			self.statsTextDict["HP"].SetText("|cFFa6a6a6%s|r |cFFff4d4d%s|r" % (localeInfo.UITARGETINFO_HP, str(hp)))
			self.statsTextDict["DAMAGE"].SetText("|cFFa6a6a6%s|r |cFFff9933%s - %s|r" % (localeInfo.UITARGETINFO_DAMAGE, str(dmg_min), str(dmg_max)))
			self.statsTextDict["DEFENSE"].SetText("|cFFa6a6a6%s|r |cFFe6e6e6%s|r" % (localeInfo.UITARGETINFO_DEFENSE, str(defense)))
			self.statsTextDict["EXP"].SetText("|cFFa6a6a6%s|r |cFF33ccff%s|r" % (localeInfo.UITARGETINFO_EXP, str(exp)))
			self.statsTextDict["GOLD"].SetText("|cFFa6a6a6%s|r |cFFFFD700%s ~ %s|r" % (localeInfo.UITARGETINFO_GOLD, str(gold_min), str(gold_max)))
			
			race_str = localeInfo.TARGET_INFO_MAINRACE % localeInfo.TARGET_INFO_NO_RACE
			self.statsTextDict["RACE_MAIN"].SetText("|cFFa6a6a6%s|r |cFFe6e6e6%s|r" % (localeInfo.UITARGETINFO_RACE, race_str))
			
			self.statsTextDict["REGEN"].SetText("|cFFa6a6a6%s|r |cFF66ff66%s%%|r |cFFa6a6a6%s|r" % (localeInfo.UITARGETINFO_REGEN, regen_pct, localeInfo.UITARGETINFO_REGEN_CYCLE % regen_cycle))
			self.statsTextDict["RESISTS_L1"].SetText("|cFFa6a6a6%s|r |cFFffcc99%s%%|r | |cFFa6a6a6%s|r |cFFffcc99%s%%|r" % (localeInfo.UITARGETINFO_RESIST_SWORD, res_sword, localeInfo.UITARGETINFO_RESIST_TWOHAND, res_twohand))
			self.statsTextDict["RESISTS_L2"].SetText("|cFFa6a6a6%s|r |cFFffcc99%s%%|r | |cFFa6a6a6%s|r |cFFffcc99%s%%|r" % (localeInfo.UITARGETINFO_RESIST_DAGGER, res_dagger, localeInfo.UITARGETINFO_RESIST_BOW, res_bow))
		except Exception as e:
			pass

	def AddDrop(self, vnum, count, prob):
		self.loadingText.Hide()
		
		row = DungeonStyleDropRow(290)
		row.SetParent(self.dropWindow)
		row.SetToolTip(self.tooltipItem)
		rowHeight = row.SetItemInfo(vnum, prob)
		row.Show()
		
		self.dropList.append((row, self.dropYPos, rowHeight))
		self.dropYPos += rowHeight + 2
		
		if self.dropYPos > 425:
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()
			
		self.OnScroll()

	def RefreshDrops(self):
		if not self.dropList:
			self.loadingText.SetText(localeInfo.UITARGETINFO_NO_DROPS)
			self.loadingText.Show()
#ENABLE TARGET INFO SYSTEM_AZO ONE