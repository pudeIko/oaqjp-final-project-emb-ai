from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# init the flask app
emotionDetector = Flask("Sentiment Analyzer")

@emotionDetector.route("/emotionDetector")
def send_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # process the input
    # res = emotion_detector(text_to_analyze)
    # ang = res["anger"]
    # dis = res["disgust"]
    # fea = res["fear"]
    # joy = res["joy"]
    # sad = res["sadness"]
    # dom = res["dominant_emotion"]

    output_textx = (
        f"For the given statement, the system response is "
        f" 'anger': {res["anger"]}, "
        f"'disgust': {res["disgust"]}, "
        f"'fear': {res["fear"]}, "
        f"'joy': {res["joy"]} and "
        f"'sadness': {res["sadness"]}. "
        f"The dominant emotion is {res["dominant_emotion"]}."
    )

    # Return a formatted string with the sentiment label and score
    return output_textx

@emotionDetector.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




    # # Check if the label is None, indicating an error or invalid input
    # if label is None:
    #     return "Invalid input! Try again."
    # else:
    #     # Return a formatted string with the sentiment label and score
    #     return output_textx