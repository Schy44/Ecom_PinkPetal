
$(document).ready(function () {
    $('input[type="number"]').on('input', function () {
        var quantity = parseFloat($(this).val());
        var price = parseFloat($(this).data('product-price'));

        // Check if quantity and price are valid numbers
        if (!isNaN(quantity) && !isNaN(price)) {
            var subtotal = quantity * price;
            $(this).closest('tr').find('.subtotal').text('$' + subtotal.toFixed(2));
            updateTotal(); // Update the total when the quantity changes
        } else {
            // Handle invalid input (e.g., display an error message)
        }
    });

    // Initial total calculation
    updateTotal();
    /* The `}` is closing the `updateTotal` function. It marks the end of the function's code block. */
});

function updateTotal() {
    var subtotal = 0;

    // Calculate the subtotal for each row
    $('input[type="number"]').each(function () {
        var quantity = parseFloat($(this).val());
        var price = parseFloat($(this).data('product-price'));

        if (!isNaN(quantity) && !isNaN(price)) {
            subtotal += quantity * price;
        }
    });
    var vat = 6;
    var total = subtotal + vat; // Assuming VAT is a fixed value
    $('#subtotal').text('$' + subtotal.toFixed(2));
    $('#total').text('$' + total.toFixed(2));
}

