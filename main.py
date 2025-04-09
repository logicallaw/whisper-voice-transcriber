import whisper
import os
import sys
import time
from tqdm import tqdm
import threading

# Whisper 모델 로드
model = whisper.load_model("small")  # 또는 "base", "tiny" 등

# MP3 파일 -> 텍스트 -> .txt 저장 함수
def transcribe_mp3_to_txt(mp3_path):
    print(f"🧠 MP3 파일 텍스트 변환 중: {mp3_path}")

    result = {}

    def run_transcription():
        result['data'] = model.transcribe(mp3_path)

    thread = threading.Thread(target=run_transcription)
    thread.start()

    # 진행률 표시 (실제 처리 시간 기반 추정)
    with tqdm(total=100, desc='⏳ 변환 중', ncols=100) as pbar:
        while thread.is_alive():
            time.sleep(0.1)
            pbar.update(1 if pbar.n < 100 else 0)
        pbar.n = 100
        pbar.refresh()

    text = result['data']['text']
    print("📝 인식된 텍스트:", text)

    txt_path = os.path.splitext(mp3_path)[0] + ".txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"📄 텍스트 파일 저장 완료: {txt_path}")

# 실행
if __name__ == "__main__":
    mp3_filename = "input.mp3"  # 변환할 MP3 파일명
    transcribe_mp3_to_txt(mp3_filename)