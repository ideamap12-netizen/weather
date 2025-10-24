import streamlit as st
import requests
import json
import os
from datetime import datetime, timedelta
import pytz
from dotenv import load_dotenv
import geocoder

# 환경변수 로드
load_dotenv()

# 페이지 설정
st.set_page_config(
    page_title="🌤️ 날씨 앱",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)



# OpenWeather API 설정
# Streamlit Secrets 우선, 없으면 환경변수 사용
try:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
except KeyError:
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_api_key_here")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

# 한국 도시 한글-영어 매핑 딕셔너리
KOREAN_CITIES = {
    # 특별시/광역시
    "서울": "Seoul", "서울시": "Seoul", "서울특별시": "Seoul",
    "부산": "Busan", "부산시": "Busan", "부산광역시": "Busan",
    "인천": "Incheon", "인천시": "Incheon", "인천광역시": "Incheon",
    "대구": "Daegu", "대구시": "Daegu", "대구광역시": "Daegu",
    "대전": "Daejeon", "대전시": "Daejeon", "대전광역시": "Daejeon",
    "광주": "Gwangju", "광주시": "Gwangju", "광주광역시": "Gwangju",
    "울산": "Ulsan", "울산시": "Ulsan", "울산광역시": "Ulsan",
    "세종": "Sejong", "세종시": "Sejong", "세종특별자치시": "Sejong",
    
    # 경기도
    "수원": "Suwon", "수원시": "Suwon",
    "성남": "Seongnam", "성남시": "Seongnam",
    "고양": "Goyang", "고양시": "Goyang",
    "용인": "Yongin", "용인시": "Yongin",
    "부천": "Bucheon", "부천시": "Bucheon",
    "안산": "Ansan", "안산시": "Ansan",
    "안양": "Anyang", "안양시": "Anyang",
    "남양주": "Namyangju", "남양주시": "Namyangju",
    "화성": "Hwaseong", "화성시": "Hwaseong",
    "평택": "Pyeongtaek", "평택시": "Pyeongtaek",
    "의정부": "Uijeongbu", "의정부시": "Uijeongbu",
    "시흥": "Siheung", "시흥시": "Siheung",
    "파주": "Paju", "파주시": "Paju",
    "김포": "Gimpo", "김포시": "Gimpo",
    "광명": "Gwangmyeong", "광명시": "Gwangmyeong",
    "구리": "Guri", "구리시": "Guri",
    "이천": "Icheon", "이천시": "Icheon",
    "양주": "Yangju", "양주시": "Yangju",
    "오산": "Osan", "오산시": "Osan",
    "하남": "Hanam", "하남시": "Hanam",
    "과천": "Gwacheon", "과천시": "Gwacheon",
    
    # 강원도
    "춘천": "Chuncheon", "춘천시": "Chuncheon",
    "원주": "Wonju", "원주시": "Wonju",
    "강릉": "Gangneung", "강릉시": "Gangneung",
    "동해": "Donghae", "동해시": "Donghae",
    "태백": "Taebaek", "태백시": "Taebaek",
    "속초": "Sokcho", "속초시": "Sokcho",
    "삼척": "Samcheok", "삼척시": "Samcheok",
    
    # 충청북도
    "청주": "Cheongju", "청주시": "Cheongju",
    "충주": "Chungju", "충주시": "Chungju",
    "제천": "Jecheon", "제천시": "Jecheon",
    
    # 충청남도
    "천안": "Cheonan", "천안시": "Cheonan",
    "공주": "Gongju", "공주시": "Gongju",
    "보령": "Boryeong", "보령시": "Boryeong",
    "아산": "Asan", "아산시": "Asan",
    "서산": "Seosan", "서산시": "Seosan",
    "논산": "Nonsan", "논산시": "Nonsan",
    "계룡": "Gyeryong", "계룡시": "Gyeryong",
    "당진": "Dangjin", "당진시": "Dangjin",
    
    # 전라북도
    "전주": "Jeonju", "전주시": "Jeonju",
    "군산": "Gunsan", "군산시": "Gunsan",
    "익산": "Iksan", "익산시": "Iksan",
    "정읍": "Jeongeup", "정읍시": "Jeongeup",
    "남원": "Namwon", "남원시": "Namwon",
    "김제": "Gimje", "김제시": "Gimje",
    
    # 전라남도
    "목포": "Mokpo", "목포시": "Mokpo",
    "여수": "Yeosu", "여수시": "Yeosu",
    "순천": "Suncheon", "순천시": "Suncheon",
    "나주": "Naju", "나주시": "Naju",
    "광양": "Gwangyang", "광양시": "Gwangyang",
    
    # 경상북도
    "포항": "Pohang", "포항시": "Pohang",
    "경주": "Gyeongju", "경주시": "Gyeongju",
    "김천": "Gimcheon", "김천시": "Gimcheon",
    "안동": "Andong", "안동시": "Andong",
    "구미": "Gumi", "구미시": "Gumi",
    "영주": "Yeongju", "영주시": "Yeongju",
    "영천": "Yeongcheon", "영천시": "Yeongcheon",
    "상주": "Sangju", "상주시": "Sangju",
    "문경": "Mungyeong", "문경시": "Mungyeong",
    "경산": "Gyeongsan", "경산시": "Gyeongsan",
    
    # 경상남도
    "창원": "Changwon", "창원시": "Changwon",
    "진주": "Jinju", "진주시": "Jinju",
    "통영": "Tongyeong", "통영시": "Tongyeong",
    "사천": "Sacheon", "사천시": "Sacheon",
    "김해": "Gimhae", "김해시": "Gimhae",
    "밀양": "Miryang", "밀양시": "Miryang",
    "거제": "Geoje", "거제시": "Geoje",
    "양산": "Yangsan", "양산시": "Yangsan",
    
    # 제주특별자치도
    "제주": "Jeju", "제주시": "Jeju",
    "서귀포": "Seogwipo", "서귀포시": "Seogwipo",
}

