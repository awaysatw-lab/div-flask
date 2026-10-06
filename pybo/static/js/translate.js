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
// 6. 언어 변경
// ==========================================================================

function changeLanguage(lang) {

    const menu =
        document.getElementById(
            'customLangMenu'
        );

    const currentLanguageText =
        document.getElementById(
            'currentLanguageText'
        );


    const languageNames = {

        'ko': '한국어',
        'en': 'English',
        'ja': '日本語',
        'zh-CN': '简体中文'

    };


    if (currentLanguageText) {

        currentLanguageText.textContent =
            languageNames[lang] || '한국어';

    }


    if (menu) {

        menu.style.display = 'none';

    }


    const googleSelect =
        document.querySelector(
            '.goog-te-combo'
        );


    if (!googleSelect) {

        console.log(
            'Google Translate 로딩 대기 중...'
        );

        setTimeout(
            function () {

                changeLanguage(lang);

            },
            500
        );

        return;
    }


    googleSelect.value = lang;

    googleSelect.dispatchEvent(
        new Event('change')
    );


    // 번역이 적용된 뒤 슬라이더 크기 재계산
    setTimeout(
        fixBannerText,
        500
    );
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