<?php

	$temp = $_REQUEST["rain"];
	$rainfall = $_REQUEST["temp"];
	$ndvi = $_REQUEST["ndvi"];

	file_put_contents("../model/test_csv", ",0\n0,$temp\n1,$rainfall\n2,$ndvi");

	shell_exec("python3 ../model/run.py ../model/test_csv");

	$result = file_get_contents("../model/result.txt");
	echo $result;

?>
