<?php
include 'connectmysql.php' ;

// $sqlq = "INSERT INTO myKeys VALUES('test1', 'Asia', '1')";
//mysql_query($sqlq) or die ('Failed to add values');

// Performing SQL query


$query = "SELECT * FROM myKeys
		WHERE key_region = 'Asia'
		AND key_isused = 0
		LIMIT 0, 5
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


// Free resultset
mysql_free_result($result);

// Closing connection
mysql_close($link);
?>


<table border="1">
  <tr>
    <td align="center">Query Beta Key System</td>
  </tr>
  <tr>
    <td>
      <table>
        <form method="post" action="querykey.php">
        <tr>
          <td>Keys</td>
          <td>

          <select type="number" name ="select_limit" id="select_limit">
          	<option value="5">5</option>
          	<option value="10">10</option>
          	<option value="15">10</option>
          </select>

          </td>
        </tr>
        <tr>
          <td>Region</td>
          <td>

          <select type="text" name ="key_region" id="key_region">
          	<option value="Asia">Asia</option>
          	<option value="China">China</option>
          </select>
          </td>
        </tr>
       	<tr>
          <td></td>
          <td align="right"><input type="submit" 
          name="submit" value="Sent"></td>
        </tr>
        </table>
      </td>
    </tr>
</table>