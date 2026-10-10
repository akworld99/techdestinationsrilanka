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
      hire: ['Hire Sri Lankan talent', 'Tell us the roles you need and when. We will point you to people and partners who have done it before.'],
      setup: ['Set up in Sri Lanka', 'Tell us the size of team you have in mind. We will walk you through entity, Board of Investment and Port City options.'],
      recruit: ['Recruit at scale', 'Tell us how many people you need and how fast. We will connect you with recruiters and employers of record who do this every week.'],
      feature: ['Suggest a company', 'Tell us what was built, who uses it outside Sri Lanka, and where we can verify the numbers.']
    };
    if (copy[need]) {
      document.getElementById('contact-title').textContent = copy[need][0];
      document.getElementById('contact-lede').textContent = copy[need][1];
      var sel = document.getElementById('need');
      if (sel) sel.value = need;
      Array.prototype.forEach.call(needs.querySelectorAll('.door'), function (d) {
        if (d.getAttribute('href').indexOf('need=' + need) !== -1) d.classList.add('is-on');
      });
    }
    var form = document.getElementById('contact-form');
    if (form) {
      form.addEventListener('submit', function (ev) {
        ev.preventDefault();
        var status = document.getElementById('form-status');
        var submit = form.querySelector('button[type=submit]');
        submit.disabled = true;
        status.textContent = 'Sending your message.';
        fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
          .then(function (r) {
            if (!r.ok) throw new Error();
            form.reset();
            status.textContent = 'Message sent. We reply within two working days.';
          })
          .catch(function () {
            status.textContent = 'The message did not send. Check your connection and try again, or message us on LinkedIn.';
          })
          .then(function () { submit.disabled = false; });
      });
    }
  }

  // copy link on story pages
  var copyBtn = document.querySelector('[data-copy]');
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      var done = function () { copyBtn.textContent = 'Link copied'; setTimeout(function () { copyBtn.textContent = 'Copy link'; }, 2000); };
      if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(done); else done();
    });
  }
})();
