# APY Calculator Microservice

This microservice calculates and displays the potential earnings from different savings or investment accounts over a specified period. The calculation is based on the Annual Percentage Yield (APY), initial deposit, monthly deposit, and the investment period in years.

## Features

- **Calculate APY Savings:** Calculate the future value of investments using different APY rates.
- **Compare APYs:** Compare the future values of savings across different APY rates.
- **APY Savings Projection:** Estimate the total interest earned over a specified period.

## Endpoints

### `/calculate` (POST)

Calculate the future value of investments based on the provided parameters.

**Request Parameters:**
- `initial_deposit` (float): The initial amount of money deposited.
- `monthly_deposit` (float): The amount of money deposited monthly.
- `apy` (float): The annual percentage yield (in percent).
- `time_period` (int): The time period over which the money is invested (in years).

**Response:**
- `initial_deposit` (float): The initial deposit amount.
- `monthly_deposit` (float): The monthly deposit amount.
- `apy` (float): The annual percentage yield.
- `time_period` (int): The time period (in years).
- `total_savings` (float): The total savings after the specified period.
- `interest_earned` (float): The total interest earned after the specified period.

**Example Request:**
```json
{
    "initial_deposit": 1000,
    "monthly_deposit": 100,
    "apy": 5,
    "time_period": 12
}
```
**Example Response:**
```json
{
    "status": "Sent",
    "initial_deposit": 1000.0,
    "monthly_deposit": 100.0,
    "apy": 5.0,
    "time_period": 12,
    "total_savings": 28504.53,
    "interest_earned": 14504.53
}
```
## How to use the Microservice

**Install Dependencies:**
- pip install Flask
  
**Run the Flask Application:**
- python app.py

**Access the HTML Form:**
- Open your web browser and go to: (http://127.0.0.1:5000/)

## Using API Programmatically
You can also use the API programmatically by sending a POST request to the '/calculate' endpoint with a JSON payload. 

**Example with 'request' library:**
```python
import requests

url = 'http://127.0.0.1:5000/calculate'
payload = {
    "initial_deposit": 1000,
    "monthly_deposit": 100,
    "apy": 5,
    "time_period": 12
}

response = requests.post(url, json=payload)
data = response.json()
print(data)
```
## UML Sequence Diagram
![image](https://github.com/BlaytonV/APY-Calculator-Microservice/assets/129786072/aa0ae3eb-4fc4-491a-9d97-d89fd02b1d77)

