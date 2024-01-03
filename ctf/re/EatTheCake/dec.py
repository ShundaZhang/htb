'''
upx -d cake.exe

Ghidra

  if ((local_41d == 'k') && (local_418 == 'a')) {
    cVar1 = local_439;
    if ((local_420 != 'h') || (local_416 != 'a')) goto LAB_004014fd;
    if (((local_41b == 'h') && (local_417 == 'r')) && (local_415 == 'd')) {
      cVar1 = '\x01';
      goto LAB_004014fd;
    }
  }
  cVar1 = '\0';
LAB_004014fd:
  if ((local_41f == '@') && (local_412 == 'E')) {
    if ((local_41e == 'c') && (local_413 == '$')) {
      local_439 = '\x01';
    }
  }


uint __fastcall FUN_004012f0(int param_1)
{
  uint uVar1;
  int iVar2;

  uVar1 = isdigit((int)*(char *)(param_1 + 6));
  if (uVar1 != 0) {
    uVar1 = isdigit((int)*(char *)(param_1 + 0xc));
    if (uVar1 != 0) {
      iVar2 = atoi((char *)(param_1 + 6));
      uVar1 = atoi((char *)(param_1 + 0xc));
      if ((((iVar2 == 3) && (uVar1 == 1)) && (*(char *)(param_1 + 4) == 't')) &&
         (*(char *)(param_1 + 7) == 'p')) {
        return 1;
      }
    }
  }
  return uVar1 & 0xffffff00;
}



cat cat.txt |sort

local_412 'E'
local_413 '$'
       14 '1'  c
local_415 'd'
local_416 'a'
local_417 'r'
local_418 'a'
       19 'p'  7
       1a '3'  6
local_41b 'h'
       1c 't'  4
local_41d 'k'
local_41e 'c'
local_41f '@'
local_420 'h'

HTB{h@ckth3parad1$E}
'''

