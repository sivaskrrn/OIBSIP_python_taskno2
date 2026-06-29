# OIBSIP_python_taskno2


### Objective

To develop a Python application that retrieves and displays the current weather information for a user-specified location using an online weather service.

### Steps Performed

1. Imported the required Python modules (`json`, `urllib`, and `datetime`).
2. Accepted a city name or ZIP/postal code as input from the user.
3. Sent a request to the **wttr.in** weather service.
4. Parsed the JSON response received from the server.
5. Extracted weather details such as temperature, humidity, wind speed, pressure, and weather condition.
6. Displayed the weather report in a clear, formatted layout.
7. Included error handling for invalid locations, network issues, and unexpected responses.

### Tools Used

* **Programming Language:** Python
* **Modules/Libraries:**

  * `json` – to parse JSON weather data.
  * `urllib.request`, `urllib.parse`, `urllib.error` – to send HTTP requests and handle errors.
  * `datetime` – to display the current date and time.
* **Weather API/Service:** **wttr.in**
* **Development Environment:** Any Python IDE (e.g., IDLE, VS Code, PyCharm, or Jupyter Notebook).

### Outcome

A Python-based weather checker was successfully developed. It fetches and displays real-time weather information for any valid location, including temperature, humidity, wind details, pressure, and weather conditions, with appropriate error handling for a smooth user experience.
