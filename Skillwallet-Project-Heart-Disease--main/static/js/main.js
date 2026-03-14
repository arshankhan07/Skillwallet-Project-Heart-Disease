// DataVision Analytics — Main JS

// Active nav link highlight
document.querySelectorAll('.nav-link').forEach(link => {
  if (link.href && link.href !== '#' && window.location.pathname === new URL(link.href).pathname) {
    link.classList.add('active');
  }
});

// Smooth entrance animations on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.feature-card, .embed-block').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity .5s ease, transform .5s ease';
  observer.observe(el);
});

// Hamburger (mobile)
const ham = document.getElementById('hamburger');
if (ham) {
  ham.addEventListener('click', () => {
    const nav = document.querySelector('.main-nav');
    if (!nav) return;
    nav.style.display = nav.style.display === 'flex' ? 'none' : 'flex';
    nav.style.flexDirection = 'column';
    nav.style.position = 'absolute';
    nav.style.top = '68px';
    nav.style.left = '0';
    nav.style.right = '0';
    nav.style.background = '#fff';
    nav.style.padding = '16px 24px';
    nav.style.borderBottom = '1px solid #D6E0FF';
    nav.style.zIndex = '99';
  });
}
