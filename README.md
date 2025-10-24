# 🌤️ 한국 날씨 정보 앱# 🌤️ 날씨 정보 웹앱



OpenWeather API를 사용한 실시간 한국 날씨 정보 웹 애플리케이션입니다.OpenWeather API를 활용한 실시간 날씨 정보 제공 웹 애플리케이션



![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)## 📋 기능

![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)

![License](https://img.shields.io/badge/License-MIT-green.svg)- **실시간 날씨 정보**: 현재 온도, 습도, 풍속, 기압

- **상세 정보**: 체감온도, 가시거리, 일출/일몰 시간

## 🌟 주요 기능- **5일 예보**: 향후 5일간의 날씨 예보

- **다국어 지원**: 한국어 날씨 설명

- 🇰🇷 **한국 전국 도시 지원**: 80개 이상의 한국 도시 날씨 조회- **인기 도시**: 주요 도시 빠른 선택 기능

- 🔤 **한글 검색**: 한글 도시명으로 간편하게 검색 가능

- 🌡️ **실시간 정보**: 온도, 습도, 바람, 기압 등 상세 날씨 정보## 🛠️ 설치 및 실행

- 🌅 **일출/일몰**: 일출 및 일몰 시간 표시

- 🗺️ **지역별 분류**: 수도권, 강원도, 충청도, 전라도, 경상도, 제주도별 도시 선택### 1. 필요한 패키지 설치

- 📱 **반응형 디자인**: 모바일과 데스크톱 모두 최적화```bash

pip install streamlit requests pytz

## 🚀 빠른 시작```



### 1. 저장소 클론### 2. 애플리케이션 실행

```bash```bash

git clone https://github.com/your-username/korean-weather-app.gitstreamlit run app.py

cd korean-weather-app```

```

## 🔑 API 키 설정

### 2. 가상환경 생성 및 활성화

```bash현재 코드에는 API 키가 포함되어 있습니다. 실제 운영 시에는 환경 변수를 사용하는 것을 권장합니다:

python -m venv .venv

```python

# Windowsimport os

.venv\Scripts\activateAPI_KEY = os.getenv("OPENWEATHER_API_KEY", "your-default-api-key")

```

# macOS/Linux  

source .venv/bin/activate## 🌍 지원 도시

```

전 세계 모든 주요 도시를 지원합니다:

### 3. 패키지 설치- 한국: Seoul, Busan, Incheon, Daegu 등

```bash- 해외: Tokyo, New York, London, Paris 등

pip install -r requirements.txt

```## 📱 사용법



### 4. 환경변수 설정1. 웹 애플리케이션 실행

`.env` 파일을 생성하고 OpenWeather API 키를 설정하세요:2. 사이드바에서 도시명 입력 또는 인기 도시 선택

3. 실시간 날씨 정보 및 예보 확인

```env

OPENWEATHER_API_KEY=your_openweather_api_key_here## 🎨 주요 특징

```

- **반응형 디자인**: 다양한 화면 크기에 대응

> 💡 **API 키 발급 방법**: [OpenWeather](https://openweathermap.org/api)에서 무료 계정을 생성하고 API 키를 발급받으세요.- **직관적 UI**: 사용하기 쉬운 인터페이스

- **실시간 업데이트**: 최신 날씨 정보 제공

### 5. 애플리케이션 실행- **다양한 정보**: 종합적인 날씨 데이터

```bash

streamlit run app.py## 📦 프로젝트 구조

```

```

브라우저에서 `http://localhost:8501`로 접속하세요!weather/

├── app.py          # 메인 애플리케이션 파일

## 🏙️ 지원 도시├── README.md       # 프로젝트 설명서

└── .venv/          # 가상환경 (자동 생성)

### 특별시/광역시```

서울, 부산, 인천, 대구, 대전, 광주, 울산, 세종

## 🔧 개발 환경

### 경기도

수원, 성남, 고양, 용인, 부천, 안산, 안양, 남양주, 화성, 평택, 의정부, 시흥, 파주, 김포, 광명, 구리, 이천, 양주, 오산, 하남, 과천- **언어**: Python 3.13.7

- **프레임워크**: Streamlit

### 강원도- **API**: OpenWeather API

춘천, 원주, 강릉, 동해, 태백, 속초, 삼척- **추가 라이브러리**: requests, pytz, datetime



### 충청도## 📄 라이선스

청주, 충주, 제천, 천안, 공주, 보령, 아산, 서산, 논산, 계룡, 당진

이 프로젝트는 개인 사용 및 학습 목적으로 제작되었습니다.

### 전라도
전주, 군산, 익산, 정읍, 남원, 김제, 목포, 여수, 순천, 나주, 광양

### 경상도
포항, 경주, 김천, 안동, 구미, 영주, 영천, 상주, 문경, 경산, 창원, 진주, 통영, 사천, 김해, 밀양, 거제, 양산

### 제주도
제주, 서귀포

## 📝 사용 방법

1. **직접 입력**: 검색창에 한글 도시명 입력 (예: "서울", "부산")
2. **주요 도시**: 인기 도시 버튼 클릭
3. **지역별 선택**: 드롭다운에서 지역 선택 후 도시 클릭

## 🛠️ 기술 스택

- **Backend**: Python 3.8+
- **Frontend**: Streamlit
- **API**: OpenWeather API
- **환경관리**: python-dotenv

## 📂 프로젝트 구조

```
korean-weather-app/
├── app.py              # 메인 애플리케이션
├── .env               # 환경변수 (git에서 제외)
├── .gitignore         # Git 제외 파일 목록
├── requirements.txt   # Python 패키지 목록
└── README.md         # 프로젝트 문서
```

## 🔑 환경변수

| 변수명 | 설명 | 필수 여부 |
|--------|------|-----------|
| `OPENWEATHER_API_KEY` | OpenWeather API 키 | 필수 |

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 문의

프로젝트 관련 문의사항이 있으시면 이슈를 생성해 주세요.

---

⭐ 이 프로젝트가 도움이 되셨다면 별표를 눌러주세요!