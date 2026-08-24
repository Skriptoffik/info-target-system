// «»ÕÀ ⁄‰ 

		bool SendAttackPacket(UINT uMotAttack, DWORD dwVIDVictim);
		bool SendCharacterStatePacket(const TPixelPosition& c_rkPPosDst, float fDstRot, UINT eFunc, UINT uArg);
		bool SendUseSkillPacket(DWORD dwSkillIndex, DWORD dwTargetVID=0);
		bool SendTargetPacket(DWORD dwVID);


// ÷⁄ «”›·Â« 

//ENABLE TARGET INFO SYSTEM_AZO ONE
		bool SendTargetInfoLoadPacket(DWORD dwVID);
//ENABLE TARGET INFO SYSTEM_AZO ONE


// «»ÕÀ ⁄‰

		// Target
		bool RecvTargetPacket();

// ÷⁄ «”›·Â« 

//ENABLE TARGET INFO SYSTEM_AZO ONE
		bool RecvTargetInfoPacket();
//ENABLE TARGET INFO SYSTEM_AZO ONE
