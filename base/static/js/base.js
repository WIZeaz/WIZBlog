var isHover=false;
var isScrollDown=false;
$(document).ready(function(){
  var blocks=$(".block");
  /*var i=0;
  var handle=setInterval(
    function(){
      if (i<blocks.length){
        blocks[i].style.opacity=1;
        blocks[i].style.top='0px';
        i++;
      } else {
        window.clearInterval(handle);
      }
    },
    100
  );*/
  function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }
  (async function(){
    for (var i=0;i<blocks.length;++i){
      blocks[i].style.opacity=1;
      blocks[i].style.top='0px';
      await sleep(50);
    }
  })();
  var _checkScroll=function(){
    if ($(document).scrollTop()>=100){
      isScrollDown=true;
      $(".main-nav").addClass("main-nav-floating");
      $(".nav-item").css('color','black');
      $('#logo').removeClass("hide-div");
    } else {
      isScrollDown=false;
      if (!isHover && !isScrollDown){
        $(".main-nav").removeClass("main-nav-floating");
        $(".nav-item").css('color','white');
      }
      $('#logo').addClass("hide-div");
    }
  };
  _checkScroll();
  $(document).scroll(_checkScroll);

  $(".main-nav").hover(
    function(){
      isHover=true;
      $(".main-nav").addClass("main-nav-floating");
      $(".nav-item").css('color','black');
    },
    function(){
      isHover=false;
      if (!isHover && !isScrollDown){
        $(".main-nav").removeClass("main-nav-floating");
        $(".nav-item").css('color','white');
      }
    }
  );
});