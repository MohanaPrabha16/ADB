<!DOCTYPE html>
<html>
<head>
<title>Contact Form - PHP/MySQL Demo Code</title>
</head>

<body>

<table>
    <tr>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
<!--         <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th>
        <th>col1</th> -->
    </tr>
<?php
try {
    $serverName = "tcp:assignmentserver01.database.windows.net,1433";
    $databaseName = "adbserver";
    $uid = "admin1@assignmentserver01";
    $pwd = "Ajithsivadas#1";
    
    $conn = new PDO("sqlsrv:server = $serverName; Database = $databaseName;", $uid, $pwd);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Select Query
    $sql = "SELECT TOP 2 * FROM earthquake";

    // Executes the query
    $stmt = $conn->query("$sql");
    $row = $stmt->fetchAll();
    echo "$row[0] $row[1] $row[2]";
    $conn=NULL;
} catch (PDOException $exception1) {die(print_r($e));
//     echo "<h1>Caught PDO exception:</h1>";
//     echo $exception1->getMessage() . PHP_EOL;
//     echo "<h1>PHP Info for troubleshooting</h1>";
//     phpinfo();
}

?>

    </table>

</body>

</html>
