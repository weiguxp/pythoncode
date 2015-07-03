我们测试地址是 <a href="http://218.97.54.41/userCenter">http://218.97.54.41/userCenter</a><br>


<?php
include 'connectmysql.php' ;

$key_region = $_POST['key_region'];
$select_limit = $_POST['select_limit'];



$query = "SELECT * FROM myKeys
		WHERE key_region = '$key_region'
		AND key_isused = 0
		LIMIT 0, $select_limit
		";
$result = mysql_query($query) or die('Query failed: ' . mysql_error());


// Printing results in HTML
echo "<table>\n";
while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
    echo "\t<tr>\n";
    foreach ($line as $col_value) {
        echo "\t\t<td>$col_value</td>\n";
    }
    echo "\t</tr>\n";
}
echo "</table>\n";


?>