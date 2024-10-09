let map, marker;

function initMap() {
    var initialLocation = { lat: 28.7041, lng: 77.1025 }; // Default location (e.g., Delhi)
    
    map = new google.maps.Map(document.getElementById('map'), {
        center: initialLocation,
        zoom: 12
    });

    marker = new google.maps.Marker({
        position: initialLocation,
        map: map,
        draggable: true,
        title: "Clinic Location",

    });

    // Update hidden fields with the marker's initial position
    document.getElementById('id_latitude').value = initialLocation.lat;
    document.getElementById('id_longitude').value = initialLocation.lng;

    // Update hidden fields when marker is dragged
    google.maps.event.addListener(marker, 'dragend', function () {
        var latLng = marker.getPosition();
        document.getElementById('id_latitude').value = latLng.lat();
        document.getElementById('id_longitude').value = latLng.lng();
    });
}

function geocodeAddress(geocoder) {
    var city = document.getElementById('id_city').value;
    var state = document.getElementById('id_state').value;
    var zipcode = document.getElementById('id_zipcode').value;
    geocoder.geocode({ 'address': zipcode }, function (results, status) {
        if (status === 'OK') {
            // Center the map on the geocoded result
            map.setCenter(results[0].geometry.location);

            // Move the marker to the geocoded location
            marker.setPosition(results[0].geometry.location);

            // Update hidden fields with the geocoded position
            document.getElementById('id_latitude').value = results[0].geometry.location.lat();
            document.getElementById('id_longitude').value = results[0].geometry.location.lng();
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}

document.getElementById('id_zipcode').addEventListener('blur', function () {
    var geocoder = new google.maps.Geocoder();
    geocodeAddress(geocoder);
});
