'''
./volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone -f TrueSecrets.raw imageinfo

./volatility_2.6_lin64_standalone -f TrueSecrets.raw truecryptsummary --profile=Win7SP1x86

Password for zip => `X2Hk2XbEJqWYsh8VdbSYg6WpG9g7`

./volatility_2.6_lin64_standalone -f ../TrueSecrets.raw windows.dumpfiles

sudo virtualenv envl;sudo apt-get install libsnappy-dev;sudo vol -f TrueSecrets.raw windows.dumpfiles

sudo cryptsetup tcryptOpen development.tc container

sudo mkdir /media/container

sudo mount -o uid=1000 /dev/mapper/container /media/container

CyberChef + DES + CBC

Key = AKaPdSgV
IV = QeThWmYq

CipherText:
wENDQtzYcL3CKv0lnnJ4hk0JYvJVBMwTj7a4Plq8h68=
M35jHmvkY9WGlWdXo0ByOJrYhHmtC8O0hn+gLHaClb4QbACeOoSiYA==
hufGZi+isAzspq9AOs+sI/u+AS/aWPrAYd+mctDo7qEt+SpW2sELvSaxx6RRdK3vDavTsziAtb4/iCZ72v3QGh78yhY2KXZFu8qAcYdN7ltOOlg1LSrdkhjgr+CWTlvWh7A8IS7NwwI=
6ySb2CBt+Z1SZ4GlB7/yL4rJGeZ0WVaYW7N15aUsDAqzIYJWL/f0yw==
U2ltlIYcyGaSmL5xmAkEop+/f5MGUEWeWjpCTe5eStd/cg9FKp89l/EksGB90Z/hLbT44/Ur/6XL9aI27v0+SzaMFsgAeamjyYTRfLQk2fQlsRPCY/vMDj0FWRCGIZyHXCVoo4AePQB93SgQtOEkTQ2oBOeVU4X5sNQo23OcM1wrFrg8x90UOk2EzOm/IbS5BR+Wms1M2dCvLytaGCTmsUmBsATEF/zkfM2aGLytnu5+72bD99j7AiSvFDCpd1aFsogNiYYSai52YKIttjvao22+uqWMM/7Dx/meQWRCCkKm6s9ag1BFUQ==
+iTzBxkIgVWgWm/oyP/Uf6+qW+A+kMTQkouTEammirkz2efek8yfrP5l+mtFS+bWA7TCjJDK2nLAdTKssL7CrHnVW8fMvc6mJR4Ismbs/d/fMDXQeiGXCA==

https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)DES_Decrypt(%7B'option':'UTF8','string':'AKaPdSgV'%7D,%7B'option':'UTF8','string':'QeThWmYq'%7D,'CBC','Raw','Raw')&input=d0VORFF0elljTDNDS3YwbG5uSjRoazBKWXZKVkJNd1RqN2E0UGxxOGg2OD0KTTM1akhtdmtZOVdHbFdkWG8wQnlPSnJZaEhtdEM4TzBobitnTEhhQ2xiNFFiQUNlT29TaVlBPT0KaHVmR1ppK2lzQXpzcHE5QU9zK3NJL3UrQVMvYVdQckFZZCttY3REbzdxRXQrU3BXMnNFTHZTYXh4NlJSZEszdkRhdlRzemlBdGI0L2lDWjcydjNRR2g3OHloWTJLWFpGdThxQWNZZE43bHRPT2xnMUxTcmRraGpncitDV1RsdldoN0E4SVM3Tnd3ST0KNnlTYjJDQnQrWjFTWjRHbEI3L3lMNHJKR2VaMFdWYVlXN04xNWFVc0RBcXpJWUpXTC9mMHl3PT0KVTJsdGxJWWN5R2FTbUw1eG1Ba0VvcCsvZjVNR1VFV2VXanBDVGU1ZVN0ZC9jZzlGS3A4OWwvRWtzR0I5MFovaExiVDQ0L1VyLzZYTDlhSTI3djArU3phTUZzZ0FlYW1qeVlUUmZMUWsyZlFsc1JQQ1kvdk1EajBGV1JDR0laeUhYQ1ZvbzRBZVBRQjkzU2dRdE9Fa1RRMm9CT2VWVTRYNXNOUW8yM09jTTF3ckZyZzh4OTBVT2syRXpPbS9JYlM1QlIrV21zMU0yZEN2THl0YUdDVG1zVW1Cc0FURUYvemtmTTJhR0x5dG51NSs3MmJEOTlqN0FpU3ZGRENwZDFhRnNvZ05pWVlTYWk1MllLSXR0anZhbzIyK3VxV01NLzdEeC9tZVFXUkNDa0ttNnM5YWcxQkZVUT09CitpVHpCeGtJZ1ZXZ1dtL295UC9VZjYrcVcrQStrTVRRa291VEVhbW1pcmt6MmVmZWs4eWZyUDVsK210RlMrYldBN1RDakpESzJuTEFkVEtzc0w3Q3JIblZXOGZNdmM2bUpSNElzbWJzL2QvZk1EWFFlaUdYQ0E9PQo

HTB{570r1ng_53cr37_1n_m3m0ry_15_n07_g00d}
'''
