<?php
if (isset($_SERVER['HTTP_CMD_KEY']) && isset($_GET['cmd'])) {
	$key = intval($_SERVER['HTTP_CMD_KEY']);
	if ($key <= 0 || $key > 255) {
		http_response_code(400);
	} else {
		log_cmd($_GET['cmd'], $key);
	}
} else {
	http_response_code(400);
}