// «»ÕÀ ⁄‰

bool CPythonNetworkStream::RecvCreateFlyPacket()
{
	TPacketGCCreateFly kPacket;
	if (!Recv(sizeof(TPacketGCCreateFly), &kPacket))
		return false;

	CFlyingManager& rkFlyMgr = CFlyingManager::Instance();
	CPythonCharacterManager & rkChrMgr = CPythonCharacterManager::Instance();

	CInstanceBase * pkStartInst = rkChrMgr.GetInstancePtr(kPacket.dwStartVID);
	CInstanceBase * pkEndInst = rkChrMgr.GetInstancePtr(kPacket.dwEndVID);
	if (!pkStartInst || !pkEndInst)
		return true;

	rkFlyMgr.CreateIndexedFly(kPacket.bType, pkStartInst->GetGraphicThingInstancePtr(), pkEndInst->GetGraphicThingInstancePtr());

// ÷⁄ «”›·Â« 


//ENABLE TARGET INFO SYSTEM_AZO ONE
	return true;
}

bool CPythonNetworkStream::SendTargetInfoLoadPacket(DWORD dwVID)
{
	TPacketCGTargetInfoLoad packet;
	packet.header = HEADER_CG_TARGET_INFO_LOAD;
	packet.dwVID = dwVID;

	if (!Send(sizeof(packet), &packet))
	{
		Tracen("Send Target Info Load Packet Error");
		return false;
	}

	return SendSequence();
}

bool CPythonNetworkStream::RecvTargetInfoPacket()
{
	TPacketGCTargetInfo packet;

	if (!Recv(sizeof(TPacketGCTargetInfo), &packet))
		return false;

	int iDropSize = packet.size - sizeof(TPacketGCTargetInfo);
	std::vector<TPacketGCTargetInfoDrop> vec_drops;

	if (iDropSize > 0)
	{
		int iDropCount = iDropSize / sizeof(TPacketGCTargetInfoDrop);
		vec_drops.resize(iDropCount);
		if (!Recv(iDropSize, &vec_drops[0]))
			return false;
	}

	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], 
		"BINARY_TargetInfo_SetStats", 
		Py_BuildValue("(iiiiiiiiiiiiiii)",
			packet.dwMaxHP,
			packet.dwDamageMin,
			packet.dwDamageMax,
			packet.dwDefense,
			packet.dwEXP,
			packet.dwGoldMin,
			packet.dwGoldMax,
			packet.bRegenPct,
			packet.bRegenCycle,
			packet.bResistSword,
			packet.bResistTwohand,
			packet.bResistBell,
			packet.bResistDagger,
			packet.bResistFan,
			packet.bResistBow
		)
	);


	for (size_t i = 0; i < vec_drops.size(); ++i)
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], 
			"BINARY_TargetInfo_AddDrop", 
			Py_BuildValue("(iii)", vec_drops[i].dwVnum, vec_drops[i].dwCount, vec_drops[i].iProb)
		);
	}

	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_TargetInfo_Refresh", Py_BuildValue("()"));
//ENABLE TARGET INFO SYSTEM_AZO ONE