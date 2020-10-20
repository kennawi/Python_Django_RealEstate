const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


setTimeout(function() {
    $('#message').fadeOut('slow');
  }, 3000);



   // $(window).scroll (function(){
   // $('nav').toggleClass('scrolled', $(this).scrollTop() > 10);
   // });

// w.fn.init [Window]
// ----------------------- Sticky nave --------------
// down NavBar
// When the user scrolls down 20px from the top of the document, slide down the navbar
// When the user scrolls to the top of the page, slide up the navbar (50px out of the top view)
window.onscroll = function() {scrollFunction()};
home = document.getElementById( "showcase" )
// console.log(home);
if(home){
  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      document.getElementById("navbar").style.top = "0";
    } else {
      document.getElementById("navbar").style.top = "-130px";
    }
  }
}else{
  document.getElementById("navbar").style.top = "0";
  document.getElementById("navbar").style.position=" sticky";
}



// function scrollFunction() {
//   if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
//     document.getElementById("navbar").style.top = "0";
//   } else {
//     document.getElementById("navbar").style.top = "-130px";
//   }
// }

// owel crousal
mydir = $("html").attr("dir");

if (mydir == 'rtl') {
     rtlVal=true
}
else{
     rtlVal=false
    }

$('.owl-carousel').owlCarousel({
    rtl: rtlVal,
    center: true,
    autoplay:true,
    autoplayTimeout:2500,
    autoplayHoverPause:true,
   items:2,
   loop:true,
   margin:10,
   responsive:{
       600:{
           items:4
       }
   }
});


// Mobole Showcase




//    jQuery(document).ready(function($) {
//   var alterClass = function() {
//     var ww = document.body.clientWidth;
//     if (ww < 990) {
//       $('#card-wrapper1').each.removeClass('card-wrapper');
//       $('#img-wrapper').each.removeClass('card-img-wrapper');
//       $('#listing-heading').each.removeClass('card-title');
//       $('#card-title').each.removeClass('card-title');
//     } else if (ww >= 1024) {
//       $('#card-wrapper1').each.addClass('card-wrapper');
//      $('#img-wrapper').each.addClass('card-img-wrapper');
//      $('#listing-heading').each.addClass('card-title');
//      $('#card-title').each.addClass('card-title');
//     };
//   };
//   $(window).resize(function(){
//     alterClass();
//   });
//   //Fire it when the page first loads:
//   alterClass();
// });
