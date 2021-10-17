/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/js
*/

var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
	base: {
		iconColor: "#000",
		color: "#000",
		fontWeight: "500",
		fontFamily: '"Roboto", Open Sans, Segoe UI, sans-serif',
		fontSmoothing: "antialiased",
		fontSize: "16px",
		"::placeholder": {
			color: "#aab7c4",
		},
	},
	invalid: {
		color: "#ff2fc0",
		iconColor: "#ff2fc0",
	},
};
// Stripe injects an iframe into the DOM
var cardElement = elements.create("card", { style: style });
cardElement.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
	var errorDiv = document.getElementById("card-errors");
	if (event.error) {
		var html = `
            <span class="material-icons" role="alert">
                error_outline
            </span> 
            <span>${event.error.message}</span>
        `;
		$(errorDiv).html(html);
	} else {
		errorDiv.textContent = "";
	}
});

// Handle form submit
var form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
	// Prevent form from submitting, disable card element &
	// trigger loading overlay
	ev.preventDefault();
	card.update({ disabled: true });
	$("#submit-button").attr("disabled", true);
	$("#payment-form").fadeToggle(100);
	$("#loading-overlay").fadeToggle(100);

	// Capture form data
	var saveInfo = Boolean($("#id-save-info").attr("checked"));
	var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
	var postData = {
		csrfmiddlewaretoken: csrfToken,
		client_secret: clientSecret,
		save_info: saveInfo,
	};
	var url = "/checkout/cache_checkout_data/";

	// Post to cache_checkout_data view
	// View updates PaymentIntent  returns 200 response
	// Call confirmCardPayment from Stripe
	// Store billing and shipping details
	$.post(url, postData)
		.done(function () {
			stripe
				.confirmCardPayment(clientSecret, {
					payment_method: {
						card: card,
						billing_details: {
							name: $.trim(form.full_name.value),
							phone: $.trim(form.phone_number.value),
							email: $.trim(form.email.value),
							address: {
								line1: $.trim(form.street_address1.value),
								line2: $.trim(form.street_address2.value),
								city: $.trim(form.town_or_city.value),
								country: $.trim(form.country.value),
								state: $.trim(form.state_or_county.value),
							},
						},
					},
					shipping: {
						name: $.trim(form.full_name.value),
						phone: $.trim(form.phone_number.value),
						address: {
							line1: $.trim(form.street_address1.value),
							line2: $.trim(form.street_address2.value),
							city: $.trim(form.town_or_city.value),
							country: $.trim(form.country.value),
							postal_code: $.trim(form.postcode.value),
							state: $.trim(form.state_or_county.value),
						},
					},
				})
				.then(function (result) {
					// Handle any errors
					if (result.error) {
						var errorDiv = document.getElementById("card-errors");
						var html = `
							<span class="material-icons" role="alert">
								error_outline
							</span> 
							<span>${result.error.message}</span>`;
						// Display error message
						$(errorDiv).html(html);
						$("#payment-form").fadeToggle(100);
						$("#loading-overlay").fadeToggle(100);
						// Overlay hidden and card element re-enabled
						card.update({ disabled: false });
						$("#submit-button").attr("disabled", false);

						// Submit form
					} else {
						if (result.paymentIntent.status === "succeeded") {
							form.submit();
						}
					}
				});
			// If data not posted to view, reload the page
			// & display error message
		})
		.fail(function () {
			location.reload();
		});
});
