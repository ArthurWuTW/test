$(document).ready(function(e){
  $("#top3-button").click(function(){
      $.ajax({
          type: "GET",
          url: top3_url,  // URL to your view that serves new info
          data: {},
      }).done(function(response){
          alert_str = "Top3 Product ID: ";
          for(var order of response['top3']){
            alert_str += order;
            alert_str += ", ";
          }
          alert(alert_str);
      })
  });
});
