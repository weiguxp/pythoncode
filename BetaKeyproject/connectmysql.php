<?php

$username = "weitest";
$password = "JSx3NKE4pKs2G2bM";
$hostname = "localhost"; 

//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password) 
  or die("Unable to connect to MySQL");
echo "Connected to MySQL<br>";

mysql_select_db('Keys') or die('Could not select database');

?>