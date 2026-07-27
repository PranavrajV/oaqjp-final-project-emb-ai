from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def emo_detector():
    """
    Reads the 'textToAnalyze' query parameter from the URL,
    runs it through the emotion detector, and returns a formatted string.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is 'anger': {}, "
        "'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. "
        "The dominant emotion is {}.".format(
            response["anger"],
            response["disgust"],
            response["fear"],
            response["joy"],
            response["sadness"],
            response["dominant_emotion"],
        )
    )

@app.route('/')
def render_index_page():
    """
    Renders the main index.html page (must live in a 'templates' folder).
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", 5000)

