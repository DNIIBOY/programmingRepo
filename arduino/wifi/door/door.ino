#include <ESP8266WiFi.h>
#include <Servo.h>

Servo myservo; // create servo object to control a servo

int servoRelay = 16; // D0
int servopin = 2; // D4
int moveDelay = 15; // Delay per degree of the servo.
int relayDelay = 400; // Delay between relay toggle and servo movement
int servoStartPos = 0; // Servo starting position
int servoEndPos = 172; // Servo ending position

int dcRelay = 5; // D1
int dcDuration = 5000; // Duration of dc motor spin

// WiFi credentials 
const char *ssid = "DMIL";
const char *password = "Leicester";

WiFiServer server(80); // Set web server port number to 80

String header; // Variable to store the HTTP request

String activeState = "off"; // State of system

// Current time
unsigned long currentTime = millis();
// Previous time
unsigned long previousTime = 0;
// Define timeout time in milliseconds (example: 2000ms = 2s)
const long timeoutTime = 2000;

void setup()
{
    Serial.begin(115200);
    // Initialize the output variables as outputs
    myservo.attach(servopin);
    pinMode(servoRelay, OUTPUT);
    pinMode(dcRelay, OUTPUT);
    // Invert relays
    digitalWrite(dcRelay, HIGH);
    digitalWrite(servoRelay, HIGH);

    // Connect to Wi-Fi network with SSID and password
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    // Print local IP address and start web server
    Serial.println("");
    Serial.println("WiFi connected.");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
    server.begin();
}

void loop()
{
    WiFiClient client = server.available(); // Listen for incoming clients

    if (client)
    {                                  // If a new client connects,
        Serial.println("New Client."); // print a message out in the serial port
        String currentLine = "";       // make a String to hold incoming data from the client
        currentTime = millis();
        previousTime = currentTime;
        while (client.connected() && currentTime - previousTime <= timeoutTime)
        { // loop while the client's connected
            currentTime = millis();
            if (client.available())
            {                           // if there's bytes to read from the client,
                char c = client.read(); // read a byte, then
                Serial.write(c);        // print it out the serial monitor
                header += c;
                if (c == '\n')
                { // if the byte is a newline character
                    // if the current line is blank, you got two newline characters in a row.
                    // that's the end of the client HTTP request, so send a response:
                    if (currentLine.length() == 0)
                    {
                        // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
                        // and a content-type so the client knows what's coming, then a blank line:
                        client.println("HTTP/1.1 200 OK");
                        client.println("Content-type:text/html");
                        client.println("Connection: close");
                        client.println();

                        // turns the GPIOs on and off
                        if (header.indexOf("GET /on") >= 0)
                        {
                            Serial.println("Activation signal recieved!");
                            activeState = "on";
                            spinMotor(dcRelay, dcDuration);
                            delay(200);
                            servoReturn(servoRelay, servoStartPos, servoEndPos, moveDelay, relayDelay, 2000);
                        }
                        else if (header.indexOf("GET /off") >= 0)
                        {
                            Serial.println("Deactivated page displayed");
                            activeState = "off";
                        }

                        // Display the HTML web page
                        client.println("<!DOCTYPE html><html>");
                        client.println("<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
                        client.println("<link rel=\"icon\" href=\"data:,\">");
                        // CSS to style the on/off buttons
                        client.println("<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center; background-color: black;}");
                        client.println(".buttonRed { background-color: #ff0000; border: none; color: white; padding: 64px 160px;");
                        client.println("text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}");
                        client.println(".buttonOff { background-color: #77878A; border: none; color: white; padding: 64px 160px;");
                        client.println("text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}");
                        client.println("h1 { color: white;}");
                        client.println("p { color: white;}</style></head>");

                        // Web Page Heading
                        client.println("<body><h1>Daniels Gamerserver</h1>");

                        client.println("<p>System status: " + activeState + "</p>");
                        // If the activeState is off, it displays the OFF button
                        if (activeState == "off")
                        {
                            client.println("<p><a href=\"/on\"><button class=\"button buttonOff\">OFF</button></a></p>");
                        }
                        else
                        {
                            client.println("<p><a href=\"/off\"><button class=\"button buttonRed\">RESET</button></a></p>");
                        }

                        client.println("</body></html>");

                        // The HTTP response ends with another blank line
                        client.println();
                        // Break out of the while loop
                        break;
                    }
                    else
                    { // if you got a newline, then clear currentLine
                        currentLine = "";
                    }
                }
                else if (c != '\r')
                {                     // if you got anything else but a carriage return character,
                    currentLine += c; // add it to the end of the currentLine
                }
            }
        }
        // Clear the header variable
        header = "";
        // Close the connection
        client.stop();
        Serial.println("Client disconnected.");
        Serial.println("");
    }
}

void servoReturn(int relay, int from, int to, int moveDelay, int relayDelay, int pause){
  
  int pos = 0;
  digitalWrite(relay, LOW);
  Serial.println("Servo relay off");
  delay(relayDelay);
  
  for (pos = from; pos <= to; pos += 1) {
      myservo.write(pos);
      Serial.println(pos);
      delay(moveDelay);
  }
  
  delay(pause);
  
  for (pos = 174; pos >= 0; pos -= 1) {
      myservo.write(pos);
      Serial.println(pos);
      delay(moveDelay);
  }
  
  delay(relayDelay);
  digitalWrite(servoRelay, HIGH);
  Serial.println("Servo relay on");
}

void spinMotor(int relay, int duration){
  digitalWrite(relay, LOW);
  Serial.println("DC relay off");
  delay(duration);
  digitalWrite(relay, HIGH);
  Serial.println("DC relay on");
}
