$(document).ready(() => {

	$('#afterdabox').height($(window).height() - 730);

	$(window).resize(() => {
		$('#afterdabox').height($(window).height() - 730);
	});

	setInterval(() => {
		$('#advert').toggle();
	}, 1200);

	$("#reset-btn-absolute").on("click", function() {
		resetMachine();
	})

	resetMachine();
});

const screenplay = async () => {
	$('#screen-txt').marquee({
		duration: 3000,
		gap: 50,
		delayBeforeStart: 0,
		direction: 'left',
		duplicated: false
	});
}

var validItems = ['A1', 'A2', 'A3', 'B4', 'B5', 'B6', 'C7', 'C8', 'C9'];


const enableVendingBtns = async () => {
	$('.vending-btns').on("click", async function() {
		$(".vending-btns").css({
			"pointer-events": "none"
		});
		screenText = $("#screen-txt").text();
		if (screenText.length >= 2) {
			$("#screen-txt").text("");
			$("#screen-txt").text($(this).text());
		} else {
			$("#screen-txt").text(`${screenText}${$( this ).text()}`);
		}
		screenText = $("#screen-txt").text();
		if (screenText.length == 2) {
			if (jQuery.inArray(screenText, validItems) == -1) {
				$("#screen-txt").text("Invalid item code!");
				screenplay();
				$(".vending-btns").css({
					"pointer-events": "auto"
				});
				return;
			}
			$("#screen-txt").text("Order processing...");
			screenplay();
			$(".vending-btns").css({
				"pointer-events": "none"
			});

			await processOrder(screenText);

		}
		$(".vending-btns").css({
			"pointer-events": "auto"
		});
	});
}


const redeemCoupon = async () => {
	const data = {
		coupon_code: 'HTB_100'
	};

	await fetch(`/api/coupons/apply`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})
		.then((response) => response.json()
			.then((resp) => {
				$('.vending-btns').off('click');
				enableVendingBtns();
				$(".vending-btns").css({
					"pointer-events": "auto"
				});
				$("#screen-txt").text(resp.message);
				screenplay();
			}))
		.catch((error) => {
			$("#screen-txt").text(error);
			screenplay();
		});
}

const processOrder = async (itemId) => {

	const data = {
		item: itemId
	};

	await fetch(`/api/purchase`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})
		.then((response) => response.json()
			.then((resp) => {
				if (response.status == 200) {
					$("#bottom-panel-flicker").attr("id", "bottom-panel-flicker-active");
					$("#receivable-item").attr("src", $("#" + itemId).attr("src"))
					$("#receivable-item").show();
					if (resp["flag"] !== undefined) {
						$("#receivable-item").on('click', function() {
							$("#screen-txt").text(resp.flag);
							screenplay();
						})
						$(".vending-btns").css({
							"pointer-events": "none"
						});
						return;
					}
				}
				$("#receivable-item").off('click');
				$("#receivable-item").on("click", function() {
					$(this).hide();
					$("#bottom-panel-flicker-active").attr("id", "bottom-panel-flicker");
				});
				$(".vending-btns").css({
					"pointer-events": "auto"
				});
				$("#screen-txt").text(resp.message);
				screenplay();
			}))
		.catch((error) => {
			$(".vending-btns").css({
				"pointer-events": "auto"
			});
			$("#screen-txt").text(error);
			screenplay();
		});
}

const resetMachine = async () => {

	$("#screen-txt").text("Please wait...");
	screenplay();
	await fetch(`/api/reset`, {
			method: 'GET',
			credentials: 'include'
		})
		.then((response) => response.json())
		.then((resp) => {
			$("#coupon").show();
			$("#coupon").css({
				"bottom": "50px",
				"left": "600px",
				"top": "auto"
			});
			$("#coupon").draggable();
			$("#coin-in-area").droppable({
				drop: async (event, ui) => {
					$("#coupon").hide();
					$("#screen-txt").text("Processing coupon voucher...");
					screenplay();
					await redeemCoupon();
				}
			});
			$(".vending-btns").css({
				"pointer-events": "none"
			});
			$("#screen-txt").text(resp.message);
			screenplay();
		});

}

