$(".btnTest").click(function(e){
$id = $(this).value();
$.ajax({
  type:"GET",
  url:pk+"/test",
  data:$(this).data("id"),
  success:function(data){
    location.reload();
  }
});

});
