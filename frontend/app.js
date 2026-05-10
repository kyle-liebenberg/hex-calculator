// Grab the display elements
const mainDisplay = document.getElementById('main-display');
const equationDisplay = document.getElementById('equation-display');

// Variables to hold the state
let currentInput = '0';
let previousInput = '';
let currentOperation = null;

// Add event listeners to all generic buttons (numbers, hex, and operators)
document.querySelectorAll('.btn-num, .btn-hex').forEach(button => {
    button.addEventListener('click', () => {
        // Enforce the max 2-digit limit on the frontend side for better UX
        if (currentInput.length >= 2 && currentInput !== '0') return;

        if (currentInput === '0') {
            currentInput = button.dataset.val;
        } else {
            currentInput += button.dataset.val;
        }
        updateDisplay();
    });
});

document.querySelectorAll('.btn-op').forEach(button => {
    button.addEventListener('click', () => {
        if (currentInput === '0' && previousInput === '') return;
        
        currentOperation = button.dataset.val;
        previousInput = currentInput;
        currentInput = '0';
        
        equationDisplay.innerText = `${previousInput} ${currentOperation}`;
        updateDisplay();
    });
});

// Clear Button
document.getElementById('btn-clear').addEventListener('click', () => {
    currentInput = '0';
    previousInput = '';
    currentOperation = null;
    equationDisplay.innerText = '';
    updateDisplay();
});

// Equal Button (Placeholder for Video 2 API connection)
document.getElementById('btn-equal').addEventListener('click', async () => {
    if (!currentOperation || previousInput === '') return;
    
    // For Video 1: We just display a loading state. 
    // In Video 2, we will send these values to Python!
    equationDisplay.innerText = `${previousInput} ${currentOperation} ${currentInput} =`;
    mainDisplay.innerText = "Loading...";

    try {
        const response = await fetch('http://127.0.0.1:8000/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                val1: previousInput,
                val2: currentInput,
                operation: currentOperation
            })
        });

        const data = await response.json();

        if (response.ok) {
            mainDisplay.innerText = data.result;
            // Set the result as current input so we can chain math operations
            currentInput = data.result; 
        } else {
            mainDisplay.innerText = "Error";
            alert(data.detail); // Shows our Python ValueError constraints to the user 
        }
    } catch (error) {
        mainDisplay.innerText = "Error";
        console.error("API Error:", error);
    }

    previousInput = '';
    currentOperation = null;
});

function updateDisplay() {
    mainDisplay.innerText = currentInput;
}