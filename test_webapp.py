from webapp.app import create_app
from webapp.db import get_db
from webapp.views.game import game_view

if __name__ == "__main__":
    app = create_app()
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert "Hello " in r.data.decode('utf-8')

    with app.app_context():
        assert isinstance(get_db().get_cards(), list)

    with app.test_request_context("/game"):
        app.preprocess_request()
        game_view()
