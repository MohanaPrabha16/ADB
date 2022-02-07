<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Contact Form - PHP/MySQL Demo Code</title>
</head>

<body>
<fieldset>
<legend>Contact Form</legend>
<form name="frmContact" method="post" action="<?php echo $PHP_SELF;?>">
<p>
<label for="Name">Name </label>
<input type="text" name="txtName" id="txtName">
</p>
<p>
<label for="email">Email</label>
<input type="text" name="txtEmail" id="txtEmail">
</p>
<p>
<label for="phone">Phone</label>
<input type="text" name="txtPhone" id="txtPhone">
</p>
<p>
<label for="message">Message</label>
<textarea name="txtMessage" id="txtMessage"></textarea>
</p>
<p>&nbsp;</p>
<p>
<input type="submit" name="Submit" id="Submit" value="Submit">
</p>
</form>
</fieldset>
<?php
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
//     echo "<h1>Caught PDO exception:</h1>";
//     echo $exception1->getMessage() . PHP_EOL;
//     echo "<h1>PHP Info for troubleshooting</h1>";
//     phpinfo();
}

?>

<h1> Success Results : </h1>
<!-- 
<?php
try {
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo $row['SQL_VERSION'] . PHP_EOL;
    }
} catch (PDOException $exception2) {
    // Display errors
    echo "<h1>Caught PDO exception:</h1>";
    echo $exception2->getMessage() . PHP_EOL;
}

unset($stmt);
unset($conn);
?>
?>
</body> -->

</html>


