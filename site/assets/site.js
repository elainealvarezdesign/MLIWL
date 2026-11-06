/* Page behavior (Home, Watch, For parents, For educators, Meet the team) for the static build. On WordPress the same behaviors come
   from Elementor (Loop Grid / taxonomy filter, Popup, Form). */
(function () {
	'use strict';

	// ---- Story data (Figma: Home › Stories). One entry per story card. ----
	var stories = [
		{ name: 'Amie', topic: 'Suicide survivor', tags: ['suicide'], meta: '4 episodes · trailer', note: 'suicide attempt',
			desc: 'When negative thoughts keep haunting a teenage suicide survivor, the support of her family and boyfriend helps her find purpose.' },
		{ name: 'Kyle', topic: 'Bullying + substance use', tags: ['bullying', 'substance'], meta: '4 episodes · trailer · PSA', note: 'bullying, alcohol use',
			desc: 'Bullied at school, a teen turns to alcohol to drown out the bad feelings and his own negative voice.' },
		{ name: 'Dante', topic: 'LGBTQ+', tags: ['lgbtq'], meta: '4 episodes · trailer', note: 'identity, family conflict',
			desc: 'A football star’s struggles with identity and an overbearing father challenge him to accept support.' },
		{ name: 'Danny', topic: 'Trauma survivor', tags: ['trauma'], meta: '4 episodes · trailer', note: 'serious injury, trauma',
			desc: 'After a life-changing accident, a teen learns to rely on his network of supporters.' },
		{ name: 'Emily', topic: 'Abuse', tags: ['abuse'], meta: '4 episodes', note: 'abuse at home',
			desc: 'Escaping an abusive home, a teen protects her own wellbeing while shielding her mother from the truth.' },
		{ name: 'Kaia', topic: 'Body image', tags: ['body'], meta: '2 episodes', note: 'low self-esteem, body image',
			desc: 'Low self-esteem makes Kaia feel she doesn’t measure up, until she finds hope in the people she loves.' },
		{ name: 'Vince', topic: 'Body image', tags: ['body'], meta: '2 episodes', note: 'body image, anxiety',
			desc: 'Asked to be a groomsman, Vince can’t stand people looking at him. His brother’s support is crucial.' },
		{ name: 'Raquelle', slug: 'raquelle', title: 'Are You OK?', watch: 'Watch “Are You OK?”', lesson: 'Classroom activities (PDF)',
			topic: 'Bullying', tags: ['bullying'], meta: '[N] episodes · classroom activities', note: 'bullying',
			desc: '[CLIENT TO PROVIDE: one-sentence summary of Raquelle’s story]' }
	];

	var grid = document.getElementById('story-grid');
	if (grid) {
		grid.innerHTML = stories.map(function (s) {
			var slug = s.slug || s.name.toLowerCase();
			var title = s.title || (s.name + '’s story');
			return '<li id="story-' + slug + '" data-tags="' + s.tags.join(' ') + '"><article class="mliwl-story-card">' +
				'<div class="mliwl-story-media"><img src="assets/img/story-' + slug + '.webp" width="576" height="432" alt="" loading="lazy">' +
				'<span class="mliwl-tag mliwl-tag-on-image">' + s.topic + '</span></div>' +
				'<div class="mliwl-story-body">' +
				'<h4 class="text-heading-h4">' + title + '</h4>' +
				'<p class="text-body-small desc">' + s.desc + '</p>' +
				'<p class="text-caption meta">' + s.meta + '</p>' +
				'<p class="text-caption note">Includes: ' + s.note + '. Need to talk? Call or text 988.</p>' +
				'<div class="mliwl-story-actions">' +
				'<a class="mliwl-btn mliwl-btn-primary mliwl-btn-sm" href="#"><svg aria-hidden="true"><use href="#i-play"/></svg>' + (s.watch || ('Watch ' + s.name + '’s story')) + '</a>' +
				'<a class="mliwl-text-link" href="#">' + (s.lesson || 'Lesson plan (PDF)') + '<span class="screen-reader-text"> for ' + title + '</span></a>' +
				'</div></div></article></li>';
		}).join('');
	}

	// ---- Resource cards: parent playbooks and lesson plans. Figma: Lesson Card. ----
	function resourceCards(el, o) {
		el.innerHTML = stories.map(function (s) {
			var slug = s.slug || s.name.toLowerCase();
			var title = s.title || (s.name + '’s story');
			var file = (s.slug && o.altFile) || o.file;
			return '<li data-tags="' + s.tags.join(' ') + '" data-grades="6-8 9-12"><article class="mliwl-playbook-card">' +
				'<div class="media"><img src="assets/img/story-' + slug + '.webp" width="576" height="432" alt="" loading="lazy"></div>' +
				'<div class="body"><span class="mliwl-tag">' + s.topic + '</span>' +
				'<h3 class="text-heading-h4">' + title + '</h3>' +
				'<p class="text-body-small desc">' + o.desc + '</p>' +
				'<p class="text-caption meta">' + ((s.slug && o.altMeta) || o.meta) + '</p>' +
				'<div class="mliwl-actions">' +
				'<a class="mliwl-btn mliwl-btn-primary mliwl-btn-sm" href="#" download><svg aria-hidden="true"><use href="#i-download"/></svg>' + o.download + '<span class="screen-reader-text"> ' + file + ' for ' + title + ' (PDF)</span></a>' +
				'<a class="mliwl-btn mliwl-btn-outline mliwl-btn-sm" href="watch.html#story-' + slug + '"><svg aria-hidden="true"><use href="#i-play"/></svg>' + o.watch + '<span class="screen-reader-text"> ' + title + '</span></a>' +
				'</div></div></article></li>';
		}).join('');
	}
	var playbooks = document.getElementById('playbook-grid');
	if (playbooks) resourceCards(playbooks, { download: 'Playbook', watch: 'Watch', file: 'parent playbook',
		desc: '[Playbook title from the PDF cover, e.g. “How to support a loved one with their mental health struggles”]',
		meta: 'Parent playbook · PDF · [size]' });
	var lessons = document.getElementById('lesson-grid');
	if (lessons) resourceCards(lessons, { download: 'Download', watch: 'Watch story', file: 'lesson plan', altFile: 'classroom activities',
		desc: '[Client copy: what students learn in this lesson, in one or two lines.]',
		meta: 'Lesson plan · Grades 7–12 · 45 min · PDF', altMeta: 'Classroom activities · Grades 6–12 · PDF' });

	// ---- Filter chips: topic (data-topic) and grade (data-grade), combined ----
	var count = document.getElementById('story-count');
	var filterList = grid || playbooks || lessons;
	var noun = (count && count.getAttribute('data-noun')) || 'story';
	var plural = noun === 'story' ? 'stories' : noun + 's';
	var active = { topic: 'all', grade: 'all' };
	['topic', 'grade'].forEach(function (key) {
		var chips = document.querySelectorAll('[data-' + key + ']');
		chips.forEach(function (chip) {
			chip.addEventListener('click', function () {
				active[key] = chip.getAttribute('data-' + key);
				chips.forEach(function (c) { c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
				var shown = 0;
				filterList.querySelectorAll('li').forEach(function (li) {
					var show = (active.topic === 'all' || li.getAttribute('data-tags').split(' ').indexOf(active.topic) > -1) &&
						(active.grade === 'all' || li.getAttribute('data-grades').split(' ').indexOf(active.grade) > -1);
					li.hidden = !show;
					if (show) shown++;
				});
				count.textContent = 'Showing ' + shown + ' ' + (shown === 1 ? noun : plural) + langNote();
			});
		});
	});

	// ---- Video language (Watch). On WordPress this is a Loop Grid taxonomy filter. ----
	var langSelect = document.getElementById('story-language');
	function langNote() {
		return langSelect && langSelect.value !== 'en' ? ' in ' + langSelect.options[langSelect.selectedIndex].text : '';
	}
	if (langSelect && count) {
		langSelect.addEventListener('change', function () {
			count.textContent = count.textContent.replace(/ in .*$/, '') + langNote();
		});
	}

	// ---- Mobile carousel arrows ----
	document.querySelectorAll('[data-scroll]').forEach(function (btn) {
		btn.addEventListener('click', function () {
			var item = grid.querySelector('li:not([hidden])');
			var step = item ? item.getBoundingClientRect().width + 16 : 300;
			grid.scrollBy({ left: step * Number(btn.getAttribute('data-scroll')), behavior: 'smooth' });
		});
	});

	// ---- Mobile menu ----
	var menu = document.getElementById('mobile-menu');
	var openBtn = document.querySelector('.site-menu-button');
	if (menu && openBtn && menu.showModal) {
		openBtn.addEventListener('click', function () { menu.showModal(); openBtn.setAttribute('aria-expanded', 'true'); });
		menu.querySelector('.site-menu-close').addEventListener('click', function () { menu.close(); });
		menu.addEventListener('close', function () { openBtn.setAttribute('aria-expanded', 'false'); openBtn.focus(); });
		menu.querySelectorAll('a[href^="#"]').forEach(function (a) { a.addEventListener('click', function () { menu.close(); }); });
	}

	// ---- Bio dialog (Meet the team). Focus returns to the button that opened it. ----
	var bio = document.getElementById('bio-dialog');
	if (bio && bio.showModal) {
		var opener = null;
		document.querySelectorAll('[data-bio-name]').forEach(function (btn) {
			btn.addEventListener('click', function () {
				opener = btn;
				document.getElementById('bio-name').textContent = btn.getAttribute('data-bio-name');
				document.getElementById('bio-role').textContent = btn.getAttribute('data-bio-role');
				bio.showModal();
			});
		});
		bio.querySelector('.mliwl-dialog-close').addEventListener('click', function () { bio.close(); });
		bio.addEventListener('click', function (e) { if (e.target === bio) bio.close(); });
		bio.addEventListener('close', function () { if (opener) opener.focus(); });
	}

	// ---- Newsletter: audience chips (one selected), validation, success state ----
	document.querySelectorAll('#audience-chips .mliwl-chip').forEach(function (chip, i, all) {
		chip.addEventListener('click', function () { all.forEach(function (c) { c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); }); });
	});
	var form = document.getElementById('newsletter-form');
	if (form) {
		form.addEventListener('submit', function (e) {
			e.preventDefault();
			var input = document.getElementById('nl-email');
			var help = document.getElementById('nl-help');
			var ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim());
			if (!ok) {
				input.setAttribute('aria-invalid', 'true');
				help.classList.add('is-error');
				help.textContent = 'Enter a full email address, like name@example.com';
				input.focus();
				return;
			}
			var area = document.getElementById('newsletter-area');
			area.innerHTML = '<div class="mliwl-newsletter-success" role="status"><h3 class="text-heading-h3" tabindex="-1">You’re signed up!</h3>' +
				'<p class="text-body-default mliwl-muted-text">Check your inbox to confirm your email. We’ll send new stories and resources — about once a month.</p>' +
				'<a class="mliwl-btn mliwl-btn-outline" href="#featured-title"><svg aria-hidden="true"><use href="#i-play"/></svg>Watch the newest story</a></div>';
			area.querySelector('h3').focus();
		});
	}
})();
