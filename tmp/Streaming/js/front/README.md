# js-web-app

This is a simple web application that consumes a Django REST API using the Fetch API.

## Project Structure

```
js-web-app
├── src
│   ├── index.html       # Main HTML document
│   ├── app.js           # JavaScript code for the application
│   └── styles
│       └── style.css    # CSS styles for the web application
├── package.json         # npm configuration file
└── README.md            # Project documentation
```

## Getting Started

To set up and run the application, follow these steps:

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd js-web-app
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Open the application:**
   Open `src/index.html` in your web browser.

## Usage

The application fetches content from the Django REST API at the endpoint `/contents`. Ensure that your Django server is running and accessible.

## License

This project is licensed under the MIT License.