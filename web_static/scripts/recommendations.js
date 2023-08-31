$(document).ready(function () {
    const savedBooksForBookshelf = [];

    $('.book-cover').on('click', function () {
        $('.book-cover-description').toggleClass("hidden");
        $('.book-cover-description').toggleClass("book-description");
    });

    $('.recommended-book .options .like').on('click', function () {
        const grandparentID = $(this).closest('.recommended-book').attr('id');
        if(!savedBooksForBookshelf.includes(grandparentID)) {
            savedBooksForBookshelf.push(grandparentID);
            $(this).css('opacity', 0.5);
        } else {
            const index = savedBooksForBookshelf.indexOf(grandparentID);
            savedBooksForBookshelf.splice(index, 1);
            $(this).css('opacity', 1);
        }
    });

    $('.recommended-book .options .not-like').on('click', function () {
        const grandparentID = $(this).closest('.recommended-book').attr('id');
        $('#' + grandparentID).animate({ opacity: 0 }, 500, function() {
            $('#' + grandparentID).remove();
        });
        if(savedBooksForBookshelf.includes(grandparentID)) {
            const index = savedBooksForBookshelf.indexOf(grandparentID);
            savedBooksForBookshelf.splice(index, 1);
        }
    });

    $('.view-your-bookshelf').on('click', function () {
        /* Using the savedBooksForBookshelf arrays, make API call to genres table to populate the
        bookshelf section before revealing the section as below */
        if($('#bookshelf').hasClass("hidden")) {
            $('#bookshelf').removeClass("hidden");
            $('#bookshelf').addClass("bookshelf-section");
        }
    });
});
