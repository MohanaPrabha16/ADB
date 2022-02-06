<html>
    <head>
        <h1>Hello World</h1>
</head>
<body>
    
    <h2> WELCOME </h2>
</body>
</html>
<?php
// PHP Data Objects(PDO) Sample Code:
try {
    $conn = new PDO("sqlsrv:server = tcp:assignmentserver01.database.windows.net,1433; Database = adbserver", "admin1", "{Ajithsivadas#1}");
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}
catch (PDOException $e) {
    print("Error connecting to SQL Server.");
    die(print_r($e));
}

// SQL Server Extension Sample Code:
$connectionInfo = array("UID" => "admin1", "pwd" => "{your_password_here}", "Database" => "adbserver", "LoginTimeout" => 30, "Encrypt" => 1, "TrustServerCertificate" => 0);
$serverName = "tcp:assignmentserver01.database.windows.net,1433";
$conn = sqlsrv_connect($serverName, $connectionInfo);
    
    $sql = "SELECT * FROM earthquake";
$result = $conn->query($sql);
echo $result;
/*if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Place: " . $row["place"]. " " . $row["type"]. "<br>";
    }
} else {
    echo "0 results";*/
}
?>
