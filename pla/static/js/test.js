$(".btnTest").click(function(e){
  console.log("deveria verse");
  e.preventDefault();
  e.stopPropagation();
$pk = $(this).value();
$.ajax({
  type:"GET",
  url:pk+"/test",
  data:$(this).data("id"),
  success:function(data){
    alert(data);
    location.reload();
  }
});

});
