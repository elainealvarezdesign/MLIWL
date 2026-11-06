/**
 * Opens the "MLIWL Mobile Menu" Elementor Pro popup from the header Menu button
 * (a Button widget linking to #mliwl-open-menu) and keeps aria-expanded in sync.
 * The popup ID is passed in from functions.php (mliwlMenu.popupId).
 */
(function () {
	var cfg = window.mliwlMenu || {};
	if (!cfg.popupId) return;

	function buttons() {
		return document.querySelectorAll('a[href="#mliwl-open-menu"]');
	}

	function setExpanded(value) {
		buttons().forEach(function (b) { b.setAttribute('aria-expanded', value ? 'true' : 'false'); });
	}

	document.addEventListener('click', function (e) {
		var trigger = e.target.closest('a[href="#mliwl-open-menu"]');
		if (!trigger) return;
		e.preventDefault();
		var popup = window.elementorProFrontend && elementorProFrontend.modules && elementorProFrontend.modules.popup;
		if (popup) {
			popup.showPopup({ id: cfg.popupId });
			setExpanded(true);
		}
	});

	document.addEventListener('DOMContentLoaded', function () {
		buttons().forEach(function (b) {
			b.setAttribute('aria-expanded', 'false');
			b.setAttribute('aria-haspopup', 'dialog');
		});
	});

	// Elementor fires this jQuery event when any popup closes: return focus to the Menu button.
	if (window.jQuery) {
		jQuery(document).on('elementor/popup/hide', function (event, id) {
			if (String(id) !== String(cfg.popupId)) return;
			setExpanded(false);
			var b = buttons()[0];
			if (b) b.focus();
		});
	}
})();
