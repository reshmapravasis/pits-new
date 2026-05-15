/**
 * components.js
 * Centralized logic for loading HTML components (header, footer)
 * and handling global navigation behaviors.
 */

function loadComponent(id, file) {
    console.log(`Attempting to load component: ${file} into ${id}`);
    fetch(file)
        .then(response => {
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return response.text();
        })
        .then(data => {
            const container = document.getElementById(id);
            if (!container) {
                console.error(`Container with ID ${id} not found.`);
                return;
            }
            container.innerHTML = data;
            
            // Re-execute script tags within the injected HTML
            const scripts = container.querySelectorAll("script");
            scripts.forEach(oldScript => {
                const newScript = document.createElement("script");
                Array.from(oldScript.attributes).forEach(attr => {
                    newScript.setAttribute(attr.name, attr.value);
                });
                newScript.appendChild(document.createTextNode(oldScript.innerHTML));
                oldScript.parentNode.replaceChild(newScript, oldScript);
            });

            // Initialize active state highlighting
            highlightActiveLink();
            
            console.log(`Successfully loaded: ${file}`);
        })
        .catch(err => {
            console.error(`Error loading component ${file}:`, err);
        });
}

function highlightActiveLink() {
    // Extract current page name (e.g., 'index.html' or 'about.html')
    const path = window.location.pathname;
    const page = path.split("/").pop() || "index.html";
    
    // Find all navigation links
    const links = document.querySelectorAll('nav a');
    
    links.forEach(link => {
        const href = link.getAttribute('href');
        
        // Check if link matches current page
        if (href === page) {
            // Apply active styles (matching your site's theme)
            link.classList.add('text-blue-500');
            link.classList.remove('text-gray-300');
            
            // Also handle mobile menu if necessary
            const dot = link.querySelector('.active-dot');
            if (dot) dot.classList.remove('hidden');
        }
    });
}

// Global initialization if needed
document.addEventListener('DOMContentLoaded', () => {
    // Potential for global AOS refresh if items are dynamic
    if (typeof AOS !== 'undefined') {
        AOS.refresh();
    }
});
