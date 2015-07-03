<?php
$username = "weitest";
$password = "JSx3NKE4pKs2G2bM";
$hostname = "localhost"; 

//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password) 
  or die("Unable to connect to MySQL");
echo "Connected to MySQL<br>";

mysql_select_db('Keys') or die('Could not select database');

$inputKey = $_POST['inputKey'];
$inputRegion = $_POST['inputRegion'];
$used = $_POST['used'];

//inserting data order
$order = "INSERT INTO myKeys
			(beta_key, key_region, key_isused)
			VALUES
			('$inputKey',
			'$inputRegion',
			'$used')";

//declare in the order variable
$result = mysql_query($order);	//order executes
if($result){
	echo("<br>Input data is succeed");
} else{
	echo("<br>Input data is fail");
}


?>