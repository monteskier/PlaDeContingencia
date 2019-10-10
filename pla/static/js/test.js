function closeLoading(bol){
    if(bol===true){
      $('.loading').hide(0.5);
    }else if(bol===false){
      $('.loading').show(0.5);
    }
}

function clieckTest(pk, auto=false){
  closeLoading(false);
  $(this).addClass("load");
  $('button').attr("disabled", true);

  $.ajax({
    type:"GET",
    url:"Placon/"+pk+"/test",
    data:pk,
    success:function(data){
      $('button').attr("disabled", false);
      $("#content").removeClass("load");
      data = JSON.parse(data);
      closeLoading(true);
      if(auto === false){
        alert("Operatius = "+data.Operatius+"\n"+"Inoperatius = "+data.Inoperatius);
        location.reload();
      }

    },
});
}
