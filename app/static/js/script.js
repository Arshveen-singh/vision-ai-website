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

    // Chat Sidebar Logic
    const chatSidebar = document.getElementById('chat-sidebar');
    const openChatBtn = document.getElementById('open-chat');
    const closeChatBtn = document.getElementById('close-chat');
    const chatInput = document.getElementById('chat-input');
    const sendChatBtn = document.getElementById('send-chat');
    const chatMessages = document.getElementById('chat-messages');

    function toggleChat() {
        chatSidebar.classList.toggle('open');
        const isOpen = chatSidebar.classList.contains('open');
        openChatBtn.style.opacity = isOpen ? '0' : '1';
        openChatBtn.style.pointerEvents = isOpen ? 'none' : 'auto';
        
        if (isOpen) {
            setTimeout(() => chatInput.focus(), 500); // Wait for transition
        }
    }

    openChatBtn.addEventListener('click', toggleChat);
    closeChatBtn.addEventListener('click', toggleChat);

    // Close chat when clicking outside
    document.addEventListener('click', (e) => {
        if (chatSidebar.classList.contains('open') && 
            !chatSidebar.contains(e.target) && 
            !openChatBtn.contains(e.target)) {
            toggleChat();
        }
    });

    // Send Message Logic
    async function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add User Message
        addMessage(message, 'user');
        chatInput.value = '';

        // Show Typing Indicator
        const typingId = showTypingIndicator();

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            removeTypingIndicator(typingId);

            if (response.ok) {
                addMessage(data.response, 'bot');
            } else {
                // Show specific backend error if available
                const errorText = data.error || "The assistant is busy or unavailable.";
                addMessage(`⚠️ ${errorText}`, 'bot');
            }
        } catch (error) {
            removeTypingIndicator(typingId);
            addMessage("📡 Network error. Please check your connection.", 'bot');
            console.error('Chat Error:', error);
        }
    }

    sendChatBtn.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);
        
        try {
            if (sender === 'bot') {
                // Ensure marked is available
                const parser = window.marked || marked;
                if (typeof parser !== 'undefined') {
                    // Support both .parse() and direct function call
                    messageDiv.innerHTML = parser.parse ? parser.parse(text) : parser(text);
                } else {
                    // Fallback to plain text with link conversion
                    const linkedText = text.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank" style="color: inherit; text-decoration: underline;">$1</a>');
                    messageDiv.innerHTML = linkedText;
                    console.warn('Markdown parser not found');
                }
            } else {
                // User message formatting
                const linkedText = text.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank" style="color: inherit; text-decoration: underline;">$1</a>');
                messageDiv.innerHTML = linkedText;
            }
        } catch (err) {
            console.error('Formatting error:', err);
            messageDiv.textContent = text;
        }
        
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    function showTypingIndicator() {
        const id = 'typing-' + Date.now();
        const typingDiv = document.createElement('div');
        typingDiv.classList.add('typing-indicator');
        typingDiv.id = id;
        typingDiv.innerHTML = `
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        `;
        chatMessages.appendChild(typingDiv);
        scrollToBottom();
        return id;
    }

    function removeTypingIndicator(id) {
        const element = document.getElementById(id);
        if (element) element.remove();
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
