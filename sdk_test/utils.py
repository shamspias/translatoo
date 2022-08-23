import io
import os
import warnings

from IPython.display import display
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


def get_image(prompt_text, api_key):
    stability_api = client.StabilityInference(
        # key="sk-DjokWBqmsW7VP1TyWUoofT8NbsxmRFvp6rRixz8xpjFE5MzN",
        key=api_key,
        verbose=True,
    )

    # the object returned is a python generator
    answers = stability_api.generate(
        prompt=prompt_text
    )

    # iterating over the generator produces the api response
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                # img = Image.open(io.BytesIO(artifact.binary))
                img = io.BytesIO(artifact.binary)
                # display(img)
                return img
