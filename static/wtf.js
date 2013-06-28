$(document).ready(function(){
	for (var i = 0; i < 225; i++) {
		$("#wrap").append($("<div class=\"boxx\" id=box"+i+" onclick=\"user_play("+i+")\"></div>"));
		//$("#box"+i).click(function(){user_play(i)});               debug
	};
});

function user_play(i){
	var t = $("#box"+i)
	if (t.css("background-image") == "none") {
		t.css("background-image", "url(static/img/white.png)");
	};
	$.get("/play", { id : i }, function(id){AI_play(id)})
}

function AI_play (id) {
  if ( parseInt(id) >= 0 ){
	  $("#box"+id).css("background-image", "url(static/img/black.png)");
  }
}
