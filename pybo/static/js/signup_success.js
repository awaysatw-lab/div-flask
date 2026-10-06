/**
 * 회원가입 완료 팝업 처리 스크립트
 */
(function() {
    alert("회원가입이 성공적으로 완료되었습니다! 🎉");
    const redirectUrl = (document.body && document.body.dataset.redirectUrl) || '/';
    if (window.opener && !window.opener.closed) {
        window.opener.location.href = redirectUrl;
        window.close();
    } else {
        window.location.href = redirectUrl;
    }
})();
