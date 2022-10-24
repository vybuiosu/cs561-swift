from fastapi import FastAPI
app = FastAPI()

@app.get("/info")
async def read_info_root():
    return {"Hello" : "This is mock weather"}

@app.get("/data/2.5/weather/lat={lat}&lon={lon}&appid={apikey}")
async def read_weather_mock(lat: float, lon: float, apikey: str):
    weather_json ={
    "coord": {
        "lon": lon,
        "lat": lat
    },
    "weather": [
        {
        "id": 800,
        "main": "Clear",
        "description": "clear sky",
        "icon": "01n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 290.14,
        "feels_like": 285.23,
        "temp_min": 284.16,
        "temp_max": 289.51,
        "pressure": 1016,
        "humidity": 86
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.54,
        "deg": 290
    },
    "clouds": {
        "all": 0
    },
    "dt": 1664609050,
    "sys": {
        "type": 1,
        "id": 3727,
        "country": "US",
        "sunrise": 1664633455,
        "sunset": 1664675654
    },
    "timezone": -25200,
    "id": 5720727,
    "name": "Corvallis",
    "cod": 200
    }
    
    return weather_json

#uvicorn WeatherMockAPI:app --reload
