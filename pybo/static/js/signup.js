document.addEventListener("DOMContentLoaded", function() {
    const btnCheckId = document.getElementById('btnCheckId');
    const userIdInput = document.getElementById('user_id');
    const messageEl = document.getElementById('idCheckMessage');
    const btnGoToLogin = document.getElementById('btnGoToLogin');


    if (btnCheckId) {
        btnCheckId.addEventListener('click', function(e) {
            e.preventDefault();
            const userId = userIdInput.value.trim();

            if (!userId) {
                alert('아이디를 먼저 입력해 주세요.');
                return;
            }

            const requestUrl = window.checkIdUrl || '/auth/check_id';
            const csrfInput = document.getElementById('csrf_token');
            const csrfToken = csrfInput ? csrfInput.value : '';

            messageEl.style.color = "orange";
            messageEl.innerText = "⏳ 중복 확인 중...";

            fetch(requestUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRF-Token": csrfToken
                },
                body: JSON.stringify({ user_id: userId })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`서버 연결 실패 (상태코드: ${response.status})`);
                }
                return response.json();
            })
            .then(data => {
                if (data.status === 'success') {
                    messageEl.style.color = "green";
                    messageEl.innerText = "✓ " + data.message;
                } else {
                    messageEl.style.color = "red";
                    messageEl.innerText = "✕ " + data.message;
                }
            })
            .catch(err => {
                console.error("비동기 중복확인 통신 에러 상세:", err);
                messageEl.style.color = "red";
                messageEl.innerText = "✕ 서버 통신 에러가 발생했습니다.";
                alert(`중복 확인 요청 중 서버 에러가 발생했습니다.\n에러 내용: ${err.message}`);
            });
        });
    }

    if (userIdInput) {
        userIdInput.addEventListener('input', function() {
            messageEl.innerText = "";
        });
    }

    const toggleIcons = document.querySelectorAll('.toggle-password');
    toggleIcons.forEach(icon => {
        icon.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const passwordInput = document.getElementById(targetId);

            if (passwordInput && passwordInput.type === "password") {
                passwordInput.type = "text";
                this.classList.replace("fa-regular", "fa-solid");
            } else if (passwordInput) {
                passwordInput.type = "password";
                this.classList.replace("fa-solid", "fa-regular");
            }
        });
    });

    if (btnGoToLogin) {
        btnGoToLogin.addEventListener('click', function() {
            if (window.opener && !window.opener.closed) {
                window.opener.focus();
            }
            window.close();
        });
    }
});
