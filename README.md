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

![Sequence UML diagram](https://github.com/user-attachments/assets/a10ab854-8793-466a-a96e-58cd6909f301)

**Runescape HiScores List**
![image](https://github.com/user-attachments/assets/c21118e0-fa55-4c01-8d35-66657bf6942b)


