# **VAAYU: AI-Powered Air Quality Monitoring**



## 🌬️ Project Overview

**VAAYU** is an AI-powered system designed to estimate and forecast PM2.5 and PM10 air pollution levels across India, even in regions lacking ground-based sensors. Leveraging satellite data, weather patterns, and ML models, VAAYU bridges the air quality data gap in rural and underserved areas, delivering real-time insights and health guidance via a multilingual mobile interface and SMS/IVR channels.

---

## ✨ Features

* 📡 AI-based PM2.5/PM10 predictions using INSAT satellite data
* 🗺️ Real-time pollution heatmaps across India
* 📱 Multilingual mobile app with air quality forecasts and alerts
* 📞 SMS and IVR support for low-connectivity or non-smartphone users
* 🤖 ML model trained on limited ground sensor + satellite data
* 🔔 Personalized alerts and health recommendations

---

## 🛠️ Tech Stack

| Layer          | Technology                             |
| -------------- | -------------------------------------- |
| ML Models      | Scikit-learn, XGBoost, Pandas          |
| Satellite Data | INSAT, MODIS, Sentinel                 |
| Weather Data   | IMD (Indian Meteorological Department) |
| Mobile App     | Flutter (Dart), Firebase               |
| Backend        | Python, FastAPI                        |
| Alert System   | Twilio (SMS/IVR), FCM                  |
| Deployment     | AWS Lambda, S3, EC2                    |

---

## 📦 Local Setup (for model inference)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/vaayu.git
cd vaayu
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Inference Script

```bash
python predict_pm.py --lat 28.61 --lon 77.23 --date 2025-07-21
```

This returns PM2.5/PM10 estimates for the specified location and date.

---

## 📱 Mobile App Features

* 🔍 Search by PIN code or current location
* 📊 View daily and weekly air quality forecasts
* 🔔 Get health alerts based on AQI thresholds
* 🌐 Available in 8 Indian languages
* 🗣️ Call or receive SMS with localized pollution updates

---

## 📂 Project Structure

```
vaayu/
├── models/
│   ├── pm25_model.pkl
│   └── pm10_model.pkl
├── data/
│   ├── satellite/
│   └── ground/
├── mobile_app/
│   └── flutter_code/
├── backend/
│   ├── api.py
│   └── utils.py
├── alert_system/
│   └── ivr_sms_handler.py
├── predict_pm.py
├── requirements.txt
└── README.md
```

---

## 🔍 Example Output

```json
{
  "location": "Barmer, Rajasthan",
  "date": "2025-07-21",
  "PM2.5": 62.4,
  "PM10": 118.9,
  "AQI_Level": "Moderate",
  "advisory": "Sensitive groups should limit prolonged outdoor exertion."
}
```

---

## 🌍 Impact

* 📶 Works in areas with no sensors or limited connectivity
* 🏥 Helps vulnerable communities take early precautions
* 📈 Empowers NGOs, health workers, and policy makers with accurate data
* 📲 Brings air quality monitoring to every citizen's phone

---

## 🚧 Future Improvements

* 🛰️ Expand to global datasets for other countries
* 🧠 Fine-tune models with transfer learning
* 🕹️ Add interactive web dashboard for researchers
* 💬 WhatsApp alert bot integration

---

## 📄 License

Licensed under the **MIT License**.

---

## 🙌 Acknowledgments

* [ISRO](https://www.isro.gov.in/) for satellite imagery
* [IMD](https://mausam.imd.gov.in/) for meteorological datasets
* [Twilio](https://www.twilio.com/) for SMS/IVR infrastructure
* [Flutter](https://flutter.dev/) for the mobile app framework
* All communities working on climate data and clean air initiatives
