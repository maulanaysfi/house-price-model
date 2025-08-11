const form = document.getElementById('predictForm');
const resultDiv = document.getElementById('result');

const areaRange = document.getElementById('areaRange');
const areaValue = document.getElementById('areaValue');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const payload = {
    Area: parseInt(formData.get('Area')),
    Room: parseInt(formData.get('Room')),
    Parking: formData.get('Parking') ? 1 : 0,
    Warehouse: formData.get('Warehouse') ? 1 : 0,
    Elevator: formData.get('Elevator') ? 1 : 0,
    };

    try {
    const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (response.ok && data.predicted_price !== undefined) {
        resultDiv.textContent = `Predicted Price: $${data.predicted_price.toLocaleString(undefined, { maximumFractionDigits: 2 })}`;
        resultDiv.className = "mt-6 text-xl font-semibold text-center text-green-600";
    } else {
        throw new Error('Invalid response');
    }
    } catch (error) {
    resultDiv.textContent = 'error: Could not get prediction';
    resultDiv.className = "mt-6 text-xl font-semibold text-center text-red-600";
    }

    resultDiv.classList.remove('hidden');
});

areaRange.addEventListener('input', () => {
    areaValue.textContent = areaRange.value;
});

console.log("script loaded successfully.")