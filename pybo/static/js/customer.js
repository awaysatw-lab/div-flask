document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('faqSearch');

    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            const value = this.value.toLowerCase();
            const accordionItems = document.querySelectorAll('#faqAccordion .accordion-item');

            accordionItems.forEach(function(item) {
                const text = item.textContent.toLowerCase();
                if (text.indexOf(value) > -1) {
                    item.style.display = "";
                } else {
                    item.style.display = "none";
                }
            });
        });
    }
});
