import requests

# The Shawshank Redemption 포스터 이미지 URL
image_url = "http://image.tmdb.org/t/p/w185/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg"

# 이미지 요청
response = requests.get(image_url)

# 이미지 다운로드 및 저장
if response.status_code == 200:
    with open("shawshank_redemption_poster.jpg", "wb") as file:
        file.write(response.content)
    print("이미지 다운로드 완료: shawshank_redemption_poster.jpg")
else:
    print("이미지 다운로드 실패. 상태 코드:", response.status_code)