const navigation = document.querySelector('[data-navigation]');
const mobileNavigation = navigation.querySelector('[data-mobile-navigation]');
const body = document.querySelector('body');
const mobileNavigationToggle = navigation.querySelector(
  '[data-mobile-navigation-toggle]',
);

// Mobile Navigation
function toggleMobileNavigation() {
  if (mobileNavigation.hidden) {
    body.classList.add('no-scroll');
    mobileNavigation.hidden = false;
    mobileNavigationToggle.setAttribute('aria-expanded', 'true');
  } else {
    body.classList.remove('no-scroll');
    mobileNavigation.hidden = true;
    mobileNavigationToggle.setAttribute('aria-expanded', 'false');
  }
}


// Load Image
async function load_image(image, container) {
  if (image !== null && image !== "") {
    let response = await fetch(`/api/gtimg/${image}`);
    let data = await response.json();
    
    let img = new Image();
    let url = `${media_prefix}${data.file}`;

    img.onload = function() {
      container.style.backgroundImage = `url(${url})`;
      container.style.opacity = 1;
    }

    img.src = url;

    if (img.complete) img.onload();
  }
  else {
    return;
  }
}


// Footer lines animation
function footerAnimation() {
  let footer = document.querySelector("footer");
  let footerPos = footer.getBoundingClientRect().bottom;

  if (footerPos < (window.innerHeight + 100)) {
    document.querySelector(`.footer .line-right`).style.height = "100%";
    document.querySelector(`.footer .line-top`).style.width = "100%";
  }
}


// Main: Funciton calls
document.addEventListener('DOMContentLoaded', () => {

  mobileNavigationToggle.addEventListener('click', () => {
    toggleMobileNavigation();
  });

  if (typeof loadProduct === "function") {
    loadProduct();

    let loadBtn = document.querySelector('.load-button');
    loadBtn.addEventListener('click', (event) => {
      let loadText = loadBtn.querySelector('.load-text');
      loadText.style.transform = "translateY(100%)";

      let loadLine = loadBtn.querySelector('.load-line');
      loadLine.classList.remove("hide");
      loadLine.classList.remove("load-line-hover");
      loadLine.style.animationPlayState = "running";

      setTimeout(loadProduct, 2000);
    });
  }

  // Load Designs on design page
  if (typeof loadDesign === "function") {
    loadDesign();
  }

  // Load 404 page when page not found
  if (typeof load404 === "function") {
    load404();
  }

  footerAnimation();

  // If scrolled to bottom, load the next 20 posts
  if (typeof parallexScrollEffect === "function") {
    window.addEventListener('scroll', () => {
      footerAnimation();
      parallexScrollEffect();
    });
  } else {
    window.addEventListener('scroll', () => {
      footerAnimation();
    });
  }
});
