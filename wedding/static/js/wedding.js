/**
 * Created by dpst on 03/08/2017.
 */
$(".nav a").on("click", function(){
   $(".nav").find(".active").removeClass("active");
   $(this).parent().addClass("active");
   console.log("clicked");
   console.log(this);
});

console.log("test");
console.log("test2");