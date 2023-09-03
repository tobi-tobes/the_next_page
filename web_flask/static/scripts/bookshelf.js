$(document).ready(function () {
    $(document).on('bookshelfReady', function () {
	$('body').off('click', '.bookshelf-book-cover');
        $('body').on('click', '.bookshelf-book-cover', function () {
            const bookDescription = $(this).siblings('.bookshelf-book-cover-description');
            bookDescription.toggleClass("hidden");
            bookDescription.toggleClass("bookshelf-book-description");
	    console.log('book clicked');
        });

	$('body').off('click', '.bookshelf-book .options .remove');

        $('.bookshelf-book .options .remove').on('click', function () {
            const grandparentID = $(this).closest('.bookshelf-book').attr('id');
            $('#' + grandparentID).animate({ opacity: 0 }, 500, function() {
                $('#' + grandparentID).remove();
            });
        });

        $('body').on('click', '.get-new-recommendations', function () {
            if($('#recommendations').hasClass("recommendations-section")) {
                $('#recommendations').removeClass("recommendations-section");
                $('#recommendations').addClass("hidden");
            }
            if($('#bookshelf').hasClass("bookshelf-section")) {
                $('#bookshelf').removeClass("bookshelf-section");
                $('#bookshelf').addClass("hidden");
            }
        });

        $('body').on('click', '.download-your-bookshelf', generatePDF);

        function generatePDF() {
            const { jsPDF } = window.jspdf;
            const pdf = new jsPDF();

	    let left = 20;
	    let top = 20;
	    let lineHeight = 10;

	    const bookshelfBooks = document.querySelectorAll('.bookshelf-book');

	    bookshelfBooks.forEach(function(book, index) {
		const title = book.querySelector('h3').textContent;
		const author = book.querySelector('h4').textContent;
		const description = book.querySelector('p').textContent;

		pdf.text(title, left, top);
		top += lineHeight;

		pdf.text(author, left, top);
		top += lineHeight;

		pdf.text(description, left, top, { maxWidth: 170 });
		let textHeight = pdf.getTextDimensions(description, { maxWidth: 170 }).h;
		top += textHeight + lineHeight;

		if(index < bookshelfBooks.length - 1) {
		    top += lineHeight;
		    pdf.line(left, top, 210 - left, top);
		}
	    });
	    pdf.save('my-bookshelf.pdf');
	}
    });
});
