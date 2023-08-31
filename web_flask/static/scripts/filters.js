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
            $.ajax({
                type: GET,
                url: 'http://0.0.0.0.5001/api/v1/genres/' + $(this).data('name'),
                success: function (topics) {
                    $.each(topics, function(index, element) {
                        const topicItem = `<li class="popover-option ${element.parent_genre}"><input type="checkbox" data-id=${element.id}>${element.name}</li>`;
                        $('div.topic-filters ul').append(topicItem);
                    });
                }
            });
        } else {
            const index = checkedGenres.indexOf($(this).data('name'));
            checkedGenres.splice(index, 1);
            $('li.' + $(this).data('name')).remove();
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
        $.ajax({
            type: POST,
            url: 'http://0.0.0.0.5001/api/v1/recommended_books/',
            data: JSON.stringify({ age_categories: checkedAgeCategories, book_lengths: checkedBookLengths, genres: checkedTopics }),
            contentType: 'application/json',
            success: function (recommendedBooks) {
                $('div.recommended-books').empty()
                $.each(recommendedBooks, function(index, element) {
                    const recommendedBookItem = `<div class="recommended-book" id="${element.id}"><div class="book-cover"></div><div class="book-cover-description hidden"><p>${element.description}</p></div><div class="options"><div class="like"></div><div class="not-like"></div></div></div>`;
                    $('div.recommended-books').append(recommendedBookItem);
                    $(`div#${element.id} .book-cover`).css({
                        'background-image': `url(${element.cover_image})`,
                        'background-repeat': 'no-repeat',
                        'background-size': 'contain',
                        'background-position': 'center center'
                    });
                });
            }
        });
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
        $.ajax({
            type: GET,
            url: 'http://0.0.0.0.5001/api/v1/random/',
            success: function (book) {
                $('div#random-book').empty()
                const randomBookItem = `<div class="randomized-book" id="${book.id}"><div class="randomized-book-cover"></div><div class="randomized-book-description hidden"><p>${book.description}</p></div></div>`;
                $('div#random-book').append(randomBookItem);
                $(`div#${book.id} .randomized-book-cover`).css({
                    'background-image': `url(${book.cover_image})`,
                    'background-repeat': 'no-repeat',
                    'background-size': 'contain',
                    'background-position': 'center center'
                });
            }
        });
        if($('#random-book').hasClass("hidden")) {
            $('#random-book').removeClass("hidden");
            $('#random-book').addClass("random-book-section");
        }
    });
});
