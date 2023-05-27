document.addEventListener('DOMContentLoaded', function() {
    const content = document.querySelector(".content");
    const header =  document.querySelector(".header");

    const headerHeight = header.getBoundingClientRect().height;

    content.style.height = `${window.innerHeight - headerHeight}px`;
});