  int trigPin = 9;  // Trigger pin of the SR04M-2 sensor
  int echoPin = 10; // Echo pin of the SR04M-2 sensor
  int trigPin_1 = 7;  // Trigger pin of the SR04M-2 sensor
  int echoPin_1 = 8;
  int trigPin_2 = 11;  // Trigger pin of the SR04M-2 sensor
  int echoPin_2 = 12;
  void setup() {
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(trigPin_1, OUTPUT);
    pinMode(echoPin_1, INPUT);
    pinMode(trigPin_2, OUTPUT);
    pinMode(echoPin_2, INPUT);
  }

  void loop() {
    long duration;
    long duration_1;
    long duration_2;
    float distance_cm;
    float distance_cm_1;
    float distance_cm_2;

    // Trigger the ultrasonic sensor
    digitalWrite(trigPin, LOW);
    digitalWrite(trigPin_1, LOW);
    digitalWrite(trigPin_2, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    digitalWrite(trigPin_1, HIGH);
    digitalWrite(trigPin_2, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    digitalWrite(trigPin_1, HIGH);
    digitalWrite(trigPin_2, HIGH);
    
    // Measure the echo duration
    duration = pulseIn(echoPin, HIGH);
    duration_1 = pulseIn(echoPin_1, HIGH);
    duration_2 = pulseIn(echoPin_2, HIGH);
    // Convert the duration to distance in centimeters
    distance_cm = duration * 0.034 / 2;
    distance_cm_1 = duration_1 * 0.034 / 2;
    distance_cm_2 = duration_2 * 0.034 / 2;

    // Print the distance to the serial monitor
    Serial.print("Distance: ");
    Serial.print(distance_cm);
    Serial.print("Distance1: ");
    Serial.print(distance_cm_1);
    Serial.print("Distance2: ");
    Serial.print(distance_cm_2);
    Serial.println("");

    // Delay before the next measurement
    delay(100);
    // You can adjust the delay to change the measurement rate
  }