def convert_korean_city(city):
    """
    한글 도시명을 영어로 변환합니다.
    """
    city = city.strip()
    
    # 정확히 매칭되는 경우
    if city in KOREAN_CITIES:
        return KOREAN_CITIES[city]
    
    # '시'가 없는 경우 '시'를 붙여서 검색
    if city + "시" in KOREAN_CITIES:
        return KOREAN_CITIES[city + "시"]
    
    # '시'로 끝나는 경우 '시'를 빼고 검색
    if city.endswith("시"):
        city_without_si = city[:-1]
        if city_without_si in KOREAN_CITIES:
            return KOREAN_CITIES[city_without_si]
    
    # 일치하는 것이 없으면 원래 입력값 반환 (영어 도시명일 수도 있음)
    return city

def get_current_location():
    """
    사용자의 현재 위치 정보를 가져옵니다.
    개선된 자동 감지로 한국 위치를 더 정확하게 찾습니다.
    """
    try:
        # 다양한 위치 서비스를 순차적으로 시도
        location_services = [
            ('ipinfo', lambda: geocoder.ipinfo('me')),
            ('ip', lambda: geocoder.ip('me')),
            ('freegeoip', lambda: geocoder.freegeoip('me'))
        ]
        
        best_result = None
        
        for service_name, service_func in location_services:
            try:
                g = service_func()
                if g.ok and g.latlng:
                    lat, lon = g.latlng
                    
                    # 한국 좌표 범위 확인 (더 정확한 범위)
                    # 위도 33.0-38.6, 경도 124.0-131.9 (한반도 범위)
                    if 33.0 <= lat <= 38.6 and 124.0 <= lon <= 131.9:
                        city_name = g.city or g.address or '한국'
                        
                        # 영어 도시명을 한글로 매핑 시도
                        korean_city_mapping = {
                            'Seoul': '서울', 'Busan': '부산', 'Incheon': '인천',
                            'Daegu': '대구', 'Daejeon': '대전', 'Gwangju': '광주',
                            'Ulsan': '울산', 'Suwon': '수원', 'Goyang': '고양',
                            'Yongin': '용인', 'Seongnam': '성남'
                        }
                        
                        if city_name in korean_city_mapping:
                            city_name = korean_city_mapping[city_name]
                        
                        return {
                            'lat': lat,
                            'lon': lon,
                            'city': city_name,
                            'country': 'KR',
                            'detected': True,
                            'service': service_name
                        }
                    
                    # 한국 밖의 위치도 저장 (폴백용)
                    elif not best_result:
                        best_result = {
                            'lat': lat,
                            'lon': lon,
                            'city': g.city or g.address or '알 수 없음',
                            'country': g.country or '알 수 없음',
                            'detected': True,
                            'service': service_name,
                            'outside_korea': True
                        }
                        
            except Exception as e:
                continue
        
        # 한국 외 위치가 감지된 경우 사용자에게 알림
        if best_result and best_result.get('outside_korea'):
            # 한국이 아닌 위치로 감지되면 서울을 기본값으로 설정
            return {
                'lat': 37.5665,
                'lon': 126.9780,
                'city': '서울',
                'country': 'KR',
                'detected': False,
                'detected_location': f"{best_result['city']}, {best_result['country']}",
                'reason': 'outside_korea'
            }
        
        # 모든 서비스 실패 시 서울을 기본값으로 설정
        return {
            'lat': 37.5665,
            'lon': 126.9780,
            'city': '서울',
            'country': 'KR',
            'detected': False,
            'reason': 'no_location_detected'
        }
        
    except Exception as e:
        return {
            'lat': 37.5665,
            'lon': 126.9780,
            'city': '서울',
            'country': 'KR',
            'detected': False,
            'reason': 'error'
        }

