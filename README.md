# ml
POC zu ML

## Install using pip

`cd` to `service`

    pip install -r requirements.txt
   
## Docker Container bauen für den Service

`cd` to `service`

    sudo docker build -t ml .
    
## Docker Container start und service starten

`cd` to `service`

    sudo docker run -it -p 5000:5000 ml:latest /bin/bash
    
Im Container dann:

    python /service/service.py
    
    

## Example Request

```javascript
{
	"name": "Annette",
	"gender": 1,
	"numChildren": 1,
	"ownsHouse": 1,
	"yearBorn": 1990,
	"numCats": 0,
	"numDogs": 1,
	"numHorses": 0
}
```
