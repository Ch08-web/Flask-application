document.getElementById('query-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const userInput = document.getElementById('user-input').value;
    
    fetch('/api/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
});
