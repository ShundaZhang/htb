<?php spl_autoload_register(function ($name) {
    if (preg_match('/Controller$/', $name)) {
        $name = "controllers/${name}";
    } elseif (preg_match('/Model$/', $name)) {
        $name = "models/${name}";
    }
    include_once "${name}.php";
});

$database = new Database('localhost', 'xclow3n', 'xCl0w3n1337!!', 'web_htbank');
$database->connect();

$router = new Router();
$router->new('POST', '/api/withdraw', 'WithdrawController@index');

die($router->match());