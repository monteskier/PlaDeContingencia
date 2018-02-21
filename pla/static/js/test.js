function closeLoading(bol){
  if(bol===true){
    $('.loading').hide(0.5);
  }else if(bol===false){
    $('.loading').show(0.5);
  }
}

function clieckTest(pk){
  closeLoading(false);

$.ajax({
  type:"GET",
  url:pk+"/test",
  data:$(this).data("id"),
  success:function(data){
    closeLoading(true);
    alert(data);
    location.reload();
  }
});
}
