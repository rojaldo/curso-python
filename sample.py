empresa = {
    "nombre": "Tech Co",
    "empleados": {
        "1": {"nombre": "Juan", "edad": 30},
        "2": {"nombre": "Ana", "edad": 25}
    }
}

for key, value in empresa.items():
    # check if value is a dictionary
    if isinstance(value, dict):
        for k, v in value.items():
            print(f'{k}: {v}')
    else:
        print(f'{key}: {value}')