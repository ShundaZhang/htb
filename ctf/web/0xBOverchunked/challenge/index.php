<!DOCTYPE html>
<html>
	<head>
		<title>0xBOverchunked</title>
		<link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
		<link rel="stylesheet" type="text/css" href="/assets/styles/style.css">
		<link rel="shortcut icon" type="image/x-icon" href="/assets/images/game-boy8bit.png">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
	</head>
	<body>
		<div class="wrapper">
			<div class="header-msg">
				<font color="#4CAF50">0xB</font><font color="#8BC34A">Overchunked</font>
			</div>
			<br>
			<div class="body-content">
				<p>Welcome to Overchunked - where game characters come to life!</p>
				<img src="/assets/images/game-boy8bit.png" width=100>
				<form id="search-form">
					<label for="my-input">Search:</label>
					<input type="text" class="bit8-textfield" name="search">
					<button type="submit" class="bit8-button">Submit</button>
				</form>
				<br>
				<p style="font-weight: bold;font-size: 20px;padding-top:20px;">Search Results:</p>
				<div id="results">
                    No results yet. Please insert the ID of the post.
				</div>
				<script>
					$(document).ready(function(){
					    $('#search-form').submit(function(event){
					        event.preventDefault();
					        var searchValue = $('input[name=search]').val();
					        $.ajax({
					            url: 'Controllers/Handlers/SearchHandler.php',
					            method: 'post',
					            data: {search: searchValue},
					            success: function(response){
					                $('#results').html(response);
					            }
					        });
					    });
					});
				</script>
			</div>
		</div>
	</body>
</html>

