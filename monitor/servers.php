
<?php

$min_ip = "2";
$max_ip = "30";
echo "<h2>Checking ports $min_ip to $max_ip<h2>";
//$onlinetext = "On-Line" ; // this is the on-line message
$offlinetext = "<span style=\"background-color: red; color: white;\">Off-Line</span>" ; // this is the off-line message
$onlinetext = "<span style=\"background-color: green; color: white;\">Online</span>" ; // this is the off-line message
$sshport = "22"; // this is the port that you check
echo "<h1>SSH Port 22 Servers:</h1>";
echo "<table>";
foreach (range($min_ip, $max_ip) as $addr) {
    $ip = "192.168.0." . $addr;
    if(@fsockopen($ip,$sshport,$errno,$errstr,1)) {
        echo "<tr>";
        echo "<td>$ip</td>" .
             "<td><img src='serveron.gif' width='16' height='15' border='0'></td>" .
             "<td>$onlinetext</td>";
        echo"<tr/>";
    }
}
echo "</table>";
$http_port="80";
echo "<h1>HTTP Port 80 Servers:</h1>";
echo "<table>";
foreach (range($min_ip, $max_ip) as $addr) {
    $ip = "192.168.0." . $addr;
    if(@fsockopen($ip,$http_port,$errno,$errstr,1)) {
        echo "<tr>";
        echo "<td>$ip</td>" .
             "<td><img src='serveron.gif' width='16' height='15' border='0'></td>" .
             "<td>$onlinetext</td>";
        echo"<tr/>";
    }
}
echo "</table>";
?>
