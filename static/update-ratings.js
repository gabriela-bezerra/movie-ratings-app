edit_ratings = document.querySelector

fetch('/users/<user_id>')
    .then((response) => response.json())
    .then((responseData) => {
        document.querySelector('#my-div').innerText = responseData;
    });