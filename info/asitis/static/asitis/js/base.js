$('#select_register').on('click', clickSelect);
$('#select_search').on('click', clickSelect);

function clickSelect() {
    $('.select_bar').removeClass('black');
    $(this).addClass('black');
    $('#search_box').css('display', 'block');
    $('#search_btn').css('display', 'flex');

    // select 무엇이 되었는지 구별(족보 등록인지 족보 검색인지)
    if (document.getElementById("select_register").classList.contains("black") === true) {
        $('#select').val('register');
    } else {
        $('#select').val('search');
    };
}


$('#search_btn').on('click', function () {
    if ($("#search").val()) {
        $("#search_form").submit();
    };
});