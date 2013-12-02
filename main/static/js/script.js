$(document).ready(function () {

    $( ".placeholder" ).click(function() {
        $( ".placeholder" ).fadeOut( 1, function(){});
        $( "#search_text" ).focus();
    });

    $( "#search_text" ).click(function() {
        $( ".placeholder" ).fadeOut( 1, function(){});
    });

    $( "#search_text" ).blur(function() {
        if($( "#search_text").val() == ''){
            $( ".placeholder" ).fadeIn( 1, function(){});
        }
    });

    if($('#id_city').find(":selected").text() != 'Красноярск'){
       $( "#id_area_tr").addClass('area_none');
    }


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

});


