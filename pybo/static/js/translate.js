/**
 * [길마중] 구글 번역 엔진 기반 실시간 다국어 번역 및 UI 토글 최종 통합 스크립트
 */

// 1. 구글 번역 엔진 초기화 설정 (글로벌 함수로 선언하여 구글 코어가 호출하게 함)
function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: 'ko',
        includedLanguages: 'ko,en,ja,zh-CN', // 한국어, 영어, 일본어, 중국어(간체)만 허용
        autoDisplay: false
    }, 'google_translate_element');
}

// 2. 텍스트 라벨 맵 객체 선언 (상단 토글 글자 연동용)
var langTextMap = {
    'ko': '한국어',
    'en': 'English',
    'ja': '日本語',
    'zh-CN': '简体中文'
};

// 3. [핵심 수정] 언어 클릭 시 구글 셀렉트 박스를 강제로 조작하여 번역을 집행하는 함수
function changeLanguage(langCode) {
    // 선택한 언어를 브라우저 저장소에 보존
    localStorage.setItem('selected_lang', langCode);

    // 헤더 버튼의 텍스트를 즉시 변경
    var textEl = document.getElementById('currentLanguageText');
    if (textEl && langTextMap[langCode]) {
        textEl.innerText = langTextMap[langCode];
    }

    // 구글 내장 번역 컴포넌트 강제 헨들링
    var selectEl = document.querySelector('.goog-te-combo');
    if (selectEl) {
        selectEl.value = langCode;
        selectEl.dispatchEvent(new Event('change'));
    } else {
        // 만약 구글 스크립트 로드가 미세하게 늦은 경우, 0.1초 뒤 다시 강제 집행
        setTimeout(function() {
            var reSelectEl = document.querySelector('.goog-te-combo');
            if (reSelectEl) {
                reSelectEl.value = langCode;
                reSelectEl.dispatchEvent(new Event('change'));
            }
        }, 150);
    }
}

// 4. 드롭다운 메뉴 열고 닫기 제어 함수
function toggleLangMenu() {
    var menu = document.getElementById('customLangMenu');
    if (!menu) return;

    if (menu.style.display === 'none' || menu.style.display === '') {
        menu.style.display = 'block';
    } else {
        menu.style.display = 'none';
    }
}

// 5. 드롭다운 바깥 영역 클릭 시 자동으로 닫히는 안전장치
window.addEventListener('click', function(e) {
    var dropdown = document.querySelector('.cs-lang-dropdown');
    var menu = document.getElementById('customLangMenu');

    if (dropdown && !dropdown.contains(e.target)) {
        if (menu) {
            menu.style.display = 'none';
        }
    }
});

// 6. 페이지가 켜질 때 기억된 언어가 있다면 자동으로 구글 엔진 가동
document.addEventListener('DOMContentLoaded', function() {
    var currentLang = localStorage.getItem('selected_lang') || 'ko';

    // 상단 토글 라벨 글자 상태 복구
    var textEl = document.getElementById('currentLanguageText');
    if (textEl && langTextMap[currentLang]) {
        textEl.innerText = langTextMap[currentLang];
    }

    // 구글 번역 엘리먼트가 완전히 렌더링될 때까지 감시 (최대 4초간 추적)
    var attempts = 0;
    var checkInterval = setInterval(function() {
        var selectEl = document.querySelector('.goog-te-combo');
        attempts++;

        if (selectEl) {
            clearInterval(checkInterval);
            if (currentLang !== 'ko') {
                selectEl.value = currentLang;
                selectEl.dispatchEvent(new Event('change'));
            }
        }

        if (attempts > 40) { // 4초 이상 안 뜨면 타이머 해제
            clearInterval(checkInterval);
        }
    }, 100);

    // 언어 아이템 마우스 호버 비주얼 인터랙션 연결
    var items = document.querySelectorAll('.lang-item');
    items.forEach(function(item) {
        item.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#FAF8F5';
            this.style.color = '#1E3A5F';
        });

        item.addEventListener('mouseleave', function() {
            this.style.backgroundColor = 'transparent';
            this.style.color = '#2B2D42';
        });

        item.addEventListener('click', function() {
            var menu = document.getElementById('customLangMenu');
            if (menu) {
                menu.style.display = 'none';
            }
        });
    });
});

// 7. 구글 번역 코어 인프라 스크립트를 동적으로 안전하게 바인딩
(function() {
    if (!document.getElementById('google-translate-core-script')) {
        var gtScript = document.createElement('script');
        gtScript.id = 'google-translate-core-script';
        gtScript.type = 'text/javascript';
        gtScript.src = 'https://google.com';
        document.body.appendChild(gtScript);
    }
})();
