function closeLoading(bol){
    if(bol===true){
      $('.loading').hide(0.5);
    }else if(bol===false){
      $('.loading').show(0.5);
    }
}

function clieckTest(pk){
  closeLoading(false);
  $("#content").addClass("load");
  $('button').attr("disabled", true);

$.ajax({
  type:"GET",
  url:pk+"/test",
  data:$(this).data("id"),
  success:function(data){
    $('button').attr("disabled", false);
    $("#content").removeClass("load");
    data = JSON.parse(data);
    closeLoading(true);
    alert("Operatius = "+data.Operatius+"\n"+"Inoperatius = "+data.Inoperatius);
    location.reload();
  }
});
}
