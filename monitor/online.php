<?php
//########################################
//############## Server Monitor ##############
//###################################################
//###### Free Script by Gscripts.net ###############
//################# visit us at ############################
//#### http://gscripts.net ##################################
//##################### Free PHP/MySQL Scripts Direcotory ##########
//############################################################

$ip = "192.168.1.22"; // this is the host of the monitored server
$ip2 = "192.168.1.31"; // this is the host of the monitored server
$ip3 = "192.168.1.36"; // this is the host of the monitored server
$ip4 = "192.168.1.32";
$ip4 = "192.168.1.34";
$onlinetext = "On-Line" ; // this is the on-line message
$offlinetext = "Off-Line" ; // this is the off-line message
//$port = "80"; // this is the port that you check
$port = "22"; // this is the port that you check

if(@fsockopen($ip,$port,$errno,$errstr,1)) {
echo"Maple<a href='http://$ip' target='_blank'><img src='serveron.gif' width='16' height='15' border='0'></a>  $onlinetext";
} else {
echo"Maple<img src='serveroff.gif' width='16' height='15' border='0'> $offlinetext";
}

echo"<br />";

if(@fsockopen($ip2,$port,$errno,$errstr,1)) {
echo"Druid<a href='http://$ip2' target='_blank'><img src='serveron.gif' width='16' height='15' border='0'></a>  $onlinetext";
} else {
echo"Druid<img src='serveroff.gif' width='16' height='15' border='0'> $offlinetext";
}
echo"<br />";
if(@fsockopen($ip3,$port,$errno,$errstr,1)) {
echo"Cypress<a href='http://$ip3' target='_blank'><img src='serveron.gif' width='16' height='15' border='0'></a>  $onlinetext";
} else {
echo"Cypress<img src='serveroff.gif' width='16' height='15' border='0'> $offlinetext";
}

echo"<br />";

?>
