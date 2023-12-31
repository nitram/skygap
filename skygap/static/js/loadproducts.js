// Start with the first product
var counter = 0;

// Load 12 products at a time
// Load one more to check if there is no more data
var quantity = window.innerWidth <= 758 ? 9 : 13;

// Load next set of posts
async function loadProduct() {

    // Set start and end post numbers, and update counter
    let start = counter;
    let end = start + quantity;
    counter = end - 1;

    // Get new posts and add posts
    api = (pageId == null) ? `/api/gtprods/${start}/${end}` : `/api/gtprods/${start}/${end}/${pageId}`;
    let response = await fetch(api);
    let data = await response.json();

    if (data.length == quantity) {
        data = data.slice(0, -1);
        document.querySelector('.load-button').style.display = "block";
    }
    else {
        document.querySelector('.load-button').style.display = "none";
    }

    data.forEach((product) => {
        add_product(product).then((thumbnail) => {
            document.querySelector(`#${thumbnail.id} .line-right`).style.height = "100%";

            if (thumbnail.image !== null) {
                load_image(thumbnail.image, thumbnail.product);
            }
        });
    });



    document.querySelector('.load-text').style.transform = "translateY(0)";

    let loadLine = document.querySelector('.load-line');
    loadLine.style.animationPlayState = "paused";

    loadLine.classList.add("hide");
    loadLine.classList.add("load-line-hover");

    loadLine.style.animation = "none";
    loadLine.offsetHeight;
    loadLine.style.animation = null;
    
};

function add_product(contents) {

    return new Promise((resolve) => {

        let id = `pd${contents.type}${contents.id}`;
    
        // Create new product
        let product = document.createElement('li');
        product.className = 'gallery-item product';
        product.id = id;
        product.innerHTML = `
            <span class="line-bottom"></span>
            <span class="line-right"></span>
            
            <div class="image-container">
                <div class="gallery-image fadeimg"></div>
            </div>

            <div class="gallery-text">
                <div class="product-name upper">
                    ${contents.name}
                </div>
                <div class="product-price">
                    ${contents.price == null ? '<span>Price</span>' + 'N/A' : '<span>Starting at</span>' + '$' + contents.price}
                </div>
            </div>
            
        `

        // Add post to DOM
        document.querySelector('.product-list').append(product);

        resolve({
            'id': id,
            'image': contents.primary_thumbnail,
            'product': document.querySelector(`#${id} > .image-container > .gallery-image`),
        });
    });
}