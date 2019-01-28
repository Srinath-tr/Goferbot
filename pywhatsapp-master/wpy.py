from whatsapp import Client
import base64

phone_to = "919715874993"
pwd = base64.b64encode("G1ZAzb/C4maCXBKY4hAEYoeIJW8=")
print pwd
client = Client('918124572345', pwd)
client.send_message(phone_to, 'Hello BR')
#client.send_media(phone_to, path='/Users/tax/Desktop/logo.jpg')
