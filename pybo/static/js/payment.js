// payment.js - PortOne V2 결제 연동 스크립트

document.addEventListener('DOMContentLoaded', function() {
  const paymentForm = document.getElementById('paymentForm');
  const payBtnMain = document.getElementById('btnPayMain');
  const payBtnSidebar = document.getElementById('btnPayComplete');
  const allPayButtons = [payBtnMain, payBtnSidebar].filter(Boolean);

  if (!paymentForm) return;

  const defaultBtnText = payBtnMain ? payBtnMain.innerText.trim() : '결제하기';

  function setButtonsState(disabled, text) {
    allPayButtons.forEach(btn => {
      btn.disabled = disabled;
      if (text) btn.innerText = text;
    });
  }

  /**
   * PortOne V2 결제 요청 함수 (결제 테스트용: 항상 결제 성공 처리)
   * @param {Object} options 파라미터 오버라이드 객체 (선택)
   */
  async function requestPayment(options = {}) {
    const uuid = (typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function')
      ? crypto.randomUUID()
      : `${Date.now()}-${Math.random().toString(36).substring(2, 9)}`;
    const paymentId = options.paymentId || `payment-${uuid}`;
    const totalAmount = options.totalAmount !== undefined ? 1000 :options.totalAmount;
    const orderName = options.orderName || paymentForm.dataset.orderName || "테스트 상품 결제";
    const payMethod = options.payMethod || "CARD";
    // 결제 진행 애니메이션 효과를 위한 짧은 대기 (300ms)
    await new Promise(resolve => setTimeout(resolve, 300));
    // 항상 결제가 정상 승인된 것으로 모의(Mock) 응답 반환
    const response = {
      paymentId: paymentId,
      txId: `tx-${uuid}`,
      status: "PAID"
    };
    console.log('[PortOne Mock] 테스트 결제 정상 승인 완료:', response);
    return { response, paymentId, totalAmount, orderName };
    // UUID 기반 주문별 고유 식별자 설정
    // const storeId = options.storeId 
    //   || paymentForm.dataset.storeId 
    //   || "store-7f00ba71-7aff-42b3-b1e7-2e6e2e19a745";
    // const channelKey = options.channelKey 
    //   || paymentForm.dataset.channelKey 
    //   || "channel-key-8aa7da59-1180-4c4e-9723-ed30e22b7ff4";

    // const uuid = (typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function')
    //   ? crypto.randomUUID()
    //   : `${Date.now()}-${Math.random().toString(36).substring(2, 9)}`;
    // const paymentId = options.paymentId || `payment-${uuid}`;

    // // 정상 결제 금액 산출 (전달받은 옵션값 또는 폼의 data-total-amount 정상 결제 금액 적용)
    // const rawTotalAmount = options.totalAmount !== undefined 
    //   ? options.totalAmount 
    //   : (paymentForm.dataset.totalAmount || document.getElementById('formPaidAmount')?.value);
    // const totalAmount = parseInt(rawTotalAmount, 10) || 0;

    // const orderName = options.orderName || paymentForm.dataset.orderName  || "테스트 상품 결제";
    // const payMethod = options.payMethod || "CARD";

    // const reserverName = paymentForm.dataset.reserverName || '';
    // const reserverPhone = paymentForm.dataset.reserverPhone || '';
    // const reserverEmail = paymentForm.dataset.reserverEmail || '';

    // // PortOne.requestPayment 파라미터 구성
    // const paymentParams = {
    //   storeId: storeId,
    //   channelKey: channelKey,
    //   paymentId: paymentId,
    //   orderName: orderName,
    //   totalAmount: totalAmount,
    //   currency: "KRW",
    //   payMethod: payMethod,
    // };

    // if (reserverName || reserverEmail || reserverPhone) {
    //   paymentParams.customer = {
    //     fullName: reserverName || '고객',
    //     phoneNumber: reserverPhone || undefined,
    //     email: reserverEmail || undefined,
    //   };
    // }

    // console.log('[PortOne] requestPayment 호출 파라미터:', paymentParams);

    // // PortOne V2 결제창 호출
    // const response = await PortOne.requestPayment(paymentParams);
    // return { response, paymentId, totalAmount, orderName };
  }

  // 브라우저 개발자 도구 콘솔 등에서 수동 호출 가능하도록 window에 등록
  window.requestPayment = requestPayment;

  // 폼 제출 이벤트 가로채기 -> PortOne 결제 모달 띄우기
  paymentForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    setButtonsState(true, '결제창을 여는 중입니다...');

    try {
      const { response, paymentId, totalAmount } = await requestPayment();

      console.log('[PortOne] 결제 응답 결과:', response);

      // 결제창 닫힘, 취소 또는 실패 시
      if (response && response.code != null) {
        alert(`결제가 취소되었거나 승인에 실패하였습니다.\n[사유] ${response.message || response.code}`);
        setButtonsState(false, defaultBtnText);
        return;
      }

      // 결제 성공 시
      setButtonsState(true, '결제 승인 완료! 저장 중...');

      const portonePaymentIdEl = document.getElementById('portonePaymentId');
      const portoneTxIdEl = document.getElementById('portoneTxId');
      const formPaidAmountEl = document.getElementById('formPaidAmount');

      if (portonePaymentIdEl) {
        portonePaymentIdEl.value = (response && response.paymentId) ? response.paymentId : paymentId;
      }
      if (portoneTxIdEl) {
        portoneTxIdEl.value = (response && response.txId) ? response.txId : ((response && response.paymentId) ? response.paymentId : paymentId);
      }
      if (formPaidAmountEl) {
        formPaidAmountEl.value = totalAmount;
      }

      // 서버의 /order/pay/complete 로 주문 저장 처리
      paymentForm.submit();

    } catch (error) {
      console.error('[PortOne] 결제 처리 에러:', error);
      alert(`결제 처리 중 오류가 발생했습니다: ${error.message || error}`);
      setButtonsState(false, defaultBtnText);
    }
  });
});
