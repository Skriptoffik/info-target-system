## „Ã·œ pack
##root/game.py

## «»ÃÀ ⁄‰

	# QUEST_CONFIRM
	def BINARY_OnQuestConfirm(self, msg, timeout, pid):
		confirmDialog = uiCommon.QuestionDialogWithTimeLimit()
		confirmDialog.Open(msg, timeout)
		confirmDialog.SetAcceptEvent(lambda answer=True, pid=pid: net.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		confirmDialog.SetCancelEvent(lambda answer=False, pid=pid: net.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		self.confirmDialog = confirmDialog
	# END_OF_QUEST_CONFIRM

## ÷⁄ «”›·Â«

#ENABLE TARGET INFO SYSTEM_AZO ONE
	def BINARY_TargetInfo_SetStats(self, hp, dmg_min, dmg_max, defense, exp, gold_min, gold_max, regen_pct, regen_cycle, res_sword, res_twohand, res_bell, res_dagger, res_fan, res_bow):
		if self.targetBoard and hasattr(self.targetBoard, "targetInfoDialog") and self.targetBoard.targetInfoDialog:
			if self.targetBoard.targetInfoDialog.IsShow():
				self.targetBoard.targetInfoDialog.SetStats(hp, dmg_min, dmg_max, defense, exp, gold_min, gold_max, regen_pct, regen_cycle, res_sword, res_twohand, res_bell, res_dagger, res_fan, res_bow)

	def BINARY_TargetInfo_AddDrop(self, vnum, count, prob):
		if self.targetBoard and hasattr(self.targetBoard, "targetInfoDialog") and self.targetBoard.targetInfoDialog:
			if self.targetBoard.targetInfoDialog.IsShow():
				self.targetBoard.targetInfoDialog.AddDrop(vnum, count, prob)

	def BINARY_TargetInfo_Refresh(self):
		if self.targetBoard and hasattr(self.targetBoard, "targetInfoDialog") and self.targetBoard.targetInfoDialog:
			if self.targetBoard.targetInfoDialog.IsShow():
				self.targetBoard.targetInfoDialog.RefreshDrops()
#ENABLE TARGET INFO SYSTEM_AZO ONE