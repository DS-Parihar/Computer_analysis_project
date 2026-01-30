
URLS = {
    'home': 'https://localhost:8080/',
    'handling_missing_values': 'https://localhost:8080/handling_missing_values/',
    'set_outliers': 'https://localhost:8080//set_outliers/',
    'speed_v_price': 'https://localhost:8080/speed_v_price/',
    'touch_v_price': 'https://localhost:8080/touch_v_price/',
    'battery_v_price': 'https://localhost:8080/battery_v_price/',
    'backlit_v_price': 'https://localhost:8080/backlit_v_price/',
    'graphic_v_price': 'https://localhost:8080/graphic_v_price/',
}

def get_url(name, **kwargs):
    url = URLS[name]
    for key, value in kwargs.items():
        url = url.format(**{key: value})
    return url
