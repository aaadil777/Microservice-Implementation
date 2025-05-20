# Wilson's RuneScape Hiscores Microservice

This README defines the communication contract for the microservice implemented for Wilson Ku's Price & Skills Tracker game. This contract is fixed and will not change to ensure reliability for the teammate.

## Communication Contract

### Instructions for Programmatically Requesting Data

To request data from the microservice, send a POST request to the `/fetch-hiscores/` endpoint with a JSON body containing the `player_name` field. The microservice will append the player name to the RuneScape Hiscores API URL and return the fetched JSON data.

- **Endpoint**: `http://localhost:8000/fetch-hiscores/`
- **Method**: POST
- **Content-Type**: `application/json`
- **Request Body**: `{"player_name": "<player_name>"}` (e.g., `{"player_name": "Aadil Ali"}`)
- **Example Call** (using Python with `requests`):
  ```python
  import requests

  url = "http://localhost:8000/fetch-hiscores/"
  payload = {"player_name": "Aadil Ali"}
  response = requests.post(url, json=payload)
  if response.status_code == 200:
      data = response.json()
      print(data)
  ```

### Instructions for Programmatically Receiving Data

The microservice returns a JSON response with the following structure:
- `status`: String indicating "success" or "error"
- `message`: String with a delivery status or error message
- `player`: String with the requested player name
- `hiscores`: JSON object (present only if status is "success") or absent if an error occurs

- **Response Format** (Success):
  ```json
  {
    "status": "success",
    "message": "Data delivered",
    "player": "Aadil Ali",
    "hiscores": {...}
  }
  ```
- **Response Format** (Error):
  ```json
  {
    "status": "error",
    "message": "404 Client Error: Not Found for url: ...",
    "player": "Aadil Ali"
  }
  ```
- **Example Call** (using Python with `requests`):
  ```python
  import requests

  url = "http://localhost:8000/fetch-hiscores/"
  payload = {"player_name": "Aadil Ali"}
  response = requests.post(url, json=payload)
  if response.status_code == 200:
      data = response.json()
      if data["status"] == "success":
          hiscores = data["hiscores"]
          print("Hiscores:", hiscores)
      else:
          print("Error:", data["message"])
  ```

### UML Sequence Diagram

```
@startuml
actor "Wilson's Main Program"
participant "Microservice"
participant "RuneScape API"

== Request Data ==
Wilson's Main Program -> Microservice: POST /fetch-hiscores/ {player_name: "Aadil Ali"}
Microservice -> RuneScape API: GET https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player=Aadil Ali
RuneScape API --> Microservice: JSON Response (Hiscores Data)
Microservice --> Wilson's Main Program: JSON Response {status: "success", message: "Data delivered", player: "Aadil Ali", hiscores: {...}}

== Error Case ==
Wilson's Main Program -> Microservice: POST /fetch-hiscores/ {player_name: "InvalidPlayer"}
Microservice -> RuneScape API: GET https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player=InvalidPlayer
RuneScape API --> Microservice: HTTP 404 Error
Microservice --> Wilson's Main Program: JSON Response {status: "error", message: "404 Client Error: Not Found", player: "InvalidPlayer"}
@enduml
```

*Note: Use a PlantUML-compatible tool to render the above diagram.*

