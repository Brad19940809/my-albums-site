function xx() {
    $.ajax({
        url: "/captcha/refresh/",
        type: "GET",
        // 此处不用加headers，因为不知为何，ajax有自动加XMLrequest
        success: function (data) {
            console.log(data.key)
            document.getElementById("img1").src=data.image_url

            // $.ajax({
            //     url: data.image_url,
            //     success: function (data) {
            //         document.getElementById("img1").src=data.toString()
            //     }
            // })
        },
        error: function (xhr) {
            alert(xhr.status)
        }
    })
}
