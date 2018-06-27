# HTTP Client and Server frameworks.
from http.client import HTTPSConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

# Webpage parser framework.
# Install: pip3 install beautifulsoup4
from bs4 import BeautifulSoup


# Object that Python uses to route incoming HTTP requests.
class RequestHandler(BaseHTTPRequestHandler):
    # Handle and route GET HTTP requests.
    def do_GET(self):
        if self.path == "/":
            display_temperature(handler = self)
        else:
            send_error_page(handler = self)


# Handle HTTP requests with URL paths that are routed for loading the weather.
def display_temperature(handler):
    handler.send_response(200)
    handler.send_header("Content-type", "text/html; charset=utf-8")
    handler.end_headers()
    handler.wfile.write(bytes("<h1>" + get_temperature() + "</h1>", "utf-8"))


# Downloads the forecast webpage, parse the HTML, and scrape the temperature.
def get_temperature():
    # Open a connection to the domain.
    conn = HTTPSConnection("forecast.weather.gov")

    # Make a request to load the forecast webpage.
    conn.request("GET", "/MapClick.php?lat=42.5067&lon=-89.0379",
        headers={"User-agent": "educational"})

    # Get the response from the request.
    resp = conn.getresponse()

    # Read the content of the request payload.
    body = resp.read()

    # Close the connection to cleanup resources.
    conn.close()

    # Parse the webpage's HTML.
    soup = BeautifulSoup(body, "html.parser")

    # Find the HTML Element with the temperature value.
    elm = soup.find("p", class_="myforecast-current-lrg")

    # Return the text value of the temperature Element.
    return elm.text


# Handle HTTP requests that do not match an expected URL path.
def send_error_page(handler):
    handler.send_response(404)
    handler.send_header("Content-type", "text/html; charset=utf-8")
    handler.end_headers()
    handler.wfile.write(bytes("<p>404 - Page not found</p>", "utf-8"))


# Start the server and run it until it is signalled to stop.
def run_server():
    print("Starting server...")

    # Create the HTTP server bound to all hosts on a specific port.
    server = HTTPServer(("", 8080), RequestHandler)

    try:
        # Keep the HTTP server running until signalled to stop.
        server.serve_forever()
    except KeyboardInterrupt:
        pass # Ignore KeyboardInterrupt exceptions.

    # Stop the HTTP server from running.
    server.server_close()

    print("Server stopped.")


# Start the server; to view the webpage, visit: http://localhost:8080/
run_server()
