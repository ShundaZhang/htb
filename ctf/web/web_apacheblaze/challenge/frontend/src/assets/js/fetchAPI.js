$(document).ready(function() {
  $(".game a").click(function(event) {
      event.preventDefault();
      var gameName = $(this).attr("div");

      $.ajax({
          url: "/api/games/" + gameName,
          success: function(data) {
              var message = data.message;
              $("#gameplayresults").text(message);
          },
          error: function() {
              $("#gameplayresults").text("Error fetching API data.");
          }
      });
  });
});