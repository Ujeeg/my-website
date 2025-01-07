var swiper = new Swiper(".mySwiper", {
    slidesPerView: 2, 
    spaceBetween: 30,
    loop: true, // This enables the loop behavior
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });