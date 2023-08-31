$(document).ready(function () {
    const checkedGenres = [];
    const checkedTopics = [];
    const checkedBookLengths = [];
    const checkedAgeCategories = [];

    $('.genre-filters input[type="checkbox"]').change(function () {
        if($(this).is(':checked')) {
            checkedGenres.push($(this).data('name'));
            /* Using the checkedGenres array, API call to genres table to populate the
            topic-filters dropdown menu */
        } else {
            const index = checkedGenres.indexOf($(this).data('name'));
            checkedGenres.splice(index, 1);
        }
    });

    $('.topic-filters input[type="checkbox"]').change(function () {
        if($(this).is(':checked')) {
            checkedTopics.push($(this).data('id'));
        } else {
            const index = checkedTopics.indexOf($(this).data('id'));
            checkedTopics.splice(index, 1);
        }
    });

    $('.age-category-filters input[type="checkbox"]').change(function () {
        if($(this).is(':checked')) {
            checkedAgeCategories.push($(this).data('name'));
        } else {
            const index = checkedAgeCategories.indexOf($(this).data('name'));
            checkedAgeCategories.splice(index, 1);
        }
    });

    $('.book-length-filters input[type="checkbox"]').change(function () {
        if($(this).is(':checked')) {
            checkedBookLengths.push($(this).data('name'));
        } else {
            const index = checkedBookLengths.indexOf($(this).data('name'));
            checkedBookLengths.splice(index, 1);
        }
    });

    $('.get-your-recommendations').on('click', function () {
        /* Using the checkedTopics, checkedBookLengths, and checkedAgeCategories arrays,
        API call to genres table to populate the recommendations section before revealing
        the section as below */
        if($('#recommendations').hasClass("hidden")) {
            $('#recommendations').removeClass("hidden");
            $('#recommendations').addClass("recommendations-section");
        }
        if($('#random-book').hasClass("random-book-section")) {
            $('#random-book').removeClass("random-book-section");
            $('#random-book').addClass("hidden");
        }
    });

    $('.pick-a-random-book').on('click', function () {
        /* Make API call to retrieve random book from the database before revealing
        the random book section */
        if($('#random-book').hasClass("hidden")) {
            $('#random-book').removeClass("hidden");
            $('#random-book').addClass("random-book-section");
        }
    });
});
