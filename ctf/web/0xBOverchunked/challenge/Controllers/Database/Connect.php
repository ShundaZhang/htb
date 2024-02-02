<?php
$dbFile = '/opt/app/db/chunked.db';

try
{
    $pdo = new PDO("sqlite:$dbFile");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}
catch(PDOException $e)
{
    die("Failed to connect to database: " . $e->getMessage());
}
?>
