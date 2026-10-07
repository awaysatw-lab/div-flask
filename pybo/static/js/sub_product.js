var swiper = new Swiper('.mySwiper', {
        spaceBetween: 10,
        slidesPerView: 4,
        freeMode: true,
        watchSlidesProgress: true,
      });
      var swiper2 = new Swiper('.mySwiper2', {
        spaceBetween: 10,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
        thumbs: {
          swiper: swiper,
        },
      });



document.addEventListener("DOMContentLoaded", function () {
    // 1. 필요한 모든 요소들을 가져옵니다.
    const likeBtn = document.getElementById('like-btn');
    const logHeartBtn = document.querySelector('.log_heart');
    const heartTextEl = document.getElementById('heart');

    if (!heartTextEl) return; // 오류 방지 안전장치

    let isLiked = false;

    // 💡 두 버튼의 상태(텍스트, 스타일)를 동시에 업데이트하는 함수
    function updateButtons(liked, newCount) {
        // 상단 텍스트 업데이트
        heartTextEl.innerHTML = `❤️ ${newCount.toLocaleString()}명이 추천했습니다!`;

        if (liked) {
            // [추천 완료 상태 일괄 적용]
            if (likeBtn) {
                likeBtn.innerHTML = '♥';
                likeBtn.classList.add('active');
            }
            if (logHeartBtn) {
                logHeartBtn.textContent = '추천완료 ❤️';
                logHeartBtn.classList.add('active');
            }
        } else {
            // [추천 취소 상태 일괄 적용]
            if (likeBtn) {
                likeBtn.innerHTML = '♡';
                likeBtn.classList.remove('active');
            }
            if (logHeartBtn) {
                logHeartBtn.textContent = '추천하기';
                logHeartBtn.classList.remove('active');
            }
        }
    }

    // 💡 클릭 시 실행할 추천/취소 연산 핵심 로직
    function handleLikeClick() {
        const match = heartTextEl.textContent.match(/[0-9,]+/);
        if (!match) return;
        let currentCount = parseInt(match[0].replace(/,/g, ''), 10);

        if (!isLiked) {
            let newCount = currentCount + 1;
            isLiked = true;
            updateButtons(true, newCount);
            alert("추천되었습니다!");
        } else {
            let newCount = currentCount - 1;
            isLiked = false;
            updateButtons(false, newCount);
            alert("추천을 취소했습니다.");
        }
    }

    // 2. 두 버튼 모두에 각각 클릭 이벤트를 연결합니다.
    if (likeBtn) {
        likeBtn.addEventListener('click', handleLikeClick);
    }
    if (logHeartBtn) {
        logHeartBtn.addEventListener('click', handleLikeClick);
    }
});

document.querySelector('#copy-btn').addEventListener('click', function() {
    // 현재 웹사이트의 전체 주소(URL)를 가져옵니다.
    const currentUrl = window.location.href;

    // 브라우저 클립보드에 주소 복사 실행
    navigator.clipboard.writeText(currentUrl).then(() => {
        // 복사가 성공했을 때 알림(Alert) 띄우기
        alert("링크가 복사되었습니다!");
    }).catch(err => {
        // 구형 브라우저나 일부 환경에서 에러 발생 시 예외 처리
        console.error("복사 실패:", err);
    });
});