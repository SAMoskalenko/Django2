window.onload = function () {
    $('.basket_list').on('change', 'input[type="number"]', function (event) {
        var t_href = event.target;

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



    $('.basket_list').on('click', '.product_button_del', function (event) {


        var t_href = event.target;

        if (t_href) {
            $.ajax({
                url: "/basket/ajaxdelete/" + t_href.name + "/",
                success: function (data) {
                    $('.basket_list').html(data['result']);
                    console.log('ajax done');
                },
            });
        }
        event.preventDefault();
    });
}