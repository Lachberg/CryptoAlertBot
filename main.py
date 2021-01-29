from binance.client import Client
import time
from config import API_KEY, SECRET_KEY
from plyer import notification
from playsound import playsound


client = Client(API_KEY,SECRET_KEY)



def send_desktop_notification(title, message,):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\some9\\Desktop\\Crypto\\Alert\\icon.ico",
        timeout=5,
    )
    playsound('Bike Horn-SoundBible.com-602544869.wav')


def getprice(call_every=30,call_amount=-1,inidication_price):
    called = 0
    while(called != call_amount):
        called += 1
        info = client.get_symbol_ticker(symbol='DOGEBUSD')
        price = info['price']
        if(price > (inidication_price*5)):
            send_desktop_notification(title="DOGECOIN Price Change",message="DOGECOIN value is now atleast up by atleast 5 times!!!!")
        time.sleep(call_every)



getprice(call_every=360,inidication_price=0.05)






