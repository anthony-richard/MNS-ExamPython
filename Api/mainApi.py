from fastapi import Request, FastAPI
from json import JSONDecodeError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
import vehicule

app = FastAPI()

###Routes
####1ère route
@app.get("/")
def index():
    return {"info": "api fonctionne"}

####2ème route
@app.post("/creation")
def createVehicule(request: Request):
    try:
        data : {
            "id ": request.get['id'],
            "type" : request.get['type'],
            "nom" : request.get['nom'],
            "marque" : request.get['marque'],
            "vitesseMax" : request.get['vitesseMax'],
            "km" : request.get['km']
        }
    ### instance qui ne marche pas donc le reste aussi ... pourquoi ?
    instancedata = vehicule(data)
    print(instancedata)
    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body'})
    except:
        return JSONResponse({'error': 'interne depuis le serveur'})
    return JSONResponse({'test': "test"})


####3ème route
@app.get("/nbVehicules")
def nbVehicule():
    if instancedata in globals():
        totalVehicule += 1
    return {"info": "nombre de véhicules : {totalVehicule}"}

####4ème route
@app.get("/nbVehicules/nbTypeVehicules")
def nbVehiculeType():
    ### incrémentation de 1 après le calcul de la longueur
    for i in type:
        len(type[i])
        type[i+1]
    return {'info': 'nombre de véhicules par type {type[0]}{type[1]}{type[2]}{type[3]}'}

####5ème route
@app.get("/nbVehicules/vehicule/{id}")
def getVehicule(id: int):
    print(f"Voici le véhicule ayant l'id numéro : {id}")


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "endpoint not found" })