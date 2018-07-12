import requests
import json
def nanonetf (file)
    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/efcfa8a3-0677-4ae1-b7b2-4db50e390ff6/LabelFile/'
    data = {'file': open('image.jpg', 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('d2QrDfG7m3OUnaxCRcttCXAiVTvaFOlg2zIoI5JIPus', ''), files=data)
    parsed_data = json.loads(response.text)
    items = parsed_data['result'][0]['prediction'][0]['score']
    return(items)

