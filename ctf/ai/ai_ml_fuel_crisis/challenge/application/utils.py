import numpy as np
from io import BytesIO
from PIL import Image
import base64

class DockingException(Exception):
    pass

class Station():
    def __init__(self, spaceships, first_gate, second_gate) -> None:
        self.first_gate = first_gate
        self.second_gate = second_gate
        self.bannedId = "32166"
        self.spaceships = spaceships

    def passFirstGate(self, id_image):
        id_confidence = []
        id = ""
        for num in id_image:
            num = num.reshape(1,28,28,1)
            pred = self.first_gate.predict(num)
            id = id+str(np.argmax(pred))
            id_confidence.append(pred[0][np.argmax(pred)])
        return id, id_confidence

    def passSecondGate(self, id,  id_image, id_confidence, validation_check = True):
        validated_id = ""
        for i in range(len(id_image)):
            num = id_image[i].reshape(1,28,28,1)
            pred = self.second_gate.predict(num)
            if validation_check:
                if round(pred[0][int(id[i])],1) == round(id_confidence[i],1):
                    pass
                else:
                    raise DockingException("'s ID was misclassified.")

            validated_id = validated_id + str(np.argmax(pred))
        
        if validated_id == self.bannedId:
            raise DockingException("'s ID is banned from the station.")

            

class Spaceship():
    def __init__(self, id, name, id_image) -> None:
        self.id = id
        self.name = name
        self.id_image = id_image

    def idToBase64(self):
        mergedImage = np.concatenate((self.id_image), axis=1)
        pil_img = Image.fromarray(mergedImage)
        buff = BytesIO()
        pil_img.save(buff, format="JPEG")
        new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        return new_image_string
