$(document).ready(function () {
    $("#loginbtn").click(function () {
        $.ajax({
            type: "POST",
            url: "127.0.0.1/login",
            data: "{"username":"test","passwd":"test"}",
            success: function (msg) {
                console.log(msg);
            }
        });
    })


})