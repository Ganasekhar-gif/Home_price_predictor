function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    if (!sqft.value || !location.value) {
        alert("Please enter area and select a location!");
        return;
    }

    var url = "http://127.0.0.1:5000/predict_home_price";
 // Adjust according to your server setup

    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    }, function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = `<h2>${data.estimated_price} Lakh</h2>`;
        console.log(status);
    }).fail(function() {
        alert("Error connecting to the server. Please try again later.");
    });
}

function onPageLoad() {
    console.log("Document loaded");

    var url = "http://127.0.0.1:5000/get_location_names"; // Adjust according to your server setup

    $.get(url, function(data, status) {
        console.log("Got response for get_location_names request");
        if (data && data.locations) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");

            $('#uiLocations').empty();
            locations.forEach(function(loc) {
                $('#uiLocations').append(new Option(loc, loc));
            });
        }
    }).fail(function() {
        alert("Failed to load locations. Check your API.");
    });
}

window.onload = onPageLoad;
