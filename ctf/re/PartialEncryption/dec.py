'''
https://x64dbg.com/

ghidra/IDA Pro:

void __fastcall sub_1400012B0(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
	int i; // [rsp+20h] [rbp-38h]
	void (__fastcall *v5)(__int64, __int64); // [rsp+38h] [rbp-20h]
	void (__fastcall *v6)(__int64, __int64); // [rsp+40h] [rbp-18h]
	for ( i = 0; i < 22; ++i )
	{
		if ( !*(_BYTE *)(*(_QWORD *)(a4 + 8) + i) )
		{
			v5 = (void (__fastcall *)(__int64, __int64))sub_140001050((__int64)&unk_140004070, 64);
			v5(a1, a2);
			VirtualFree(v5, 0i64, 0x8000u);
			v6 = (void (__fastcall *)(__int64, __int64))sub_140001050((__int64)&unk_140004110, 48);
			v6(a1, a2);
			VirtualFree(v6, 0i64, 0x8000u);
		}
	}
}

x64dbg command line change to partialencryption.exe 0123546789012345678901

SetBPX VirtualAlloc
SetBPX VirtualFree

Break at VirtualAlloc, Step over until ret and RAX Register contains the memory address
Follow RAX content in memory dump
Then run the program until it hit VirtualFree
Follow in disassembler or disassembly the dump (for the address in Dump1/RAX content in memory dump from VirualAlloc)

Found:

HTB{}}

Repeat:

W3iRd_
RUnT1m3_
DEC

HTB{W3iRd_RUnT1m3_DEC}

'''
