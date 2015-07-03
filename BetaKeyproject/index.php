<?php
include 'connectmysql.php' ;

// $sqlq = "INSERT INTO myKeys VALUES('test1', 'Asia', '1')";
//mysql_query($sqlq) or die ('Failed to add values');

// Performing SQL query


$query = "SELECT * FROM myKeys
		WHERE key_region = 'Asia'
		AND key_isused = 0
		LIMIT 0, 30
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
    <td align="center">Form Input Employees Data</td>
  </tr>
  <tr>
    <td>
      <table>
        <form method="post" action="input.php">
        <tr>
          <td>Key</td>
          <td><input type="text" name="inputKey" size="20" id ="inputKey">
          </td>
        </tr>
        <tr>
          <td>Region</td>
          <td>

          <select type="text" name ="inputRegion" id="inputRegion">
          	<option value="Asia">Asia</option>
          	<option value="China">China</option>
          </select>
          </td>
        </tr>
        <tr>
        	<td> Used </td>
        	<td><input type="text" name="used" sized = "1" id="used">
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