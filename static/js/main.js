document.addEventListener('DOMContentLoaded', function() {
    const content = document.querySelector(".content");
    const header =  document.querySelector(".header");

    const headerHeight = header.getBoundingClientRect().height;

    content.style.height = `${window.innerHeight - headerHeight}px`;

});

document.addEventListener('click', e => {
    const isDropdownButton = e.target.matches('[dropdown-button]');
    const d = document.querySelector('.dropdown-menu');
    if (!isDropdownButton && e.target.closest('[dropdown]') != null) return;

    let currentDropdown;
    if (isDropdownButton) {
        currentDropdown = e.target.closest('[dropdown]');
        currentDropdown.classList.toggle('active');
        console.log('Dropdown:', currentDropdown, 'active:', currentDropdown.classList.contains('active'));

        if (currentDropdown.classList.contains('active')) {
            d.style.opacity = '1';

        } else {
            d.style.opacity = '0';
        }
    }

    document.querySelectorAll("[data-dropdown].active").forEach(dropdown => {
        if (dropdown === currentDropdown) return;
        dropdown.classList.remove('active');
        console.log('Dropdown:', dropdown, 'active:', dropdown.classList.contains('active'));
        d.style.opacity = '0';
    });
});
