function explorar_errors(){
  $(".item span").each(function(){
    var $span = $(this);

    if($span.data("error")=="True") {
      $(this).parents(".item").css( "background-color", "#E60026");
      //$(this).parents(".item").addClass("parpadea")
      $(this).parent().addClass("parpadea");
      $(this).addClass("parpadea");
      //$(this).parent(".item").css( "background-color", "red");
    }
  })
}
function closeSeguiment(){
  $("#seguiment").hide();
  console.log("deveria no verse");
}
$(document).ready(function(){
  closeSeguiment();
  explorar_errors();
  $(".item").click(function(e){//Aixo es produeix quan es clica un Servei, obtenim el id del servei
    var pk = $(this).data("id");
    $.ajax({
      type:"GET",
      url:pk+"/getSeguimentsServei",
      data:$(this).data("id"),
      success:function(data){
        data = JSON.parse(data);

        $("#seguiment").empty();
        $("#seguiment").show();

        $.each(data,function(i, item){
          $("#seguiment").append("<h4><strong>"+item.fields.descripcio+"</strong></h4>"+item.fields.data_creacio);
          $("#seguiment").append("<br>");
          $("#seguiment").append("<p class='text'>"+item.fields.text+"</p>");

        });

        $("#seguiment").append("<button class='btn btn-danger center-block' onclick='closeSeguiment()'>Tancar</button>");
      }
    });
  });
  $(".item .childs").click(function(e){
    
    e.stopPropagation();
  });//Aixo es produeix quan es clica un Item, obtenim el id del Item
});
