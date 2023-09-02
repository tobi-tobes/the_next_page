$(document).ready(function () {
    $(document).on('randomBookReady', function () {
        $('body').on('click', '.randomized-book-cover', function () {
            $('.randomized-book-cover-description').toggleClass("hidden");
            $('.randomized-book-cover-description').toggleClass("randomized-book-description");
        });

        $('body').on('click', '.pick-a-new-random-book', function () {
            /* Make API call to retrieve random book from the database before revealing
            the random book section */
            $.ajax({
                type: GET,
                url: 'http://0.0.0.0:5001/api/v1/books/random/',
                success: function (book) {
                    $('div#random-book').empty()
                    const randomBookItem = `<div class="randomized-book" id="${book.id}"><div class="randomized-book-cover"></div><div class="randomized-book-cover-description hidden"><p>${book.description}</p></div></div>`;
                    $('div#random-book').append(randomBookItem);
                    $(`div#${book.id} .randomized-book-cover`).css({
                        'background-image': `url(${book.cover_image})`,
                        'background-repeat': 'no-repeat',
                        'background-size': 'contain',
                        'background-position': 'center center'
                    });
                    $(document).trigger('randomBookReady');
                }
            });
        });
    });
});