def get_weather_by_coordinates(lat, lon):
    """
    좌표를 사용하여 날씨 정보를 가져옵니다.
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "lang": "kr"
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"현재 위치의 날씨 정보를 가져오는데 실패했습니다: {e}")
        return None

def get_weekly_forecast(lat, lon):
    """
    5일간의 일기예보를 가져옵니다. (3시간 간격)
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "lang": "kr"
    }
    
    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"주간 예보를 가져오는데 실패했습니다: {e}")
        return None

def get_weather_data(city):
    """
    OpenWeather API를 사용하여 도시의 날씨 정보를 가져옵니다.
    한글 도시명은 자동으로 영어로 변환됩니다.
    """
    # 한글 도시명을 영어로 변환
    english_city = convert_korean_city(city)
    
    params = {
        "q": english_city,
        "appid": API_KEY,
        "units": "metric",  # 섭씨 온도로 설정
        "lang": "kr"  # 한국어로 설정
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 처리
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"날씨 정보를 가져오는데 실패했습니다: {e}")
        return None

def format_weather_display(weather_data):
    """
    날씨 데이터를 보기 좋게 포맷하여 표시합니다.
    """
    if not weather_data:
        return
    
    # 기본 정보 추출
    city_name = weather_data.get("name", "알 수 없음")
    country = weather_data.get("sys", {}).get("country", "")
    
    # 온도 정보
    main_data = weather_data.get("main", {})
    temp = main_data.get("temp", 0)
    feels_like = main_data.get("feels_like", 0)
    temp_min = main_data.get("temp_min", 0)
    temp_max = main_data.get("temp_max", 0)
    humidity = main_data.get("humidity", 0)
    pressure = main_data.get("pressure", 0)
    
    # 날씨 상태
    weather_list = weather_data.get("weather", [])
    weather_desc = weather_list[0].get("description", "정보 없음") if weather_list else "정보 없음"
    weather_icon = weather_list[0].get("icon", "") if weather_list else ""
    
    # 바람 정보
    wind_data = weather_data.get("wind", {})
    wind_speed = wind_data.get("speed", 0)
    
    # 가시거리
    visibility = weather_data.get("visibility", 0) / 1000  # km로 변환
    
    # 일출/일몰 시간
    sys_data = weather_data.get("sys", {})
    sunrise = datetime.fromtimestamp(sys_data.get("sunrise", 0))
    sunset = datetime.fromtimestamp(sys_data.get("sunset", 0))
    
    # 헤더
    st.header(f"🌤️ {city_name}, {country}의 날씨")
    
    # 메인 온도 정보 (3개 컬럼)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="🌡️ 현재 온도",
            value=f"{temp:.1f}°C",
            delta=f"체감온도 {feels_like:.1f}°C"
        )
    
    with col2:
        st.metric(
            label="📊 최고/최저",
            value=f"{temp_max:.1f}°C",
            delta=f"최저 {temp_min:.1f}°C"
        )
    
    with col3:
        st.metric(
            label="☀️ 날씨 상태",
            value=weather_desc
        )
    
    # 추가 정보 (4개 컬럼)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.info(f"💧 **습도**  \n{humidity}%")
    
    with col2:
        st.info(f"🌬️ **바람**  \n{wind_speed:.1f} m/s")
    
    with col3:
        st.info(f"🔍 **가시거리**  \n{visibility:.1f} km")
    
    with col4:
        st.info(f"📏 **기압**  \n{pressure} hPa")
    
    # 일출/일몰 정보
    st.subheader("🌅 일출/일몰 정보")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"🌅 **일출**: {sunrise.strftime('%H:%M:%S')}")
    
    with col2:
        st.write(f"🌇 **일몰**: {sunset.strftime('%H:%M:%S')}")

