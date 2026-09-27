(() => {
  const nav = document.querySelector('.nav');
  const toggle = document.querySelector('.nav__toggle');
  const menu = document.getElementById('menu');

  // Sticky-Header-Schatten
  const onScroll = () => nav && nav.classList.toggle('is-scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobiles Menü
  if (toggle && menu) {
    const setOpen = (open) => {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
      menu.classList.toggle('is-open', open);
    };
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setOpen(false); });
  }

  // Einblenden beim Scrollen
  const items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach((el) => io.observe(el));
  } else {
    items.forEach((el) => el.classList.add('is-visible'));
  }

  // Heutigen Tag markieren + "Jetzt geöffnet" (Zeit in Europe/Berlin)
  const status = document.getElementById('status');
  try {
    const parts = new Intl.DateTimeFormat('en-GB', {
      timeZone: 'Europe/Berlin', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false
    }).formatToParts(new Date());
    const get = (t) => parts.find((p) => p.type === t).value;
    const day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(get('weekday'));
    const minutes = Number(get('hour')) * 60 + Number(get('minute'));
    const row = document.querySelector(`.hours tr[data-day="${day}"]`);
    if (row) row.classList.add('is-today');
    if (status) {
      const open = day !== 1 && minutes >= 9 * 60 && minutes < 17 * 60;
      status.textContent = open ? 'Jetzt geöffnet' : 'Gerade geschlossen';
      status.classList.toggle('is-open', open);
      status.hidden = false;
    }
  } catch (_) { /* Anzeige ist optional */ }

  // Anfrageformular: öffnet das E-Mail-Programm mit vorausgefüllter Anfrage
  const form = document.getElementById('anfrage-form');
  if (form) {
    const error = form.querySelector('.form__error');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let valid = true;
      form.querySelectorAll('input, textarea').forEach((field) => {
        const ok = field.checkValidity() && (!field.required || field.value.trim() !== '');
        field.classList.toggle('is-invalid', !ok);
        if (!ok) valid = false;
      });
      error.hidden = valid;
      if (!valid) return;
      const d = Object.fromEntries(new FormData(form));
      const datum = d.datum ? new Date(d.datum + 'T00:00').toLocaleDateString('de-DE') : '–';
      const body = [
        `Name: ${d.vorname} ${d.nachname}`,
        `E-Mail: ${d.email}`,
        `Telefon: ${d.telefon}`,
        `Wunschtermin: ${datum}`,
        `Personenzahl: ${d.personen || '–'}`,
        '',
        d.nachricht
      ].join('\n');
      const subject = `${form.dataset.subject || 'Anfrage private Feier'} – ${d.vorname} ${d.nachname}`;
      window.location.href = `mailto:info@cafebenjamico.de?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });
  }

  // Speisekarte: aktiven Abschnitt in den Sprungmarken hervorheben
  const tabs = document.querySelectorAll('.menu-tabs a');
  if (tabs.length && 'IntersectionObserver' in window) {
    const byId = new Map([...tabs].map((a) => [a.getAttribute('href').slice(1), a]));
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        tabs.forEach((a) => a.classList.remove('is-active'));
        const tab = byId.get(entry.target.id);
        if (tab) {
          tab.classList.add('is-active');
          tab.scrollIntoView({ block: 'nearest', inline: 'center' });
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    byId.forEach((_, id) => { const el = document.getElementById(id); if (el) spy.observe(el); });
    const intro = document.querySelector('.page-hero');
    if (intro) new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) tabs.forEach((a) => a.classList.remove('is-active'));
    }, { rootMargin: '-45% 0px -50% 0px' }).observe(intro);
  }

  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
