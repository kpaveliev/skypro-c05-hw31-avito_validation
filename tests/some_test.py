
def test_root_not_found(client):
    response = client.get('/some')
    assert response.status_code == 404
