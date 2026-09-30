document.addEventListener('DOMContentLoaded', function () {

    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.travel-tab-content');


    tabButtons.forEach(function (button) {

        button.addEventListener('click', function () {

            const target = button.dataset.tab;


            // 모든 버튼 비활성화
            tabButtons.forEach(function (btn) {
                btn.classList.remove('active');
            });


            // 클릭한 버튼 활성화
            button.classList.add('active');


            // 모든 내용 숨기기
            tabContents.forEach(function (content) {
                content.classList.remove('active');
            });


            // 선택한 내용만 표시
            const targetContent =
                document.getElementById(target + '-tab');

            if (targetContent) {
                targetContent.classList.add('active');
            }

        });

    });

});
