import os
import sys
import requests
from dotenv import load_dotenv


from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

load_dotenv()

# Add your Computer Vision key and endpoint to your environment variables. 
VISION_APIKEY = os.getenv('VISION_APIKEY')
VISION_ENDPOINT = os.getenv('VISION_ENDPOINT')

def people_in_img (img) -> int:
    with open("/home/theo/Dev/FranceInter/api/app/images/"+img, "rb") as f:
        image_data = f.read()
    client = ImageAnalysisClient(
        endpoint=VISION_ENDPOINT,
        credential=AzureKeyCredential(VISION_APIKEY),
        logging_enable=True
    )
    visual_features =[
            VisualFeatures.PEOPLE,
        ]
    result = client.analyze(
        image_data=image_data,
        visual_features=visual_features,
        smart_crops_aspect_ratios=[0.9, 1.33],
        gender_neutral_caption=True,
        language="en"
    )
    people_with_accuracy = []
    print("Image analysis results:")
    if result.people is not None:
        print(" People:")
        for person in result.people.list:
            if person.confidence > 0.5 :
                people_with_accuracy.append(person.confidence)
    return len(people_with_accuracy)

def is_too_much_ppl(ppl_img, max_ppl) -> bool:
    if max_ppl:
        print(ppl_img)
        if ppl_img > max_ppl:
            return True
        else :
            return False
    return True
