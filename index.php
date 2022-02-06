<html>
    <head>
        <h2>Head</h2>
</head>
<body>
    <?php
// PHP Data Objects(PDO) Sample Code:
try {
    $conn = new PDO("sqlsrv:server = tcp:assignmentserver01.database.windows.net,1433; Database = adbserver", "admin1", "Ajithsivadas#1");
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
?>
</body>
</html>
