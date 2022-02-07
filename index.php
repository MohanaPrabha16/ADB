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
    echo "<th><tr>mag type</tr><tr>id</tr></th>"
    echo "$row[0] $row[1] $row[2]";
    $conn=NULL;
} catch (PDOException $exception1) {die(print_r($e));
//     echo "<h1>Caught PDO exception:</h1>";
//     echo $exception1->getMessage() . PHP_EOL;
//     echo "<h1>PHP Info for troubleshooting</h1>";
//     phpinfo();
}

?>



</body>

</html>
