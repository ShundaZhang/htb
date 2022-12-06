'''
void FUN_00400978(byte *param_1)

{
  int local_14;
  byte *local_10;

  local_14 = 0;
  local_10 = param_1;
  while ((*local_10 != 9 && (local_14 < 0x14))) {
    putchar((int)(char)(*local_10 ^ 9));
    local_10 = local_10 + 1;
    local_14 = local_14 + 1;
  }
  putchar(10);
  return;
}

  local_48 = 0x41;
  local_47 = 0x5d;
  local_46 = 0x4b;
  local_45 = 0x72;
  local_44 = 0x3d;
  local_43 = 0x39;
  local_42 = 0x6b;
  local_41 = 0x30;
  local_40 = 0x3d;
  local_3f = 0x30;
  local_3e = 0x6f;
  local_3d = 0x30;
  local_3c = 0x3b;
  local_3b = 0x6b;
  local_3a = 0x31;
  local_39 = 0x3f;
  local_38 = 0x6b;
  local_37 = 0x38;
  local_36 = 0x31;
  local_35 = 0x74;
'''
flag = ''
x = [ 0x41, 0x5d, 0x4b, 0x72, 0x3d, 0x39, 0x6b, 0x30, 0x3d, 0x30, 0x6f, 0x30, 0x3b, 0x6b, 0x31, 0x3f, 0x6b, 0x38, 0x31, 0x74]
for i in x:
	flag += chr(i^9)
print flag
