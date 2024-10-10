<?php
    // default to Orion
    $project = "orion";

    $allProjects = ["orion", "ares", "ceres"];

    if (isset($_GET["project"])) {
        $project = strtolower($_GET["project"]);
    }
?>

<html>
   <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="chrome=1">
      <link rel="stylesheet" type="text/css" href="css/rpgui.css">
      <script src="css/rpgui.js"></script>
      <style>
         body, #container
         {
         background: #222;
         padding-top:20px;
         padding-bottom:20px;
         }
         .inner
         {
         background: #444;
         padding-left:20px;
         padding-right:20px;
         min-width: 740px;
         max-width: 900px;
         margin: 0 auto;
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
               <?php include "navbar.php"; ?>
               <hr>
               <p>Our Projects: </p>
               <select id="projectDropdown" class="rpgui-dropdown" data-rpguitype="dropdown" style="display: none;" onchange="reloadPage()">
                  <?php foreach ($allProjects as $proj): ?>
                  <option value="<?= $proj ?>" <?= $proj == $project ? "selected" : "" ?>>
                     <?= ucfirst($proj) ?>
                  </option>
                  <?php endforeach; ?>
               </select>
               <div id="containers" style="margin-top:30px;" class="rpgui-container framed-grey">
                  <h1><?php echo ucfirst($project); ?></h1>
                  <p><?php include "../projects/" . $project; ?></p>
               </div>
            </div>
         </div>
      </div>
   </body>
   <script>
      function reloadPage() {
          var dropdown = document.getElementById('projectDropdown');
          var selectedProject = dropdown.options[dropdown.selectedIndex].value;
          window.location.href = '/our-projects.php?project=' + selectedProject;
      }
   </script>
</html>