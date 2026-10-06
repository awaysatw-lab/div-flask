# seed_accommodations_data.py
import sys
import os
sys.path.insert(0, r'd:\hongdonjoo\flask\project1\div-flask')

from pybo import create_app, db
from pybo.models import Accommodation, RegionEnum

accommodations_data = [
    # =========================================================================
    # 1. 서울/경기 (SEOUL_GYEONGGI) - 호텔 10건
    # =========================================================================
    {
        'name': '시그니엘 서울',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '서울 송파구 올림픽로 300 롯데월드타워 76-101층',
        'price_per_night': 380000,
        'image_url': '/static/img/accomodation/hotel_seoul_01.jpg',
        'description': '초고층 롯데월드타워에서 서울 도심 파노라마 스카이라인을 조망하는 최상급 럭셔리 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '그랜드 워커힐 서울',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '서울 광진구 워커힐로 177 아차산 자락',
        'price_per_night': 240000,
        'image_url': '/static/img/accomodation/hotel_seoul_02.jpg',
        'description': '아차산 숲과 한강의 청정한 자연을 품어 도심 속 진정한 쉼을 선사하는 특급 힐링 리조트입니다.',
        'rating': 4.8
    },
    {
        'name': '파라스파라 서울 북한산',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '서울 강북구 삼양로 689 북한산 국립공원 입구',
        'price_per_night': 290000,
        'image_url': '/static/img/accomodation/hotel_seoul_03.jpg',
        'description': '북한산 국립공원의 맑은 공기와 천연 온천 스파, 사계절 루프탑 풀을 갖춘 포레스트 리조트입니다.',
        'rating': 4.9
    },
    {
        'name': '네스트 호텔 인천',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '인천 중구 영종해안남로 19-5 영종도',
        'price_per_night': 195000,
        'image_url': '/static/img/accomodation/hotel_seoul_04.jpg',
        'description': '서해 바다와 갈대숲이 어우러진 국내 최초 디자인 호텔스 멤버 특급 디자인 부티크 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '롤링힐스 호텔 화성',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 화성시 남양읍 시청로 29',
        'price_per_night': 180000,
        'image_url': '/static/img/accomodation/hotel_seoul_05.jpg',
        'description': '아름다운 조경 정원과 실내 온수풀, 키즈존을 완비하여 가족 여행객에게 사랑받는 자연 친화 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '소노캄 고양',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 고양시 일산동구 태극로 20 일산 호수공원 인근',
        'price_per_night': 175000,
        'image_url': '/static/img/accomodation/hotel_seoul_06.jpg',
        'description': '킨텍스와 일산 호수공원 인근 경기 북부 유일의 5성급 럭셔리 프리미엄 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '코트야드 메리어트 판교',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 성남시 분당구 판교역로 192번길 12',
        'price_per_night': 190000,
        'image_url': '/static/img/accomodation/hotel_seoul_07.jpg',
        'description': '판교 테크노밸리 중심에 위치하여 모던하고 감각적인 객실과 최고급 다이닝을 자랑합니다.',
        'rating': 4.8
    },
    {
        'name': '스탠포드 호텔 코리아 서울',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '서울 마포구 월드컵북로58길 15 상암 DMC',
        'price_per_night': 140000,
        'image_url': '/static/img/accomodation/hotel_seoul_08.jpg',
        'description': '상암 디지털미디어시티 중심에 위치한 안락하고 세련된 시티 라이프 비즈니스 호텔입니다.',
        'rating': 4.6
    },
    {
        'name': '호텔 마리나베이 서울 김포',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 김포시 고촌읍 아라육로152번길 210-50 아라뱃길',
        'price_per_night': 135000,
        'image_url': '/static/img/accomodation/hotel_seoul_09.jpg',
        'description': '경인 아라뱃길 요트 마리나 항구의 이국적인 수변 전망을 감상할 수 있는 감성 호텔입니다.',
        'rating': 4.6
    },
    {
        'name': '글래드 여의도',
        'category': '호텔',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '서울 영등포구 의사당대로 16 국회의사당역 앞',
        'price_per_night': 150000,
        'image_url': '/static/img/accomodation/hotel_seoul_10.jpg',
        'description': '스마트하고 실용적인 감각과 최고급 에이스 침대로 도심 속 최적의 휴식을 선사합니다.',
        'rating': 4.7
    },

    # =========================================================================
    # 1. 서울/경기 (SEOUL_GYEONGGI) - 민박 10건
    # =========================================================================
    {
        'name': '북촌 한옥마을 다온재 한옥민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '서울 종로구 북촌로11길 18 북촌한옥마을',
        'price_per_night': 120000,
        'image_url': '/static/img/accomodation/minbak_seoul_01.jpg',
        'description': '전통 한옥의 고즈넉한 멋과 아름다운 마당 정원이 살아있는 정통 한옥스테이 민박입니다.',
        'rating': 4.9
    },
    {
        'name': '서촌 풍경 감성 게스트민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '서울 종로구 옥인길 24-6 서촌마을',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_seoul_02.jpg',
        'description': '인왕산 자락 골목길에 자리잡은 소박하고 따뜻한 정취의 골목길 감성 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '양평 두물머리 황토흙집민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 양평군 양서면 두물머리길 68-5',
        'price_per_night': 90000,
        'image_url': '/static/img/accomodation/minbak_seoul_03.jpg',
        'description': '남한강과 북한강이 만나는 두물머리 인근 전통 참나무 장작 황토 구들장 흙집입니다.',
        'rating': 4.8
    },
    {
        'name': '가평 잣나무골 통나무 숲속민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 가평군 상면 축령로 115 잣향기푸른숲 인근',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_seoul_04.jpg',
        'description': '축령산 잣나무 숲 피톤치드 가득한 통나무 오두막에서 즐기는 자연 힐링 쉼터입니다.',
        'rating': 4.8
    },
    {
        'name': '파주 헤이리 예술마을 아트민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 파주시 탄현면 헤이리마을길 70-21',
        'price_per_night': 95000,
        'image_url': '/static/img/accomodation/minbak_seoul_05.jpg',
        'description': '예술가들의 공방과 갤러리가 이웃한 개성 있는 건축미와 정취의 문화 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '강화도 갯벌체험 노을바다민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '인천 강화군 화도면 해안남로 1476 동막해변 앞',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_seoul_06.jpg',
        'description': '동막해변 앞 서해 붉은 낙조를 감상하며 갯벌 체험을 바로 즐길 수 있는 바닷가 민박입니다.',
        'rating': 4.6
    },
    {
        'name': '포천 산정호수 솔바람민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 포천시 영북면 산정호수로 411번길 32',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_seoul_07.jpg',
        'description': '명성산 억새군락지와 산정호수 둘레길 산책로 바로 곁에 자리한 아늑하고 조용한 쉼터입니다.',
        'rating': 4.7
    },
    {
        'name': '남한산성 성곽길 솔향기한옥민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 광주시 남한산성면 남한산성로 780',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_seoul_08.jpg',
        'description': '유네스코 세계유산 남한산성 소나무 숲길 속 사계절 고즈넉한 한국 전통 한옥 쉼터입니다.',
        'rating': 4.7
    },
    {
        'name': '안성 허브마을 감성가든민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 안성시 삼죽면 국사봉로 641-12',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_seoul_09.jpg',
        'description': '허브 향기와 야생화가 만발한 정원에서 바비큐와 여유를 즐기는 전원 민박입니다.',
        'rating': 4.6
    },
    {
        'name': '연천 DMZ 평화마을 청정민박',
        'category': '민박',
        'region': RegionEnum.SEOUL_GYEONGGI.value,
        'location': '경기 연천군 군남면 평화로 210 임진강변',
        'price_per_night': 65000,
        'image_url': '/static/img/accomodation/minbak_seoul_10.jpg',
        'description': '임진강 청정 자연과 두루미 도래지 인근에서 누리는 맑고 평화로운 농촌 힐링 민박입니다.',
        'rating': 4.5
    },

    # =========================================================================
    # 2. 강원 (GANGWON) - 호텔 10건
    # =========================================================================
    {
        'name': '씨마크 호텔 강릉',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 강릉시 해안로 406번길 2 경포해변 앞',
        'price_per_night': 360000,
        'image_url': '/static/img/accomodation/hotel_gangwon_01.jpg',
        'description': '경포 해변 백사장과 동해 바다가 파노라마처럼 펼쳐지는 최고급 럭셔리 오션 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '세인트존스 호텔 강릉',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 강릉시 창해로 307 강문해변 앞',
        'price_per_night': 185000,
        'image_url': '/static/img/accomodation/hotel_gangwon_02.jpg',
        'description': '곰솔림 소나무 숲과 동해 바다를 잇는 대형 인피니티 풀이 매력적인 오션뷰 랜드마크 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '쏠비치 양양 리조트앤호텔',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 양양군 손양면 선사유적로 678',
        'price_per_night': 220000,
        'image_url': '/static/img/accomodation/hotel_gangwon_03.jpg',
        'description': '스페인 안달루시아 풍의 이국적인 붉은 지붕과 프라이빗 비치를 보유한 동해안 명품 리조트 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '롯데리조트 속초',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 속초시 대포항길 186 대포항 인근',
        'price_per_night': 250000,
        'image_url': '/static/img/accomodation/hotel_gangwon_04.jpg',
        'description': '외옹치 바다향기로 해안 산책로와 3면 바다 조망을 갖춘 속초 최고급 오션 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '파크로쉬 리조트앤웰니스 정선',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 정선군 북평면 중봉길 9-12 가리왕산 자락',
        'price_per_night': 280000,
        'image_url': '/static/img/accomodation/hotel_gangwon_05.jpg',
        'description': '가리왕산 청정 자연 속에서 요가와 명상, 스파를 통해 온전한 휴식을 경험하는 웰니스 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '탑스텐 호텔 강릉',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 강릉시 옥계면 헌화로 455-34 금진항 절벽 위',
        'price_per_night': 160000,
        'image_url': '/static/img/accomodation/hotel_gangwon_06.jpg',
        'description': '금진항 해안 절벽 위에 우뚝 솟아 환상적인 동해 일출과 해안 드라이브길을 조망하는 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '소노펠리체 비발디파크 홍천',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 홍천군 서면 한치골길 262 팔봉산 자락',
        'price_per_night': 210000,
        'image_url': '/static/img/accomodation/hotel_gangwon_07.jpg',
        'description': '팔봉산 자락 골프와 스키, 승마 클럽 및 인피니티 풀을 갖춘 프리미엄 복합 휴양 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '하이원 그랜드호텔 정선',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 정선군 사북읍 하이원길 265 백운산 고원',
        'price_per_night': 190000,
        'image_url': '/static/img/accomodation/hotel_gangwon_08.jpg',
        'description': '백운산 고원에 자리하여 사계절 야생화 트레킹과 스키를 즐기는 고원 마운틴 특급 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '켄싱턴호텔 설악',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 속초시 설악산로 998 설악산 입구',
        'price_per_night': 145000,
        'image_url': '/static/img/accomodation/hotel_gangwon_09.jpg',
        'description': '설악산 국립공원 입구 권금성 봉우리가 한눈에 올려다보이는 영국풍 클래식 헤리티지 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '체스터톤스 속초',
        'category': '호텔',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 속초시 엑스포로 109 청초호 인근',
        'price_per_night': 130000,
        'image_url': '/static/img/accomodation/hotel_gangwon_10.jpg',
        'description': '청초호 호수공원 인근의 신축 온천 수영장과 루프탑 라운지를 갖춘 올인클루시브 레저 호텔입니다.',
        'rating': 4.6
    },

    # =========================================================================
    # 2. 강원 (GANGWON) - 민박 10건
    # =========================================================================
    {
        'name': '대관령 양떼마을 목장통나무민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 평창군 대관령면 꽃밭양지길 128',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_gangwon_01.jpg',
        'description': '대관령 고원 목초지의 시원한 바람과 양떼를 만나며 힐링하는 통나무 전원 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '영월 동강 별빛한옥민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 영월군 영월읍 동강로 824 굽이치는 동강변',
        'price_per_night': 95000,
        'image_url': '/static/img/accomodation/minbak_gangwon_02.jpg',
        'description': '굽이치는 동강 래프팅 비경과 밤하늘 은하수가 쏟아지는 고즈넉한 전통 한옥 쉼터입니다.',
        'rating': 4.9
    },
    {
        'name': '춘천 남이섬 강변솔밭민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 춘천시 남산면 북한강변길 350',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_gangwon_03.jpg',
        'description': '북한강 물안개와 물새들을 벗 삼아 여유롭게 쉬어가는 조용하고 정겨운 강변 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '속초 아바이마을 바다골목민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 속초시 청호로 122-8 갯배 선착장 인근',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_gangwon_04.jpg',
        'description': '갯배 선착장과 아바이 순대골목, 속초해변이 도보 5분 거리인 소박하고 따뜻한 어촌 민박입니다.',
        'rating': 4.6
    },
    {
        'name': '인제 자작나무숲 쉼터민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 인제군 인제읍 자작나무숲길 760',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_gangwon_05.jpg',
        'description': '순백의 자작나무 숲 트레킹 코스 입구에 자리하여 맑은 계곡물 소리를 들을 수 있는 숲속 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '삼척 장호항 나폴리바다민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 삼척시 근덕면 장호항길 58',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_gangwon_06.jpg',
        'description': '한국의 나폴리로 불리는 장호항 투명카약과 스노클링 명소 바로 앞 에메랄드 바다 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '고성 화진포 호수솔향민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 고성군 거진읍 화진포길 280',
        'price_per_night': 65000,
        'image_url': '/static/img/accomodation/minbak_gangwon_07.jpg',
        'description': '동해 바다와 거대한 석호 화진포 호수가 만나는 울창한 송림 숲길 곁의 한적한 쉼터입니다.',
        'rating': 4.6
    },
    {
        'name': '홍천 살둔마을 오지계곡민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 홍천군 내면 살둔길 52 내린천 상류',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_gangwon_08.jpg',
        'description': '원시림 계곡 내린천 상류에서 맑은 계곡물과 반딧불이를 만나는 자연 그대로의 오지 힐링 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '태백산 자락 너와집민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 태백시 태백산로 4778 당골광장 인근',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_gangwon_09.jpg',
        'description': '태백산 청정 고산지대 전통 붉은소나무 너와지붕 가옥에서 체험하는 정취 있는 산촌 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '동해 묵호등대 논골담길민박',
        'category': '민박',
        'region': RegionEnum.GANGWON.value,
        'location': '강원 동해시 일출로 135-2 논골담길 정상',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_gangwon_10.jpg',
        'description': '아기자기한 벽화 골목 논골담길 정상 묵호등대 아래 바다 전망이 한눈에 트인 언덕 민박입니다.',
        'rating': 4.7
    },

    # =========================================================================
    # 3. 충청 (CHUNGCHEONG) - 호텔 10건
    # =========================================================================
    {
        'name': '아일랜드 리솜 태안',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 태안군 안면읍 꽃지해안로 204 꽃지해변 앞',
        'price_per_night': 260000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_01.jpg',
        'description': '꽃지해수욕장 붉은 서해 낙조를 객실과 인피니티 풀에서 감상하는 명품 해양 리조트 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '포레스트 리솜 제천',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충북 제천시 백운면 금봉로 365 원시림 숲속',
        'price_per_night': 310000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_02.jpg',
        'description': '구학산 원시림 숲속 인피니티 해브나인 스파로 유명한 국내 최고의 에코 힐링 숲 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '롯데리조트 부여',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 부여군 규암면 백제문로 400',
        'price_per_night': 195000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_03.jpg',
        'description': '백제 역사문화단지 맞은편 전통 궁궐 루프 디자인과 아쿠아가든을 갖춘 역사문화 테마 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '소노문 단양',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충북 단양군 단양읍 삼봉로 187-17',
        'price_per_night': 170000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_04.jpg',
        'description': '남한강과 단양팔경 소백산 자락을 조망하는 아쿠아월드 보유 가족 휴양 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '오엔시티 호텔 천안',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 천안시 서북구 검은들3길 46 불당동',
        'price_per_night': 130000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_05.jpg',
        'description': '천안 불당 신도시 중심 루프탑 사우나와 모던하고 쾌적한 객실의 비즈니스 & 레저 호텔입니다.',
        'rating': 4.6
    },
    {
        'name': '호텔 오노마 대전 오토그래프 컬렉션',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '대전 유성구 엑스포로 1 엑스포타워 38-42층',
        'price_per_night': 240000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_06.jpg',
        'description': '갑천 수변 뷰와 신세계 Art&Science 시설을 함께 즐기는 메리어트 럭셔리 라이프스타일 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '인터시티 호텔 대전 유성',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '대전 유성구 온천로 92 유성온천역 인근',
        'price_per_night': 140000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_07.jpg',
        'description': '100년 전통 유성 천연 온천수를 공급하는 사우나 스파 시설을 갖춘 온천 힐링 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '스플라스 리솜 예산 덕산',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 예산군 덕산면 온천단지3로 45-7',
        'price_per_night': 200000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_08.jpg',
        'description': '덕산 게르마늄 온천 워터파크와 쾌적한 객실로 온 가족이 사계절 물놀이를 즐기는 온천 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '벨포레 리조트 증평',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충북 증평군 도안면 벨포레길 346',
        'price_per_night': 180000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_09.jpg',
        'description': '원남저수지와 루지, 양떼목장, 마리나클럽을 품은 충청 내륙 최대 규모의 복합 힐링 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '호텔 온양온천 아산',
        'category': '호텔',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 아산시 온천대로 1459 온양온천역 앞',
        'price_per_night': 125000,
        'image_url': '/static/img/accomodation/hotel_chungcheong_10.jpg',
        'description': '조선 왕실 온양행궁의 역사를 간직한 국내에서 가장 오래된 온천 전통을 지닌 클래식 호텔입니다.',
        'rating': 4.5
    },

    # =========================================================================
    # 3. 충청 (CHUNGCHEONG) - 민박 10건
    # =========================================================================
    {
        'name': '공주 한옥마을 백제고택민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 공주시 관광단지길 12 무령왕릉 인근',
        'price_per_night': 110000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_01.jpg',
        'description': '무령왕릉 인근 참나무 장작 구들장 난방을 하는 친환경 전통 한옥마을 명품 한옥민박입니다.',
        'rating': 4.9
    },
    {
        'name': '서산 해미읍성 솔바람민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 서산시 해미면 남문2로 33 해미읍성 돌담길',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_02.jpg',
        'description': '조선시대 해미읍성 돌담길을 따라 솔숲 향이 은은한 정겨운 전통 시골 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '대천해수욕장 머드바다민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 보령시 대해로 894 보령머드광장 앞',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_03.jpg',
        'description': '대천 머드광장 바로 뒤편, 서해 바다 내음 가득하고 신선한 해산물이 풍성한 해변가 민박입니다.',
        'rating': 4.6
    },
    {
        'name': '영동 감나무골 황토민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충북 영동군 심천면 국악로 18',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_04.jpg',
        'description': '난계 국악마을과 주홍빛 감나무 가로수길 곁에 자리한 토속 황토방 힐링 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '괴산 산막이옛길 강변민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충북 괴산군 칠성면 산막이옛길 88 괴산호 인근',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_05.jpg',
        'description': '괴산호 수변 산책로 산막이옛길 유람선 선착장 인근 푸른 호수를 마주한 쉼터 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '제천 청풍호반 물안개민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충북 제천시 청풍면 청풍호로 2040 청풍문화재단지 앞',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_06.jpg',
        'description': '청풍문화재단지와 비봉산 케이블카가 한눈에 내려다보이는 아름다운 호반 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '단양 도담삼봉 호젓한민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충북 단양군 매포읍 삼봉로 640 도담삼봉 앞',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_07.jpg',
        'description': '남한강 도담삼봉의 절경을 마당에서 마주하며 조용히 쉬어가는 강변 쉼터입니다.',
        'rating': 4.7
    },
    {
        'name': '태안 안면도 솔향기바다민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 태안군 안면읍 안면대로 3150 안면송 숲길',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_08.jpg',
        'description': '안면도 자연휴양림 울창한 안면송 붉은 소나무 숲길 옆 아늑하고 운치 있는 바다 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '서천 신성리 갈대밭 낭만민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충남 서천군 한산면 신성리 110 금강변',
        'price_per_night': 65000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_09.jpg',
        'description': '금강 하구 광활한 갈대밭과 한산 소곡주 향기 그윽한 소담한 감성 민박입니다.',
        'rating': 4.6
    },
    {
        'name': '옥천 향수마을 시인민박',
        'category': '민박',
        'region': RegionEnum.CHUNGCHEONG.value,
        'location': '충북 옥천군 옥천읍 향수길 56 정지용 생가 인근',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_chungcheong_10.jpg',
        'description': '정지용 생가와 실개천 골목길에 자리잡은 문학적 감성의 소담하고 아늑한 민박입니다.',
        'rating': 4.6
    },

    # =========================================================================
    # 4. 전라 (JEONLA) - 호텔 10건
    # =========================================================================
    {
        'name': '유탑유블레스 호텔 여수',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 여수시 오동도로 61-15 엑스포공원 입구',
        'price_per_night': 210000,
        'image_url': '/static/img/accomodation/hotel_jeonla_01.jpg',
        'description': '여수 엑스포 해양공원과 오동도 입구 루프탑 오션 오아시스 풀을 보유한 특급 오션뷰 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '라마다프라자 바이 윈덤 여수',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 여수시 돌산읍 강남로 11 돌산대교 앞',
        'price_per_night': 190000,
        'image_url': '/static/img/accomodation/hotel_jeonla_02.jpg',
        'description': '돌산대교와 여수 밤바다 전망, 옥상 짚라인 익스트림 시설을 갖춘 랜드마크 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '호텔현대 바이 라한 목포',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 영암군 삼호읍 대불로 91 다도해 조망',
        'price_per_night': 170000,
        'image_url': '/static/img/accomodation/hotel_jeonla_03.jpg',
        'description': '다도해 푸른 바다와 영암호를 조망하는 서남해안 최고급 특급 비즈니스 & 휴양 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '엘도라도 리조트 신안 증도',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 신안군 지도읍 지도증도로 1766-15 우전해변',
        'price_per_night': 230000,
        'image_url': '/static/img/accomodation/hotel_jeonla_04.jpg',
        'description': '증도 슬로시티 우전해변 갯벌과 해수 유황 스파를 즐기는 남도 대표 해양 빌라 리조트입니다.',
        'rating': 4.8
    },
    {
        'name': '유탑 부티크 호텔 광주 상무',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '광주 서구 시청로 53 상무지구 중심',
        'price_per_night': 135000,
        'image_url': '/static/img/accomodation/hotel_jeonla_05.jpg',
        'description': '상무지구 중심 첨단 IoT 시설과 세련된 인테리어를 갖춘 스타일리시 시티 라이프 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '라한호텔 전주 한옥마을',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '전북 전주시 완산구 기린대로 85 한옥마을 입구',
        'price_per_night': 195000,
        'image_url': '/static/img/accomodation/hotel_jeonla_06.jpg',
        'description': '전주 한옥마을 기와지붕들이 한눈에 펼쳐지는 루프탑 야외 수영장을 보유한 명품 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '소노벨 변산 부안',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '전북 부안군 변산면 변산해변로 51 격포해변 앞',
        'price_per_night': 200000,
        'image_url': '/static/img/accomodation/hotel_jeonla_07.jpg',
        'description': '채석강 해안 절벽과 격포해수욕장 노을을 마주하는 오션 워터파크 복합 리조트 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '여수 베네치아 호텔앤리조트',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 여수시 오동도로 61-13 여수항 앞',
        'price_per_night': 180000,
        'image_url': '/static/img/accomodation/hotel_jeonla_08.jpg',
        'description': '전 객실 오션뷰와 옥상 루프탑 인피니티 풀을 자랑하는 인기 만점 해양 휴양 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '지리산 더케이 가족호텔 구례',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 구례군 산동면 온천관광로 107 지리산 온천랜드',
        'price_per_night': 130000,
        'image_url': '/static/img/accomodation/hotel_jeonla_09.jpg',
        'description': '지리산 노고단 자락 게르마늄 게르마늄 천연 온천수 스파를 즐기는 가족 친화 호텔입니다.',
        'rating': 4.6
    },
    {
        'name': '군산 에이본 호텔',
        'category': '호텔',
        'region': RegionEnum.JEONLA.value,
        'location': '전북 군산시 해망로 10 군산 고속버스터미널 인근',
        'price_per_night': 125000,
        'image_url': '/static/img/accomodation/hotel_jeonla_10.jpg',
        'description': '근대역사문화거리와 경암동 철길마을 인근의 깔끔하고 모던한 시설을 자랑하는 호텔입니다.',
        'rating': 4.6
    },

    # =========================================================================
    # 4. 전라 (JEONLA) - 민박 10건
    # =========================================================================
    {
        'name': '전주 한옥마을 향교스테이 명품민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전북 전주시 완산구 향교길 42 전주향교 옆',
        'price_per_night': 115000,
        'image_url': '/static/img/accomodation/minbak_jeonla_01.jpg',
        'description': '수백 년 은행나무가 뜰을 지키는 전주향교 옆 전통 구들장 온돌 명품 한옥민박입니다.',
        'rating': 4.9
    },
    {
        'name': '담양 죽녹원 대숲바람민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 담양군 담양읍 죽녹원로 125 대나무숲 앞',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_jeonla_02.jpg',
        'description': '사각사각 대나무 잎소리와 피톤치드가 마당 가득 차오르는 대숲 힐링 쉼터입니다.',
        'rating': 4.8
    },
    {
        'name': '순천만 갈대밭 갯벌생태민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 순천시 순천만길 512 순천만습지 인근',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_jeonla_03.jpg',
        'description': '순천만습지 흑두루미 도래지와 붉은 칠면초 군락을 마주하는 청정 생태 쉼터 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '보성 녹차밭 솔향기다도민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 보성군 보성읍 녹차로 763 대한다원 인근',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_jeonla_04.jpg',
        'description': '대한다원 차밭 초록 능선 아래 다도 체험과 솔숲 산책을 함께 누리는 감성 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '구례 섬진강 벚꽃강변민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 구례군 문척면 섬진강변로 280 사성암 아래',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_jeonla_05.jpg',
        'description': '굽이치는 섬진강 맑은 물줄기와 지리산 능선이 병풍처럼 둘러선 풍경 좋은 강변 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '완도 청산도 슬로길돌담민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 완도군 청산면 당락길 25 서편제 촬영지',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_jeonla_06.jpg',
        'description': '노란 유채꽃과 청보리밭이 넘실대는 서편제 언덕 구들장 돌담길 안쪽 전통 어촌 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '남원 광한루원 달빛한옥민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전북 남원시 요천로 1447 광한루원 정문 앞',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_jeonla_07.jpg',
        'description': '춘향의 고향 광한루원 연못 곁 요천 생태공원의 맑은 바람이 스치는 고전미 한옥민박입니다.',
        'rating': 4.7
    },
    {
        'name': '강진 다산초당 다향숲민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 강진군 도암면 다산초당길 68',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_jeonla_08.jpg',
        'description': '다산 정약용 유배지의 오솔길 끝 동백나무 숲과 찻잎 향이 그윽한 인문학 감성 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '고창 선운사 동백골황토민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전북 고창군 아산면 선운사로 188 도솔천 곁',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_jeonla_09.jpg',
        'description': '천년고찰 선운사 울창한 동백꽃 숲과 도솔천 계곡 곁에 자리한 고즈넉한 황토 민박입니다.',
        'rating': 4.6
    },
    {
        'name': '신안 퍼플섬 보랏빛바다민박',
        'category': '민박',
        'region': RegionEnum.JEONLA.value,
        'location': '전남 신안군 안좌면 소곡두리길 88 퍼플교 앞',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_jeonla_10.jpg',
        'description': '보라색 다리와 라벤더 꽃밭이 펼쳐진 퍼플섬 증도 바닷가 이색 테마 감성 민박입니다.',
        'rating': 4.8
    },

    # =========================================================================
    # 5. 경북 (GYEONGSANG) - 호텔 10건
    # =========================================================================
    {
        'name': '힐튼 경주',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 경주시 보문로 422 보문호수 앞',
        'price_per_night': 280000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_01.jpg',
        'description': '보문호수 산책로와 미술관 우양미술관을 품은 경주 최고의 5성급 럭셔리 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '라한셀렉트 경주',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 경주시 보문로 338 보문호수 뷰',
        'price_per_night': 250000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_02.jpg',
        'description': '보문호수 정면 파노라마 뷰와 북스토어 경주산책을 갖춘 감성 호반 특급 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '라한호텔 포항',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 포항시 북구 삼호로 265번길 1 영일대해변 앞',
        'price_per_night': 175000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_03.jpg',
        'description': '영일대 해수욕장 모래사장과 영일대 해상누각 전망의 전 객실 오션뷰 랜드마크 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '리첼호텔 안동',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 안동시 관광단지로 346-9 안동관광단지',
        'price_per_night': 145000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_04.jpg',
        'description': '안동문화관광단지 중심 유교랜드와 인접한 쾌적하고 넉넉한 전통 문화 관광 호텔입니다.',
        'rating': 4.6
    },
    {
        'name': 'STX리조트 문경',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 문경시 농암면 청화로 509 속리산 자락',
        'price_per_night': 185000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_05.jpg',
        'description': '속리산 자락 청화산 원시림 계곡 속 스파 스파빌라를 보유한 대규모 청정 산악 리조트입니다.',
        'rating': 4.7
    },
    {
        'name': '호텔 인터불고 대구',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '대구 수성구 팔현길 212 망우공원 내',
        'price_per_night': 210000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_06.jpg',
        'description': '금호강변 망우공원 울창한 숲에 둘러싸인 유서 깊고 품격 있는 대구 대표 특급 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '소노벨 청송',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 청송군 주왕산면 주왕산로 494-1',
        'price_per_night': 190000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_07.jpg',
        'description': '주왕산 국립공원 입구 솔샘온천 탄산약수 노천탕을 즐기는 명품 웰빙 스파 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '힐링스테이 영주 소백헌',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 영주시 풍기읍 소백산로 2156',
        'price_per_night': 155000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_08.jpg',
        'description': '소백산 희방사 계곡과 풍기 인삼마을 인근 풍경 좋은 친자연 웰니스 힐링 호텔입니다.',
        'rating': 4.7
    },
    {
        'name': '울릉도 힐링스테이 코스모스 리조트',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 울릉군 북면 추산길 88-13 추산 송곳봉 앞',
        'price_per_night': 450000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_09.jpg',
        'description': '추산 송곳바위 절벽 아래 세계 건축상을 석권한 동해 울릉도의 하이엔드 럭셔리 리조트입니다.',
        'rating': 5.0
    },
    {
        'name': '덕구온천 리조트호텔 울진',
        'category': '호텔',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 울진군 북면 덕구온천로 924 응봉산 계곡',
        'price_per_night': 160000,
        'image_url': '/static/img/accomodation/hotel_GYEONGSANG_10.jpg',
        'description': '국내 유일 자연용출 천연 온천수가 샘솟는 응봉산 계곡의 청정 스파 힐링 호텔입니다.',
        'rating': 4.7
    },

    # =========================================================================
    # 5. 경북 (GYEONGSANG) - 민박 10건
    # =========================================================================
    {
        'name': '안동 하회마을 옥연정사 고택민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 안동시 풍천면 광덕솔밭길 86 부용대 아래',
        'price_per_night': 130000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_01.jpg',
        'description': '부용대 절벽 아래 낙동강이 감싸 안은 서애 류성룡 선생의 유서 깊은 보물급 고택민박입니다.',
        'rating': 4.9
    },
    {
        'name': '경주 첨성대 달빛한옥민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 경주시 첨성로 99번길 16 황리단길 인근',
        'price_per_night': 95000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_02.jpg',
        'description': '대릉원 고분군과 황리단길 인근 밤이면 첨성대 야경이 아름다운 전통 한옥민박입니다.',
        'rating': 4.8
    },
    {
        'name': '청송 주왕산 사과나무과수원민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 청송군 주왕산면 당마을길 15',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_03.jpg',
        'description': '달콤한 청송 꿀사과 과수원 옆 주왕산 기암괴석 봉우리가 올려다보이는 과수원 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '울릉도 나리분지 너와집민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 울릉군 북면 나리1길 45 화산 분화구 평야',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_04.jpg',
        'description': '울릉도 유일한 평야 화산 분화구 나리분지 속 전통 너와 투막집에서 체험하는 특별한 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '영덕 강구항 대게거리 바다민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 영덕군 강구면 강구대게길 112 강구항 앞',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_05.jpg',
        'description': '영덕 블루로드 도보길과 강구항 대게거리 앞 시원한 동해 파도 소리가 들리는 바다 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '문경새재 황토돌담옛길민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 문경시 문경읍 새재로 865 문경새재 1관문 아래',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_06.jpg',
        'description': '과거 선비들이 걷던 문경새재 황톳길과 전통 도자기 가마터 곁의 운치 있는 돌담 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '봉화 닭실마을 청암한옥민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 봉화군 봉화읍 충재길 44 청암정 앞',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_07.jpg',
        'description': '금닭이 알을 품은 명당 500년 전통마을 청암정 정자 앞 고즈넉한 종택 한옥 쉼터입니다.',
        'rating': 4.8
    },
    {
        'name': '성주 가야산 야생화골민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 성주군 수륜면 가야산로 1250 가야산 국립공원 입구',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_08.jpg',
        'description': '가야산 만물상 코스 초입 맑은 계곡과 사계절 야생화 향기 가득한 숲속 힐링 민박입니다.',
        'rating': 4.6
    },
    {
        'name': '포항 호미곶 일출바다민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 포항시 남구 호미곶면 해맞이로 150 상생의손 앞',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_09.jpg',
        'description': '상생의 손 조형물과 호미곶 등대 앞 한반도에서 가장 빠른 해돋이를 맞이하는 바닷가 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '경주 양동마을 회재고택민박',
        'category': '민박',
        'region': RegionEnum.GYEONGSANG.value,
        'location': '경북 경주시 강동면 양동마을길 124 양동마을 내',
        'price_per_night': 90000,
        'image_url': '/static/img/accomodation/minbak_gyeongbuk_10.jpg',
        'description': '유네스코 세계문화유산 600년 조선 반촌의 기와집과 초가집이 어우러진 전통 가옥 민박입니다.',
        'rating': 4.8
    },

    # =========================================================================
    # 6. 제주 (JEJU) - 호텔 10건
    # =========================================================================
    {
        'name': '그랜드 조선 제주',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 중문관광로 72번길 60 중문관광단지',
        'price_per_night': 350000,
        'image_url': '/static/img/accomodation/hotel_jeju_01.jpg',
        'description': '중문 야자수 정원과 루프탑 피크풀, 사계절 온수풀을 갖춘 클래식 럭셔리 휴양 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '제주 신라호텔',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 중문관광로 72번길 75 숨비정원 앞',
        'price_per_night': 420000,
        'image_url': '/static/img/accomodation/hotel_jeju_02.jpg',
        'description': '숨비정원 해변 산책로와 글램핑, 야외 온수풀을 즐기는 국내 최고 권위의 럭셔리 리조트입니다.',
        'rating': 5.0
    },
    {
        'name': '롯데호텔 제주',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 중문관광로 72번길 35',
        'price_per_night': 380000,
        'image_url': '/static/img/accomodation/hotel_jeju_03.jpg',
        'description': '풍차 라운지와 대형 야외 온수 스파 풀 해온을 품은 남태평양풍 휴양 리조트 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': '해비치 호텔앤드리조트 제주',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 표선면 민속해안로 537 표선백사장 앞',
        'price_per_night': 330000,
        'image_url': '/static/img/accomodation/hotel_jeju_04.jpg',
        'description': '표선 백사장 에메랄드 바다와 국내 최대 규모 실내 아트리움 정원을 자랑하는 특급 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '휘닉스 아일랜드 제주 섭지코지',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 성산읍 섭지코지로 107',
        'price_per_night': 290000,
        'image_url': '/static/img/accomodation/hotel_jeju_05.jpg',
        'description': '섭지코지 해안 절벽 위 안도 타다오의 글라스하우스와 유민미술관을 품은 오션 리조트입니다.',
        'rating': 4.9
    },
    {
        'name': '파르나스 호텔 제주',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 중문관광로 72번길 100 중문 벼랑 끝',
        'price_per_night': 390000,
        'image_url': '/static/img/accomodation/hotel_jeju_06.jpg',
        'description': '중문 절벽 끝 국내 최장 110m 인피니티 오션 풀을 보유한 신축 하이엔드 럭셔리 호텔입니다.',
        'rating': 5.0
    },
    {
        'name': '그랜드 하얏트 제주 드림타워',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 제주시 노연로 12 제주 드림타워 8-38층',
        'price_per_night': 320000,
        'image_url': '/static/img/accomodation/hotel_jeju_07.jpg',
        'description': '제주 최고층 38층 트윈타워에서 도심과 제주 바다를 굽어보는 전 객실 올스위트 호텔입니다.',
        'rating': 4.9
    },
    {
        'name': 'JW 메리어트 제주 리조트앤스파',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 호근서호로 399 올레7코스 절벽 위',
        'price_per_night': 480000,
        'image_url': '/static/img/accomodation/hotel_jeju_08.jpg',
        'description': '올레 7코스 주상절리 절벽 위 제주 자연과 한국 전통미를 현대적으로 승화한 최고급 럭셔리 호텔입니다.',
        'rating': 5.0
    },
    {
        'name': '제주 신화월드 메리어트 리조트',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 안덕면 신화역사로304번길 38',
        'price_per_night': 240000,
        'image_url': '/static/img/accomodation/hotel_jeju_09.jpg',
        'description': '워터파크, 테마파크, 쇼핑 스트리트가 집결된 대규모 올인원 복합 레저 리조트 호텔입니다.',
        'rating': 4.8
    },
    {
        'name': '메종 글래드 제주',
        'category': '호텔',
        'region': RegionEnum.JEJU.value,
        'location': '제주 제주시 연삼로 80 연동 도심',
        'price_per_night': 160000,
        'image_url': '/static/img/accomodation/hotel_jeju_10.jpg',
        'description': '제주 국제공항 10분 거리, 40년 전통의 솔나무 야외 정원 수영장을 품은 도심 속 휴양 호텔입니다.',
        'rating': 4.7
    },

    # =========================================================================
    # 6. 제주 (JEJU) - 민박 10건
    # =========================================================================
    {
        'name': '구좌 월정리 현무암돌담민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 제주시 구좌읍 월정1길 46 월정리 해변 앞',
        'price_per_night': 90000,
        'image_url': '/static/img/accomodation/minbak_jeju_01.jpg',
        'description': '에메랄드빛 월정리 바다와 검은 현무암 돌담이 어우러진 정겨운 감성 제주 가옥 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '애월 바다품은 노을언덕민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 제주시 애월읍 애월로 11길 18 한담해변 벼랑 위',
        'price_per_night': 95000,
        'image_url': '/static/img/accomodation/minbak_jeju_02.jpg',
        'description': '한담해변 산책로 벼랑 위 서쪽 바다로 떨어지는 붉은 일몰이 환상적인 바닷가 민박입니다.',
        'rating': 4.9
    },
    {
        'name': '성산일출봉 유채꽃밭민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 성산읍 성산등용로 84 성산일출봉 앞',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_jeju_03.jpg',
        'description': '창문 너머 웅장한 성산일출봉 분화구가 손에 잡힐 듯 가깝고 노란 유채꽃이 만발한 쉼터입니다.',
        'rating': 4.8
    },
    {
        'name': '서귀포 귤밭 스테이민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 남원읍 태위로 320 감귤 농원',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_jeju_04.jpg',
        'description': '노란 감귤 나무 향기가 그윽한 과수원 속 아담하고 평온한 제주 시골 돌집 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '조천 함덕서우봉 감성민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 제주시 조천읍 함덕16길 22 함덕해수욕장 곁',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_jeju_05.jpg',
        'description': '함덕해수욕장 맑은 바다와 서우봉 오름 둘레길이 도보 거리에 있는 따뜻한 감성 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '한림 협재금능 하얀모래민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 제주시 한림읍 금능길 35 금능으뜸해변 앞',
        'price_per_night': 90000,
        'image_url': '/static/img/accomodation/minbak_jeju_06.jpg',
        'description': '비양도가 손에 잡힐 듯 보이는 금능 해변 하얀 백사장 옆의 시원하고 깨끗한 바닷가 민박입니다.',
        'rating': 4.9
    },
    {
        'name': '표선 돌집스테이 오름민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 표선면 번영로 2350 따라비오름 인근',
        'price_per_night': 75000,
        'image_url': '/static/img/accomodation/minbak_jeju_07.jpg',
        'description': '제주 전통 흙벽과 돌담을 리모델링하여 아늑한 정취를 자랑하는 중산간 오름 민박입니다.',
        'rating': 4.7
    },
    {
        'name': '대정 모슬포 노을항민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 대정읍 하모항구로 64 모슬포항',
        'price_per_night': 70000,
        'image_url': '/static/img/accomodation/minbak_jeju_08.jpg',
        'description': '가파도 마라도 여객선 터미널 인근 방어 축제와 정겨운 남쪽 포구 풍경의 바다 민박입니다.',
        'rating': 4.6
    },
    {
        'name': '안덕 산방산 솔바람민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 서귀포시 안덕면 산방로 218 산방산 아래',
        'price_per_night': 80000,
        'image_url': '/static/img/accomodation/minbak_jeju_09.jpg',
        'description': '종 모양의 거대한 산방산 바위산과 용머리해안 바다를 품은 수려한 자연 힐링 민박입니다.',
        'rating': 4.8
    },
    {
        'name': '우도 서빈백사 산호바다민박',
        'category': '민박',
        'region': RegionEnum.JEJU.value,
        'location': '제주 제주시 우도면 우도해안길 252 산호해변 앞',
        'price_per_night': 85000,
        'image_url': '/static/img/accomodation/minbak_jeju_10.jpg',
        'description': '눈부신 하얀 홍조단괴 산호해변 바로 앞, 섬 속의 섬 우도 바다 풍경을 누리는 감성 민박입니다.',
        'rating': 4.8
    }
]

