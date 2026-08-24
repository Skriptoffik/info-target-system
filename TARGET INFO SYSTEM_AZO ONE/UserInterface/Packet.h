// «»ÕÀ ⁄‰

typedef struct command_target
{
    BYTE        header;
    DWORD       dwVID;
} TPacketCGTarget;


// ÷⁄ «”›·Â« 

//ENABLE TARGET INFO SYSTEM_AZO ONE
typedef struct command_target_info_load
{

	BYTE		header;
	DWORD		dwVID;
} TPacketCGTargetInfoLoad;

typedef struct packet_target_info
{

	BYTE		header;
	WORD		size;
	DWORD		dwVID;
	DWORD		race;
	DWORD		dwMaxHP;
	DWORD		dwDamageMin;
	DWORD		dwDamageMax;
	DWORD		dwDefense;
	DWORD		dwEXP;
	DWORD		dwGoldMin;
	DWORD		dwGoldMax;
	BYTE		bRegenPct;
	BYTE		bRegenCycle;
	BYTE		bResistSword;
	BYTE		bResistTwohand;
	BYTE		bResistBell;
	BYTE		bResistDagger;
	BYTE		bResistFan;
	BYTE		bResistBow;
} TPacketGCTargetInfo;

typedef struct packet_target_info_drop
{

	DWORD		dwVnum;
	DWORD		dwCount;
	int			iProb;
} TPacketGCTargetInfoDrop;
//ENABLE TARGET INFO SYSTEM_AZO ONE