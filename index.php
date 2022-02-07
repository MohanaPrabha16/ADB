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
    $sql = "SELECT TOP 5 * FROM earthquake";

    // Executes the query
    $result = $conn->query("$sql");
    if($result->nums_rows > 0){
        while($row = $result-> fetch_assoc()){
            echo "<tr><td>".$row["0"] . "</td><td>".$row[1] . "</td><td>".$row["longitude"] . "</td><tr>"; 
    }
    }
    else{
    echo "No Results";
    }
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
