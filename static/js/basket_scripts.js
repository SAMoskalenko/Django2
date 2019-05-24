window.onload = function () {
    $('.basket_list').on('change', 'input[type="number"]', function () {
        let t_href = event.target;

        if (t_href) {
            $.ajax({
                url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
                success: function (data) {
                    $('.basket_list').html(data.result);
                },
            });
        }
        event.preventDefault();
    });

};