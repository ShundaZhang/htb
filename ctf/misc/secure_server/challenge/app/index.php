<html>

<head>
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="chrome=1">
   <link rel="stylesheet" type="text/css" href="css/rpgui.css">
   <script src="css/rpgui.js"></script>
   <style>
      body,
      #container {
         background: #222;
         padding-top: 20px;
         padding-bottom: 20px;
      }

      .inner {
         background: #444;
         padding-left: 20px;
         padding-right: 20px;
         min-width: 740px;
         max-width: 900px;
         margin: 0 auto;
      }

      li {
         user-select: text !important;
         cursor: text;
      }

      code {
         user-select: text !important;
         cursor: text;
      }

      span {
         user-select: text !important;
         font-size: 10px !important;
      }
   </style>
</head>

<body>
   <div class="rpgui-content rpgui-cursor-default" style="position: relative;">
      <div id="container">
         <div id="main"></div>
         <div class="inner rpgui-container framed" style="position:relative">
            <header>
               <h1 style="font-size:250%">Secure Coding</h1>
               <hr class="golden">
            </header>
            <?php include("navbar.php"); ?>
            <br><br>
            <ul>
               <li>This challenge is a <i>secure coding</i> challenge. With the help of the provided exploit script,
                  identify ALL of the flaws in the application. Once you have identified them all, it's up to you
                  to fix them!
               </li>
               <br><br>
               <li>You can access the filesystem of the remote instance by mounting it into your own filesystem:<br>
                    <code style="background-color:#2e3440; color:white; padding:5px; border-radius:5px;">
                        <span style="color:#81a1c1;">sudo</span>
                        <span style="color:#88c0d0;">mount</span>
                        <span style="color:#8fbcbb;">-t cifs</span>
                        <span style="color:#d08770;">//&lt;IP&gt;/app</span>
                        <span style="color:#ebcb8b;">~/mnt/</span>
                        <span style="color:#a3be8c;">-o username=guest,port=&lt;PORT&gt;</span>
                    </code>
                </li>
               <br><br>
               <li>Once you have done this, you can use any IDE of your choice to edit the files by accessing ~/mnt.<br></li>
               <br><br>
               <li>Once you think you have fixed the problems, connect to the last port to run the checker script. It
                  <i>should</i> tell you if anything is wrong.</li>
               <br><br>
               <li>The webserver has to have the same capabilities as it started with, so "fixing" the vulnerabilities by removing features and extensibility does not qualify as a valid solution. The URL format should remain the same for all pages as much as possible.</li><br><br>
               <li>If you have challenge feedback or believe you have a valid solution that is not properly detected, please reach out to ir0nstone via Discord!</li>
            </ul>
         </div>
      </div>
   </div>
</body>

</html>