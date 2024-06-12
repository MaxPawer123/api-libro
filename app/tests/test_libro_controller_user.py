
def test_get_libros_as_user(test_client, user_auth_headers):
    response = test_client.get("/api/libros", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_libro(test_client, admin_auth_headers):
    data = {"autor": "Diana", "titulo": "gatos_blancos", "edicion": "segunda","disponibilidad":"buena"}
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["autor"] == "Diana"
    assert response.json["titulo"] == "gatos_blancos"
    assert response.json["edicion"] == "segunda"
    assert response.json["disponibilidad"] =="buena"


def test_get_libro_as_user(test_client, user_auth_headers):
    response = test_client.get("/api/libros/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "autor" in response.json


def test_create_libro_as_user(test_client, user_auth_headers):
    data = {"autor": "Diana", "titulo": "gatos_blancos", "edicion": "segunda","disponibilidad":"buena"}
    response = test_client.post("/api/libros", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_update_libro_as_user(test_client, user_auth_headers):
    data = {"autor": "Diana", "titulo": "gatos_blancos", "edicion": "tercero","disponibilidad":"mal"}
    response = test_client.put("/api/libros/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_libro_as_user(test_client, user_auth_headers):
    response = test_client.delete("/api/libros/1", headers=user_auth_headers)
    assert response.status_code == 403
