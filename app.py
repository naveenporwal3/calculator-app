<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Calculator by Naveen</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Apply the Inter font for a modern look */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            /* Subtle radial gradient for depth and interest */
            background: radial-gradient(circle at 10% 20%, #e0f2fe 0%, #ffffff 100%);
            color: #1f2937; /* Default dark text color */
        }
        .calculator-card {
            /* Subtle blue glow */
            box-shadow: 0 15px 40px rgba(59, 130, 246, 0.25); 
        }
        input, select, button {
            transition: all 0.2s ease-in-out;
        }
        /* Custom class for button press effect */
        .calculate-button:active {
            transform: translateY(1px) scale(0.99); 
            box-shadow: 0 4px 10px rgba(234, 88, 12, 0.4); /* Subtle glow when pressed */
        }
        /* Style for the fixed sidebar on larger screens */
        @media (min-width: 1024px) {
            #instructions-sidebar {
                position: sticky;
                top: 1rem; /* Adjust based on desired top margin */
                height: fit-content;
            }
        }
    </style>
</head>
<body class="flex flex-col lg:flex-row items-center lg:items-start justify-center min-h-screen p-4">

    <!-- Instructions Sidebar (Placed on the left for large screens) -->
    <div id="instructions-sidebar" class="w-full max-w-sm lg:w-64 bg-blue-50 p-6 rounded-xl border border-blue-300 mb-6 lg:mb-0 lg:mr-8 text-sm space-y-3 shadow-lg">
        <h2 class="text-xl font-bold text-blue-700 border-b pb-2 mb-3 border-blue-200">📖 Instructions</h2>
        <div class="text-gray-700 space-y-2">
            <p>1. Enter two numbers **(A and B)** in the input fields.</p>
            <p>2. Select an **operator** from the dropdown menu.</p>
            <p>3. Click **CALCULATE RESULT** to see the solution.</p>
        </div>
        
        <div class="pt-3 border-t border-blue-200 text-xs text-blue-600 space-y-1">
            <p>Note: For **Square Root** and **Factorial**, only non-negative integers are valid.</p>
            <p class="font-semibold pt-1">Built by: Naveen Porwal</p>
        </div>
    </div>

    <!-- Calculator Card (Kept centered and focused) -->
    <div id="calculator-app" class="calculator-card w-full max-w-sm bg-white p-6 sm:p-8 rounded-2xl border border-blue-500">
        
        <!-- Header with a slight separator -->
        <header class="mb-6 pb-4 text-center border-b border-gray-200">
            <!-- Darker Blue primary text color for contrast -->
            <h1 class="text-3xl font-bold text-blue-600">🔢 Advanced Calculator</h1>
            <p class="text-gray-600 mt-1 text-sm">A sleek and powerful calculator for all your mathematical needs!</p>
        </header>

        <main class="space-y-5">
            <!-- Input A -->
            <div>
                <label for="numA" class="block text-sm font-medium text-gray-700 mb-1">First Number (A)</label>
                <input type="number" id="numA" value="10" placeholder="Enter number A"
                       class="w-full p-3 bg-gray-100 text-gray-800 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:ring-4 focus:ring-blue-100 appearance-none">
            </div>

            <!-- Input B -->
            <div>
                <label for="numB" class="block text-sm font-medium text-gray-700 mb-1">Second Number (B)</label>
                <input type="number" id="numB" value="5" placeholder="Enter number B"
                       class="w-full p-3 bg-gray-100 text-gray-800 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:ring-4 focus:ring-blue-100 appearance-none">
            </div>

            <!-- Operator Select -->
            <div>
                <label for="operator" class="block text-sm font-medium text-gray-700 mb-1">Operation</label>
                <select id="operator"
                        class="w-full p-3 bg-gray-100 text-gray-800 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:ring-4 focus:ring-blue-100 appearance-none">
                    <option value="Addition (+)">Addition (+)</option>
                    <option value="Subtraction (-)">Subtraction (-)</option>
                    <option value="Multiplication (*)">Multiplication (*)</option>
                    <option value="Division (/)">Division (/)</option>
                    <option value="Power (a^b)">Power (A^B)</option>
                    <option value="Modulo (a % b)">Modulo (A % B)</option>
                    <option value="Square Root (√a, √b)">Square Root (√A, √B)</option>
                    <option value="Factorial (a!, b!)">Factorial (A!, B!)</option>
                </select>
            </div>

            <!-- Calculate Button: Highlighted with a vibrant orange color and stronger shadow -->
            <button onclick="calculate()"
                    class="w-full py-3 mt-4 bg-orange-500 text-white font-extrabold rounded-lg shadow-xl hover:bg-orange-600 transition-all duration-200 transform hover:scale-[1.01] calculate-button">
                CALCULATE RESULT
            </button>

            <!-- Result Display -->
            <div id="result-display" class="pt-4">
                <p class="text-sm font-medium text-gray-700">Result:</p>
                <!-- Enhanced result box style: larger text, tracking, inner shadow -->
                <div id="result-value" class="min-h-[3rem] flex items-center justify-center p-3 text-lg sm:text-2xl font-mono font-extrabold text-center bg-gray-100 border-2 border-gray-200 rounded-lg text-amber-600 shadow-inner tracking-wider">
                    
                </div>
            </div>
        </main>
        
    </div>

    <script>
        // Get references to DOM elements
        const numAInput = document.getElementById('numA');
        const numBInput = document.getElementById('numB');
        const operatorSelect = document.getElementById('operator');
        const resultValueDiv = document.getElementById('result-value');
        const appCard = document.getElementById('calculator-app');
        
        /**
         * Helper function to compute factorial (n!).
         */
        function factorial(n) {
            n = Math.floor(n);
            if (n < 0) return 'Invalid (Negative)';
            if (n === 0 || n === 1) return 1;
            
            let res = 1;
            // Stop at a reasonable limit to prevent JavaScript overflow
            if (n > 20) return 'Too large'; 

            for (let i = 2; i <= n; i++) {
                res *= i;
            }
            return res;
        }

        /**
         * Performs the calculation based on user input.
         */
        function calculate() {
            // Parse inputs as floats. Use 0 as default if parsing fails.
            const a = parseFloat(numAInput.value) || 0;
            const b = parseFloat(numBInput.value) || 0;
            const operator = operatorSelect.value;
            let result;

            // Simple validation
            if (isNaN(a) || isNaN(b)) {
                showFeedback("❌ Please enter valid numbers.", 'error');
                return;
            }

            try {
                switch (operator) {
                    case 'Addition (+)':
                        result = a + b;
                        showFeedback(`✅ ${a} + ${b} = ${result.toFixed(2)}`, 'success');
                        break;
                    case 'Subtraction (-)':
                        result = a - b;
                        showFeedback(`✅ ${a} - ${b} = ${result.toFixed(2)}`, 'success');
                        break;
                    case 'Multiplication (*)':
                        result = a * b;
                        showFeedback(`✅ ${a} × ${b} = ${result.toFixed(2)}`, 'success');
                        break;
                    case 'Division (/)':
                        if (b === 0) {
                            showFeedback("❌ Cannot divide by zero.", 'error');
                            return;
                        }
                        result = a / b;
                        showFeedback(`✅ ${a} ÷ ${b} = ${result.toFixed(4)}`, 'success');
                        break;
                    case 'Power (a^b)':
                        result = Math.pow(a, b);
                        showFeedback(`✅ ${a} ^ ${b} = ${result.toFixed(4)}`, 'success');
                        break;
                    case 'Modulo (a % b)':
                        if (b === 0) {
                            showFeedback("❌ Cannot perform modulo by zero.", 'error');
                            return;
                        }
                        result = a % b;
                        showFeedback(`✅ ${a} % ${b} = ${result.toFixed(4)}`, 'success');
                        break;
                    case 'Square Root (√a, √b)':
                        let sqrt_a = a >= 0 ? Math.sqrt(a).toFixed(4) : "Invalid";
                        let sqrt_b = b >= 0 ? Math.sqrt(b).toFixed(4) : "Invalid";
                        
                        let a_text = a >= 0 ? `√${a} = ${sqrt_a}` : `√A: ${sqrt_a}`;
                        let b_text = b >= 0 ? `√${b} = ${sqrt_b}` : `√B: ${sqrt_b}`;

                        showFeedback(`✅ ${a_text} | ${b_text}`, 'success');
                        break;
                    case 'Factorial (a!, b!)':
                        if (a < 0 || b < 0 || a !== Math.floor(a) || b !== Math.floor(b)) {
                            showFeedback("❌ Factorial only defined for non-negative integers.", 'error');
                            return;
                        }
                        let fact_a = factorial(a);
                        let fact_b = factorial(b);
                        
                        showFeedback(`✅ ${a}!: ${fact_a} | ${b}!: ${fact_b}`, 'success');
                        break;
                    default:
                        showFeedback("❌ Invalid operator selected.", 'error');
                        return;
                }
            } catch (e) {
                showFeedback(`❌ Error: ${e.message}`, 'error');
            }
        }


        /**
         * Displays the calculation result or an error message and updates app card border.
         */
        function showFeedback(message, type) {
            resultValueDiv.textContent = message;
            
            // Reset classes
            resultValueDiv.classList.remove('text-amber-600', 'text-red-600');
            appCard.classList.remove('border-blue-500', 'border-red-600');
            
            // Apply new styles based on the result type
            if (type === 'success') {
                resultValueDiv.classList.add('text-amber-600'); 
                appCard.classList.add('border-blue-500'); 
            } else {
                // Ensure error messages are highly visible
                resultValueDiv.classList.remove('text-2xl'); 
                resultValueDiv.classList.add('text-lg', 'text-red-600'); 
                appCard.classList.add('border-red-600');
            }
        }
        
        // Run initial calculation when the page loads
        document.addEventListener('DOMContentLoaded', () => {
             // Initial calculation using default values
             calculate(); 
        });
    </script>
</body>
</html>
