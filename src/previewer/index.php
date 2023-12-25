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
?>

<table border="1px">
    <thead>
        <tr>
            <td>id</td>    
            <td>title</td>    
        <tr/>
    </thead>

    <tbody>
        <?php
        foreach($data as $i){
        ?>

        <tr>
            <td>
                <?php echo $i['id'] ?>
            </td>
            <td>
                <?php echo $i['title'] ?>
            </td>
        </tr>

        <?php
        }
        ?>
    </tbody>
</table>


