document.addEventListener('DOMContentLoaded', function() {
    var zipcodeField = document.getElementById('id_zipcode');

    zipcodeField.addEventListener('blur', function () {
        var zipcode = this.value;

        if (zipcode) {
            fetch(`https://api.postalpincode.in/pincode/${zipcode}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Invalid Zipcode');
                    }
                    return response.json();
                })
                .then(data => {
                    var city = data[0]['PostOffice'][0]['District'];
                    var state = data[0]['PostOffice'][0]['State'];

                    // Set the city and state fields with the fetched data
                    document.getElementById('id_city').value = city;
                    document.getElementById('id_state').value = state;
                })
                .catch(error => {
                    console.error('Error fetching city from zipcode:', error);
                    alert('Could not fetch city. Please check your zipcode.');
                });
        }
    });
});
