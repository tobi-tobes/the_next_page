$(document).ready(function () {
    $('.bookshelf-book-cover').on('click', function () {
        $('.bookshelf-book-cover-description').toggleClass("hidden");
        $('.bookshelf-book-cover-description').toggleClass("bookshelf-book-description");
    });

    $('.bookshelf-book .options .remove').on('click', function () {
        const grandparentID = $(this).closest('.bookshelf-book').attr('id');
        $('#' + grandparentID).animate({ opacity: 0 }, 500, function() {
            $('#' + grandparentID).remove();
        });
    });

    $('.get-new-recommendations').on('click', function () {
        if($('#recommendations').hasClass("recommendations-section")) {
            $('#recommendations').removeClass("recommendations-section");
            $('#recommendations').addClass("hidden");
        }
        if($('#bookshelf').hasClass("bookshelf-section")) {
            $('#bookshelf').removeClass("bookshelf-section");
            $('#bookshelf').addClass("hidden");
        }
    });

    $('.download-your-bookshelf').on('click', generatePDF);

    function generatePDF() {
        const { jsPDF } = window.jspdf;
        const pdf = new jsPDF();
        const content = document.querySelector('.bookshelf-books');

        pdf.html(content, {
            callback: function(pdf) {
                // Save the PDF
                pdf.save('my_bookshelf.pdf');
            },
            x: 15,
            y: 15,
            width: 170, //target width in the PDF document
            windowWidth: 650 //window width in CSS pixels
        });
    }
});
