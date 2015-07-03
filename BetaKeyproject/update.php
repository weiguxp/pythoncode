<?php
include 'connectmysql.php' ;

$sqlq = "UPDATE myKeys 
		SET BetaKey =  'werewsfewer' 
		WHERE Region =  'China'
		LIMIT 1
		";


mysql_query($sqlq) or die ('Failed to Update');

?>