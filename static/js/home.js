$(document).ready(function () {
  $(".slide").super({
    autoplay: true,
    arrowLeft: "<i class='fa-regular fa-circle-left fa-3x'></i>",
    arrowRight: "<i class='fa-regular fa-circle-right fa-3x'></i>",
    arrowElement: "<button style='background-color: white;'></button>",
    slidesToShow: 1,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
    ],
  });
});
