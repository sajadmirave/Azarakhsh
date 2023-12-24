<?php

function space($count){
    $str = "";

    for($i = 0; $i < $count; $i++){
        $str .= "&nbsp;";
    }

    return $str;
}

$db = new PDO("sqlite:app.db");

$query = $db->prepare("SELECT * FROM fruit");
$query->execute();

// fetch all data
$rows = $query->fetchall();

$jsonData = json_encode($rows);
header('Content-Type: application/json');

$data = json_decode($jsonData,true);

foreach($data as $i){
    echo $i['id'];
    echo space(4);
    echo $i['title'];
    echo "<br/>";
}