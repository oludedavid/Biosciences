const navigation = new Navigation(document.getElementById("navigation"));

$(window).on("load", function () {
  setTimeout(function () {
    // allowing 3 secs to fade out loader
    $(".page-loader").fadeOut("slow");
  }, 2000);
});
