我们测试地址是 <a href="http://218.97.54.41/userCenter">http://218.97.54.41/userCenter</a><br>


<?php
include 'connectmysql.php' ;

$key_region = $_POST['key_region'];
$select_limit = $_POST['select_limit'];



$query = "SELECT * FROM myKeys
		WHERE key_region = '$key_region'
		AND is_issued = 0
		LIMIT 0, $select_limit
		";
$result = mysql_query($query) or die('Query failed: ' . mysql_error());


// Printing results in HTML
while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
    $myKey = $line['beta_key'];
    echo $myKey;
    echo "<br>";

    $sqlq = "UPDATE myKeys 
    SET is_issued =  '1'
    WHERE beta_key =  '$myKey'
    ";
    mysql_query($sqlq) or die ('Failed to Update');

}


?>