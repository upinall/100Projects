const int redPin = 9; // Pins for RGB module
const int greenPin = 10;
const int bluePin = 11;
const int potPin = A0; // Potentiometer Pin

const int numReadings = 10; // Number of readings for smoothing
int readings[numReadings];  // Array to store the readings
int index = 0;              // Index of the current reading
int total = 0;              // Sum of the readings
int averagePotValue = 0;    // Averaged potentiometer value

void setColor(int red, int green, int blue) { // sets color of RGB module
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(potPin, INPUT);

  // Initialize the readings array and the total value
  for (int i = 0; i < numReadings; i++) {
    readings[i] = 0;
  }
}

void loop() {
  total = total - readings[index]; // Subtract the previous reading
  readings[index] = analogRead(potPin); // Read the potentiometer value (0-1023)
  total = total + readings[index]; // Add the current reading
  index = (index + 1) % numReadings; // Increment the index, wrap around if necessary

  averagePotValue = total / numReadings; // Calculate the average potentiometer value

  int redValue, greenValue, blueValue;
  
  // Switching between different colors now as the potentiometer is twisted!
  
  if (averagePotValue < 342) {
    redValue = map(averagePotValue, 0, 341, 255, 0);
    greenValue = map(averagePotValue, 0, 341, 0, 255);
    blueValue = 0;
  } else if (averagePotValue < 684) {
    redValue = 0;
    greenValue = map(averagePotValue, 342, 683, 255, 0);
    blueValue = map(averagePotValue, 342, 683, 0, 255);
  } else {
    redValue = map(averagePotValue, 684, 1023, 0, 255);
    greenValue = 0;
    blueValue = map(averagePotValue, 684, 1023, 255, 0);
  }

  setColor(redValue, greenValue, blueValue); // Set color based on the averaged potentiometer value
  delay(10); // Add a small delay for stability
}


/*

  While working with an Arduino Uno I got a bunch of sensors to mess with and this was one of many projects that demonstrate how I bring code to hardware.
  
  This specific program uses a potentiometer along with an RGB module to create a sliding color changer. It's really cool. I've documented notes to have you understand how this works!

*/
