$(document).ready(function () {
	$("input[name='row'], input[name='column']").change(function() {
		let column = $("input[name='column']").val();
		let row = $("input[name='row']").val();

		let positionSelected = $('#row-' + row).children()[column - 1];

		$('td:has(> div)').html('');
		if($(positionSelected).is(':empty')) {
			$(positionSelected).append(`<div class="selected"></div>`);
		}
	});
});

function changePosition(column, row) {
	let positionSelected = $('#row-' + row).children()[column - 1];

	positionSelected.append("♜");
}

function positionError(weHaveAProblem) {
	if(weHaveAProblem == false) {
		$("td:contains(♜)").css({'animation': 'shake 0.5s 5'});
	}
}