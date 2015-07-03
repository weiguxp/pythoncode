<?php
include 'connectmysql.php';

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