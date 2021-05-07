
#include <dht_nonblocking.h>
#define DHT_SENSOR_TYPE DHT_TYPE_11

#define MQ_PIN 0
#define RL_VALUE 20
#define RO_CLEAN_AIR_FACTOR 4.5

#define CALIBRATION_SAMPLE_TIMES 50
#define CALIBRATION_SAMPLE_INTERVAL 500

#define READ_SAMPLE_INTERVAL 50
#define READ_SAMPLE_TIMES  5

#define GAS_CO 0
#define GAS_LPG 1
#define GAS_SMOKE 2
#define GAS_CH4 3

float ro = 10;
float coCurve[] = {2.3, 0.64, -0.45};
float lpgCurve[] = {2.3, 0.41, -0.32};
float smokeCurve[] = {2.3, 0.59, -0.1};
float ch4Curve[] = {2.3, 0.25, -0.35};

int maskState = 0;
unsigned long maskTimeStamp;

static const int DHT_SENSOR_PIN = 2;
DHT_nonblocking dht_sensor( DHT_SENSOR_PIN, DHT_SENSOR_TYPE );

float vals[4];

float temp = 0;
float humid = 0;

unsigned long timeStamp;

float mqResist(float data) {
  return RL_VALUE * (4096 - data) / float(data);
}

float calibrateMq(int mq_pin) {
  float val = 0.0;
  for (int i = 0; i < CALIBRATION_SAMPLE_TIMES; i++) {
    val += mqResist(analogRead(0));
    delay(CALIBRATION_SAMPLE_INTERVAL);
  }
  val = val / CALIBRATION_SAMPLE_TIMES ;

  val = val / RO_CLEAN_AIR_FACTOR;
  return val;
}

void mqPercent() {
  float data = mqRead(MQ_PIN);
  vals[GAS_CO] = mqGetGas(data / ro, GAS_CO);
  vals[GAS_LPG] = mqGetGas(data / ro, GAS_LPG);
  vals[GAS_SMOKE] = mqGetGas(data / ro, GAS_SMOKE);
  vals[GAS_CH4] = mqGetGas(data / ro, GAS_CH4);
}

float mqRead(int mq_pin) {
  float rs = 0.0;

  for (int i = 0; i < CALIBRATION_SAMPLE_TIMES; i++) {
    rs += mqResist(analogRead(mq_pin));
    delay(READ_SAMPLE_INTERVAL);
  }
  rs = rs / READ_SAMPLE_TIMES;

  return rs;
}

float mqGetGas(float rs_ro_ratio, int gas_id) {
  if ( gas_id == GAS_LPG ) {
    return mqGetPercent(rs_ro_ratio, lpgCurve);
  }
  else if ( gas_id == GAS_CO ) {
    return mqGetPercent(rs_ro_ratio, coCurve);
  }
  else if ( gas_id == GAS_SMOKE ) {
    return mqGetPercent(rs_ro_ratio, smokeCurve);
  }
  else if (gas_id == GAS_CH4) {
    return mqGetPercent(rs_ro_ratio, ch4Curve);
  }
  return 0;
}

float mqGetPercent(float rs_ro_ratio, float pcurve[]) {
  return pow(10, ( ((log10(rs_ro_ratio) - pcurve[1]) / pcurve[2]) + pcurve[0]));
}

static bool dhtRead(float *temperature, float *humidity) {
  static unsigned long measurement_timestamp = millis( );
  /* Measure once every two seconds. */
  if (millis() - measurement_timestamp >= 2000ul) {
    if (dht_sensor.measure(temperature, humidity)) {
      measurement_timestamp = millis();
      return true;
    }
  }
  return false;
}

void setup() {
  pinMode(9, INPUT_PULLUP);
  Serial.begin(9600);
  Serial.println("Calibrating...");
  ro = calibrateMq(MQ_PIN);
  Serial.println("Starting data log");
  timeStamp = millis();
}


void loop() {
  if(digitalRead(9) == 0 && millis() > maskTimeStamp + 500ul){
    maskTimeStamp = millis();
    maskState = 1 - maskState;
  }
  //Values read every 2.78 seconds, in practice would be sent over bluetooth
  if (dhtRead(&temp, &humid)) {
    mqPercent();
    Serial.print(millis() - timeStamp);
    Serial.print(",");
    Serial.print(temp);
    Serial.print(",");
    Serial.print(humid);
    Serial.print(",");
    //Used in data collection stage
    //Serial.print(maskState);
    Serial.print(",");
    Serial.print(vals[0]);
    Serial.print(",");
    Serial.print(vals[1]);
    Serial.print(",");
    Serial.print(vals[2]);
    Serial.print(",");
    Serial.print(vals[3]);
    Serial.println();
  }
}
