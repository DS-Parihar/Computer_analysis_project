import pandas as pd
import numpy as np

# Define the number of rows
n_rows = 500

# Define the trends
trend_price_speed = 15  # higher speed increases price
trend_price_hd = 0.2  # higher HD increases price
trend_price_ram = 70  # higher RAM increases price
trend_price_screen = 25  # larger screen increases price
trend_price_cd = 120  # having a CD increases price
trend_price_multi = 180  # having multiple cores increases price
trend_price_premium = 250  # being a premium product increases price
trend_price_ads = 8  # more ads increase price

# Hidden patterns
# - Price is lower for laptops with SSD (solid state drive)
# - Price is higher for laptops with touch screens
# - Price is higher for laptops with more USB ports
# - Price is lower for laptops with longer battery life
# - Price is higher for laptops with backlit keyboards
# - Price is higher for laptops with higher resolution screens
# - Price is higher for laptops with dedicated graphics cards

# Generate random data for each column
speed = np.random.randint(20, 100, n_rows)
hd = np.random.randint(80, 500, n_rows)
ssd = np.random.choice(['yes', 'no'], n_rows)
ram = np.random.randint(2, 32, n_rows)
screen = np.random.randint(14, 18, n_rows)
touch = np.random.choice(['yes', 'no'], n_rows)
usb = np.random.randint(1, 5, n_rows)
battery = np.random.randint(2, 10, n_rows)
backlit = np.random.choice(['yes', 'no'], n_rows)
resolution = np.random.randint(1080, 4096, n_rows)
graphics = np.random.choice(['dedicated', 'integrated'], n_rows)
cd = np.random.choice(['yes', 'no'], n_rows)
multi = np.random.choice(['yes', 'no'], n_rows)
premium = np.random.choice(['yes', 'no'], n_rows)
ads = np.random.randint(1, 100, n_rows)
trend = np.random.randint(1, 5, n_rows)

# Calculate the price based on the trends and hidden patterns
price = trend_price_speed * speed + trend_price_hd * hd - 150 * (ssd == 'yes') + trend_price_ram * ram + \
        trend_price_screen * screen + 150 * (touch == 'yes') + 50 * usb - 50 * battery + \
        100 * (backlit == 'yes') + 0.5 * resolution + 200 * (graphics == 'dedicated') + \
        trend_price_cd * (cd == 'yes') + trend_price_multi * (multi == 'yes') + \
        trend_price_premium * (premium == 'yes') + trend_price_ads * ads


# Add some noise to the price
price += np.random.normal(scale=50, size=n_rows)

# Create a DataFrame
data = pd.DataFrame({
    'price': price,
    'speed': speed,
    'hd': hd,
    'ssd': ssd,
    'ram': ram,
    'screen': screen,
    'touch': touch,
    'usb': usb,
    'battery': battery,
    'backlit': backlit,
    'resolution': resolution,
    'graphics': graphics,
    'cd': cd,
    'multi': multi,
    'premium': premium,
    'ads': ads,
    'trend': trend
})

# Save the DataFrame to a CSV file
data.to_csv('synthetic_data_with_hidden_patterns.csv', index=False)
