document.addEventListener('DOMContentLoaded', function () {

    const slideImages = ['slide1.jpg', 'slide2.jpg', 'slide3.jpg', 'slide4.jpg', 'slide5.jpg', 'slide6.jpg'];
    slideImages.forEach(img => { const i = new Image(); i.src = `/static/img/${img}`; });
    const bannerSection = document.getElementById('mainBanner');
    const bannerText = document.getElementById('bannerArrowText');
    const prevBtn = document.getElementById('prevBanner');
    const nextBtn = document.getElementById('nextBanner');
    const titleElement = document.querySelector('.banner-text h2');

    if (titleElement) {
        const textLength = titleElement.textContent.trim().length;
    }

    const slides = [
        { img: '/static/img/slide1.jpg', title: '추억이 물드는<br>가을 여행', desc: '일상에서 벗어나<br>수도권 추천 여행' },
        { img: '/static/img/slide2.jpg', title: '설악의 붉은 숨결<br>강원 단풍 여행', desc: '대자연의 황금빛 매력<br>강원권 추천 여행' },
        { img: '/static/img/slide3.jpg', title: '고즈넉한 서정<br>충청 가을 산책', desc: '은은한 단풍빛 고을<br>충청권 추천 여행' },
        { img: '/static/img/slide4.jpg', title: '천년의 억새 물결<br>경상 가을 정취', desc: '황금빛 들녘과 바다<br>경상권 추천 여행' },
        { img: '/static/img/slide5.jpg', title: '내장산 붉은 터널<br>전라 단풍 비경', desc: '가을의 깊은 향기 속으로<br>전라권 추천 여행' },
        { img: '/static/img/slide6.jpg', title: '은빛 억새의 춤<br>낭만의 제주 가을', desc: '푸른 바다와 황금빛 오름<br>제주권 추천 여행' }
    ];

    let currentIndex = 0;
    let slideTimer = null;

    function updateSlider(index) {
        if (!bannerSection) return;

        bannerSection.style.backgroundImage = `url('${slides[index].img}')`;
        if (bannerText) bannerText.innerText = `${index + 1} / ${slides.length}`;

        const titleEl = document.getElementById('bannerTitle');
        const descEl = document.getElementById('bannerDesc');
        if (titleEl) titleEl.innerHTML = slides[index].title;
        if (descEl) descEl.innerHTML = slides[index].desc;
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        updateSlider(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        updateSlider(currentIndex);
    }

    function startTimer() {
        if (bannerSection) {
            slideTimer = setInterval(nextSlide, 3000); // 3초 간격 자동 전환
        }
    }

    function resetTimer() {
        clearInterval(slideTimer);
        startTimer();
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            nextSlide();
            resetTimer();
        });
    }
    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            prevSlide();
            resetTimer();
        });
    }

    startTimer();


    // ==========================================================================
    // 2. 지역별 / 테마별 탭 버튼 전환 제어 (중복 선언부 제거 완료)
    // ==========================================================================
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
                content.style.display = "none";
            });

            const targetContent = document.getElementById(target + '-tab');
            if (targetContent) {
                targetContent.classList.add('active');
                targetContent.style.display = "block";
            }
        });
    });
    const travelDropdown = document.querySelector('.nav-item.dropdown, .dropdown');
    const dropdownMenu = document.querySelector('.dropdown-menu, .travel-tab-content-wrapper');

    let dropdownTimeoutId;

    if (travelDropdown && dropdownMenu) {
        travelDropdown.addEventListener('mouseenter', function () {
            clearTimeout(dropdownTimeoutId);
            dropdownMenu.classList.add('show');
            travelDropdown.classList.add('show');
        });

        travelDropdown.addEventListener('mouseleave', function () {
            dropdownTimeoutId = setTimeout(function () {
                dropdownMenu.classList.remove('show');
                travelDropdown.classList.remove('show');
            }, 500);
        });
    }

    // ==========================================================================
    // 3. ✨ [신규 통합] M타임딜 1초 주기 실시간 카운트다운 타이머 엔진
    // ==========================================================================
    function updateMTimeDeals() {
        const timerElements = document.querySelectorAll('.time-text, .sub-timer');

        timerElements.forEach(function (el) {
            const endTimeStr = el.getAttribute('data-endtime');
            if (!endTimeStr) return;

            const endTime = new Date(endTimeStr).getTime();
            const now = new Date().getTime();
            const distance = endTime - now;

            if (distance < 0) {
                el.innerText = "🚨 핫딜 판매가 마감되었습니다.";
                el.style.color = "#999";
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            el.innerHTML = `<strong>${days}</strong>일 <strong>${String(hours).padStart(2, '0')}</strong>:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')} 남았습니다.`;
        });
    }

    updateMTimeDeals();
    setInterval(updateMTimeDeals, 1000);
});

// ========================================
// 언어 메뉴 열기 / 닫기
// ========================================

function toggleLangMenu() {

    const menu = document.getElementById('customLangMenu');

    if (!menu) {
        return;
    }

    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
}


// ========================================
// 언어 변경
// ========================================

function changeLanguage(lang) {

    const menu = document.getElementById('customLangMenu');
    const currentLanguageText =
        document.getElementById('currentLanguageText');

    const languageNames = {
        'ko': '한국어',
        'en': 'English',
        'ja': '日本語',
        'zh-CN': '简体中文'
    };


    // -----------------------------
    // 버튼에 현재 언어 표시
    // -----------------------------

    if (currentLanguageText) {
        currentLanguageText.textContent =
            languageNames[lang] || '한국어';
    }


    // -----------------------------
    // 메뉴 닫기
    // -----------------------------

    if (menu) {
        menu.style.display = 'none';
    }


    // -----------------------------
    // Google Translate 선택창 찾기
    // -----------------------------

    const googleSelect =
        document.querySelector('.goog-te-combo');


    // Google Translate가 아직 로딩되지 않은 경우
    if (!googleSelect) {

        console.log('Google Translate 로딩 대기 중...');

        // 조금 기다렸다가 다시 실행
        setTimeout(function () {
            changeLanguage(lang);
        }, 500);

        return;
    }


    // -----------------------------
    // 한국어
    // -----------------------------

    if (lang === 'ko') {

        googleSelect.value = 'ko';

        googleSelect.dispatchEvent(
            new Event('change')
        );

        return;
    }


    // -----------------------------
    // 외국어 번역
    // -----------------------------

    googleSelect.value = lang;

    googleSelect.dispatchEvent(
        new Event('change')
    );
}


// ========================================
// 메뉴 바깥 클릭하면 닫기
// ========================================

document.addEventListener('click', function (event) {

    const dropdown =
        document.querySelector('.cs-lang-dropdown');

    const menu =
        document.getElementById('customLangMenu');

    if (!dropdown || !menu) {
        return;
    }

    if (!dropdown.contains(event.target)) {
        menu.style.display = 'none';
    }
});


// ========================================
// 후기
// ========================================

document.addEventListener("DOMContentLoaded", function () {
    const btnMore = document.getElementById("btnMoreReviews");
    const reviewGrid = document.querySelector(".review-grid");

    if (btnMore && reviewGrid) {
        btnMore.addEventListener("click", function () {
            reviewGrid.classList.toggle("is-active");

            if (reviewGrid.classList.contains("is-active")) {
                btnMore.textContent = "후기 접기 △";
            } else {
                btnMore.textContent = "후기 더보기 ▽";
                reviewGrid.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    }
});