
def test_get_libros(test_client, admin_auth_headers):
    response = test_client.get("/api/libros", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_libro(test_client, admin_auth_headers):
    data = {"autor": "David", "titulo": "chanchos", "edicion": "primera","disponibilidad":"bueno"}
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["autor"] == "David"
    assert response.json["titulo"] == "chanchos"
    assert response.json["edicion"] == "primera"
    assert response.json["disponibilidad"] == "bueno"


def test_get_libro(test_client, admin_auth_headers):
    # Primero crea un libro
    data = {"autor": "Jose", "titulo": "ovejas", "edicion": "segunda_edicion","disponibilidad":"mal"}
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    # Ahora obtén el libro
    response = test_client.get(f"/api/libros/{libro_id}", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["autor"] == "Jose"
    assert response.json["titulo"] == "ovejas"
    assert response.json["edicion"] == "segunda_edicion"
    assert response.json["disponibilidad"] == "mal"

def test_get_nonexistent_libro(test_client, admin_auth_headers):
    response = test_client.get("/api/libros/999", headers=admin_auth_headers)
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"


def test_create_libro_invalid_data(test_client, admin_auth_headers):
    data = {"autor": "David"}  # Falta species y age
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"

def test_update_libro(test_client, admin_auth_headers):
    # Primero crea un libro
    data ={"autor": "David", "titulo": "gatos_negros", "edicion": "segunda","disponibilidad":"buena"}
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    # Ahora actualiza el libro
    update_data = {"autor": "David", "titulo": "gatos_negros", "edicion": "tercero","disponibilidad":"mal"}
    response = test_client.put(
        f"/api/libros/{libro_id}", json=update_data, headers=admin_auth_headers
    )
    assert response.status_code == 200
    assert response.json["edicion"] == "tercero"
    assert response.json["disponibilidad"] == "mal"


def test_update_nonexistent_animal(test_client, admin_auth_headers):
    update_data = {"autor": "Fabricio", "titulo": "perros", "edicion": "ultimo","disponibilidad":"mal"}
    response = test_client.put(
        "/api/libros/999", json=update_data, headers=admin_auth_headers
    )
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"
    
def test_delete_libro(test_client, admin_auth_headers):
    # Primero crea un libro
    data = {"autor": "Diana", "titulo": "gatos_blancos", "edicion": "segunda","disponibilidad":"buena"}
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]
    response = test_client.delete(
        f"/api/libros/{libro_id}", headers=admin_auth_headers
    )
    assert response.status_code == 204
    response = test_client.get(f"/api/libros/{libro_id}", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"


def test_delete_nonexistent_libro(test_client, admin_auth_headers):
    response = test_client.delete("/api/libros/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"

