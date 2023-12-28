// Wrap the code in a function
function addLinkEventListeners() {
    // Get all the links with the 'underline-link' class
    const links = document.querySelectorAll('.underline-link');

    // Retrieve the previously selected link from localStorage
    const selectedLinkId = localStorage.getItem('selectedLinkId');
    const selectedLink = selectedLinkId ? document.getElementById(selectedLinkId) : null;

    // Add the underline class to the previously selected link, if any
    if (selectedLink) {
        selectedLink.classList.add('underline');
    }
    
    // Add a click event listener to each underline-link
    links.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            // Remove the underline from the previously selected link, if any
            console.log(link);
            console.log(selectedLink);
            if (selectedLink) {
            selectedLink.classList.remove('underline');
            }
    
            // Add the underline to the clicked link
            link.classList.add('underline');
            // Store the ID of the selected link in localStorage
            localStorage.setItem('selectedLinkId', link.id);

            setTimeout(() => {
                window.location.href = link.href; // Navigate to the target page
                }, 100);
        });
    });
}