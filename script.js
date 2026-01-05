// IBDPal Website JavaScript

// Tab Navigation System
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tab navigation
    initializeTabNavigation();
    
    // Email form handling
    const emailForm = document.getElementById('emailForm');
    
    if (emailForm) {
        emailForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const email = document.getElementById('email').value;
            
            if (email) {
                // Show success message
                showNotification('Thank you! We\'ll notify you when IBDPal launches.', 'success');
                
                // Clear form
                document.getElementById('email').value = '';
            }
        });
    }
});

// Tab Navigation Functions
function initializeTabNavigation() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetTab = this.getAttribute('data-tab');
            
            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Show target tab content
            const targetContent = document.getElementById(targetTab);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });
}

// Notification system
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Style the notification
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#4dcc33' : '#9933cc'};
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 1000;
        font-weight: 500;
        max-width: 300px;
        animation: slideIn 0.3s ease-out;
    `;
    
    // Add animation keyframes
    if (!document.getElementById('notification-styles')) {
        const style = document.createElement('style');
        style.id = 'notification-styles';
        style.textContent = `
            @keyframes slideIn {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            @keyframes slideOut {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(100%); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    }
    
    // Add to page
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-in';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Add loading states to submit buttons only
document.addEventListener('DOMContentLoaded', function() {
    // Only target submit buttons, not tab navigation buttons
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    
    submitButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Store original text
            const originalText = this.textContent;
            
            this.style.opacity = '0.7';
            this.textContent = 'Sending...';
            
            setTimeout(() => {
                this.style.opacity = '1';
                this.textContent = originalText; // Restore original text
            }, 2000);
        });
    });
});

// Blog Share Functions
function shareOnFacebook(event) {
    event.preventDefault();
    const url = encodeURIComponent(window.location.href);
    const title = encodeURIComponent(document.querySelector('.blog-title')?.textContent || 'IBDPal Blog');
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank', 'width=600,height=400');
}

function shareOnTwitter(event) {
    event.preventDefault();
    const url = encodeURIComponent(window.location.href);
    const text = encodeURIComponent('Check out this blog post about IBDPal - A Simple Tool for Teens Living with IBD');
    window.open(`https://twitter.com/intent/tweet?url=${url}&text=${text}`, '_blank', 'width=600,height=400');
}

function shareViaEmail(event) {
    event.preventDefault();
    const url = window.location.href;
    const subject = encodeURIComponent('IBDPal Blog: A Simple Tool for Teens Living with IBD');
    const body = encodeURIComponent(`Check out this blog post: ${url}`);
    window.location.href = `mailto:?subject=${subject}&body=${body}`;
}

