"""server"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# init the flask app
EMOTION_DETECTOR = Flask("Sentiment Analyzer")

@EMOTION_DETECTOR.route("/emotionDetector")
def send_detector():
    """send_detector function."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # process the input
    res = emotion_detector(text_to_analyze)
    ang, dis, fea = res["anger"], res["disgust"], res["fear"]
    joy, sad, dom = res["joy"], res["sadness"], res["dominant_emotion"]

    # Return a formatted string
    if dom is None:
        output_text = "Invalid text! Please try again!"
    else:
        output_text = (
            f"For the given statement, the system response is "
            f"'anger': {ang}, "
            f"'disgust': {dis}, "
            f"'fear': {fea}, "
            f"'joy': {joy} and "
            f"'sadness': {sad}. "
            f"The dominant emotion is {dom}."
        )
    return output_text


@EMOTION_DETECTOR.route("/")
def render_index_page():
    """render index page"""
    return render_template('index.html')


if __name__ == "__main__":
    EMOTION_DETECTOR.run()
