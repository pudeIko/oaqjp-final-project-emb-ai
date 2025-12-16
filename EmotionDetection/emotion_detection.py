import requests
import json

def emotion_detector(text_to_analyse):
    # URL, text to analyze and header
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request
    resp = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted = json.loads(resp.text)

    emotions = formatted["emotionPredictions"][0]["emotion"]
    dominant_val = 0
    for emotion in emotions.keys():
        if emotions[emotion] > dominant_val:
            dominant_emotion = emotion
            dominant_val = emotions[emotion]

    emotions["dominant_emotion"] = dominant_emotion

    return emotions

    # label = formatted['documentSentiment']['label']
    # score = formatted['documentSentiment']['score']

    # Returning a dictionary
    # return {'label': label, 'score': score}




    # # If the response status code is 200, extract the label and score from the response
    # if response.status_code == 200:
    #     label = formatted_response['documentSentiment']['label']
    #     score = formatted_response['documentSentiment']['score']
    # # If the response status code is 500, set label and score to None
    # elif response.status_code == 500:
    #     label = None
    #     score = None