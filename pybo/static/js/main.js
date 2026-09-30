document.addEventListener('DOMContentLoaded', function () {
    const tabButtons = document.querySelectorAll('.tab-btn, [data-tab]');
    const tabContents = document.querySelectorAll('.travel-tab-content');

    tabButtons.forEach(function (button) {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const target = button.dataset.tab;
            if (!target) return;

            tabButtons.forEach(function (btn) {
                btn.classList.remove('active');
            });

            button.classList.add('active');

            tabContents.forEach(function (content) {
                content.classList.remove('active');
            });

            const targetContent = document.getElementById(target + '-tab');
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });
});
