document.addEventListener("DOMContentLoaded", function() {
    const signupBtn = document.querySelector('.signup-button');
    const passwordInput = document.getElementById('password');
    const passwordViewBtn = document.getElementById('passwordView');
    const btnSubmitFindId = document.getElementById('btnSubmitFindId');
    const btnSubmitFindPw = document.getElementById('btnSubmitFindPw');

    const loginForm = document.querySelector('.login-form');
    const userIdInput = document.getElementById('user_id');
    const rememberIdCheckbox = document.getElementById('remember_id');

    const csrfInput = document.querySelector('input[name="csrf_token"]');
    const csrfToken = csrfInput ? csrfInput.value : '';

    const savedUserId = localStorage.getItem('saved_user_id');
    if (savedUserId && userIdInput) {
        userIdInput.value = savedUserId;
        if (rememberIdCheckbox) {
            rememberIdCheckbox.checked = true;
        }
    }

    if (loginForm) {
        loginForm.addEventListener('submit', function() {
            if (rememberIdCheckbox && rememberIdCheckbox.checked && userIdInput) {
                // 체크박스가 켜져 있다면 입력한 아이디를 브라우저에 안전하게 고정 보관
                localStorage.setItem('saved_user_id', userIdInput.value.trim());
            } else {
                // 체크박스가 꺼져 있다면 기존에 보관 중이던 기록을 파기
                localStorage.removeItem('saved_user_id');
            }
        });
    }

    window.openSignupPopup = function(e, el) {
        if (e) e.preventDefault();
        const href = (el && el.href) ? el.href : (signupBtn ? signupBtn.href : '/auth/signup/');
        const popupWidth = 460;
        const popupHeight = 580;
        const left = window.screenX + (window.outerWidth - popupWidth) / 2;
        const top = window.screenY + (window.outerHeight - popupHeight) / 2;
        const windowFeatures = `width=${popupWidth},height=${popupHeight},left=${left},top=${top},scrollbars=yes,resizable=yes`;
        window.open(href, "SignupPopup", windowFeatures);
    };

    if (signupBtn) {
        signupBtn.addEventListener('click', function(e) {
            window.openSignupPopup(e, this);
        });
    }

    if (passwordViewBtn && passwordInput) {
        passwordViewBtn.addEventListener('click', function() {
            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                this.style.color = "#1D3557";
            } else {
                passwordInput.type = "password";
                this.style.color = "#999999";
            }
        });
    }

    if (btnSubmitFindId) {
        btnSubmitFindId.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            const nameVal = document.getElementById('find_id_name').value.trim();
            const emailVal = document.getElementById('find_id_email').value.trim();
            const messageEl = document.getElementById('findIdMessage');

            if (!nameVal || !emailVal) {
                alert('이름과 이메일을 모두 입력해 주세요.');
                return;
            }

            messageEl.style.color = "orange";
            messageEl.innerText = "⏳ 데이터베이스 조회 중...";

            const targetUrl = (btnSubmitFindId && btnSubmitFindId.dataset.url) || window.findIdUrl || '/auth/find_id';
            fetch(targetUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json", "X-CSRFToken": csrfToken },
                body: JSON.stringify({ name: nameVal, email: emailVal })
            })
            .then(res => res.json())
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
                messageEl.style.color = "red";
                messageEl.innerText = "✕ 서버 통신 에러가 발생했습니다.";
            });
        });
    }

    if (btnSubmitFindPw) {
        btnSubmitFindPw.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            const idVal = document.getElementById('find_pw_id').value.trim();
            const emailVal = document.getElementById('find_pw_email').value.trim();
            const messageEl = document.getElementById('findPwMessage');

            if (!idVal || !emailVal) {
                alert('아이디와 이메일을 모두 입력해 주세요.');
                return;
            }

            messageEl.style.color = "orange";
            messageEl.innerText = "⏳ 임시 비밀번호 발급 및 메일 전송 중...";

            const targetUrl = (btnSubmitFindPw && btnSubmitFindPw.dataset.url) || window.findPwUrl || '/auth/find_pw';
            fetch(targetUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json", "X-CSRFToken": csrfToken },
                body: JSON.stringify({ user_id: idVal, email: emailVal })
            })
            .then(res => res.json())
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
                messageEl.style.color = "red";
                messageEl.innerText = "✕ 서버 통신 에러가 발생했습니다.";
            });
        });
    }

    const modalTriggerPairs = [
        { open: 'openFindId', close: 'closeFindId', modal: 'findIdModal' },
        { open: 'openFindPw', close: 'closeFindPw', modal: 'findPwModal' },
        { open: 'openTerms',  close: 'closeTerms',  modal: 'termsModal' }
    ];

    modalTriggerPairs.forEach(pair => {
        const openBtn = document.getElementById(pair.open);
        const closeBtn = document.getElementById(pair.close);
        const targetModal = document.getElementById(pair.modal);

        if (openBtn && targetModal) {
            openBtn.addEventListener('click', function(e) {
                e.preventDefault();

                if (pair.modal === 'findIdModal') {
                    if (document.getElementById('find_id_name')) document.getElementById('find_id_name').value = '';
                    if (document.getElementById('find_id_email')) document.getElementById('find_id_email').value = '';
                    if (document.getElementById('findIdMessage')) document.getElementById('findIdMessage').innerText = '';
                } else if (pair.modal === 'findPwModal') {
                    if (document.getElementById('find_pw_id')) document.getElementById('find_pw_id').value = '';
                    if (document.getElementById('find_pw_email')) document.getElementById('find_pw_email').value = '';
                    if (document.getElementById('findPwMessage')) document.getElementById('findPwMessage').innerText = '';
                }

                targetModal.classList.add('active');
            });
        }

        if (closeBtn && targetModal) {
            closeBtn.addEventListener('click', function() {
                targetModal.classList.remove('active');
            });
        }

        if (targetModal) {
            targetModal.addEventListener('click', function(e) {
                if (e.target === targetModal) {
                    targetModal.classList.remove('active');
                }
            });
        }
    });
});