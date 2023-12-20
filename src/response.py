# response structure
import json

class Response:
    def __init__(self) -> None:
        pass
    
    # defualt response
    def __str__(self) -> str:
        return "data"

    # json response
    def json(self,data,headers):
        json_data = []

        for item in data:

            json_item = {}

            for i,header in enumerate(headers):
                try:
                    json_item[header] = item[i]
                except TypeError as e:
                    print(f"err {e}")

            if json_item:
                json_data.append(json_item)

        json_string = json.dumps(json_data,indent=2)
        return json_string


