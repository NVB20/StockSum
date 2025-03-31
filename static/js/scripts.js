let currentIndex = 0; // Track the current result index
const username = "{{ session.get('username', '') }}"; // Get session username safely

function updateNavigationButtons(totalResults) {
    document.getElementById('back-btn').disabled = (currentIndex === 0);
    document.getElementById('forward-btn').disabled = (currentIndex >= totalResults - 1);
}

function navigate(direction) {
    console.log(`Navigating: ${direction}`); // Debugging log
    fetch(`/navigate?direction=${direction}&current_index=${currentIndex}`)
        .then(response => response.json())
        .then(data => {
            console.log("Response from server:", data); // Debugging log
            if (data.result) {
                document.getElementById('result-container').style.display = 'block';
                document.getElementById('result-content').innerHTML = `
                    <h3>Calculation Results:</h3>
                    <p><strong>Candle High:</strong> ${data.result.high}</p>
                    <p><strong>Candle Low:</strong> ${data.result.low}</p>
                    <p><strong>Enter Position At:</strong> ${data.result.enter_position}$</p>
                    <p><strong>Stop Loss At:</strong> ${data.result.stop_loss}$</p>
                    <p><strong>Buy Amount of Stocks:</strong> ${data.result.stock_amount}</p>
                    <p><strong>Total Deal Cost:</strong> ${data.result.deal_cost}$</p>
                    <p><strong>Date:</strong> ${data.date}</p>
                `;
                currentIndex = data.new_index;
                updateNavigationButtons(data.totalResults);
            } else {
                console.error("Error from server:", data.error);
            }
        })
        .catch(error => console.error("Fetch error:", error));
}

// Fetch total results count on page load
window.onload = function () {
    if (username) {
        fetch(`/total_results?username=${username}`)
            .then(response => response.json())
            .then(data => {
                currentIndex = data.currentIndex || 0;
                updateNavigationButtons(data.totalResults || 0);
            })
            .catch(error => console.error("Error fetching total results:", error));
    }
};

function closeResult() {
    document.getElementById('result-container').style.display = 'none';
}
