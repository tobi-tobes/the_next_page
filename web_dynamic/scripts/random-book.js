$(document).ready(function () {
    $('.pick-a-new-random-book').on('click', function () {
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
                    'background-size': 'contain'
                });
            }
        });
    });
});
