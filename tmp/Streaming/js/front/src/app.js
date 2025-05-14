const apiUrl = 'http://localhost:8001/contents';

document.addEventListener('DOMContentLoaded', () => {
    fetchContents();
});

function fetchContents() {
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            displayContents(data);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

function displayContents(contents) {
    const contentList = document.getElementById('content-list');
    contentList.innerHTML = '';

    contents.forEach(content => {
        const listItem = document.createElement('li');
        listItem.textContent = content.title; // Assuming 'title' is a field in the content object
        contentList.appendChild(listItem);
    });
}