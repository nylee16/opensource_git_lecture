#print("Hello World")
import cv2

# 카메라 열기 (0: 기본 웹캠, 1: 외부 카메라)
cap = cv2.VideoCapture(0)

# 카메라가 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:
        print("프레임을 가져올 수 없습니다.")
        break

    cv2.imshow('Camera', frame)  # 화면에 출력

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
