// «»ÕÀ ⁄‰

void CInputMain::Target(LPCHARACTER ch, const char * pcData)
{
	TPacketCGTarget * p = (TPacketCGTarget *) pcData;

	building::LPOBJECT pkObj = building::CManager::instance().FindObjectByVID(p->dwVID);

	if (pkObj)
	{
		TPacketGCTarget pckTarget;
		pckTarget.header = HEADER_GC_TARGET;
		pckTarget.dwVID = p->dwVID;
		ch->GetDesc()->Packet(&pckTarget, sizeof(TPacketGCTarget));
	}
	else
		ch->SetTarget(CHARACTER_MANAGER::instance().Find(p->dwVID));
}

// ÷⁄ «”›·Â«

//ENABLE TARGET INFO SYSTEM_AZO ONE
void CInputMain::TargetInfoLoad(LPCHARACTER ch, const char* c_pData)
{
	TPacketCGTargetInfoLoad* p = (TPacketCGTargetInfoLoad*)c_pData;

	LPCHARACTER pkVictim = CHARACTER_MANAGER::instance().Find(p->dwVID);
	if (!pkVictim || pkVictim->IsPC())
		return;

	TPacketGCTargetInfo pack;
	memset(&pack, 0, sizeof(TPacketGCTargetInfo));

	pack.header = HEADER_GC_TARGET_INFO;
	pack.dwVID = p->dwVID;
	pack.race = pkVictim->GetRaceNum();
	pack.dwMaxHP = pkVictim->GetMaxHP();
	pack.dwDamageMin = pkVictim->GetMobDamageMin();
	pack.dwDamageMax = pkVictim->GetMobDamageMax();
	pack.dwDefense = pkVictim->GetMobTable().wDef;
	pack.dwEXP = pkVictim->GetMobTable().dwExp;
	pack.dwGoldMin = pkVictim->GetMobTable().dwGoldMin;
	pack.dwGoldMax = pkVictim->GetMobTable().dwGoldMax;
	pack.bRegenPct = pkVictim->GetMobTable().bRegenPercent;
	pack.bRegenCycle = pkVictim->GetMobTable().bRegenCycle;
	pack.bResistSword = pkVictim->GetMobTable().cResists[MOB_RESIST_SWORD];
	pack.bResistTwohand = pkVictim->GetMobTable().cResists[MOB_RESIST_TWOHAND];
	pack.bResistBell = pkVictim->GetMobTable().cResists[MOB_RESIST_BELL];
	pack.bResistDagger = pkVictim->GetMobTable().cResists[MOB_RESIST_DAGGER];
	pack.bResistFan = pkVictim->GetMobTable().cResists[MOB_RESIST_FAN];
	pack.bResistBow = pkVictim->GetMobTable().cResists[MOB_RESIST_BOW];

	std::vector<TPacketGCTargetInfoDrop> vec_drops;

	const CMobItemGroup* pMobGroup = ITEM_MANAGER::instance().GetMobItemGroup(pack.race);
	if (pMobGroup)
	{
		const auto& vec = pMobGroup->GetVector();
		const auto& probs = pMobGroup->GetProbs();
		for (size_t i = 0; i < vec.size(); ++i)
		{
			TPacketGCTargetInfoDrop drop;
			drop.dwVnum = vec[i].dwItemVnum;
			drop.dwCount = vec[i].iCount;
			int iProb = probs[i];
			if (i > 0) iProb -= probs[i - 1];
			drop.iProb = iProb;
			vec_drops.push_back(drop);
		}
	}

	const CLevelItemGroup* pLevelGroup = ITEM_MANAGER::instance().GetLevelItemGroup(pack.race);
	if (pLevelGroup)
	{
		const auto& vec = pLevelGroup->GetVector();
		for (size_t i = 0; i < vec.size(); ++i)
		{
			TPacketGCTargetInfoDrop drop;
			drop.dwVnum = vec[i].dwVNum;
			drop.dwCount = vec[i].iCount;
			drop.iProb = vec[i].dwPct;
			vec_drops.push_back(drop);
		}
	}

	const CDropItemGroup* pDropGroup = ITEM_MANAGER::instance().GetDropItemGroup(pack.race);
	if (pDropGroup)
	{
		const auto& vec = pDropGroup->GetVector();
		for (size_t i = 0; i < vec.size(); ++i)
		{
			TPacketGCTargetInfoDrop drop;
			drop.dwVnum = vec[i].dwVnum;
			drop.dwCount = vec[i].iCount;
			drop.iProb = vec[i].dwPct;
			vec_drops.push_back(drop);
		}
	}

	pack.size = sizeof(TPacketGCTargetInfo) + (vec_drops.size() * sizeof(TPacketGCTargetInfoDrop));

	TEMP_BUFFER buf;
	buf.write(&pack, sizeof(TPacketGCTargetInfo));
	if (!vec_drops.empty())
	{
		buf.write(&vec_drops[0], vec_drops.size() * sizeof(TPacketGCTargetInfoDrop));
	}

	ch->GetDesc()->Packet(buf.read_peek(), buf.size());
}
//ENABLE TARGET INFO SYSTEM_AZO ONE

// «»ÕÀ ⁄‰

		case HEADER_CG_TARGET:
			Target(ch, c_pData);

// ÷⁄ «”›·Â«

//ENABLE TARGET INFO SYSTEM_AZO ONE
			break;

		case HEADER_CG_TARGET_INFO_LOAD:
			TargetInfoLoad(ch, c_pData);
//ENABLE TARGET INFO SYSTEM_AZO ONE