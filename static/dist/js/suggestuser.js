
// Managing the formular submission
// let input_field = document.querySelector('#players-search-input');
// let input_length;
// input_field.addEventListener('keyup', function (event) {

//     user_input = event.target.value;
//     input_length = user_input.length;

//     if (input_length < 3) {

//         console.log(input_length);
//     } else {
//         fetch(window.location.href + "/autosuggest/"
//         ).then(response => response.json())
//             .catch(error => console.log(error))

//     }



// });


new Autocomplete('#autocomplete', {

    search: input => {
        console.log(input)
        const url = `/autosuggest/?query=${input}`
        return new Promise(resolve => {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    resolve(data.data)
                })
        })
    }
})



