// 스와이퍼
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

// 추천
document.addEventListener("DOMContentLoaded", function () {
    const likeBtn = document.getElementById('like-btn');
    const logHeartBtn = document.querySelector('.log_heart');
    const heartTextEl = document.getElementById('heart');

    if (!heartTextEl) return;

    function getProductId() {
        const pathParts = window.location.pathname.split('/');
        const id = pathParts[pathParts.length - 1];
        return parseInt(id, 10) || 1;
    }

    const productId = getProductId();

    function updateCountUI(newCount, status) {
        heartTextEl.innerHTML = `❤️ ${newCount.toLocaleString()}명이 추천했습니다! 이 상품이 마음에 들면 추천해주세요.`;

        if (status === 'liked') {
            if (likeBtn) { likeBtn.innerHTML = '♥'; likeBtn.classList.add('active'); }
            if (logHeartBtn) { logHeartBtn.textContent = '추천완료 ❤️'; logHeartBtn.classList.add('active'); }
        } else if (status === 'canceled') {
            if (likeBtn) { likeBtn.innerHTML = '♡'; likeBtn.classList.remove('active'); }
            if (logHeartBtn) { logHeartBtn.textContent = '추천하기'; logHeartBtn.classList.remove('active'); }
        }
    }

    function handleLikeClick(e) {
        if (logHeartBtn && logHeartBtn.hasAttribute('onclick')) {
            e.preventDefault();
            e.stopPropagation();
            return;
        }

        fetch('/product/sub_product/like', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ product_id: productId })
})

            .then(response => response.json())
            .then(data => {
                if (data && data.success) {
                    updateCountUI(data.recommendation_count, data.status);
                    if (data.status === 'liked') {
                        alert("추천되었습니다!");
                    } else {
                        alert("추천을 취소했습니다.");
                    }
                } else {
                    alert("추천 처리 중 오류가 발생했습니다.");
                }
            })

            .catch(error => {
                console.error("에러 발생:", error);
                alert("서버 연결에 실패했습니다.");
            });
    }

    if (likeBtn) likeBtn.addEventListener('click', handleLikeClick);
    if (logHeartBtn) logHeartBtn.addEventListener('click', handleLikeClick);
});

// 링크 복사
document.querySelector('#copy-btn').addEventListener('click', function() {
    const currentUrl = window.location.href;

    navigator.clipboard.writeText(currentUrl).then(() => {
        alert("링크가 복사되었습니다!");
    }).catch(err => {
        console.error("복사 실패:", err);
    });
});