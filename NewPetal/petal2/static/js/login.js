var pass = document.querySelector("#password");
var icon = document.querySelector("#eyeicon");

icon.addEventListener('click', function () {
    if (pass.type === "password") {
        pass.type = "text";
        icon.src = "/static/images/eye-open.png";
    } else {
        pass.type = "password";
        icon.src = "/static/images/eye-close.png";
    }
});
