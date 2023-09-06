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

	$('body').off('click', '.download-your-bookshelf');
	$('body').on('click', '.download-your-bookshelf', generatePDF);

        function generatePDF() {
            const { jsPDF } = window.jspdf;
            const pdf = new jsPDF();

	    let left = 30;
	    let top = 30;
	    let lineHeight = 10;
	    let pageHeight = 297;
	    let pageWidth = 210;

	    const bookshelfBooks = document.querySelectorAll('.bookshelf-book');
	    pdf.setFontSize(20);
	    pdf.setFont('helvetica', 'bold');
	    pdf.text("Your Bookshelf:", 20, 10);

	    pdf.setFontSize(16);
	    pdf.setFont('helvetica', 'normal');

	    bookshelfBooks.forEach(function(book, index) {
		const title = book.querySelector('h3').textContent;
		const author = book.querySelector('h4').textContent;
		const description = book.querySelector('p').textContent;

		if(top + lineHeight * 5 > pageHeight) {
		    pdf.addPage();
		    top = 30;
		}

		pdf.text(title, left, top);
		top += lineHeight;

		pdf.text(author, left, top);
		top += lineHeight;

		pdf.text(description, left, top, { maxWidth: pageWidth - left * 2 });
		let textHeight = pdf.getTextDimensions(description, { maxWidth: pageWidth - left * 2 }).h;
		top += textHeight + lineHeight;

		if(index < bookshelfBooks.length - 1) {
		    top += lineHeight;
		    pdf.line(left, top, pageWidth - left, top);
		}
	    });
	    pdf.save('my-bookshelf.pdf');
	}
    });
});
