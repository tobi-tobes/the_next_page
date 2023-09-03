$(document).ready(function () {
    const savedBooksForBookshelf = [];
    $(document).on('recommendationsReady', function () {
	$('body').off('click', '.book-cover')
	$('body').on('click', '.book-cover', function () {
	    const bookDescription = $(this).siblings('.book-cover-description');
	    bookDescription.toggleClass("hidden");
	    bookDescription.toggleClass("book-description");
	    console.log('book cover clicked');
	});

	$('body').off('click','.recommended-book .options .like')
        $('body').on('click','.recommended-book .options .like', function () {
            const grandparentID = $(this).closest('.recommended-book').attr('id');
            if(!savedBooksForBookshelf.includes(grandparentID)) {
                savedBooksForBookshelf.push(grandparentID);
                $(this).css('opacity', 0.5);
		console.log('hearted');
            } else {
                const index = savedBooksForBookshelf.indexOf(grandparentID);
                savedBooksForBookshelf.splice(index, 1);
                $(this).css('opacity', 1);
		console.log('unhearted');
            }
        });

	$('body').off('click', '.recommended-book .options .not-like')
        $('body').on('click', '.recommended-book .options .not-like', function () {
            const grandparentID = $(this).closest('.recommended-book').attr('id');
            $('#' + grandparentID).animate({ opacity: 0 }, 500, function() {
                $('#' + grandparentID).remove();
		console.log('removed');
            });
            if(savedBooksForBookshelf.includes(grandparentID)) {
                const index = savedBooksForBookshelf.indexOf(grandparentID);
                savedBooksForBookshelf.splice(index, 1);
            }
        });

        $('body').on('click', '.view-your-bookshelf', function () {
            /* Using the savedBooksForBookshelf arrays, make API call to genres table to populate the
            bookshelf section before revealing the section as below */
            $.ajax({
                type: 'POST',
                url: 'http://0.0.0.0:5001/api/v1/books/',
                data: JSON.stringify({ book_ids: savedBooksForBookshelf }),
                contentType: 'application/json',
                success: function (bookshelf) {
                    $('div.bookshelf-books').empty()
		    console.log('bookshelf emptied');
                    $.each(bookshelf, function(index, element) {
                        const bookshelfBookItem = `<div class="bookshelf-book" id="${element.id}"><div class="bookshelf-book-cover"></div><div class="bookshelf-book-cover-description hidden"><p>${element.description}</p></div><div class="options"><div class="remove"></div></div></div>`;
                        $('div.bookshelf-books').append(bookshelfBookItem);
                        $(`div#${element.id} .bookshelf-book-cover`).css({
                            'background-image': `url(${element.cover_image})`,
                            'background-repeat': 'no-repeat',
                            'background-size': 'contain',
                            'background-position': 'center center'
                        });
                    });
                    $(document).trigger('bookshelfReady');
		    $('body').off('click', '.book-cover');
		    $('body').off('click', '.recommended-book .options .like');
		    $('body').off('click', '.recommended-book .options .not-like');
		    savedBooksForBookshelf.splice(0, savedBooksForBookshelf.length);
		    console.log(`${savedBooksForBookshelf}`);
                }
            });
            if($('#bookshelf').hasClass("hidden")) {
                $('#bookshelf').removeClass("hidden");
                $('#bookshelf').addClass("bookshelf-section");
            }
        });
    });
});
