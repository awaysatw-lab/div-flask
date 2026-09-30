document.addEventListener("DOMContentLoaded", function () {

    const password =
        document.getElementById("password");

    const passwordView =
        document.getElementById("passwordView");


    if (password && passwordView) {

        passwordView.addEventListener("click", function () {

            if (password.type === "password") {

                password.type = "text";

                passwordView.textContent = "○";

            } else {

                password.type = "password";

                passwordView.textContent = "◉";

            }

        });

    }

});

function openSignupPopup() {
    var popupUrl = "{{ url_for('pybo.signup') if url_for else 'signup.html' }}";
    var options = "width=500,height=750,top=100,left=200,scrollbars=yes,resizable=no";
    window.open(popupUrl, "SignupPopup", options);
}
