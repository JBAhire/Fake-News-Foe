# Fake-News-Foe
**Fake news** has become a huge issue in our digitally-connected world and it is no longer limited to little squabbles -- fake news spreads like wildfire and is impacting millions of people every day.

How do you deal with such a sensitive issue? Countless articles are being churned out every day on the internet -- how do you tell real from fake? It's not as easy as turning to a simple fact-checker which is typically built on a story-by-story basis. As developers, can we turn to machine learning?

Read the detailed article here: https://dev.to/twilio/fake-news-foe-machine-learning-and-twilio-5fln

Aim:
----

We will be building a WhatsApp based service which will accept news headlines from the user and predict if given news is fake news or not.

Requirements:
-------------

-   A Twilio account ---[  sign up for a free one here](https://www.twilio.com/try-twilio)

-   A Twilio whatsapp sandbox ---[  configure one here](https://www.twilio.com/console/sms/whatsapp/sandbox)

-   [Set up your Python and Flask developer environment](https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment) --- Make sure you have Python 3 downloaded as well as[  ngrok](https://ngrok.com/).

-   Tensorflow
- Run `pip install -r requirements.txt`

Demo:
----------

1. `Run app.py`

![Running Flask App](https://s3.amazonaws.com/fininity.tech/Blog_images/terminal-2.png)

2. Your Flask app will need to be visible from the web so Twilio can send requests to it. Ngrok lets us do this. With it installed, run the following command in your terminal in the directory your code is in. Run `ngrok http 5000` in a new terminal tab.

![ngrok](https://s3.amazonaws.com/fininity.tech/Blog_images/terminal-1.png)

3. Grab that ngrok URL to configure twilio whatsapp sandbox. We will try this on WhatsApp! So let’s go ahead and do it (either on our Sandbox if you want to do testing or your main WhatsApp Sender number if you have one provisioned). In a screenshot below we show the Sandbox page:

![Configuring Twilio Sandbox](https://s3.amazonaws.com/fininity.tech/Blog_images/twilio-console.png)

And we’re good to go! Let’s test our application on WhatsApp! We can send some news headlines or facts to this sandbox and get predictions in return if everything works as expected.

![Test App](https://s3.amazonaws.com/fininity.tech/Blog_images/whatsapp.png)

Hurray! You wanna try this? Complete code is available on [GitHub](https://github.com/jbahire/fake-news-foe).

## References:
1. ["Liar, Liar Pants on Fire": A New Benchmark Dataset for Fake News Detection](https://arxiv.org/abs/1705.00648)
2. [Twilio WhatsApp API](https://www.twilio.com/docs/sms/whatsapp/api)
3. [Fake News Detection with LIAR Dataset](https://github.com/nishitpatel01/Fake_News_Detection)
4. [What is Fake News?](https://30secondes.org/en/module/what-is-fake-news/)
5. [FEVER: a large-scale dataset for Fact Extraction and VERification](https://arxiv.org/pdf/1803.05355.pdf)





