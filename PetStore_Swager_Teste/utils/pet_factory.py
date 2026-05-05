

PETS_PRE_DEFINIDOS = [
    {
        "id": 0,
        "category": {"id": 1, "name": "cachorro"},
        "name": "Rex",
        "photoUrls": ["https://exemplo.com/rex.jpg"],
        "tags": [{"id": 1, "name": "vacinado"}],
        "status": "available"
    },
    {
        "id": 0,
        "category": {"id": 1, "name": "cachorro"},
        "name": "Bolt",
        "photoUrls": ["https://exemplo.com/bolt.jpg"],
        "tags": [{"id": 2, "name": "castrado"}],
        "status": "pending"
    },
    {
        "id": 0,
        "category": {"id": 2, "name": "gato"},
        "name": "Lola",
        "photoUrls": ["https://exemplo.com/lola.jpg"],
        "tags": [{"id": 1, "name": "vacinado"}],
        "status": "available"
    },
    {
        "id": 0,
        "category": {"id": 2, "name": "gato"},
        "name": "Mimi",
        "photoUrls": ["https://exemplo.com/mimi.jpg"],
        "tags": [{"id": 3, "name": "filhote"}],
        "status": "sold"
    },
    {
        "id": 0,
        "category": {"id": 3, "name": "passaro"},
        "name": "Tweety",
        "photoUrls": ["https://exemplo.com/tweety.jpg"],
        "tags": [{"id": 2, "name": "castrado"}],
        "status": "available"
    },
]

def criar_pet(nome="doggie", status="available", pet_id=0):
    return {
        "id": pet_id,
        "category": {"id": 0, "name": "cachorro"},
        "name": nome,
        "photoUrls": ["https://exemplo.com/foto.jpg"],
        "tags": [{"id": 0, "name": "vacinado"}],
        "status": status
    }

    