def format_weekly_forecast(forecast_data):
    """
    5일간 예보 데이터를 보기 좋게 포맷하여 표시합니다.
    """
    if not forecast_data or "list" not in forecast_data:
        st.error("주간 예보 데이터를 가져올 수 없습니다.")
        return
    
    st.header("📅 5일간 날씨 예보")
    
    forecast_list = forecast_data["list"]
    
    # 날짜별로 데이터를 그룹화
    daily_forecasts = {}
    for item in forecast_list:
        date_str = datetime.fromtimestamp(item["dt"]).strftime('%Y-%m-%d')
        if date_str not in daily_forecasts:
            daily_forecasts[date_str] = []
        daily_forecasts[date_str].append(item)
    
    # 처음 5일만 표시
    for i, (date_str, day_items) in enumerate(list(daily_forecasts.items())[:5]):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        
        # 해당 날의 온도 범위 계산
        temps = [item["main"]["temp"] for item in day_items]
        temp_max = max(temps)
        temp_min = min(temps)
        
        # 대표 날씨 (가장 많이 나오는 날씨 또는 첫 번째)
        weather_desc = day_items[0]["weather"][0]["description"]
        humidity = day_items[0]["main"]["humidity"]
        pressure = day_items[0]["main"]["pressure"]
        wind_speed = day_items[0]["wind"]["speed"]
        
        # 강수 확률 (있는 경우)
        pop = day_items[0].get("pop", 0) * 100 if "pop" in day_items[0] else 0
        
        # 날짜별 컨테이너
        with st.container():
            if i == 0:
                st.subheader(f"🔥 오늘 ({date_obj.strftime('%m월 %d일 %a')})")
            elif i == 1:
                st.subheader(f"➡️ 내일 ({date_obj.strftime('%m월 %d일 %a')})")
            else:
                st.subheader(f"📆 {date_obj.strftime('%m월 %d일 %a')}")
            
            # 온도와 날씨 정보를 컬럼으로 분할
            col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
            
            with col1:
                st.metric(
                    "🌡️ 최고/최저 온도",
                    f"{temp_max:.1f}°C",
                    f"최저 {temp_min:.1f}°C"
                )
            
            with col2:
                st.metric(
                    "☁️ 날씨",
                    weather_desc,
                    f"습도 {humidity}%"
                )
            
            with col3:
                st.metric(
                    "🌬️ 바람/기압",
                    f"{wind_speed:.1f} m/s",
                    f"{pressure} hPa"
                )
            
            with col4:
                st.metric(
                    "☔ 강수확률",
                    f"{pop:.0f}%",
                    f"{len(day_items)}개 예보"
                )
            
            # 시간대별 상세 정보
            with st.expander(f"📊 {date_obj.strftime('%m월 %d일')} 시간대별 상세 예보"):
                cols = st.columns(min(len(day_items), 4))
                for j, item in enumerate(day_items[:4]):  # 최대 4개만 표시
                    time_obj = datetime.fromtimestamp(item["dt"])
                    with cols[j % 4]:
                        st.write(f"**{time_obj.strftime('%H:%M')}**")
                        st.write(f"🌡️ {item['main']['temp']:.1f}°C")
                        st.write(f"☁️ {item['weather'][0]['description']}")
                        if "pop" in item:
                            st.write(f"☔ {item['pop']*100:.0f}%")
            
            st.divider()

