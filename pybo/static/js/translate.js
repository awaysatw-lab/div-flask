function toggleLangMenu() {

    const menu =
        document.getElementById(
            'customLangMenu'
        );

    if (!menu) {
        return;
    }


    if (menu.style.display === 'block') {

        menu.style.display = 'none';

    } else {

        menu.style.display = 'block';

    }
}


// ==========================================================================
// 6. 구글 번역 쿠키 및 동기화 유틸리티
// ==========================================================================

function setGoogTransCookie(lang) {
    const cookieValue = '/ko/' + lang;
    const host = window.location.hostname;

    document.cookie = 'googtrans=' + cookieValue + '; path=/;';

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

// ==========================================================================
// 언어 변경 (1회 클릭 즉시 적용)
// ==========================================================================

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

    // 1. 한국어로 복원하는 경우
    if (lang === 'ko') {
        clearGoogTransCookies();

        const googleSelect = document.querySelector('.goog-te-combo');
        if (googleSelect) {
            googleSelect.value = '';
            googleSelect.selectedIndex = 0;
            googleSelect.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
        }

        const iframe = document.querySelector('iframe.goog-te-banner-frame');
        if (iframe) {
            try {
                const innerDoc = iframe.contentDocument || iframe.contentWindow.document;
                const restoreBtn = innerDoc.querySelector('button[id*="restore"]') || innerDoc.querySelector('.goog-close-link');
                if (restoreBtn) restoreBtn.click();
            } catch (e) {}
        }

        const isTranslated = document.documentElement.classList.contains('translated-ltr') ||
                             document.documentElement.classList.contains('translated-rtl') ||
                             document.querySelector('.goog-te-banner-frame') !== null;
        if (isTranslated) {
            window.location.reload();
        }
        return;
    }

    // 2. 외국어(en, ja, zh-CN)로 번역하는 경우
    setGoogTransCookie(lang);

    const googleSelect = document.querySelector('.goog-te-combo');

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
    if (googleSelect.value && googleSelect.value !== lang) {
        googleSelect.value = '';
        googleSelect.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));

        setTimeout(function () {
            googleSelect.value = lang;
            googleSelect.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
            if (typeof fixBannerText === 'function') setTimeout(fixBannerText, 500);
        }, 100);
    } else {
        googleSelect.value = lang;
        googleSelect.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
        if (typeof fixBannerText === 'function') setTimeout(fixBannerText, 500);
    }
}


// ==========================================================================
// 7. 언어 메뉴 바깥 클릭
// ==========================================================================

document.addEventListener(
    'click',
    function (event) {

        const dropdown =
            document.querySelector(
                '.cs-lang-dropdown'
            );

        const menu =
            document.getElementById(
                'customLangMenu'
            );


        if (!dropdown || !menu) {
            return;
        }


        if (!dropdown.contains(event.target)) {

            menu.style.display = 'none';

        }

    }
);


// ==========================================================================
// 8. Google Translate 로딩 확인
// ==========================================================================

function waitForGoogleTranslate() {

    const googleSelect =
        document.querySelector(
            '.goog-te-combo'
        );


    if (googleSelect) {

        console.log(
            'Google Translate 로딩 완료'
        );

        hideGoogleTranslateBar();

        setTimeout(
            fixBannerText,
            500
        );

        return;
    }


    setTimeout(
        waitForGoogleTranslate,
        500
    );
}


// ==========================================================================
// 9. Google Translate 상단 바 숨기기
// ==========================================================================

function hideGoogleTranslateBar() {

    // Google 번역 iframe
    const frames =
        document.querySelectorAll(
            'iframe.goog-te-banner-frame, ' +
            'iframe.goog-te-banner-frame.skiptranslate'
        );


    frames.forEach(function (frame) {

        frame.style.setProperty(
            'display',
            'none',
            'important'
        );

        frame.style.setProperty(
            'visibility',
            'hidden',
            'important'
        );

        frame.style.setProperty(
            'opacity',
            '0',
            'important'
        );

        frame.style.setProperty(
            'width',
            '0px',
            'important'
        );

        frame.style.setProperty(
            'height',
            '0px',
            'important'
        );

    });


    // Google Translate 상단 영역
    const skipTranslate =
        document.querySelectorAll(
            'body > .skiptranslate'
        );


    skipTranslate.forEach(function (element) {

        element.style.setProperty(
            'display',
            'none',
            'important'
        );

        element.style.setProperty(
            'height',
            '0px',
            'important'
        );

    });


    // body 위치 초기화
    if (document.body) {

        document.body.style.setProperty(
            'top',
            '0px',
            'important'
        );

        document.body.style.setProperty(
            'margin-top',
            '0px',
            'important'
        );

    }


    // html 위치 초기화
    document.documentElement.style.setProperty(
        'margin-top',
        '0px',
        'important'
    );
}


// ==========================================================================
// 10. 번역 후 슬라이더 텍스트 보정
// ==========================================================================

function fixBannerText() {

    const title =
        document.getElementById(
            'bannerTitle'
        );

    const desc =
        document.getElementById(
            'bannerDesc'
        );


    if (!title) {
        return;
    }


    title.style.maxWidth = '100%';
    title.style.boxSizing = 'border-box';


    if (desc) {

        desc.style.maxWidth = '100%';
        desc.style.boxSizing = 'border-box';

    }
}


// ==========================================================================
// 11. Google Translate 감시
// ==========================================================================

document.addEventListener(
    'DOMContentLoaded',
    function () {

        syncCurrentLanguageDisplay();

        hideGoogleTranslateBar();

        fixBannerText();

        waitForGoogleTranslate();


        const observer =
            new MutationObserver(
                function () {

                    hideGoogleTranslateBar();
                    fixBannerText();

                }
            );


        observer.observe(
            document.documentElement,
            {
                childList: true,
                subtree: true,
                attributes: true,
                attributeFilter: [
                    'style',
                    'class'
                ]
            }
        );


        // Google Translate가 다시 표시할 경우 대비
        setInterval(
            hideGoogleTranslateBar,
            1000
        );

    }
);

syncCurrentLanguageDisplay();