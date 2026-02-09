window.addEventListener('load', () => {
    // Hide loader
    const loader = document.getElementById('loader-wrapper');
    setTimeout(() => {
        loader.classList.add('hidden');
    }, 2000); // 2 seconds delay for effect
});

document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeCheckbox = document.getElementById('themeToggle');
    const html = document.documentElement;
    
    // Check local storage or system preference
    const savedTheme = localStorage.getItem('theme');
    const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    
    // Initialize state
    if (savedTheme) {
        setTheme(savedTheme);
    } else {
        setTheme(systemTheme);
    }

    // Toggle listener
    themeCheckbox.addEventListener('change', () => {
        const newTheme = themeCheckbox.checked ? 'dark' : 'light';
        setTheme(newTheme);
    });

    function setTheme(theme) {
        html.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        
        // Sync checkbox state
        if (theme === 'dark') {
            themeCheckbox.checked = true;
        } else {
            themeCheckbox.checked = false;
        }
    }

    // Scroll Animations (Intersection Observer)
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    // Observe fade-in elements and grids
    document.querySelectorAll('.fade-in, .grid').forEach(el => {
        observer.observe(el);
    });

    // Notion-style Toggles
    const toggles = document.querySelectorAll('.toggle-header');
    
    toggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const parent = toggle.parentElement;
            parent.classList.toggle('active');
        });
    });

    // Smooth Scroll for Anchors
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Heart/Star Button for GitHub
    const heartBtn = document.getElementById('heartBtn');
    const starCount = document.getElementById('starCount');
    const GITHUB_REPO = 'Arshveen-singh/VISION-AI-DEV';
    
    // Check if user already "liked"
    const hasLiked = localStorage.getItem('visionai_liked') === 'true';
    if (hasLiked) {
        heartBtn.classList.add('liked');
    }
    
    // Fetch GitHub star count
    async function fetchStarCount() {
        try {
            const response = await fetch(`https://api.github.com/repos/${GITHUB_REPO}`);
            if (response.ok) {
                const data = await response.json();
                starCount.textContent = formatNumber(data.stargazers_count);
            }
        } catch (error) {
            console.log('Could not fetch star count');
        }
    }
    
    // Format large numbers (e.g., 1.2k)
    function formatNumber(num) {
        if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'k';
        }
        return num.toString();
    }
    
    // Heart button click handler
    heartBtn.addEventListener('click', () => {
        // Add liked state
        heartBtn.classList.add('liked');
        localStorage.setItem('visionai_liked', 'true');
        
        // Trigger animation
        heartBtn.classList.add('animate');
        setTimeout(() => {
            heartBtn.classList.remove('animate');
        }, 800);
        
        // Open GitHub repo for starring (after a small delay for animation)
        setTimeout(() => {
            window.open(`https://github.com/${GITHUB_REPO}`, '_blank');
        }, 400);
    });
    
    // Fetch star count on load
    fetchStarCount();
});
