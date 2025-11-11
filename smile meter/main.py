import random, cv2, time
import os

# Usar r-string para caminhos com caracteres especiais
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Tentar usar caminhos relativos
face_cascade_path = "haarcascade_frontalface_default.xml"
smile_cascade_path = "haarcascade_smile.xml"

# Verificar arquivos
print(f"Diretório atual: {BASE_DIR}")
print(f"Arquivo facial existe: {os.path.exists(face_cascade_path)}")
print(f"Arquivo sorriso existe: {os.path.exists(smile_cascade_path)}")

try:
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    smile_cascade = cv2.CascadeClassifier(smile_cascade_path)
    
    if face_cascade.empty():
        raise ValueError("Erro ao carregar o classificador facial")
    if smile_cascade.empty():
        raise ValueError("Erro ao carregar o classificador de sorriso")
        
except Exception as e:
    print(f"Erro ao carregar classificadores: {e}")
    exit(1)

video = cv2.VideoCapture(0)
num = 0

def smile_meter(frame, x1, y1):
    global num 
    if num > 4000:
        x = str(random.randint(0, 100))
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 0, 255)
        text = cv2.putText(frame,"your smile is",(int(x1)+15,int(y1)-70),font,1,color,4,cv2.LINE_AA)
        text = cv2.putText(frame,x+" %",(int(x1)+50,int(y1)-20), font,1,color,4,cv2.LINE_AA)
        time.sleep(15)
        num = 0
        return num
    else:
        x = str(random.randint(0,100))
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 0, 255)
        text = cv2.putText(frame,"Smile Meter",(int(x1)+15,int(y1)-70),font,1,color,4,cv2.LINE_AA)
        text = cv2.putText(frame,x+" %",(int(x1)+50,int(y1)-20), font,1,color,4,cv2.LINE_AA)
        num = num + 5
        return num

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for x,y,w,h in face:
        # Região de interesse (ROI) para detectar sorriso apenas dentro do rosto
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Desenha retângulo do rosto
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
        # Ajuste dos parâmetros para melhor detecção do sorriso
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.2,  # Reduzido para detectar melhor
            minNeighbors=22,  # Aumentado para reduzir falsos positivos
            minSize=(25, 25)  # Tamanho mínimo do sorriso
        )
        
        for x1,y1,w1,h1 in smile:
            # Ajusta coordenadas para a posição absoluta na imagem
            abs_x = x + x1
            abs_y = y + y1
            
            img = cv2.rectangle(frame,(abs_x,abs_y),(abs_x+w1,abs_y+h1),(255,0,0),2)
            smile_meter(frame,x,y)
    
    cv2.imshow("smile meter",frame)
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()