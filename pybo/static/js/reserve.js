// reserve.js - 예약 페이지 여행객 관리, 금액 계산 및 약관 동의 스크립트

document.addEventListener('DOMContentLoaded', function() {
  const app = document.getElementById('reserveApp');
  if (!app) return;

  const originalPricePerPerson = parseInt(app.dataset.unitOriginalPrice, 10) || 0;
  const discountPerPerson = parseInt(app.dataset.unitDiscount, 10) || 0;
  const finalPricePerPerson = parseInt(app.dataset.unitFinalPrice, 10) || 0;
  let currentHeadcount = parseInt(app.dataset.headcount, 10) || 1;
  const isMember = app.dataset.isMember === 'true';
  const loggedUserName = app.dataset.userName || '';
  const loggedUserPhone = app.dataset.userPhone || '';

  let isSameAsReserver = false; // 대표여행객 = 예약자와 동일 여부

  function getReserverInfo() {
    if (isMember && loggedUserName) {
      return {
        name: loggedUserName,
        phone: loggedUserPhone
      };
    } else {
      const gNameEl = document.getElementById('guest_name');
      const gPhoneEl = document.getElementById('guest_phone');
      const gName = gNameEl ? gNameEl.value.trim() : '';
      const gPhone = gPhoneEl ? gPhoneEl.value.trim() : '';
      return {
        name: gName || '예약자 (미입력)',
        phone: gPhone || '연락처 미입력'
      };
    }
  }

  // 대표여행객 '예약자와 동일' 토글 함수 (전역 window 바인딩)
  window.toggleSameAsReserver = function() {
    isSameAsReserver = !isSameAsReserver;
    renderTravelerForms(currentHeadcount);
  };

  // 인원수 변경 함수 (전역 window 바인딩)
  window.changeHeadcount = function(delta) {
    let newCount = currentHeadcount + delta;
    if (newCount < 1) newCount = 1;
    if (newCount > 20) newCount = 20;
    if (newCount === currentHeadcount) return;

    currentHeadcount = newCount;
    const inputEl = document.getElementById('headcountInput');
    const formCountEl = document.getElementById('formHeadcount');
    const labelCountEl = document.getElementById('labelTravelerCount');

    if (inputEl) inputEl.value = currentHeadcount;
    if (formCountEl) formCountEl.value = currentHeadcount;
    if (labelCountEl) labelCountEl.innerText = currentHeadcount;

    renderTravelerForms(currentHeadcount);
    updateSummary(currentHeadcount);
  };

  // 연관 숙박 선택 상태
  let selectedAccPrice = 0;
  let selectedAccName = '';
  let selectedAccCategory = '';

  // 숙소 카테고리 필터링 (전역 window 바인딩) - 호텔만 또는 민박만 선택
  window.filterAcc = function(category, btn) {
    const tabs = document.querySelectorAll('.btn-acc-tab');
    tabs.forEach(t => {
      t.classList.remove('active', 'btn-primary');
      t.classList.add('btn-outline-primary');
    });

    const activeBtn = btn || document.querySelector(`.btn-acc-tab[data-category="${category}"]`);
    if (activeBtn) {
      activeBtn.classList.add('active', 'btn-primary');
      activeBtn.classList.remove('btn-outline-primary');
    }

    const items = document.querySelectorAll('#accListGrid .acc-item');
    items.forEach(item => {
      const itemCat = item.dataset.category;
      if (itemCat === category) {
        item.style.display = '';
      } else {
        item.style.display = 'none';
      }
    });
  };

  // 숙소 선택 변경 핸들러 (전역 window 바인딩)
  window.handleAccSelect = function(radio) {
    const noneCard = document.getElementById('accCard_none');
    const allCards = document.querySelectorAll('#accListGrid .acc-card');

    if (!radio.value) {
      // 숙소 선택 안 함
      selectedAccPrice = 0;
      selectedAccName = '';
      selectedAccCategory = '';
      if (noneCard) noneCard.classList.add('selected');
      allCards.forEach(c => c.classList.remove('selected'));
    } else {
      // 특정 숙소 선택
      if (noneCard) noneCard.classList.remove('selected');
      allCards.forEach(c => c.classList.remove('selected'));
      const parentCard = radio.closest('.acc-card');
      if (parentCard) parentCard.classList.add('selected');

      selectedAccPrice = parseInt(radio.dataset.price, 10) || 0;
      selectedAccName = radio.dataset.name || '';
      selectedAccCategory = radio.dataset.category || '';
    }

    updateSummary(currentHeadcount);
  };

  // 금액 요약 갱신
  function updateSummary(count) {
    const totalOrig = (originalPricePerPerson * count) + selectedAccPrice;
    const totalDisc = discountPerPerson * count;
    const totalFin = (finalPricePerPerson * count) + selectedAccPrice;

    const summaryOrig = document.getElementById('summaryOriginal');
    if (summaryOrig) summaryOrig.innerText = totalOrig.toLocaleString() + '원';

    const discEl = document.getElementById('summaryDiscount');
    if (discEl) {
      if (isMember) {
        discEl.innerText = '- ' + totalDisc.toLocaleString() + '원';
      } else {
        discEl.innerText = '0원 (비회원 정가)';
      }
    }

    // 숙박 요금 행 표시/숨김
    const accCol = document.getElementById('summaryAccCol');
    const accNameEl = document.getElementById('summaryAccName');
    const accPriceEl = document.getElementById('summaryAccPrice');
    if (accCol && accNameEl && accPriceEl) {
      if (selectedAccPrice > 0) {
        accCol.style.display = 'flex';
        accNameEl.innerText = `[${selectedAccCategory}] ${selectedAccName}`;
        accPriceEl.innerText = `+ ${selectedAccPrice.toLocaleString()}원`;
      } else {
        accCol.style.display = 'none';
      }
    }

    const summaryHeadcount = document.getElementById('summaryHeadcount');
    if (summaryHeadcount) summaryHeadcount.innerText = count + '명';

    const summaryFinal = document.getElementById('summaryFinal');
    if (summaryFinal) summaryFinal.innerText = totalFin.toLocaleString() + '원';
  }

  // 대표 여행객 미리보기 실시간 동기화
  function syncReserverPreview() {
    if (!isSameAsReserver) return;
    const reserver = getReserverInfo();
    const repNameInput = document.getElementById('repTravelerName');
    const repPhoneInput = document.getElementById('repTravelerPhone');

    if (repNameInput && reserver.name) repNameInput.value = reserver.name;
    if (repPhoneInput && reserver.phone) repPhoneInput.value = reserver.phone;
  }

  // 여행객 폼 렌더링
  function renderTravelerForms(count) {
    const container = document.getElementById('travelersContainer');
    if (!container) return;

    const prevNames = Array.from(document.querySelectorAll('input[name="traveler_name[]"]')).map(el => el.value);
    const prevGenders = Array.from(document.querySelectorAll('select[name="traveler_gender[]"]')).map(el => el.value);
    const prevPhones = Array.from(document.querySelectorAll('input[name="traveler_phone[]"]')).map(el => el.value);

    container.innerHTML = '';
    const reserver = getReserverInfo();

    for (let i = 0; i < count; i++) {
      const card = document.createElement('div');
      card.className = 'card shadow-sm border mb-3 rounded-3';
      card.id = `travelerCard_${i + 1}`;

      const isRep = (i === 0);
      const title = isRep ? '여행객 1 (대표 여행자)' : `여행객 ${i + 1}`;
      
      let nameVal = prevNames[i] || '';
      let genderVal = prevGenders[i] || '남';
      let phoneVal = prevPhones[i] || '';

      if (isRep && isSameAsReserver) {
        nameVal = reserver.name || nameVal;
        phoneVal = reserver.phone || phoneVal;
      }

      card.innerHTML = `
        <div class="card-body p-3">
          <!-- 카드 상단 헤더: 대표예약자의 경우 타이틀과 '예약자와 동일' 버튼을 맨 오른쪽에 배치하여 1줄로 구성 -->
          <div class="d-flex justify-content-between align-items-center pb-2 mb-3 border-bottom flex-wrap gap-2">
            <div class="d-flex align-items-center gap-2">
              <span class="fw-bold text-dark fs-6">👤 ${title}</span>
              ${isRep ? `<span class="badge bg-primary-subtle text-primary border border-primary-subtle small">대표자</span>` : ''}
              ${isRep && isSameAsReserver ? `<span class="badge bg-success-subtle text-success border border-success-subtle small">✓ 예약자 정보 적용됨</span>` : ''}
            </div>
            ${isRep ? `
              <div>
                <button type="button" class="btn btn-sm ${isSameAsReserver ? 'btn-primary' : 'btn-outline-primary'} fw-semibold d-inline-flex align-items-center gap-1 shadow-sm" onclick="toggleSameAsReserver()">
                  <span>${isSameAsReserver ? '✓' : '＋'}</span> 예약자와 동일
                </button>
              </div>
            ` : ''}
          </div>

          <!-- 여행객 상세정보 Bootstrap 그리드: 이름 5칸, 성별 2칸, 전화번호 5칸 (총 12칸 1줄) -->
          <div class="row g-2 align-items-end">
            <!-- 이름 5칸 -->
            <div class="col-12 col-md-5">
              <label class="form-label fw-bold small mb-1">이름 <span class="text-danger">*</span></label>
              <input type="text" name="traveler_name[]" value="${nameVal}" required class="form-control bg-white" placeholder="성함"${isRep ? ' id="repTravelerName"' : ''}>
            </div>
            <!-- 성별 2칸 -->
            <div class="col-12 col-md-2">
              <label class="form-label fw-bold small mb-1 text-nowrap">성별 <span class="text-danger">*</span></label>
              <select name="traveler_gender[]" class="form-select text-center bg-white"${isRep ? ' id="repTravelerGender"' : ''}>
                <option value="남" ${genderVal === '남' ? 'selected' : ''}>남</option>
                <option value="여" ${genderVal === '여' ? 'selected' : ''}>여</option>
              </select>
            </div>
            <!-- 전화번호 5칸 -->
            <div class="col-12 col-md-5">
              <label class="form-label fw-bold small mb-1">전화번호 <span class="text-danger">*</span></label>
              <input type="tel" name="traveler_phone[]" value="${phoneVal}" required class="form-control bg-white" placeholder="010-1234-5678"${isRep ? ' id="repTravelerPhone"' : ''}>
            </div>
          </div>
        </div>
      `;

      container.appendChild(card);
    }
  }

  // 비회원 예약자 입력 시 실시간 연동 리스너
  const gNameEl = document.getElementById('guest_name');
  const gPhoneEl = document.getElementById('guest_phone');
  if (gNameEl) gNameEl.addEventListener('input', syncReserverPreview);
  if (gPhoneEl) gPhoneEl.addEventListener('input', syncReserverPreview);

  // 약관 전체 동의 핸들러
  window.handleAgreeAllChange = function(isChecked) {
    const termChecks = document.querySelectorAll('.term-item-check');
    termChecks.forEach(chk => {
      chk.checked = isChecked;
    });
  };

  window.toggleAgreeAll = function(event) {
    if (event.target.tagName.toLowerCase() === 'input') return;
    const agreeAll = document.getElementById('agreeAll');
    if (!agreeAll) return;
    agreeAll.checked = !agreeAll.checked;
    window.handleAgreeAllChange(agreeAll.checked);
  };

  function updateAgreeAllStatus() {
    const termChecks = document.querySelectorAll('.term-item-check');
    const allChecked = Array.from(termChecks).every(chk => chk.checked);
    const agreeAll = document.getElementById('agreeAll');
    if (agreeAll) agreeAll.checked = allChecked;
  }

  const termChecks = document.querySelectorAll('.term-item-check');
  termChecks.forEach(chk => {
    chk.addEventListener('change', updateAgreeAllStatus);
  });

  // 전문보기 토글
  window.toggleDetail = function(detailId) {
    const el = document.getElementById(detailId);
    if (!el) return;
    el.style.display = (el.style.display === 'block') ? 'none' : 'block';
  };

  // 여행 날짜 (오늘 이후 2주일만 가능) 설정 및 유효성 검증
  const travelDateInput = document.getElementById('travel_date');
  if (travelDateInput) {
    const today = new Date();
    const minDate = new Date(today.getFullYear(), today.getMonth(), today.getDate() + 1);
    const maxDate = new Date(today.getFullYear(), today.getMonth(), today.getDate() + 14);

    const pad = (n) => String(n).padStart(2, '0');
    const formatDate = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;

    const minStr = formatDate(minDate);
    const maxStr = formatDate(maxDate);

    travelDateInput.min = minStr;
    travelDateInput.max = maxStr;

    if (!travelDateInput.value || travelDateInput.value < minStr || travelDateInput.value > maxStr) {
      travelDateInput.value = minStr;
    }

    const dateNoticeEl = document.getElementById('dateRangeNotice');
    if (dateNoticeEl) {
      dateNoticeEl.innerText = `${minStr} ~ ${maxStr}`;
    }

    travelDateInput.addEventListener('change', function() {
      if (this.value < minStr || this.value > maxStr) {
        alert(`여행 날짜는 오늘 이후(${minStr})부터 2주일 이내(${maxStr})의 날짜만 선택 가능합니다.`);
        this.value = minStr;
      }
    });
  }

  // 폼 제출 시 필수 약관 및 여행 날짜 유효성 검증
  const form = document.getElementById('reserveForm');
  if (form) {
    form.addEventListener('submit', function(e) {
      if (travelDateInput) {
        const val = travelDateInput.value;
        const minVal = travelDateInput.min;
        const maxVal = travelDateInput.max;
        if (!val || val < minVal || val > maxVal) {
          e.preventDefault();
          alert(`여행 날짜는 오늘 이후(${minVal})부터 2주일 이내(${maxVal})의 날짜만 선택 가능합니다.`);
          travelDateInput.focus();
          return;
        }
      }

      const requiredTerms = document.querySelectorAll('.term-required');
      let allRequiredChecked = true;
      let firstUnchecked = null;

      requiredTerms.forEach(chk => {
        if (!chk.checked) {
          allRequiredChecked = false;
          if (!firstUnchecked) firstUnchecked = chk;
        }
      });

      if (!allRequiredChecked) {
        e.preventDefault();
        alert('필수 약관(국내여행 특별약관, 개인정보 제3자 제공동의, 민감정보 수집 및 이용 동의)에 모두 동의하셔야 결제를 진행하실 수 있습니다.');
        if (firstUnchecked) {
          firstUnchecked.focus();
          const termsSection = document.getElementById('termsSection');
          if (termsSection) {
            termsSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
      }
    });
  }

  // 초기 실행
  renderTravelerForms(currentHeadcount);
  updateSummary(currentHeadcount);
});

