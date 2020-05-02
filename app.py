from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Prediction import detecting_fake_news

app = Flask(__name__)
@app.route('/', methods=['POST'])
def sms():

    resp = MessagingResponse()
    inbMsg = request.values.get('Body')
    # print(inbMsg)
    pred, confidence = detecting_fake_news(inbMsg)

    resp.message(
        f'The news headline you entered is {pred[0]!r} and corresponds to {confidence[0][1]!r}.')
    return str(resp)

if __name__ == '__main__':
    app.run()
