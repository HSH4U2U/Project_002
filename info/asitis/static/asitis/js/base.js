$('#select_register').on('click', clickSelect);
$('#select_search').on('click', clickSelect);

// select bar 클릭
function clickSelect() {
    $('.select_bar').removeClass('black');
    $(this).addClass('black');
    $('#search_box').css('display', 'block');
    selectWhat()
}

// select 무엇이 되었는지 구별(족보 등록인지 족보 검색인지)
function selectWhat() {
    if (document.getElementById("select_register").classList.contains("black") === true) {
        $('#select').val('register');
    } else {
        $('#select').val('search');
    }
}


// 검색창 클릭 효과 구현
$('#search_form').on('click', function () {
    $(this).animate({
        width: "90%",
    });
    $(this).css('text-align', 'left');
    setTimeout(function () {
        $('#search_btn').fadeIn(1000);
    }, 500);
});

// 검색 기능 구현
$('#search_btn').on('click', function () {
    selectWhat();
    if ($("#search").val()) {
        $("#search_form").submit();
    }
});
