(function () {
  // mobile menu
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? 'Close' : 'Menu';
    });
  }

  var params = new URLSearchParams(location.search);

  // filter + search on the stories and companies pages
  var list = document.getElementById('list');
  if (list) {
    var items = Array.prototype.slice.call(list.children);
    var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
    var q = document.getElementById('q');
    var empty = document.getElementById('empty');
    var type = 'all';

    function apply() {
      var term = (q && q.value || '').trim().toLowerCase();
      var shown = 0;
      items.forEach(function (el) {
        var ok = (type === 'all' || el.dataset.type === type) && (!term || el.dataset.text.indexOf(term) !== -1);
        el.hidden = !ok;
        if (ok) shown++;
      });
      if (empty) empty.hidden = shown > 0;
    }
    function setType(t) {
      type = t;
      chips.forEach(function (c) {
        var on = c.dataset.filter === t;
        c.classList.toggle('is-on', on);
        c.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
      apply();
    }
    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        setType(c.dataset.filter);
        var url = new URL(location.href);
        if (c.dataset.filter === 'all') url.searchParams.delete('type'); else url.searchParams.set('type', c.dataset.filter);
        history.replaceState(null, '', url);
      });
    });
    if (q) q.addEventListener('input', apply);
    var start = params.get('type');
    setType(chips.some(function (c) { return c.dataset.filter === start; }) ? start : 'all');
  }

  // contact page: reflect the chosen need
  var needs = document.getElementById('needs');
  if (needs) {
    var need = params.get('need');
    var copy = {
      hire: ['Hire Sri Lankan talent', 'Tell us the roles you need and when. We will introduce people and partners who have done it before.', 'Hire Sri Lankan talent'],
      partner: ['Find a delivery partner', 'Describe the product or project. We will match you with a Sri Lankan company that has done that kind of work.', 'Find a delivery partner'],
      setup: ['Set up in Sri Lanka', 'Tell us the size of team you have in mind. We will walk you through entity, Board of Investment and Port City options.', 'Set up in Sri Lanka'],
      recruit: ['Recruit at scale', 'Tell us how many people you need and how fast. We will connect you with recruiters who do this every week.', 'Recruit at scale'],
      feature: ['Feature my company', 'Tell us what was built, who uses it outside Sri Lanka, and where we can verify the numbers.', 'Feature my company'],
      employer: ['Employer branding', 'Tell us who you are trying to hire and what makes your team worth joining.', 'Employer branding'],
      events: ['Events and delegations', 'Tell us which event you are attending and what you want out of it.', 'Events and delegations']
    };
    if (copy[need]) {
      document.getElementById('contact-title').textContent = copy[need][0];
      document.getElementById('contact-lede').textContent = copy[need][1];
      var sel = document.querySelector('#contact-form select[name=need]');
      if (sel) sel.value = copy[need][2];
      Array.prototype.forEach.call(needs.querySelectorAll('.door'), function (d) {
        if (d.dataset.need === need) d.classList.add('is-on');
      });
    }
  }

  // carry the industry or country a visitor came from into the talent form
  var ft = document.getElementById('find-talent-form');
  if (ft) {
    ['industry', 'from'].forEach(function (k) {
      var v = params.get(k);
      if (!v || !/^[a-z-]+$/.test(v)) return;
      var h = document.createElement('input');
      h.type = 'hidden'; h.name = k; h.value = v;
      ft.appendChild(h);
    });
  }

  // every form on the site posts to the same endpoint
  Array.prototype.forEach.call(document.querySelectorAll('form[data-form]'), function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var status = form.querySelector('.form-status');
      var submit = form.querySelector('button[type=submit]');
      var endpoint = form.getAttribute('action');
      if (!endpoint) {
        status.textContent = 'This form is not switched on yet. Message us on LinkedIn and we will pick it up there.';
        return;
      }
      submit.disabled = true;
      status.textContent = 'Sending.';
      fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error();
          form.reset();
          status.textContent = form.dataset.done;
        })
        .catch(function () {
          status.textContent = 'That did not send. Check your connection and try again, or message us on LinkedIn.';
        })
        .then(function () { submit.disabled = false; });
    });
  });

  // copy link on story pages
  var copyBtn = document.querySelector('[data-copy]');
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      var done = function () { copyBtn.textContent = 'Link copied'; setTimeout(function () { copyBtn.textContent = 'Copy link'; }, 2000); };
      if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(done); else done();
    });
  }
})();
