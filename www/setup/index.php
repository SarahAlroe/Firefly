<?php
$r = new Redis();
$r->connect('127.0.0.1');
$r->select(0);

$refVal=json_encode(array('r' => 0, 'g' => 0, 'b' => 0));

for( $i=0; $i<$_REQUEST["bugCount"]; $i++){
$r->set('firefly_bug_'.$i,$refVal);};

$r->set('firefly_activity',0);
?>
(re)set...
