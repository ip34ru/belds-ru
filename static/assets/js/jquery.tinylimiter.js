/**
 * Created by taksenov on 02.10.2014.
 */
/**
* TinyLimiter - scriptiny.com/tinylimiter
* License: GNU GPL v3.0 - scriptiny.com/license
*/


$(document).ready( function() {
	var elem = $("#chars");
	$("#comment").limiter(1000, elem);
});


(function($) {
	$.fn.extend( {
		limiter: function(limit, elem) {
			$(this).on("keyup focus", function() {
				setCount(this, elem);
			});
			function setCount(src, elem) {
				var chars = src.value.length;
				if (chars > limit) {
					src.value = src.value.substr(0, limit);
					chars = limit;
				}
				elem.html( limit - chars );
			}
			setCount($(this)[0], elem);
		}
	});
})(jQuery);