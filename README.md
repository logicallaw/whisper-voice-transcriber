# 🎙 Whisper 음성 인식 프로젝트 (Mac + Conda)

이 프로젝트는 Whisper 모델을 통해 마이크로부터 직접 음성을 녹음하고, 이를 실시간으로 텍스트로 변환하는 데모입니다. Conda 환경과 Mac 환경을 기준으로 설정되었으며, 학습 및 개인 프로젝트용으로 최적화되어 있습니다.

---

## ✅ 환경 구성

### 1. Conda 환경 생성 및 활성화

```bash
conda create -n whisper-env python=3.9 -y
conda activate whisper-env
```

### 2. 필수 라이브러리 설치

먼저 `portaudio`를 설치합니다. (sounddevice 사용을 위해 필요)

```bash
brew install portaudio
```

그 다음, 아래 명령어로 Python 패키지를 설치합니다:

```bash
pip install git+https://github.com/openai/whisper.git
pip install sounddevice scipy numpy torch
```

또는 `requirements.txt` 파일을 사용할 수 있습니다:

```txt
# requirements.txt
sounddevice
scipy
numpy
torch
git+https://github.com/openai/whisper.git
```

```bash
pip install -r requirements.txt
```

### 3. 마이크 권한 설정 (macOS)
	•	시스템 환경설정 → 보안 및 개인 정보 보호 → 마이크 → 터미널 또는 Visual Studio Code에 마이크 권한을 허용해야 합니다.

---

🚀 실행 방법

python main.py

실행하면 아래 순서로 동작합니다:
	1.	Whisper 모델(small)을 다운로드합니다 (최초 1회)
	2.	마이크로부터 5초간 음성을 녹음합니다
	3.	Whisper가 텍스트로 변환해 출력합니다
	4.	.wav 파일은 자동으로 삭제됩니다

---

📂 프로젝트 구조

newProjectPy/
├── main.py
└── requirements.txt

---

🧠 참고 사항
	•	whisper.load_model("small") → 속도/정확도 균형 좋음
	•	더 빠른 테스트용은 tiny 모델 추천:

model = whisper.load_model("tiny")

	•	Whisper는 내부적으로 PyTorch를 사용합니다. Mac에서도 잘 작동하지만 속도는 CPU 성능에 따라 다릅니다.

---

💬 출력 예시

🎙 5초간 녹음 중...
✅ 녹음 완료
🧠 Whisper 모델로 텍스트 변환 중...
📝 인식된 텍스트: 안녕하세요, 테스트 중입니다.

---

## ✨ 관련 링크
- [Whisper GitHub (OpenAI)](https://github.com/openai/whisper)
- [PortAudio 설치 참고](http://portaudio.com/)
