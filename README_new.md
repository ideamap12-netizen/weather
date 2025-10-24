# 🌤️ 한국 날씨 정보 앱

OpenWeather API를 사용한 실시간 한국 날씨 정보 웹 애플리케이션입니다.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 주요 기능

- 🇰🇷 **한국 전국 도시 지원**: 80개 이상의 한국 도시 날씨 조회
- 🔤 **한글 검색**: 한글 도시명으로 간편하게 검색 가능
- 🌡️ **실시간 정보**: 온도, 습도, 바람, 기압 등 상세 날씨 정보
- 🌅 **일출/일몰**: 일출 및 일몰 시간 표시
- 🗺️ **지역별 분류**: 수도권, 강원도, 충청도, 전라도, 경상도, 제주도별 도시 선택
- 📱 **반응형 디자인**: 모바일과 데스크톱 모두 최적화

## 🚀 로컬 실행 방법

### 1. 저장소 클론
```bash
git clone https://github.com/your-username/korean-weather-app.git
cd korean-weather-app
```

### 2. 가상환경 생성 및 활성화
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux  
source .venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 환경변수 설정
`.env` 파일을 생성하고 OpenWeather API 키를 설정하세요:

```env
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

> 💡 **API 키 발급 방법**: [OpenWeather](https://openweathermap.org/api)에서 무료 계정을 생성하고 API 키를 발급받으세요.

### 5. 애플리케이션 실행
```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501`로 접속하세요!

## 🌐 Streamlit Cloud 배포

### 1. GitHub에 레포지토리 업로드
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/korean-weather-app.git
git push -u origin main
```

### 2. Streamlit Cloud에서 앱 배포
1. [Streamlit Cloud](https://share.streamlit.io/)에 접속
2. "New app" 클릭
3. GitHub 레포지토리 선택
4. Main file path: `app.py`
5. **Advanced settings**에서 **Secrets** 설정:

```toml
OPENWEATHER_API_KEY = "your_openweather_api_key_here"
```

6. "Deploy!" 클릭

> 📝 **참고**: Streamlit Cloud는 자동으로 `requirements.txt`에서 의존성을 설치합니다.

## 🏙️ 지원 도시

### 특별시/광역시
서울, 부산, 인천, 대구, 대전, 광주, 울산, 세종

### 경기도
수원, 성남, 고양, 용인, 부천, 안산, 안양, 남양주, 화성, 평택, 의정부, 시흥, 파주, 김포, 광명, 구리, 이천, 양주, 오산, 하남, 과천

### 강원도
춘천, 원주, 강릉, 동해, 태백, 속초, 삼척

### 충청도
청주, 충주, 제천, 천안, 공주, 보령, 아산, 서산, 논산, 계룡, 당진

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
- **배포**: Streamlit Cloud

## 📂 프로젝트 구조

```
korean-weather-app/
├── app.py                    # 메인 애플리케이션
├── .env                     # 환경변수 (로컬용, git 제외)
├── .streamlit/
│   └── secrets.toml         # Streamlit Cloud 배포용 (git 제외)
├── .gitignore              # Git 제외 파일 목록
├── requirements.txt        # Python 패키지 목록
└── README.md              # 프로젝트 문서
```

## 🔑 환경변수 및 Secrets 설정

### 로컬 개발용 (.env)
```env
OPENWEATHER_API_KEY=your_api_key_here
```

### Streamlit Cloud용 (secrets.toml 형식)
```toml
OPENWEATHER_API_KEY = "your_api_key_here"
```

> ⚠️ **보안 주의**: API 키는 절대 Git에 커밋하지 마세요. `.gitignore`에 의해 보호됩니다.

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다.

## 📞 문의

프로젝트 관련 문의사항이 있으시면 GitHub Issues를 생성해 주세요.

---

⭐ 이 프로젝트가 도움이 되셨다면 별표를 눌러주세요!