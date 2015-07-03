<?php
include 'connectmysql.php' ;


for ($x = 0; $x <= 10; $x++){
	$sqlq = "INSERT INTO myKeys VALUES('SomeCode', 'Asia', '0')";
	mysql_query($sqlq) or die ('Failed to add values');
}

?>