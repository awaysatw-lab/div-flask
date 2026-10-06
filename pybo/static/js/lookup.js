// lookup.js - 예약 확인 및 조회 인터랙션 스크립트

/**
 * 로그인 회원 예약 목록에서 특정 주문 상세 아코디언 토글 함수
 * @param {string} orderNo 주문번호
 */
function toggleOrderDetail(orderNo) {
  const detailEl = document.getElementById(`detailWrap_${orderNo}`);
  const btnEl = document.getElementById(`expandBtn_${orderNo}`);
  if (!detailEl) return;

  const isHidden = (detailEl.style.display === 'none' || !detailEl.style.display);

  if (isHidden) {
    detailEl.style.display = 'block';
    if (btnEl) btnEl.innerHTML = '상세 정보 <span>▲</span>';
    // 부드럽게 스크롤
    setTimeout(() => {
      detailEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 50);
  } else {
    detailEl.style.display = 'none';
    if (btnEl) btnEl.innerHTML = '상세 정보 <span>▼</span>';
  }
}

// 전역 윈도우 객체 바인딩
window.toggleOrderDetail = toggleOrderDetail;

