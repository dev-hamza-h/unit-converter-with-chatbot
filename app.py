import streamlit as st
import requests


# Streamlit UI
st.set_page_config(page_title="UNIT CONVERTER", page_icon="⚖️")

# CUSTOM CSS UI 
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;    
    }
    
    .stApp {
        margin-bottom: 25px;
        background-color:rgb(38, 166, 212);
        box-shadow: 0px 8px 24px rgb(16, 221, 211);
      
    div[data-baseweb="select"] > div {
        background-color:rgb(170, 255, 251) !important;
    }
    input {
        background-color: rgb(170, 255, 251) !important;
    }    
           
    h1, label, span {
        text-align: start;
        font-weight: bold;
        background-color:rgb(170, 255, 251); 
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        transition: 0.3s;       
    }
    
    /* Sidebar bg */
    .stSidebar {
        margin-top: 57px;
        background-color:rgb(33, 122, 122);              
    }
    
    /* Arrow color change */
    .stSidebar button svg {
     fill: #20B2AA;  
    }

    .description {
        color:white;    
    } 
    
    .stButton>button {
        color: white !important;
        padding: 12px 60px;
        background:rgb(33, 122, 122);
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        transition: transform 0.3s ease-in-out;
        box-shadow: 0px 2px 12px rgba(48, 230, 224, 0.6);
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #217A7A, #2FA3A3);
    }
       
    .result {
     font-size: 20px;
     text-align: center;
     padding: 10px 20px; /* Balanced padding */
     border-radius: 8px; /* Smoother rounded corners */
     margin-top: 20px;
     box-shadow: 0px 2px 12px rgba(70, 247, 247, 0.82);
     width: fit-content; /* Adapts to content width */
     max-width: 80%; /* Prevents overflow */
     margin-left: auto;
     margin-right: auto; /* Centers the box */
     border: 2px solid #20B2AA;
     background-color: rgb(170, 255, 251);
    } 
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar for Language Selection
st.sidebar.title("Choose Language / اختر اللغة / 选择语言 / زبان منتخب کریں")
languages = ["English", "Urdu", "Arabic", "Chinese", "French", "German", "Hindi", "Spanish", "Turkish", "Russian"]
selected_language = st.sidebar.selectbox("", languages)

# ChatBOT Link
st.sidebar.markdown(
    """
    <h1>AI ChatBOT Mode?</h1>
    <a href="https://chatbot-ai-zh.streamlit.app/" target="_blank">
        <button class="animated-button">
            Use ChatBOT
        </button>
    </a>
    <style>
        .animated-button {
            background: linear-gradient(45deg, #ff0000, #ff7300,rgb(217, 199, 6),rgb(85, 219, 32), #00e1ff);
            background-size: 400% 400%;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            animation: gradientBG 3s ease infinite;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .animated-button:hover {
            transform: scale(1.05); /* Thoda bada hoga jab mouse aaye */
            box-shadow: 0px 0px 20px rgba(59, 193, 208, 0.8); /* Glow effect */
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
    </style>
    """, 
    unsafe_allow_html=True
)


# Dictionary for Multi-Language Support
translations = {
    "English": {
        "title": "Unit Converter: Effortlessly Switch Between Any Units",
        "description": "Easily convert: Length - Weight - Temperature - Currency - Time - Data storage - Speed - Energy - Volume.",
        "select_conversion": "Choose Conversion Type",
        "enter_value": "Enter Value",
        "from": "From",
        "to": "To",
        "convert": "Convert",
        "result_text": "is equal to",
        "conversion_success": "Conversion successful!"
    },
    "Urdu": {
        "title": "یونٹ کنورٹر: کسی بھی یونٹ کے درمیان بآسانی تبدیلی کریں",
        "description": "آسانی سے تبدیل کریں: لمبائی - وزن - درجہ حرارت - کرنسی - وقت - ڈیٹا اسٹوریج - رفتار - توانائی - حجم",
        "select_conversion": "تبدیلی کی قسم منتخب کریں",
        "enter_value": "ویلیو درج کریں",
        "from": "سے",
        "to": "تک",
        "convert": "تبدیل کریں",
        "result_text": "برابر ہے",
        "conversion_success": "تبدیلی کامیاب رہی!"
    },
    "Arabic": {
        "title": "محول الوحدات: التبديل بسهولة بين أي وحدات",
        "description": "تحويل بسهولة: الطول - الوزن - الحرارة - العملة - الوقت - تخزين البيانات - السرعة - الطاقة - الحجم",
        "select_conversion": "اختر نوع التحويل",
        "enter_value": "أدخل القيمة",
        "from": "من",
        "to": "إلى",
        "convert": "تحويل",
        "result_text": "يساوي",
        "conversion_success": "تم التحويل بنجاح!"
    },
    "Chinese": {
        "title": "单位转换器：轻松切换任意单位",
        "description": " 轻松转换：长度 - 重量 - 温度 - 货币 - 时间 - 数据存储 - 速度 - 能源 - 体积",
        "select_conversion": "选择转换类型",
        "enter_value": "输入值",
        "from": "从",
        "to": "到",
        "convert": "转换",
        "result_text": "等于",
        "conversion_success": "转换成功!"
    },
    "French": {
        "title": "Convertisseur d'unités : Changez facilement entre toutes les unités",
        "description": "Convertir facilement : Longueur - Poids - Température - Devise - Temps - Stockage des données - Vitesse - Énergie - Volume",
        "select_conversion": "Choisissez le type de conversion",
        "enter_value": "Entrez la valeur",
        "from": "De",
        "to": "À",
        "convert": "Convertir",
        "result_text": "équivaut à",
        "conversion_success": "Conversion réussie !"
    },
    "German": {
        "title": "Einheitenumrechner: Mühelos zwischen beliebigen Einheiten wechseln",
        "description": "Einfach umwandeln: Länge - Gewicht - Temperatur - Währung - Zeit - Datenspeicherung - Geschwindigkeit - Energie - Volumen",
        "select_conversion": "Wählen Sie den Konvertierungstyp",
        "enter_value": "Wert eingeben",
        "from": "Von",
        "to": "Nach",
        "convert": "Umwandeln",
        "result_text": "ist gleich",
        "conversion_success": "Umwandlung erfolgreich!"
    },
    "Hindi": {
        "title": "यूनिट कन्वर्टर: किसी भी इकाई के बीच आसानी से स्विच करें",
        "description": "आसानी से परिवर्तित करें: लंबाई - वजन - तापमान - मुद्रा - समय - डेटा भंडारण - गति - ऊर्जा - मात्रा",
        "select_conversion": "परिवर्तन प्रकार चुनें",
        "enter_value": "मान दर्ज करें",
        "from": "से",
        "to": "तक",
        "convert": "बदलें",
        "result_text": "के बराबर है",
        "conversion_success": "परिवर्तन सफल!"
    },
    "Spanish": {
        "title": "Convertidor de Unidades: Cambia fácilmente entre cualquier unidad",
        "description": "Convierte fácilmente: Longitud - Peso - Temperatura - Moneda - Tiempo - Almacenamiento de datos - Velocidad - Energía - Volumen",
        "select_conversion": "Elige el tipo de conversión",
        "enter_value": "Introduce el valor",
        "from": "De",
        "to": "A",
        "convert": "Convertir",
        "result_text": "es igual a",
        "conversion_success": "¡Conversión exitosa!"
    },
    "Turkish": {
        "title": "Birim Dönüştürücü: Herhangi bir birim arasında kolayca geçiş yapın",
        "description": " Kolayca dönüştürün: Uzunluk - Ağırlık - Sıcaklık - Para birimi - Zaman - Veri depolama - Hız - Enerji - Hacim",
        "select_conversion": "Dönüştürme Türünü Seçin",
        "enter_value": "Değer girin",
        "from": "Kimden",
        "to": "Kime",
        "convert": "Dönüştür",
        "result_text": "eşittir",
        "conversion_success": "Dönüştürme başarılı!"
    },
    "Russian": {
        "title": "Конвертер единиц: Легко переключайтесь между любыми единицами",
        "description": "Легко конвертировать: Длина - Вес - Температура - Валюта - Время - Хранение данных - Скорость - Энергия - Объем",
        "select_conversion": "Выберите тип конвертации",
        "enter_value": "Введите значение",
        "from": "Из",
        "to": "В",
        "convert": "Конвертировать",
        "result_text": "равно",
        "conversion_success": "Конвертация успешна!"
    }
}

# Select language dictionary
lang = translations.get(selected_language, translations["English"])

# Display UI using selected language
st.title(lang["title"])
st.write(lang["description"])

conversion_types = ["Length", "Weight", "Temperature", "Currency", "Time", "Data Storage", "Speed", "Energy", "Volume"]
conversion_type = st.selectbox(lang["select_conversion"], conversion_types)

value = st.number_input(lang["enter_value"], value=1.0)

units = {
    "Length": ["Meters", "Kilometers", "Miles", "Centimeters", "Millimeters", "Inches", "Feet", "Yards"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces", "Tons"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Currency": ["USD", "EUR", "PKR", "GBP", "INR", "JPY", "CAD", "AUD", "CNY"],
    "Speed": ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots"],
    "Time": ["Second", "Minute", "Hour", "Day"],
    "Data Storage": ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"],
    "Energy": ["Joules", "Kilojoules", "Calories", "Kilocalories", "Electronvolts"],
    "Volume": ["Liters", "Milliliters", "Gallons", "Cubic meters", "Cups"]
}


col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox(lang["from"], units.get(conversion_type, []))
with col2:
    to_unit = st.selectbox(lang["to"], units.get(conversion_type, []))


def convert_units(value, from_unit, to_unit, conversion_type):
    if conversion_type == "Currency":
        api_key = "3ceba6008e069fcde88ccbf4" 
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_unit}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if "conversion_rates" in data:
                rate = data["conversion_rates"].get(to_unit, None)
                if rate:
                    return round(value * rate, 4)
                else:
                    return "Invalid Currency"
            else:
                return "API Error: No conversion rates found"
        else:
            return f"API Error: {response.status_code} - {response.text}"
    
    conversion_factors = {
        "Length": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Centimeters": 100, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084, "Yards": 1.09361},
        "Weight": {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274, "Tons": 0.001},
        "Temperature": {"Celsius": lambda v: (v * 9/5) + 32 if to_unit == "Fahrenheit" else v, "Fahrenheit": lambda v: (v - 32) * 5/9 if to_unit == "Celsius" else v, "Kelvin": lambda v: v + 273.15 if to_unit == "Kelvin" else v},
        "Speed": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Knots": 1.94384},
        "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400},
        "Data Storage": {"Bytes": 1, "Kilobytes": 0.001, "Megabytes": 1e-6, "Gigabytes": 1e-9, "Terabytes": 1e-12, "Petabytes": 1e-15},
        "Energy": {"Joules": 1, "Kilojoules": 0.001, "Calories": 0.239006, "Kilocalories": 0.000239006, "Electronvolts": 6.242e+18},
        "Volume": {"Liters": 1, "Milliliters": 1000, "Gallons": 0.264172, "Cubic meters": 0.001, "Cups": 4.22675}
    }
    
    if conversion_type in conversion_factors:
        factors = conversion_factors[conversion_type]
        if from_unit in factors and to_unit in factors:
            if callable(factors[from_unit]):
                return round(factors[from_unit](value), 4)
            return round(value * (factors[to_unit] / factors[from_unit]), 4)
    
    return "Conversion not supported"

if st.button(lang["convert"]):
    result = convert_units(value, from_unit, to_unit, conversion_type)
    st.markdown(f"""
        <div class="result">
            {value} {from_unit} {lang['result_text']} {result} {to_unit}. {lang['conversion_success']}
        </div>
    """, unsafe_allow_html=True)
    
# Footer
st.markdown("<br><br><p style='text-align: center; color:background: linear-gradient(45deg, #217A7A, #2FA3A3); '>Created by Hamza Hassan</p>", unsafe_allow_html=True)