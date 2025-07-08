document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const closeSidebarButton = document.querySelector('.close-sidebar');
    const overlay = document.querySelector('.overlay');

    function openSidebar() {
        sidebar.classList.add('active');
        overlay.classList.add('active');
    }

    function closeSidebar() {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
    }

    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', openSidebar);
    }

    if (closeSidebarButton) {
        closeSidebarButton.addEventListener('click', closeSidebar);
    }

    // Attach closeSidebar to the global window object so it can be called from onclick in base.html
    window.closeSidebar = closeSidebar;

    // Toggle visibility of nested subject lists in the sidebar
    document.querySelectorAll('.sidebar-degree-program h4').forEach(header => {
        header.addEventListener('click', function() {
            const ul = this.nextElementSibling;
            if (ul && ul.tagName === 'UL') {
                ul.classList.toggle('collapsed');
            }
        });
    });

    document.querySelectorAll('.semester-name').forEach(span => {
        span.addEventListener('click', function(event) {
            event.stopPropagation(); // Prevent the degree program click from also triggering
            const ul = this.nextElementSibling;
            if (ul && ul.tagName === 'UL') {
                ul.classList.toggle('collapsed');
            }
        });
    });
}); 