document.addEventListener('DOMContentLoaded', function () {
    syncCurrentLanguageDisplay();

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
// 구글 번역 쿠키 및 동기화 유틸리티
// ========================================

function setGoogTransCookie(lang) {
    const cookieValue = '/ko/' + lang;
    const host = window.location.hostname;

    // 루트 경로 쿠키 설정
    document.cookie = 'googtrans=' + cookieValue + '; path=/;';

    // 호스트 도메인 쿠키 설정
    if (host && host !== 'localhost') {
        document.cookie = 'googtrans=' + cookieValue + '; domain=' + host + '; path=/;';
        document.cookie = 'googtrans=' + cookieValue + '; domain=.' + host + '; path=/;';
    }
}

function clearGoogTransCookies() {
    const host = window.location.hostname;
    const domainVariations = ['', host, '.' + host];
    const hostParts = host.split('.');
    if (hostParts.length > 2) {
        domainVariations.push('.' + hostParts.slice(-2).join('.'));
    }

    const pathVariations = ['/', window.location.pathname];

    domainVariations.forEach(function (domain) {
        pathVariations.forEach(function (path) {
            const domainAttr = domain ? '; domain=' + domain : '';
            document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=' + path + domainAttr;
        });
    });
}

function syncCurrentLanguageDisplay() {
    const languageNames = {
        'ko': '한국어',
        'en': 'English',
        'ja': '日本語',
        'zh-CN': '简体中文'
    };

    const currentLanguageText = document.getElementById('currentLanguageText');
    if (!currentLanguageText) return;

    const match = document.cookie.match(/(?:^|;\s*)googtrans=\/ko\/([a-zA-Z\-]+)/);
    if (match && match[1] && languageNames[match[1]]) {
        currentLanguageText.textContent = languageNames[match[1]];
    } else {
        currentLanguageText.textContent = '한국어';
    }
}

// ========================================
// 언어 변경 (1회 클릭 즉시 적용)
// ========================================

function changeLanguage(lang) {
    const menu = document.getElementById('customLangMenu');
    const currentLanguageText = document.getElementById('currentLanguageText');

    const languageNames = {
        'ko': '한국어',
        'en': 'English',
        'ja': '日本語',
        'zh-CN': '简体中文'
    };

    if (currentLanguageText) {
        currentLanguageText.textContent = languageNames[lang] || '한국어';
    }

    if (menu) {
        menu.style.display = 'none';
    }

    // ----------------------------------------
    // 1. 한국어로 복원하는 경우
    // ----------------------------------------
    if (lang === 'ko') {
        clearGoogTransCookies();

        const googleSelect = document.querySelector('.goog-te-combo');
        if (googleSelect) {
            googleSelect.value = '';
            googleSelect.selectedIndex = 0;
            googleSelect.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
        }

        // 번역 배너의 원본 복원 버튼이 있는 경우 트리거
        const iframe = document.querySelector('iframe.goog-te-banner-frame');
        if (iframe) {
            try {
                const innerDoc = iframe.contentDocument || iframe.contentWindow.document;
                const restoreBtn = innerDoc.querySelector('button[id*="restore"]') || innerDoc.querySelector('.goog-close-link');
                if (restoreBtn) restoreBtn.click();
            } catch (e) {}
        }

        // 이미 번역이 적용된 상태인 경우 새로고침으로 깨끗하게 복원
        const isTranslated = document.documentElement.classList.contains('translated-ltr') ||
                             document.documentElement.classList.contains('translated-rtl') ||
                             document.querySelector('.goog-te-banner-frame') !== null;
        if (isTranslated) {
            window.location.reload();
        }
        return;
    }

    // ----------------------------------------
    // 2. 외국어(en, ja, zh-CN)로 번역하는 경우
    // ----------------------------------------
    // 쿠키를 즉시 설정하여 다음 페이지 이동 및 로딩 지연 시에도 자동 적용되도록 보장
    setGoogTransCookie(lang);

    const googleSelect = document.querySelector('.goog-te-combo');

    // Google Translate 위젯이 아직 로딩되지 않은 경우 폴링하여 로딩 즉시 적용
    if (!googleSelect) {
        let attempts = 0;
        const checkTimer = setInterval(function () {
            attempts++;
            const select = document.querySelector('.goog-te-combo');
            if (select) {
                clearInterval(checkTimer);
                applyGoogleLanguage(select, lang);
            } else if (attempts >= 30) {
                clearInterval(checkTimer);
            }
        }, 100);
        return;
    }

    applyGoogleLanguage(googleSelect, lang);
}

function applyGoogleLanguage(googleSelect, lang) {
    // 이미 다른 외국어로 번역된 상태인 경우: 리셋 후 목표 언어로 변경하여 2회 클릭 문제 방지
    if (googleSelect.value && googleSelect.value !== lang) {
        googleSelect.value = '';
        googleSelect.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));

        setTimeout(function () {
            googleSelect.value = lang;
            googleSelect.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
        }, 100);
    } else {
        googleSelect.value = lang;
        googleSelect.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
    }
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

syncCurrentLanguageDisplay();