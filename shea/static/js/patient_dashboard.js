function addHospitalToMap(lat, lon, name, hospitalId) {
    L.marker([lat, lon]).addTo(map)
        .bindPopup(
            `${name}<br><button onclick="requestAmbulance('${hospitalId}')">Request Ambulance</button>`
        );
}

function requestAmbulance(hospitalId) {
    fetch(`/patient/request-ambulance/${hospitalId}/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert("Ambulance request sent successfully.");
        } else {
            alert("Failed to send ambulance request.");
        }
    });
}
