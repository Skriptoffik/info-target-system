// «»ÕÀ ⁄‰

		const SMobItemGroupInfo& GetOne() const
		{
			return m_vecItems[GetOneIndex()];
		}


// ÷⁄ «”›·Â«

//ENABLE TARGET INFO SYSTEM_AZO ONE
		const std::vector<int>& GetProbs() const { return m_vecProbs; }
		const std::vector<SMobItemGroupInfo>& GetVector() const { return m_vecItems; }
//ENABLE TARGET INFO SYSTEM_AZO ONE

// «»ÕÀ ⁄‰

	public:
	CDropItemGroup(DWORD dwVnum, DWORD dwMobVnum, const std::string& r_stName)
		:
		m_dwVnum(dwVnum),
	m_dwMobVnum(dwMobVnum),
	m_stName(r_stName)
	{
	}

	const std::vector<SDropItemGroupInfo> & GetVector()
	{
		return m_vec_items;
	}

// «” »œ· ”ÿ— Ê«Õœ ›ﬁÿ
	const std::vector<SDropItemGroupInfo> & GetVector()

// ≈·Ï ”ÿ— ÃœÌœ

//ENABLE TARGET INFO SYSTEM_AZO ONE
	const std::vector<SDropItemGroupInfo> & GetVector() const
//ENABLE TARGET INFO SYSTEM_AZO ONE

// ‰›” ‘—Õ »«·«⁄·Ï «»ÕÀ ⁄‰ 

	public :
		CLevelItemGroup(DWORD dwLevelLimit)
			: m_dwLevelLimit(dwLevelLimit)
		{}

		DWORD GetLevelLimit() { return m_dwLevelLimit; }

		void AddItem(DWORD dwItemVnum, DWORD dwPct, int iCount)
		{
			m_vec_items.emplace_back(SLevelItemGroupInfo(dwItemVnum, dwPct, iCount));
		}

		const std::vector<SLevelItemGroupInfo> & GetVector()
		{
			return m_vec_items;
		}
};

// «” »œ· «·”ÿ— «· «·Ì

//ENABLE TARGET INFO SYSTEM_AZO ONE
		const std::vector<SLevelItemGroupInfo> & GetVector() const
//ENABLE TARGET INFO SYSTEM_AZO ONE

// «»ÕÀ ⁄‰

		int			GetSpecialGroupFromItem(DWORD dwVnum) const { itertype(m_ItemToSpecialGroup) it = m_ItemToSpecialGroup.find(dwVnum); return (it == m_ItemToSpecialGroup.end()) ? 0 : it->second; }


// ÷⁄ «”›·Â«

//ENABLE TARGET INFO SYSTEM_AZO ONE
		const CMobItemGroup* GetMobItemGroup(DWORD dwMobVnum) const
		{
			auto it = m_map_pkMobItemGroup.find(dwMobVnum);
			if (it == m_map_pkMobItemGroup.end()) return NULL;
			return it->second;
		}
		const CLevelItemGroup* GetLevelItemGroup(DWORD dwMobVnum) const
		{
			auto it = m_map_pkLevelItemGroup.find(dwMobVnum);
			if (it == m_map_pkLevelItemGroup.end()) return NULL;
			return it->second;
		}
		const CDropItemGroup* GetDropItemGroup(DWORD dwMobVnum) const
		{
			auto it = m_map_pkDropItemGroup.find(dwMobVnum);
			if (it == m_map_pkDropItemGroup.end()) return NULL;
			return it->second;
		}
//ENABLE TARGET INFO SYSTEM_AZO ONE