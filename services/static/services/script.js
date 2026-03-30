const searchInput = document.getElementById("search-bar");
const cards = document.querySelectorAll(".service-card");
const cardContainer = document.getElementById("service-container")

if (searchInput) {
    searchInput.addEventListener("input", searchCards);
}

console.log("Js working");

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

    cards.forEach(card => {
        const cardText = card.textContent.toLowerCase();
        let cardCount = 0;
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

        if (cardCount === 0) {
            cardContainer.innerHTML = `
            <div>
                <h3>No Services Found</h3>
            </div>`
        }

    })

}
