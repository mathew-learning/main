import pytest
import requests


class Test_proghis_apis():
    def test_id(self):
        response = requests.get("http://127.0.0.1:5000")
        assert response.status_code == 200
