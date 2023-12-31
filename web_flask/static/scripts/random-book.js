$(document).ready(function () {
    $(document).on('randomBookReady', function () {
        /* Reveal book description when book cover is clicked */
	$('body').off('click', '.randomized-book-cover')
        $('body').on('click', '.randomized-book-cover', function () {
            $('.randomized-book-cover-description').toggleClass("hidden");
            $('.randomized-book-cover-description').toggleClass("randomized-book-description");
        });

	$('body').off('click', '.pick-a-new-random-book');
        $('body').on('click', '.pick-a-new-random-book', function () {
            /* Make API call to retrieve random book from the database before revealing the random book section */
	    console.log("Got a new random book");
            $.ajax({
                type: 'GET',
                url: 'http://54.82.111.149:5001/api/v1/books/random/',
                success: function (book) {
                    $('.randomized-book').remove()
		    $('.pick-a-new-random-book').remove()
                    const randomBookItem = `<div class="randomized-book" id="${book.id}"><div class="randomized-book-cover"></div><div class="randomized-book-cover-description hidden"><h3>${book.title}</h3><h4>${book.author}</h4><p>${book.description}</p></div></div>`;
                    $('#random-book').append(randomBookItem);
                    $(`#random-book #${book.id} .randomized-book-cover`).css({
                        'background-image': `url(${book.cover_image})`,
                        'background-repeat': 'no-repeat',
                        'background-size': 'contain',
                        'background-position': 'center center'
                    });
		    $('#random-book').append('<button class="pick-a-new-random-book"><a href="#random-book">Pick a new random book!</a></button>');
                    $(document).trigger('randomBookReady');
                }
            });
        });
    });
});
