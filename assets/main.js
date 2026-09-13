document.documentElement.classList.add('js');

const header = document.querySelector('.site-header');
const navToggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.site-nav');

function updateHeader() {
  if (!header) return;
  header.classList.toggle('scrolled', window.scrollY > 24);
}

updateHeader();
window.addEventListener('scroll', updateHeader, { passive: true });

if (navToggle && nav) {
  navToggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
  });

  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

document.querySelectorAll('[data-year]').forEach((el) => {
  el.textContent = new Date().getFullYear();
});

const form = document.querySelector('[data-contact-form]');
if (form) {
  const status = form.querySelector('.form-status');
  const button = form.querySelector('button[type="submit"]');

  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    if (form.action.includes('YOUR_FORM_ID')) {
      if (status) status.textContent = 'Online enquiries are being connected. Please email patrick@ortonheritage.com in the meantime.';
      return;
    }

    const originalLabel = button ? button.textContent : '';
    if (button) {
      button.disabled = true;
      button.textContent = 'Sending…';
    }
    if (status) status.textContent = '';

    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      });

      if (!response.ok) throw new Error('Form submission failed');

      form.reset();
      if (status) status.textContent = 'Thanks — your enquiry has been sent. We’ll be in touch shortly.';
    } catch (error) {
      if (status) status.textContent = 'Something went wrong. Please email patrick@ortonheritage.com instead.';
    } finally {
      if (button) {
        button.disabled = false;
        button.textContent = originalLabel;
      }
    }
  });
}
