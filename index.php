<?php 
session_start();

    include("connection.php"); #linking connection and function pages
    include("functions.php");

    $userData = check_login($con); #obtaining user data

?>

<!DOCTYPE html>
<html> 
    <head>
        <title>Space Simulator Programming: Login</title>
        <link rel="stylesheet" href="Simulation Website SytleSheet.css">
        <script src="Simulation Javascript.js"></script>
    </head>
    <body>
        <h1>Physics Simulation Programming: Login</h1>
        <a href = "Simulation Website Title.html">Main Page</a>
        <a href = "Logout.php">Logout</a>
        <p>This page can let you log into the website, this will be able to allow you to save your settings or save your progress 
            on the tutorial system</p>
        Welcome, <?php echo $userData['user_name']; ?>
    </body>
</html>