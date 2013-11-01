$(document).ready(function () {
    sfHover = function() {
	var sfEls = document.getElementById("nav").getElementsByTagName("li");
	for (var i=0; i<sfEls.length; i++) {
		sfEls[i].onmouseover=function() {
			this.className+="sfhover";
		}
		sfEls[i].onmouseout=function() {
			this.className=this.className.replace(new RegExp("sfhover\\b"), "");
		}
	}
}
if (window.attachEvent) window.attachEvent("onload", sfHover);

    var placeholder = $( "#search_text").value

    if(placeholder == null){
        $( ".placeholder" ).fadeIn( 1, function(){});
    }

    $( "#search_text" ).click(function() {
        $( ".placeholder" ).fadeOut( 1, function(){});
    });

    $( "#search_text" ).blur(function() {
        $( ".placeholder" ).fadeIn( 1, function(){});
    });

});


