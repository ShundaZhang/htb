<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ScreenCrack</title>
    <link rel="shortcut icon" href="/icon.png" type="image/png">
    <link href="/style.css" type="text/css" rel="stylesheet"></link>
</head>
<body>
    <pre>
███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗
██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║██║     ██████╔╝███████║██║     █████╔╝ 
╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
███████║╚█████╗██║  ██║███████╗███████╗██║ ╚████║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    </pre>

    <center>
        <p>Users can view screenshots and the source code of any entered URL using the free web service ScreenCrack. To protect user privacy, our service deletes all screenshots and source files. Our primary goal is to protect users from malicious, shady, and fraudulent links.</p>
    </center>
    <br>
    <input type="text" id="url-input" placeholder="Enter a URL">
    <br>
    <div>
        <button type="button" id="screenshot-btn">
            SHOW SCREENSHOT
        </button>
        <button type="button" id="source-btn">
            VIEW SOURCE
        </button>
    </div>
    
    <center>
    <div id="screenshot"></div>
    </center>

    <center>
    <iframe id="filesource" class="hidden" height="500" width="1000"></iframe>
    </center>

    <script src="index.js"></script>
</body>
</html>

