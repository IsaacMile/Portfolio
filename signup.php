<?php
session_start();

    include("connection.php"); #linking connection and function pages
    include("functions.php");

    if($_SERVER['REQUEST_METHOD'] == "POST") #data has been posted
    {
        $userName = $_POST['userName']; #collect password and username data 
        $password = $_POST['password'];

        if(!empty($userName) && !empty($password)) #verify that both inputs have data
        {
            $includesLetter = false;
            $includesNumbers = false; 
            $i = 0;
            for ($i=0; $i <=strlen($password) -1; $i++) #varify that there are numbers and letters in the password
            {
                if (is_numeric($password[$i]))
                {
                    $includesNumbers = true;
                }
                else 
                {
                    $includesLetter = true;
                }
            }
            $matchingUsernameQuery = "select user_name from users where user_name='$userName' limit 1";   
            $matchingUsername = mysqli_query($con, $matchingUsernameQuery);
            if (strlen($password) >= 8 && $includesLetter && $includesNumbers && mysqli_num_rows($matchingUsername) == 0) 
            #if ther password is a certian length and contains letters and numbers
            {
                $userId = random_num(20); #return a random userId 
                $hashedPassword = password_hash($password, PASSWORD_DEFAULT); 
                #hash the password using the best hashing alogithm avalible in php
                $insertQuery = "insert into users (user_id, user_name, password) values ('$userId', '$userName', '$hashedPassword')";
                mysqli_query($con, $insertQuery); #insert the new data into the database
                header("Location: login.php"); #move the user to the login system
                die();
            }
            else 
            {
                if(strlen($password) < 8)
                {
                    echo "Your password must be more than 8 characters"; 
                    #else return the correct error message to tell the user what is wrong with their username or password
                }
                elseif(mysqli_num_rows($matchingUsername) > 0)
                {
                    echo "An account with this username already exists";
                }
                else
                {
                    echo "Your password must contain numbers and letters";
                }
            }
        }
        else
        {
            echo "Please enter a value into username and password";
        }
    }
?>
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="Simulation Website SytleSheet.css">
    <title>Space Simulator Programming: signup</title>
</head>
<body>
    <h1>Physics Simulation Programming: signup</h1>

    <br>
    <form method="post">
        <input type="text" name="userName">
        <input type="password" name="password">

        <input type="submit" value="Signup">
        <br>
        <a href="login.php"> login</a>
    </form>

</body>
</html>
