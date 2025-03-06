<?php 
session_start();

if (isset($_SESSION["user_id"])) #if a user is logged on 
{
    unset($_SESSION["user_id"]); #unset the user id
}

header("Location: index.php"); #move the user back to index
die;
