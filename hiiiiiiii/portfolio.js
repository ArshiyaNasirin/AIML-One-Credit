// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Hamburger menu functionality
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        hamburger.classList.toggle('active');
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });
}

// Animate elements on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all cards and content sections
document.querySelectorAll('.project-card, .cert-card, .skill-category, .info-card, .timeline-content').forEach(el => {
    observer.observe(el);
});

// Add animation classes
const style = document.createElement('style');
style.textContent = `
    .project-card:not(.animate),
    .cert-card:not(.animate),
    .skill-category:not(.animate),
    .info-card:not(.animate),
    .timeline-content:not(.animate) {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }

    .project-card.animate,
    .cert-card.animate,
    .skill-category.animate,
    .info-card.animate,
    .timeline-content.animate {
        opacity: 1;
        transform: translateY(0);
    }
`;
document.head.appendChild(style);

// Profile view counter update
function updateProfileViews() {
    // This would typically be connected to a backend service
    // For now, they'll use shields.io which handles this automatically
    console.log('Profile views tracking enabled via shields.io');
}

// Initialize particles effect for hero section (optional)
function createParticles() {
    const starsContainer = document.querySelector('.stars');
    if (!starsContainer) return;

    for (let i = 0; i < 50; i++) {
        const star = document.createElement('div');
        star.style.cssText = `
            position: absolute;
            width: ${Math.random() * 2 + 1}px;
            height: ${Math.random() * 2 + 1}px;
            background: white;
            border-radius: 50%;
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            opacity: ${Math.random() * 0.5 + 0.5};
            animation: twinkle ${Math.random() * 3 + 2}s infinite;
        `;
        starsContainer.appendChild(star);
    }
}

// Add twinkle animation
const twinkelStyle = document.createElement('style');
twinkelStyle.textContent = `
    @keyframes twinkle {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 1; }
    }
`;
document.head.appendChild(twinkelStyle);

// Initialize particles on load
window.addEventListener('load', createParticles);

// Add smooth fade-in for images
document.querySelectorAll('img').forEach(img => {
    img.style.opacity = '0';
    img.addEventListener('load', () => {
        img.style.transition = 'opacity 0.5s ease';
        img.style.opacity = '1';
    });
    // If image is already loaded (cached)
    if (img.complete) {
        img.style.opacity = '1';
    }
});

// Active navigation link on scroll
window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('section');

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// Add active state styling for navigation
const navStyle = document.createElement('style');
navStyle.textContent = `
    .nav-link.active {
        color: var(--primary-pink);
    }

    .nav-link.active::after {
        width: 100%;
    }
`;
document.head.appendChild(navStyle);

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        const scrollPosition = window.pageYOffset;
        heroContent.style.transform = `translateY(${scrollPosition * 0.5}px)`;
    }
});

// Form handling (if you add a contact form later)
const contactForm = document.querySelector('form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        // Add your form submission logic here
        alert('Thank you for your message. I will get back to you soon!');
        contactForm.reset();
    });
}

// Add cursor glow effect (optional)
document.addEventListener('mousemove', (e) => {
    const glow = document.getElementById('cursorGlow');
    if (glow) {
        glow.style.left = `${e.clientX}px`;
        glow.style.top = `${e.clientY}px`;
    }
});

// Typing animation for hero tagline
const typingElement = document.getElementById('typingRole');
const typingWords = ['AI Enthusiast', 'Data Explorer', 'Innovator'];
let typingWordIndex = 0;
let typingCharIndex = 0;
let isDeleting = false;

function runTypingEffect() {
    if (!typingElement) return;

    const currentWord = typingWords[typingWordIndex];

    if (!isDeleting) {
        typingElement.textContent = currentWord.slice(0, typingCharIndex + 1);
        typingCharIndex += 1;

        if (typingCharIndex === currentWord.length) {
            isDeleting = true;
            setTimeout(runTypingEffect, 900);
            return;
        }
    } else {
        typingElement.textContent = currentWord.slice(0, typingCharIndex - 1);
        typingCharIndex -= 1;

        if (typingCharIndex === 0) {
            isDeleting = false;
            typingWordIndex = (typingWordIndex + 1) % typingWords.length;
        }
    }

    setTimeout(runTypingEffect, isDeleting ? 55 : 95);
}

// Copy email to clipboard
document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
    link.addEventListener('click', function (e) {
        const email = this.getAttribute('href').replace('mailto:', '');
        // Allow default behavior but you could add copy-to-clipboard logic here
    });
});

// Prevent loading of external images that might slow down the site
document.addEventListener('DOMContentLoaded', () => {
    console.log('Portfolio loaded successfully!');
    updateProfileViews();
    runTypingEffect();
});

// Add scroll reveal animation for stats
const github = document.querySelector('.github-stats');
if (github) {
    observer.observe(github);
}
