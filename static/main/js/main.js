$(function () {
    $(".like").submit(function (e) {
        let postId = $(this).attr("id");
        e.preventDefault();

        let serialize = $(this).serialize();
        let url = $(this).data("url");
        $.ajax({
            type: "POST",
            url: url,
            data: serialize,
            beforeSend: function () {
                $(".spinner" + postId).show();
                $("#like_icon" + postId).hide()
                $("#text" + postId).text('');
            },
            complete: function () {
                $(".spinner" + postId).hide();
                $("#like_icon" + postId).show();
                $("#text" + postId).show();
            },
            success: function (response) {
                console.log(response.data);
                $("#like_icon" + postId).toggleClass("far fa-heart fa fa-heart ");
                $("#text" + postId).text(response.data);
            },
        });



    });
});