def main():
    """
    메인 애플리케이션 함수
    """
    # 타이틀
    st.title("🌤️ 한국 날씨 정보")
    st.markdown("**🇰🇷 전국 모든 도시의 실시간 날씨를 한글로 조회하세요!**")
    st.caption("OpenWeather API를 사용한 정확한 날씨 정보 서비스")
    
    # 사이드바
    with st.sidebar:
        st.header("� 날씨 조회 방법")
        
        # 탭으로 구분
        tab1, tab2 = st.tabs(["📍 현재 위치", "�🏙️ 도시 선택"])
        
        with tab1:
            st.subheader("📍 내 위치 날씨")
            
            if st.button("🎯 현재 위치 날씨 보기", type="primary", key="current_location_btn"):
                st.session_state.use_current_location = True
                st.session_state.city = None
            
            st.info("📱 IP 기반 위치 정보를 사용합니다")
            st.caption("⚠️ IP 위치가 부정확할 수 있습니다. 정확한 날씨가 필요하면 '도시 선택' 탭을 이용하세요.")
        
        with tab2:
            # 도시 입력
            city = st.text_input(
                "도시명을 입력하세요",
                placeholder="예: 서울, 부산, 인천, 대전, 춘천",
                help="한글 또는 영문 도시명을 입력해주세요"
            )
        
            # 한국 주요 도시 버튼
            st.subheader("🇰🇷 한국 주요 도시")
            korean_major_cities = ["서울", "부산", "인천", "대구", "대전", "광주", "울산", "수원", "고양", "용인"]
            
            cols = st.columns(2)
            for i, kor_city in enumerate(korean_major_cities):
                with cols[i % 2]:
                    if st.button(kor_city, key=f"kor_city_{i}"):
                        city = kor_city
                        st.session_state.use_current_location = False
        
            # 지역별 도시 선택
            st.subheader("🗺️ 지역별 도시")
            
            regions = {
                "수도권": ["서울", "인천", "고양", "수원", "성남", "용인", "안양", "부천", "안산", "김포"],
                "강원도": ["춘천", "원주", "강릉", "속초", "동해", "태백", "삼척"],
                "충청도": ["대전", "청주", "천안", "충주", "제천", "공주", "보령", "아산", "서산", "논산"],
                "전라도": ["광주", "전주", "목포", "여수", "순천", "군산", "익산", "정읍", "남원", "김제"],
                "경상도": ["부산", "대구", "울산", "포항", "경주", "안동", "구미", "창원", "진주", "김해"],
                "제주도": ["제주", "서귀포"]
            }
            
            selected_region = st.selectbox("지역을 선택하세요", ["선택안함"] + list(regions.keys()))
            
            if selected_region != "선택안함":
                region_cities = regions[selected_region]
                cols = st.columns(2)
                for i, region_city in enumerate(region_cities):
                    with cols[i % 2]:
                        if st.button(region_city, key=f"region_city_{selected_region}_{i}"):
                            city = region_city
                            st.session_state.use_current_location = False
        
        # 새로고침 버튼
        if st.button("🔄 새로고침", type="primary"):
            st.rerun()
    
    # session_state 초기화
    if 'use_current_location' not in st.session_state:
        st.session_state.use_current_location = False
    
    # 메인 컨텐츠
    weather_data = None
    forecast_data = None
    location_info = None
    
    # 현재 위치 사용
    if st.session_state.get('use_current_location', False):
        with st.spinner("현재 위치의 날씨 정보를 가져오는 중..."):
            location_info = get_current_location()
            weather_data = get_weather_by_coordinates(location_info['lat'], location_info['lon'])
            forecast_data = get_weekly_forecast(location_info['lat'], location_info['lon'])
        
        if weather_data:
            # 위치 표시 메시지 개선
            if location_info.get('detected', False):
                service = location_info.get('service', '')
                st.success(f"� 감지된 위치: {location_info['city']} (자동 감지)")
            else:
                reason = location_info.get('reason', 'unknown')
                if reason == 'outside_korea':
                    detected_loc = location_info.get('detected_location', '해외')
                    st.warning(f"📍 기본 위치: {location_info['city']} (감지된 위치: {detected_loc} → 한국 기본값 사용)")
                elif reason == 'no_location_detected':
                    st.warning(f"📍 기본 위치: {location_info['city']} (위치 감지 실패 → 기본값 사용)")
                else:
                    st.warning(f"📍 기본 위치: {location_info['city']} (자동 감지 실패 → 기본값 사용)")
                
                st.info("💡 정확한 날씨가 필요하면 '도시 선택' 탭에서 직접 도시를 선택하세요.")
            
            # 메인 날씨 정보와 주간 예보를 탭으로 구분
            tab1, tab2 = st.tabs(["🌤️ 현재 날씨", "📅 주간 예보"])
            
            with tab1:
                format_weather_display(weather_data)
            
            with tab2:
                if forecast_data:
                    format_weekly_forecast(forecast_data)
                else:
                    st.error("주간 예보 정보를 가져올 수 없습니다.")
        else:
            st.error("현재 위치의 날씨 정보를 가져올 수 없습니다.")
    
    # 도시 검색 사용
    elif city:
        with st.spinner(f"{city}의 날씨 정보를 가져오는 중..."):
            weather_data = get_weather_data(city)
            
            # 도시의 좌표를 얻어서 주간 예보도 가져오기
            if weather_data and 'coord' in weather_data:
                lat = weather_data['coord']['lat']
                lon = weather_data['coord']['lon']
                forecast_data = get_weekly_forecast(lat, lon)
        
        if weather_data:
            # 메인 날씨 정보와 주간 예보를 탭으로 구분
            tab1, tab2 = st.tabs(["🌤️ 현재 날씨", "📅 주간 예보"])
            
            with tab1:
                format_weather_display(weather_data)
            
            with tab2:
                if forecast_data:
                    format_weekly_forecast(forecast_data)
                else:
                    st.error("주간 예보 정보를 가져올 수 없습니다.")
        else:
            st.error("날씨 정보를 가져올 수 없습니다. 도시명을 확인해주세요.")
    else:
        # 초기 화면
        st.info("👈 왼쪽 사이드바에서 도시를 선택하거나 입력해주세요!")
        
        # 예시 이미지나 설명
        st.subheader("📋 사용 방법")
        st.write("1. 왼쪽 사이드바에서 한글 도시명을 입력하거나")
        st.write("2. 한국 주요 도시 버튼을 클릭하거나")
        st.write("3. 지역별 도시에서 선택하세요")
        st.write("4. 실시간 날씨 정보가 표시됩니다!")
        
        st.subheader("🌟 지원 기능")
        st.write("✅ 📍 현재 위치 자동 인식")
        st.write("✅ 🏙️ 전국 모든 시/도 날씨 조회")
        st.write("✅ 🔤 한글 도시명 완벽 지원")
        st.write("✅ 🌡️ 실시간 온도, 습도, 바람 정보")
        st.write("✅ 🌅 일출/일몰 시간 표시")
        st.write("✅ 📅 7일간 주간 예보")
        st.write("✅ ☔ 강수확률 및 UV 지수")
        
        # 현재 시간 표시
        current_time = datetime.now(pytz.timezone('Asia/Seoul'))
        st.caption(f"현재 시간: {current_time.strftime('%Y-%m-%d %H:%M:%S')} (KST)")

if __name__ == "__main__":
    main()