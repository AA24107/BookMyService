const searchInput = document.getElementById("search-bar");
const cards = document.querySelectorAll(".service-card");
const cardContainer = document.getElementById("service-container")
const noServices = document.getElementById("no-services");

if (searchInput) {
    searchInput.addEventListener("input", searchCards);
}


cards.forEach(card => {
    const id = card.dataset.id;

    card.addEventListener("click", () => {
        window.location.href = `/service/${id}`
    })
})

// function for searching cards
function searchCards () {
    const searchTerm = searchInput.value.toLowerCase();
    const words = searchTerm.split(" ");
    let cardCount = 0;

    cards.forEach(card => {
        const cardText = card.textContent.toLowerCase();
        let show = true;

        words.forEach(word => {
            if (!cardText.includes(word)) {
                show = false;
            }
        })

        card.style.display = show ? 'block' : 'none';

        if (show) {
            cardCount++;
        }
    })
    if (cardCount === 0) {
        noServices.style.display = 'block';
        cardContainer.style.display = 'none';
    } else {
        noServices.style.display = 'none';
        cardContainer.style.display = 'block';
    }

}
