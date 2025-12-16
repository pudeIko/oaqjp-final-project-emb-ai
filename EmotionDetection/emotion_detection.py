import requests
import json

def emotion_detector(text_to_analyse):
    # URL, text to analyze and header
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request
    resp = requests.post(url, json=myobj, headers=header)

    output = {}
    output["anger"] = None
    output["disgust"] = None
    output["fear"] = None
    output["joy"] = None
    output["sadness"] = None
    output["dominant_emotion"] = None

    # Parsing the JSON response from the API
    if resp.status_code == 200:
        formatted = json.loads(resp.text)
        emotions = formatted["emotionPredictions"][0]["emotion"]
        dominant_val = 0
        for emotion in emotions.keys():
            output[emotion] = emotions[emotion]
            if emotions[emotion] > dominant_val:
                output["dominant_emotion"] = emotion
                dominant_val = emotions[emotion]
        return output
    elif resp.status_code == 400:
        return output

