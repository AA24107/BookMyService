const searchInput = document.getElementById("search-bar");
const cards = document.querySelectorAll(".service-card");

if (searchInput) {
    searchInput.addEventListener("input", filterCards);
}

console.log("Js working");

cards.forEach(card => {
    const id = card.dataset.id;

    card.addEventListener("click", () => {
        window.location.href = `/service/${id}`
    })
})


function filterCards () {
    const searchTerm = searchInput.value.toLowerCase();
    const words = searchTerm.split(" ");

    cards.forEach(card => {
        const cardText = card.textContent.toLowerCase();

        let show = true;

        words.forEach(word => {
            if (!cardText.includes(word)) {
                show = false;
            }
        })

        card.style.display = show ? 'block' : 'none';

    })

}
