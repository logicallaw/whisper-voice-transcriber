import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import os
import datetime

# 모델 로드
model = whisper.load_model("small")  # 필요한 경우 "small" 추천

# 마이크 녹음 함수
def record_audio(filename="recorded.wav", duration=5, samplerate=16000):
    print(f"🎙 {duration}초간 녹음 중...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    write(filename, samplerate, recording)
    print("✅ 녹음 완료")

# Whisper로 텍스트 변환
def transcribe_audio(filename):
    print("🧠 Whisper 모델로 텍스트 변환 중...")
    result = model.transcribe(filename)
    print("📝 인식된 텍스트:", result['text'])
    return result['text']

# 실행
if __name__ == "__main__":
    filename = f"record_{datetime.datetime.now().strftime('%H%M%S')}.wav"
    record_audio(filename=filename, duration=5)
    transcribe_audio(filename)
    os.remove(filename)  # 파일 자동 삭제 (선택)