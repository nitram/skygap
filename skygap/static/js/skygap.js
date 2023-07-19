const navigation = document.querySelector('[data-navigation]');
const mobileNavigation = navigation.querySelector('[data-mobile-navigation]');
const body = document.querySelector('body');
const mobileNavigationToggle = navigation.querySelector(
  '[data-mobile-navigation-toggle]',
);


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


async function load_image(image, container) {
  if (image !== null && image !== "") {
    let response = await fetch(`/api/gtimg/${image}`);
    let data = await response.json();
    
    let img = new Image();
    let url = `/media/${data.file}`;

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

var copied = false;

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

  if (typeof loadDesign === "function") {
    loadDesign();
  }
});