def seed_accommodations():
    app = create_app()
    with app.app_context():
        # Create all tables (accommodations, order_accommodations, etc.)
        db.create_all()

        added_cnt = 0
        updated_cnt = 0
        for data in accommodations_data:
            acc = Accommodation.query.filter_by(name=data['name']).first()
            if not acc:
                acc = Accommodation(
                    name=data['name'],
                    category=data['category'],
                    region=data['region'],
                    location=data['location'],
                    price_per_night=data['price_per_night'],
                    image_url=data['image_url'],
                    description=data['description'],
                    rating=data['rating']
                )
                db.session.add(acc)
                added_cnt += 1
            else:
                acc.category = data['category']
                acc.region = data['region']
                acc.location = data['location']
                acc.price_per_night = data['price_per_night']
                acc.image_url = data['image_url']
                acc.description = data['description']
                acc.rating = data['rating']
                updated_cnt += 1
        
        db.session.commit()
        total_acc = Accommodation.query.count()
        print(f"[Seed Accommodations] 성공! 신규 {added_cnt}건 추가, {updated_cnt}건 갱신 (총 {total_acc}건)")

        # Verify by region and category
        for r in RegionEnum:
            h_cnt = Accommodation.query.filter_by(region=r.value, category='호텔').count()
            m_cnt = Accommodation.query.filter_by(region=r.value, category='민박').count()
            print(f" - {r.value}: 호텔 {h_cnt}건, 민박 {m_cnt}건 (합계 {h_cnt + m_cnt}건)")

if __name__ == '__main__':
    seed_accommodations()

