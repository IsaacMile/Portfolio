<?php

function check_login($con) #check if the user is logged in
{
    if(isset($_SESSION['user_id'])) #if there is a user ID in session
    {
        $checkId = $_SESSION['user_id'];
        $query = "select * from users where user_id = '$checkId' limit 1";  
        #SQL query to check if the userID in session exists in the database
        
        $checkResult = mysqli_query($con, $query); #query the database
        if ($checkResult && mysqli_num_rows($checkResult) > 0) #if the user ID exists
        {
            $userData = mysqli_fetch_assoc($checkResult);
            return $userData; #fetch and return the users data
        }
    }
    #otherwise redirect to login
    else {
        header("Location: login.php");
        die; #finish code
    }
}
function random_num($length) #function to get a random user ID with a set length 
{
    $userId = ""; #start the id as an empty string 
    if($length < 5) 
    {
        $length = 5; #minimum length 5 
    }
    $len = rand(4, $length);
    for ($i = 0; $i < $len; $i++) #for the length of the id 
    {
        $userId .= rand(0,9); #append a new random letter
    }
    return $userId; #return userID
}