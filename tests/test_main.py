from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_read_main():
    # 홈 페이지나 메인 라우트가 잘 열리는지 확인하는 테스트
    response = client.get("/")
    assert response.status_code == 200

def test_get_activities():
    # 액티비티 목록을 잘 가져오는지 확인하는 테스트
    response = client.get("/activities") # 만약 라우트 주소가 다르다면 유니티/FastAPI 주소에 맞게 수정
    assert response.status_code == 200