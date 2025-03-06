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
                if (is_numeric($password[$i])) #verification to make sure password includes numbers
                {
                    $includesNumbers = true;
                }
                else 
                {
                    $includesLetter = true;
                }
            }
            if (strlen($password) >= 8 && $includesLetter && $includesNumbers) 
            #if ther password is a certian length and contains letters and numbers
            {
                $insertQuery = "select * from users where user_name = '$userName' limit 1"; #SQL query to fetch all data from user
                $result = mysqli_query($con, $insertQuery);
                if($result && mysqli_num_rows($result) > 0) #checking the user was found 
                {
                    $userData = mysqli_fetch_assoc($result); #set userdata to the fetched data
                    if(password_verify($password, $userData["password"])) 
                    #if the password is correctly verified by using the hashing algorithm
                    {
                        $_SESSION['user_id'] = $userData['user_id'];
                        header("Location: index.php"); #take the user back to index page 
                        die;
                    }
                    else 
                    {
                        echo "The username or password you entered was incorrect"; #return correct error message
                    }   
                }
                else 
                {
                    echo "The username or password you entered was incorrect";
                }   

            }
            else 
            {
                echo "The username or password you entered was incorrect";
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
    <title>Space Simulator Programming: Login</title>
</head>
<body>
    <h1>Physics Simulation Programming: Login</h1>
    <p>This page can let you log into the website, this will be able to allow you to save your settings or save your progress 
            on the tutorial system</p>
    <a href = "Simulation Website Title.html">continue without logging in </a> 
    <br>
    <form method="post">
        <input text="username"type="text" name="userName">
        <input type="password" name="password">

        <input type="submit" value="login">
        <br>
        <a href="signup.php"> signup</a>
    </form>

</body>
</html>
