#jadx and guess!

import hashlib

#{"@type":"hhhkb.ctf.fastjson_and_furious.Flag","success":true}

input_str = "@type20240227hhhkb.ctf.fastjson_and_furious.flagsuccess20240227true"
hash_object = hashlib.md5(input_str.encode())
md5_hash = hash_object.hexdigest()
flag = f"HTB{{{md5_hash}}}"
print(flag)

