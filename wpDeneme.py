import pywhatkit as kit
import time
import pyautogui
from datetime import datetime
import webbrowser

group_id = "FIXysJiDZjALjv2cLvoYYy"
message2 = ", plugun burada kalmus al"
group_link = f"https://web.whatsapp.com/accept?code={group_id}"
interval = 40  # 10 dakika = 600 saniye

while True:
    try:
        # Süreyi başlangıçta kaydet
        start_time = datetime.now()
        

        # Grubu aç ve mesajı gönder
        webbrowser.open(group_link)
        time.sleep(10)
        pyautogui.hotkey('ctrl', 'alt', 'q')  # @ işaretini yaz
        pyautogui.write('Ahmet Erer')   # Kalan kısım
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.write(message2, interval=0.1)
        pyautogui.press("enter")

        # Gönderim onayı
        print(f"Mesaj gönderildi: {start_time.strftime('%H:%M:%S')}")

        # Hassas bekleme süresi (10 dakika - işlem süresi)
        elapsed_time = (datetime.now() - start_time).total_seconds()
        sleep_time = max(interval - elapsed_time, 5)  # En az 5 saniye beklesin
        time.sleep(sleep_time)

    except Exception as e:
        print(f"Hata: {str(e)}")
        time.sleep(60)  # Hata durumunda 1 dakika bekle