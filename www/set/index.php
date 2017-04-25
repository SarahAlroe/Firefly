<?php
$r = new Redis();
$r->connect('127.0.0.1');
$r->select(0);

if(isset($_REQUEST["bug"])){
$bug = $_REQUEST["bug"];
$bugValue = json_decode($r->get('firefly_bug_'.$bug),true);

if (isset($_REQUEST["r"])){$bugValue["r"]=$_REQUEST["r"];}
if (isset($_REQUEST["g"])){$bugValue["g"]=$_REQUEST["g"];}
if (isset($_REQUEST["b"])){$bugValue["b"]=$_REQUEST["b"];}

$r->set('firefly_bug_'.$bug, json_encode($bugValue));
};

if(isset($_REQUEST["activity"])){
$r->set('firefly_activity',$_REQUEST["activity"]);
};

include_once("../index.php");
?>
