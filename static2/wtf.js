$(document).ready(function(){
	for (var i = 0; i < 225; i++) {
		$("#wrap").append($("<div class=\"boxx\" id=box"+i+" onclick=\"user_play("+i+")\"></div>"));
		//$("#box"+i).click(function(){user_play(i)});               debug
	};
	$("#hover").css({ opacity: .4 });
});

function user_play(i){
	var t = $("#box"+i)
	if (t.css("background-image") == "none") {
		t.css("background-image", "url(static/img/white.png)");
	};
	$("#hover").show();
	$.get("/play", { id : i }, function(id){AI_play(id)})
}

function AI_play (id) {
	var intId = parseInt(id)
	if ( intId>= 0 ){
		$("#box"+id).css("background-image", "url(static/img/black.png)");
	}else{
		if (intId == -2333) {
			$("#win").show();
			$("#reset").show();
		};
		if (intId >=-225) {
			$("#box" + (1 - intId)).css("background-image", "url(static/img/black.png)");
			$("#lost").show();
			$("#reset").show();
		};
	}
	$("#hover").hide();
}
