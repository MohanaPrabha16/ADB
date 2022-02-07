<!DOCTYPE html>
<html>
<head>
<title>Contact Form - PHP/MySQL Demo Code</title>
</head>

<body>


<?php
try {
    $serverName = "tcp:assignmentserver01.database.windows.net,1433";
    $databaseName = "adbserver";
    $uid = "admin1@assignmentserver01";
    $pwd = "Ajithsivadas#1";
    
    $conn = new PDO("sqlsrv:server = $serverName; Database = $databaseName;", $uid, $pwd);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Select Query
    $sql = "SELECT TOP 1 * FROM earthquake";

    // Executes the query
    $stmt = $conn->query("$sql");
    $row = $stmt->fetch();
    echo "$row[0] $row[1] $row[2]";
    $conn=NULL;
} catch (PDOException $exception1) {die(print_r($e));
echo "<table border='1'>
<tr>
<th>Id</th>
<th>name</th>
<th>Mobile</th>
<th>email</th>
</tr>";
 
while($row = mysql_fetch_array($result))
  {
  echo "<tr>";
  echo "<td>" . $row[0] . "</td>";
  echo "<td>" . $row[1] . "</td>";
  echo "<td>" . $row[2] . "</td>";
  echo "<td>" . $row[3] . "</td>";
  echo "</tr>";
  }
echo "</table>";
}

?>



</body>

</html>
