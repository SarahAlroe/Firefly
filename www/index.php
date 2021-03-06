<?php 
$r = new Redis();
$r->connect('127.0.0.1');
$r->select(0);

$activity = 0;

$bugs = $r->keys('firefly_bug_*');
sort($bugs);
$bugValues = $r->mGet($bugs);

$bugDict = array();
$i = 0;

foreach($bugs as $bug){
  $bugDict[$i] = $bugValues[$i];
  $i++;
}

$activityKeys = $r->keys('firefly_activit*');
$activityValues = $r->mGet($activityKeys);

foreach($activityValues as $activityValue){
  if($activityValue > $activity){
    $activity = $activityValue;
  }
}

$response = array('activity' => $activity, 'bugs' => $bugDict);
echo json_encode($response);
?>
