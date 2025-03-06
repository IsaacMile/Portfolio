<?php #open php

$dbhost = "localhost";
$dbuser = "root"; #creat variable for the database location, initial table and database name
$dbpass = "";
$dbname = "login_db";

if(!$con = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname)) #if the connection not possible 
{
    die("could not connect". mysqli_connect_error()); #stop program and return error message
}
