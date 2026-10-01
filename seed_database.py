import json
import random
from datetime import datetime, timezone, timedelta
from pybo import create_app, db
from pybo.models import User, TourProduct, RegionEnum, Review, Order, OrderItem, Payment

def seed_database():
    users_data = [
        {'username': 'hong', 'name': '홍길동', 'email': 'hong@example.com', 'phone': '010-1234-5678', 'role': 'MEMBER'},
        {'username': 'traveler_kim', 'name': '김여행', 'email': 'kim@example.com', 'phone': '010-2222-3333', 'role': 'MEMBER'},
        {'username': 'jeju_holic', 'name': '이바다', 'email': 'ocean@example.com', 'phone': '010-4444-5555', 'role': 'MEMBER'},
        {'username': 'tour_master', 'name': '박방랑', 'email': 'wanderer@example.com', 'phone': '010-7777-8888', 'role': 'MEMBER'},
        {'username': 'happy_min', 'name': '최민우', 'email': 'min@example.com', 'phone': '010-9999-0000', 'role': 'MEMBER'},
    ]

    created_users = []
    for u in users_data:
        user = User.query.filter_by(user_id=u['username']).first()
        if not user:
            user = User(
                user_id=u['username'],
                name=u['name'],
                email=u['email'],
                phone=u['phone'],
                #role=u['role']
            )
            user.set_password('12341234')
            db.session.add(user)
            db.session.flush()

            # 장바구니 자동 생성
            #cart = Cart(user_id=user.id)
            #db.session.add(cart)
        created_users.append(user)

    # 3. 6대 권역별 총 96개 추천 관광 상품 정의 (권역당 16개씩, 관광지별 4개 고화질 이미지 슬라이드)
    products_data = [
        # --- [1] 서울/경기 (16개) ---
        {
            'name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'description': '사계절 아름다운 야생화와 정원이 펼쳐진 수목원과 북한강을 가로지르는 남이섬에서 즐기는 수도권 최고의 낭만 힐링 코스.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 65000,
            'member_discount_rate': 0.15,
            'recommendation_count': 890,
            'image_urls': [
                '/static/img/tours/product_01_1.jpg',
                '/static/img/tours/product_01_2.jpg',
                '/static/img/tours/product_01_3.jpg',
                '/static/img/tours/product_01_4.jpg'
            ]
        },
        {
            'name': '수원 화성 성곽길 달빛 투어 & 플라잉 수원 열기구 체험',
            'description': '정조대왕의 얼이 깃든 수원화성 야경을 둘러보고 계류식 헬륨 기구에 탑승해 수원 도심의 야경을 한눈에 내려다보는 특별한 밤!',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 45000,
            'member_discount_rate': 0.10,
            'recommendation_count': 520,
            'image_urls': [
                '/static/img/tours/product_02_1.jpg',
                '/static/img/tours/product_02_2.jpg',
                '/static/img/tours/product_02_3.jpg',
                '/static/img/tours/product_02_4.jpg'
            ]
        },
        {
            'name': '포천 아트밸리 모노레일 & 허브아일랜드 불빛동화 힐링',
            'description': '버려진 채석장을 에메랄드빛 호수 예술공원으로 탈바꿈한 포천 아트밸리와 은은한 허브 향기 가득한 야경 불빛 축제 코스.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 58000,
            'member_discount_rate': 0.15,
            'recommendation_count': 710,
            'image_urls': [
                '/static/img/tours/product_03_1.jpg',
                '/static/img/tours/product_03_2.jpg',
                '/static/img/tours/product_03_3.jpg',
                '/static/img/tours/product_03_4.jpg'
            ]
        },
        {
            'name': '파주 헤이리 예술마을 도자기 공예 & 출판도시 북스테이',
            'description': '예술가들의 숨결이 깃든 헤이리 마을에서 직접 도자기를 빚어보고, 감각적인 건축미를 자랑하는 지혜의 숲에서 여유를 누립니다.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 42000,
            'member_discount_rate': 0.10,
            'recommendation_count': 460,
            'image_urls': [
                '/static/img/tours/product_04_1.jpg',
                '/static/img/tours/product_04_2.jpg',
                '/static/img/tours/product_04_3.jpg',
                '/static/img/tours/product_04_4.jpg'
            ]
        },
        {
            'name': '양평 두물머리 물안개 산책길 & 세미원 연꽃 힐링 정원',
            'description': '북한강과 남한강이 만나는 두물머리의 고즈넉한 풍경과 수생식물 정원 세미원에서 만나는 청량한 자연 휴식처.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 35000,
            'member_discount_rate': 0.10,
            'recommendation_count': 630,
            'image_urls': [
                '/static/img/tours/product_05_1.jpg',
                '/static/img/tours/product_05_2.jpg',
                '/static/img/tours/product_05_3.jpg',
                '/static/img/tours/product_05_4.jpg'
            ]
        },
        {
            'name': '용인 한국민속촌 전통 옹기 만들기 & 야간 조선 한복 축제',
            'description': '살아있는 조선 시대로의 시간 여행! 장인과 함께하는 전통 공예 체험과 달빛 아래 펼쳐지는 신명나는 전통 연희 공연.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 52000,
            'member_discount_rate': 0.15,
            'recommendation_count': 810,
            'image_urls': [
                '/static/img/tours/product_06_1.jpg',
                '/static/img/tours/product_06_2.jpg',
                '/static/img/tours/product_06_3.jpg',
                '/static/img/tours/product_06_4.jpg'
            ]
        },

        # --- [2] 강원 (6개) ---
        {
            'name': '대관령 양떼목장 산책 & 평창 익스트림 루지 체험',
            'description': '한국의 알프스 대관령 초원을 거닐며 건초 주기 체험을 하고, 신나는 마운틴 루지로 스릴을 만끽하는 강원도 대표 코스!',
            'region': RegionEnum.GANGWON.value,
            'original_price': 85000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1180,
            'image_urls': [
                '/static/img/tours/product_07_1.jpg',
                '/static/img/tours/product_07_2.jpg',
                '/static/img/tours/product_07_3.jpg',
                '/static/img/tours/product_07_4.jpg'
            ]
        },
        {
            'name': '강릉 안목해변 커피거리 & 정동진 바다열차 낭만 투어',
            'description': '동해 바다의 푸른 파도를 바라보며 즐기는 스페셜티 커피 한 잔과 해안선을 따라 달리는 정동진 바다열차 낭만 여행.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 70000,
            'member_discount_rate': 0.10,
            'recommendation_count': 940,
            'image_urls': [
                '/static/img/tours/product_08_1.jpg',
                '/static/img/tours/product_08_2.jpg',
                '/static/img/tours/product_08_3.jpg',
                '/static/img/tours/product_08_4.jpg'
            ]
        },
        {
            'name': '춘천 남이섬 스카이라인 짚와이어 & 의암호 카누 물레길',
            'description': '북한강 상공을 활강하는 짜릿한 짚와이어와 잔잔한 의암호 수면 위를 미끄러지듯 노 젓는 낭만 카누 체험.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 65000,
            'member_discount_rate': 0.15,
            'recommendation_count': 780,
            'image_urls': [
                '/static/img/tours/product_09_1.jpg',
                '/static/img/tours/product_09_2.jpg',
                '/static/img/tours/product_09_3.jpg',
                '/static/img/tours/product_09_4.jpg'
            ]
        },
        {
            'name': '속초 영랑호 벚꽃 둘레길 & 설악산 권금성 케이블카',
            'description': '웅장한 설악산의 기암괴석을 한눈에 조망하는 권금성 케이블카와 영랑호 호수변을 따라 걷는 피톤치드 힐링 산책.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 78000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1050,
            'image_urls': [
                '/static/img/tours/product_10_1.jpg',
                '/static/img/tours/product_10_2.jpg',
                '/static/img/tours/product_10_3.jpg',
                '/static/img/tours/product_10_4.jpg'
            ]
        },
        {
            'name': '정선 아리랑 열차 & 구절리 풍경 레일바이크 어드벤처',
            'description': '산세 깊은 정선 산골짜기를 레일바이크로 시원하게 달리고, 정선 아리랑 5일장에서 정겨운 먹거리를 즐깁니다.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 55000,
            'member_discount_rate': 0.10,
            'recommendation_count': 620,
            'image_urls': [
                '/static/img/tours/product_11_1.jpg',
                '/static/img/tours/product_11_2.jpg',
                '/static/img/tours/product_11_3.jpg',
                '/static/img/tours/product_11_4.jpg'
            ]
        },
        {
            'name': '인제 원대리 자작나무숲 힐링 트레킹 & 오색 탄산온천',
            'description': '순백의 자작나무가 빼곡히 솟아오른 숲길을 걸으며 심신을 정화하고, 천연 탄산온천에 몸을 담그는 웰니스 힐링.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 68000,
            'member_discount_rate': 0.15,
            'recommendation_count': 830,
            'image_urls': [
                '/static/img/tours/product_12_1.jpg',
                '/static/img/tours/product_12_2.jpg',
                '/static/img/tours/product_12_3.jpg',
                '/static/img/tours/product_12_4.jpg'
            ]
        },

        # --- [3] 충청 (6개) ---
        {
            'name': '단양 남한강 패러글라이딩 & 도담삼봉 수상 모터보트',
            'description': '청풍명월 충청의 푸른 하늘을 날아오르는 짜릿한 패러글라이딩과 남한강의 절경 도담삼봉을 누비는 익스트림 액티비티 체험!',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 110000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1250,
            'image_urls': [
                '/static/img/tours/product_13_1.jpg',
                '/static/img/tours/product_13_2.jpg',
                '/static/img/tours/product_13_3.jpg',
                '/static/img/tours/product_13_4.jpg'
            ]
        },
        {
            'name': '태안 안면도 꽃지해수욕장 일몰 & 머드 갯벌 바지락 체험',
            'description': '할미·할아비 바위 너머로 지는 환상적인 서해안 3대 낙조를 감상하고 청정 갯벌에서 조개잡이 생태 체험을 즐깁니다.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 48000,
            'member_discount_rate': 0.10,
            'recommendation_count': 690,
            'image_urls': [
                '/static/img/tours/product_14_1.jpg',
                '/static/img/tours/product_14_2.jpg',
                '/static/img/tours/product_14_3.jpg',
                '/static/img/tours/product_14_4.jpg'
            ]
        },
        {
            'name': '제천 청풍호반 케이블카 & 비봉산 하늘전망대 파노라마',
            'description': '내륙의 바다 청풍호를 가로질러 비봉산 정상에 오르면 사방으로 다도해 같은 호수 절경이 파노라마처럼 펼쳐집니다.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 62000,
            'member_discount_rate': 0.15,
            'recommendation_count': 740,
            'image_urls': [
                '/static/img/tours/product_15_1.jpg',
                '/static/img/tours/product_15_2.jpg',
                '/static/img/tours/product_15_3.jpg',
                '/static/img/tours/product_15_4.jpg'
            ]
        },
        {
            'name': '보령 대천해수욕장 해상 짚트랙 & 보령해저터널 드라이브',
            'description': '서해 바다 위를 시속 80km로 활강하는 스릴 만점 해상 짚트랙과 국내 최장 보령해저터널을 달리는 드라이브 코스.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 58000,
            'member_discount_rate': 0.10,
            'recommendation_count': 590,
            'image_urls': [
                '/static/img/tours/product_16_1.jpg',
                '/static/img/tours/product_16_2.jpg',
                '/static/img/tours/product_16_3.jpg',
                '/static/img/tours/product_16_4.jpg'
            ]
        },
        {
            'name': '부여 백제역사유적지구 & 궁남지 포룡정 밤도깨비 산책',
            'description': '찬란했던 백제 사비 시대의 왕궁 터를 둘러보고, 한국 최초의 인공 정원 궁남지 연못을 거닐며 역사의 정취를 느낍니다.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 42000,
            'member_discount_rate': 0.10,
            'recommendation_count': 450,
            'image_urls': [
                '/static/img/tours/product_17_1.jpg',
                '/static/img/tours/product_17_2.jpg',
                '/static/img/tours/product_17_3.jpg',
                '/static/img/tours/product_17_4.jpg'
            ]
        },
        {
            'name': '아산 지중해마을 골목 산책 & 파라다이스 스파 도고 힐링',
            'description': '이국적인 산토리니 감성의 하얀 골목을 걷고 유황 온천수로 피로를 녹여내는 충남 아산의 힐링 스파 여행.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 75000,
            'member_discount_rate': 0.15,
            'recommendation_count': 820,
            'image_urls': [
                '/static/img/tours/product_18_1.jpg',
                '/static/img/tours/product_18_2.jpg',
                '/static/img/tours/product_18_3.jpg',
                '/static/img/tours/product_18_4.jpg'
            ]
        },

        # --- [4] 전라 (6개) ---
        {
            'name': '여수 밤바다 낭만 요트 세일링 & 오동도 동백열차',
            'description': '선상에서 즐기는 불꽃놀이와 낭만 가득한 여수 밤바다 요트 투어, 바다 위의 꽃섬 오동도를 탐방하는 전라 대표 휴양 코스.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 80000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1340,
            'image_urls': [
                '/static/img/tours/product_19_1.jpg',
                '/static/img/tours/product_19_2.jpg',
                '/static/img/tours/product_19_3.jpg',
                '/static/img/tours/product_19_4.jpg'
            ]
        },
        {
            'name': '순천만 갈대군락지 생태 탐방 & 국가정원 스카이큐브',
            'description': '끝없이 펼쳐진 황금빛 순천만 갈대숲과 세계 각국의 정원을 한자리에서 관람할 수 있는 대한민국 생태 수도 투어.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 45000,
            'member_discount_rate': 0.10,
            'recommendation_count': 1120,
            'image_urls': [
                '/static/img/tours/product_20_1.jpg',
                '/static/img/tours/product_20_2.jpg',
                '/static/img/tours/product_20_3.jpg',
                '/static/img/tours/product_20_4.jpg'
            ]
        },
        {
            'name': '전주 한옥마을 다도 체험 & 명품 전통 한복 대여 패키지',
            'description': '고즈넉한 전주 한옥마을 골목을 전통 한복을 입고 거닐며 명인과 함께하는 전통 다도 예절을 배우는 문화 감성 여행입니다.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 50000,
            'member_discount_rate': 0.15,
            'recommendation_count': 980,
            'image_urls': [
                '/static/img/tours/product_21_1.jpg',
                '/static/img/tours/product_21_2.jpg',
                '/static/img/tours/product_21_3.jpg',
                '/static/img/tours/product_21_4.jpg'
            ]
        },
        {
            'name': '담양 죽녹원 대나무숲 산책 & 메타세쿼이아 힐링 로드',
            'description': '초록빛 대숲에서 뿜어져 나오는 음이온을 마시며 심신을 힐링하고, 곧게 뻗은 메타세쿼이아 길을 자전거로 달립니다.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 38000,
            'member_discount_rate': 0.10,
            'recommendation_count': 760,
            'image_urls': [
                '/static/img/tours/product_22_1.jpg',
                '/static/img/tours/product_22_2.jpg',
                '/static/img/tours/product_22_3.jpg',
                '/static/img/tours/product_22_4.jpg'
            ]
        },
        {
            'name': '보성 대한다원 햇녹차 찻잎 따기 & 편백 치유의 숲',
            'description': '계단식 초록 차밭의 절경을 배경으로 직접 찻잎을 덖고 맛보는 티클래스와 피톤치드 편백나무숲 트레킹.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 52000,
            'member_discount_rate': 0.15,
            'recommendation_count': 680,
            'image_urls': [
                '/static/img/tours/product_23_1.jpg',
                '/static/img/tours/product_23_2.jpg',
                '/static/img/tours/product_23_3.jpg',
                '/static/img/tours/product_23_4.jpg'
            ]
        },
        {
            'name': '신안 퍼플섬 보랏빛 다리 투어 & 태평염전 천일염 만들기',
            'description': '지붕도 다리도 온통 보라색인 환상의 섬 퍼플교를 거닐고 유네스코 생물권보전지역 증도에서 천일염 소금 만들기 체험.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 64000,
            'member_discount_rate': 0.15,
            'recommendation_count': 590,
            'image_urls': [
                '/static/img/tours/product_24_1.jpg',
                '/static/img/tours/product_24_2.jpg',
                '/static/img/tours/product_24_3.jpg',
                '/static/img/tours/product_24_4.jpg'
            ]
        },

        # --- [5] 경북 (6개) ---
        {
            'name': '울릉도 해안누리길 일주 & 독도 평화 바다 유람선',
            'description': '태고의 신비를 간직한 울릉도의 화산 비경 해안길을 걷고 대한민국 동쪽 끝 독도를 직접 밟아보는 평생의 버킷리스트 투어.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 180000,
            'member_discount_rate': 0.20,
            'recommendation_count': 1520,
            'image_urls': [
                '/static/img/tours/product_25_1.jpg',
                '/static/img/tours/product_25_2.jpg',
                '/static/img/tours/product_25_3.jpg',
                '/static/img/tours/product_25_4.jpg'
            ]
        },
        {
            'name': '경주 불국사 & 황리단길 야경 감성 힐링 산책',
            'description': '신라 천년의 역사 유적지와 트렌디한 황리단길 카페 골목, 동궁과 월지의 환상적인 야경을 감상하는 경북 힐링 명소입니다.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 75000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1190,
            'image_urls': [
                '/static/img/tours/product_26_1.jpg',
                '/static/img/tours/product_26_2.jpg',
                '/static/img/tours/product_26_3.jpg',
                '/static/img/tours/product_26_4.jpg'
            ]
        },
        {
            'name': '포항 호미곶 상생의 손 일출 & 환호공원 스페이스워크',
            'description': '한반도에서 가장 먼저 해가 뜨는 호미곶 바다 일출을 보고, 공중에 떠 있는 롤러코스터 계단 스페이스워크를 걷습니다.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 55000,
            'member_discount_rate': 0.10,
            'recommendation_count': 960,
            'image_urls': [
                '/static/img/tours/product_27_1.jpg',
                '/static/img/tours/product_27_2.jpg',
                '/static/img/tours/product_27_3.jpg',
                '/static/img/tours/product_27_4.jpg'
            ]
        },
        {
            'name': '안동 하회마을 전통 탈춤 관람 & 유교문화 한옥 고택 스테이',
            'description': '낙동강이 S자로 감싸 흐르는 하회마을에서 유서 깊은 양반 가옥을 체험하고 하회별신굿탈놀이를 관람합니다.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 85000,
            'member_discount_rate': 0.15,
            'recommendation_count': 870,
            'image_urls': [
                '/static/img/tours/product_28_1.jpg',
                '/static/img/tours/product_28_2.jpg',
                '/static/img/tours/product_28_3.jpg',
                '/static/img/tours/product_28_4.jpg'
            ]
        },
        {
            'name': '청송 주산지 왕버들 물안개 숲 & 솔기온천 스파 웰니스',
            'description': '물속에 뿌리를 내린 신비로운 왕버들과 아침 물안개의 비경을 감상하고, 미끌미끌한 알칼리 솔기온천에서 피로를 풉니다.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 72000,
            'member_discount_rate': 0.15,
            'recommendation_count': 640,
            'image_urls': [
                '/static/img/tours/product_29_1.jpg',
                '/static/img/tours/product_29_2.jpg',
                '/static/img/tours/product_29_3.jpg',
                '/static/img/tours/product_29_4.jpg'
            ]
        },
        {
            'name': '문경새재 황톳길 맨발 트레킹 & 오미자 와인동굴 투어',
            'description': '영남대로 과거길 문경새재 흙길을 맨발로 걸으며 자연을 느끼고, 와인터널에서 붉은 오미자 스파클링 와인을 시음합니다.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 49000,
            'member_discount_rate': 0.10,
            'recommendation_count': 580,
            'image_urls': [
                '/static/img/tours/product_30_1.jpg',
                '/static/img/tours/product_30_2.jpg',
                '/static/img/tours/product_30_3.jpg',
                '/static/img/tours/product_30_4.jpg'
            ]
        },

        # --- [6] 제주 (6개) ---
        {
            'name': '제주 비자림 숲길 & 함덕 해변 프라이빗 힐링 투어',
            'description': '천년의 숲 비자림에서 피톤치드를 마시고, 에메랄드빛 함덕 서우봉 해변에서 즐기는 여유로운 제주 휴양 코스입니다.',
            'region': RegionEnum.JEJU.value,
            'original_price': 120000,
            'member_discount_rate': 0.20,
            'recommendation_count': 1680,
            'image_urls': [
                '/static/img/tours/product_31_1.jpg',
                '/static/img/tours/product_31_2.jpg',
                '/static/img/tours/product_31_3.jpg',
                '/static/img/tours/product_31_4.jpg'
            ]
        },
        {
            'name': '제주 우도 전기차 일주 & 해녀와 함께하는 해산물 물질',
            'description': '산호초 백사장이 빛나는 섬 속의 섬 우도를 전기차로 시원하게 달리고, 현직 해녀와 함께 바다 물질 체험을 합니다.',
            'region': RegionEnum.JEJU.value,
            'original_price': 95000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1450,
            'image_urls': [
                '/static/img/tours/product_32_1.jpg',
                '/static/img/tours/product_32_2.jpg',
                '/static/img/tours/product_32_3.jpg',
                '/static/img/tours/product_32_4.jpg'
            ]
        },
        {
            'name': '협재 해수욕장 선셋 요트 투어 & 차귀도 야생 돌고래 탐선',
            'description': '비양도를 배경으로 노을 지는 서쪽 바다에서 샴페인을 곁들인 선셋 세일링과 차귀도 앞바다 야생 돌고래를 만납니다.',
            'region': RegionEnum.JEJU.value,
            'original_price': 110000,
            'member_discount_rate': 0.20,
            'recommendation_count': 1390,
            'image_urls': [
                '/static/img/tours/product_33_1.jpg',
                '/static/img/tours/product_33_2.jpg',
                '/static/img/tours/product_33_3.jpg',
                '/static/img/tours/product_33_4.jpg'
            ]
        },
        {
            'name': '한라산 영실 탐방로 절경 트레킹 & 흑돼지 미식 바비큐',
            'description': '오백나한 기암괴석과 병풍바위가 웅장하게 둘러싼 영실코스를 가볍게 트레킹하고 제주 청정 흑돼지 바비큐를 즐깁니다.',
            'region': RegionEnum.JEJU.value,
            'original_price': 88000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1220,
            'image_urls': [
                '/static/img/tours/product_34_1.jpg',
                '/static/img/tours/product_34_2.jpg',
                '/static/img/tours/product_34_3.jpg',
                '/static/img/tours/product_34_4.jpg'
            ]
        },
        {
            'name': '서귀포 쇠소깍 전통 나룻배 카약 & 외돌개 해안 올레길',
            'description': '용암이 굳어 형성된 기묘한 계곡 쇠소깍에서 투명 카약을 타고 남쪽 서귀포 푸른 바다의 해안 절벽 올레길을 걷습니다.',
            'region': RegionEnum.JEJU.value,
            'original_price': 65000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1080,
            'image_urls': [
                '/static/img/tours/product_35_1.jpg',
                '/static/img/tours/product_35_2.jpg',
                '/static/img/tours/product_35_3.jpg',
                '/static/img/tours/product_35_4.jpg'
            ]
        },
        {
            'name': '조천 곶자왈 에코랜드 숲속 기차 & 피톤치드 족욕 스파',
            'description': '화산 송이 곶자왈 원시림을 증기기관차를 타고 둘러보며 천연 허브 온천수에 발을 담그는 전 연령 맞춤 힐링 코스.',
            'region': RegionEnum.JEJU.value,
            'original_price': 58000,
            'member_discount_rate': 0.10,
            'recommendation_count': 890,
            'image_urls': [
                '/static/img/tours/product_36_1.jpg',
                '/static/img/tours/product_36_2.jpg',
                '/static/img/tours/product_36_3.jpg',
                '/static/img/tours/product_36_4.jpg'
            ]
        },

        # --- 추가 상품: [1] 서울/경기 추가 (10개) ---
        {
            'name': '양평 두물머리 물안개 & 세미원 연꽃정원 감성 산책',
            'description': '남한강과 북한강이 만나는 두물머리의 수려한 자연경관과 세미원의 연꽃 배다리를 거니는 당일 힐링 코스.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 48000,
            'member_discount_rate': 0.15,
            'recommendation_count': 640,
            'image_urls': ['/static/img/tours/product_01_1.jpg', '/static/img/tours/product_01_2.jpg', '/static/img/tours/product_01_3.jpg', '/static/img/tours/product_01_4.jpg']
        },
        {
            'name': '파주 헤이리 예술마을 & 임진각 평화누리 바람언덕 투어',
            'description': '감각적인 갤러리와 카페가 가득한 문화예술마을 헤이리와 평화의 소망을 담은 바람개비 언덕 탐방.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 52000,
            'member_discount_rate': 0.10,
            'recommendation_count': 780,
            'image_urls': ['/static/img/tours/product_02_1.jpg', '/static/img/tours/product_02_2.jpg', '/static/img/tours/product_02_3.jpg', '/static/img/tours/product_02_4.jpg']
        },
        {
            'name': '화성 융건릉 솔숲 산책 & 제부도 서해랑 케이블카 낙조',
            'description': '정조의 효심이 깃든 유네스코 세계유산 융건릉 숲길과 바다 위를 가로지르는 서해랑 케이블카 노을 뷰.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 58000,
            'member_discount_rate': 0.15,
            'recommendation_count': 590,
            'image_urls': ['/static/img/tours/product_03_1.jpg', '/static/img/tours/product_03_2.jpg', '/static/img/tours/product_03_3.jpg', '/static/img/tours/product_03_4.jpg']
        },
        {
            'name': '용인 한국민속촌 전통문화 체험 & 에버랜드 불꽃축제',
            'description': '조선시대 가옥과 전통 공연을 오감으로 체험하고 환상적인 야간 퍼레이드와 불꽃축제를 만끽하는 코스.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 85000,
            'member_discount_rate': 0.20,
            'recommendation_count': 1120,
            'image_urls': ['/static/img/tours/product_04_1.jpg', '/static/img/tours/product_04_2.jpg', '/static/img/tours/product_04_3.jpg', '/static/img/tours/product_04_4.jpg']
        },
        {
            'name': '안성 안성맞춤랜드 천문과학관 & 팜랜드 목장 체험',
            'description': '드넓은 초원에서 귀여운 동물들과 교감하고 밤하늘 별자리를 관측하는 온가족 감성 힐링 여행.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 42000,
            'member_discount_rate': 0.10,
            'recommendation_count': 430,
            'image_urls': ['/static/img/tours/product_05_1.jpg', '/static/img/tours/product_05_2.jpg', '/static/img/tours/product_05_3.jpg', '/static/img/tours/product_05_4.jpg']
        },
        {
            'name': '광주 남한산성 성곽길 트레킹 & 행궁 역사 기행',
            'description': '사계절 빼어난 경관을 자랑하는 호국의 성지 남한산성을 따라 걷고 유서 깊은 남한산성 행궁을 둘러보는 힐링 투어.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 39000,
            'member_discount_rate': 0.10,
            'recommendation_count': 510,
            'image_urls': ['/static/img/tours/product_06_1.jpg', '/static/img/tours/product_06_2.jpg', '/static/img/tours/product_06_3.jpg', '/static/img/tours/product_06_4.jpg']
        },
        {
            'name': '인천 차이나타운 먹거리 투어 & 월미바다열차 오션뷰',
            'description': '개항장 근대역사문화거리와 이국적인 차이나타운을 맛보고 국내 최장 도심형 모노레일을 즐기는 코스.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 36000,
            'member_discount_rate': 0.10,
            'recommendation_count': 670,
            'image_urls': ['/static/img/tours/product_01_2.jpg', '/static/img/tours/product_01_3.jpg', '/static/img/tours/product_01_4.jpg', '/static/img/tours/product_01_1.jpg']
        },
        {
            'name': '연천 재인폭포 출렁다리 & 전곡리 선사유적지 탐방',
            'description': '한탄강 지질공원의 비경 재인폭포 주상절리와 구석기 시대 인류의 발자취를 찾아 떠나는 생태 역사 여행.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 45000,
            'member_discount_rate': 0.15,
            'recommendation_count': 490,
            'image_urls': ['/static/img/tours/product_02_2.jpg', '/static/img/tours/product_02_3.jpg', '/static/img/tours/product_02_4.jpg', '/static/img/tours/product_02_1.jpg']
        },
        {
            'name': '이천 도예마을 도자 체험 & 설봉공원 호수 산책',
            'description': '흙을 빚어 나만의 도자기를 만들어보고 고즈넉한 설봉호수와 설봉산 숲길을 여유롭게 거니는 웰니스 투어.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 49000,
            'member_discount_rate': 0.10,
            'recommendation_count': 380,
            'image_urls': ['/static/img/tours/product_03_2.jpg', '/static/img/tours/product_03_3.jpg', '/static/img/tours/product_03_4.jpg', '/static/img/tours/product_03_1.jpg']
        },
        {
            'name': '시흥 갯골생태공원 흔들전망대 & 오이도 빨강등대 노을',
            'description': '옛 염전의 정취가 살아있는 드넓은 갯골과 서해 바다 낙조가 눈부신 오이도 수산시장 미식 코스.',
            'region': RegionEnum.SEOUL_GYEONGGI.value,
            'original_price': 38000,
            'member_discount_rate': 0.10,
            'recommendation_count': 620,
            'image_urls': ['/static/img/tours/product_04_2.jpg', '/static/img/tours/product_04_3.jpg', '/static/img/tours/product_04_4.jpg', '/static/img/tours/product_04_1.jpg']
        },

        # --- 추가 상품: [2] 강원 추가 (10개) ---
        {
            'name': '대관령 양떼목장 초원 산책 & 월정사 전나무숲길 명상',
            'description': '푸른 알프스를 닮은 대관령 구릉 초지와 천년고찰 오대산 월정사의 울창한 전나무 숲길 힐링.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 68000,
            'member_discount_rate': 0.15,
            'recommendation_count': 950,
            'image_urls': ['/static/img/tours/product_07_1.jpg', '/static/img/tours/product_07_2.jpg', '/static/img/tours/product_07_3.jpg', '/static/img/tours/product_07_4.jpg']
        },
        {
            'name': '인제 자작나무숲 힐링 트레킹 & 원대리 산촌 웰빙 밥상',
            'description': '순백의 자작나무 숲속에서 맑은 피톤치드를 듬뿍 마시고 강원도 산나물 건강 밥상을 즐기는 자연 여행.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 62000,
            'member_discount_rate': 0.15,
            'recommendation_count': 880,
            'image_urls': ['/static/img/tours/product_08_1.jpg', '/static/img/tours/product_08_2.jpg', '/static/img/tours/product_08_3.jpg', '/static/img/tours/product_08_4.jpg']
        },
        {
            'name': '동해 무릉계곡 베틀바위 산성길 & 추암 촛대바위 일출',
            'description': '한국의 장가계라 불리는 기암절벽 베틀바위 절경과 동해안 최고의 일출 명소 추암 해변을 잇는 코스.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 72000,
            'member_discount_rate': 0.15,
            'recommendation_count': 740,
            'image_urls': ['/static/img/tours/product_09_1.jpg', '/static/img/tours/product_09_2.jpg', '/static/img/tours/product_09_3.jpg', '/static/img/tours/product_09_4.jpg']
        },
        {
            'name': '양양 낙산사 해수관음상 해안 절경 & 하조대 전망대',
            'description': '동해 푸른 파도가 절벽에 부딪히는 천년고찰 낙산사와 기암괴석 소나무가 어우러진 하조대 바다 산책.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 59000,
            'member_discount_rate': 0.10,
            'recommendation_count': 810,
            'image_urls': ['/static/img/tours/product_10_1.jpg', '/static/img/tours/product_10_2.jpg', '/static/img/tours/product_10_3.jpg', '/static/img/tours/product_10_4.jpg']
        },
        {
            'name': '고성 통일전망대 DMZ 평화누리 & 화진포 호수 별장',
            'description': '금강산과 동해 바다가 한눈에 들어오는 한반도 최북단 전망대와 고요한 석호 화진포 역사 둘레길.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 65000,
            'member_discount_rate': 0.15,
            'recommendation_count': 670,
            'image_urls': ['/static/img/tours/product_11_1.jpg', '/static/img/tours/product_11_2.jpg', '/static/img/tours/product_11_3.jpg', '/static/img/tours/product_11_4.jpg']
        },
        {
            'name': '삼척 환선굴 대자연 석회동굴 & 맹방 명사십리 드라이브',
            'description': '5억 년 전 태고의 신비를 간직한 동양 최대 크기의 석회동굴 환선굴과 은빛 백사장의 낭만 드라이브.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 69000,
            'member_discount_rate': 0.15,
            'recommendation_count': 590,
            'image_urls': ['/static/img/tours/product_12_1.jpg', '/static/img/tours/product_12_2.jpg', '/static/img/tours/product_12_3.jpg', '/static/img/tours/product_12_4.jpg']
        },
        {
            'name': '철원 고석정 꽃밭 & 한탄강 주상절리 잔도길 트레킹',
            'description': '현무암 협곡 절벽을 따라 허공을 걷는 스릴 넘치는 잔도길과 계절마다 만개하는 고석정 꽃길.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 63000,
            'member_discount_rate': 0.10,
            'recommendation_count': 820,
            'image_urls': ['/static/img/tours/product_07_2.jpg', '/static/img/tours/product_07_3.jpg', '/static/img/tours/product_07_4.jpg', '/static/img/tours/product_07_1.jpg']
        },
        {
            'name': '홍천 수타사 산소길 생태숲 & 알파카월드 숲속 힐링',
            'description': '천년고찰 수타사를 둘러싼 공기 맑은 숲길 산책과 순수하고 사랑스러운 알파카들과의 특별한 교감.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 57000,
            'member_discount_rate': 0.10,
            'recommendation_count': 640,
            'image_urls': ['/static/img/tours/product_08_2.jpg', '/static/img/tours/product_08_3.jpg', '/static/img/tours/product_08_4.jpg', '/static/img/tours/product_08_1.jpg']
        },
        {
            'name': '영월 한반도지형 뗏목 체험 & 별마로천문대 은하수 관측',
            'description': '서강 물줄기가 빚어낸 오묘한 한반도 형상 지형과 봉래산 정상에서 쏟아지는 밤하늘 별빛 투어.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 66000,
            'member_discount_rate': 0.15,
            'recommendation_count': 770,
            'image_urls': ['/static/img/tours/product_09_2.jpg', '/static/img/tours/product_09_3.jpg', '/static/img/tours/product_09_4.jpg', '/static/img/tours/product_09_1.jpg']
        },
        {
            'name': '태백 검룡소 한강발원지 트레킹 & 바람의언덕 풍력발전',
            'description': '514km 한강의 시작점 검룡소의 원시 자연과 매봉산 고랭지 배추밭 풍력발전기 능선 뷰.',
            'region': RegionEnum.GANGWON.value,
            'original_price': 55000,
            'member_discount_rate': 0.10,
            'recommendation_count': 530,
            'image_urls': ['/static/img/tours/product_10_2.jpg', '/static/img/tours/product_10_3.jpg', '/static/img/tours/product_10_4.jpg', '/static/img/tours/product_10_1.jpg']
        },

        # --- 추가 상품: [3] 충청 추가 (10개) ---
        {
            'name': '공주 무령왕릉 백제역사유적 & 공산성 금강 달빛 야경',
            'description': '찬란했던 백제 웅진시대의 왕릉군을 살펴보고 금강 물결을 따라 은은하게 빛나는 공산성을 걷는 역사 기행.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 49000,
            'member_discount_rate': 0.15,
            'recommendation_count': 610,
            'image_urls': ['/static/img/tours/product_13_1.jpg', '/static/img/tours/product_13_2.jpg', '/static/img/tours/product_13_3.jpg', '/static/img/tours/product_13_4.jpg']
        },
        {
            'name': '부여 궁남지 연꽃 둘레길 & 백제문화단지 사비궁 야경',
            'description': '현존하는 우리나라 최초의 인공 정원 궁남지와 백제 왕궁을 웅장하게 재현한 사비궁 탐방.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 53000,
            'member_discount_rate': 0.15,
            'recommendation_count': 580,
            'image_urls': ['/static/img/tours/product_14_1.jpg', '/static/img/tours/product_14_2.jpg', '/static/img/tours/product_14_3.jpg', '/static/img/tours/product_14_4.jpg']
        },
        {
            'name': '서산 해미읍성 성곽길 산책 & 용현리 마애여래삼존상',
            'description': '조선시대 읍성의 원형이 잘 보존된 해미읍성의 잔디마당과 백제의 미소로 불리는 바위 불상 답사.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 45000,
            'member_discount_rate': 0.10,
            'recommendation_count': 490,
            'image_urls': ['/static/img/tours/product_15_1.jpg', '/static/img/tours/product_15_2.jpg', '/static/img/tours/product_15_3.jpg', '/static/img/tours/product_15_4.jpg']
        },
        {
            'name': '보령 대천해수욕장 짚트랙 & 개화예술공원 조각정원',
            'description': '서해안 대표 명사십리 대천 바다 위를 가르는 공중 짚트랙과 숲속 미술관 및 온실 화원 힐링.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 58000,
            'member_discount_rate': 0.15,
            'recommendation_count': 720,
            'image_urls': ['/static/img/tours/product_16_1.jpg', '/static/img/tours/product_16_2.jpg', '/static/img/tours/product_16_3.jpg', '/static/img/tours/product_16_4.jpg']
        },
        {
            'name': '괴산 산막이옛길 유람선 & 칠성면 숲속 트레킹',
            'description': '괴산호의 비경을 따라 복원된 옛길을 걷고 친환경 유람선에 몸을 실어 산수화를 감상하는 웰니스 여행.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 48000,
            'member_discount_rate': 0.10,
            'recommendation_count': 540,
            'image_urls': ['/static/img/tours/product_17_1.jpg', '/static/img/tours/product_17_2.jpg', '/static/img/tours/product_17_3.jpg', '/static/img/tours/product_17_4.jpg']
        },
        {
            'name': '제천 청풍호 옥순봉 출렁다리 & 카약 어드벤처',
            'description': '청풍호반의 문화유산과 옥순봉 기암절벽을 눈앞에서 마주하며 호수 위를 건너는 명품 출렁다리.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 62000,
            'member_discount_rate': 0.15,
            'recommendation_count': 690,
            'image_urls': ['/static/img/tours/product_18_1.jpg', '/static/img/tours/product_18_2.jpg', '/static/img/tours/product_18_3.jpg', '/static/img/tours/product_18_4.jpg']
        },
        {
            'name': '예산 예당호 출렁다리 음악분수 & 수덕사 덕숭산 산책',
            'description': '국내 최장급 호수 출렁다리와 야간 레이저 음악분수, 그리고 백제 고찰 수덕사의 단아한 고즈넉함.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 46000,
            'member_discount_rate': 0.10,
            'recommendation_count': 630,
            'image_urls': ['/static/img/tours/product_13_2.jpg', '/static/img/tours/product_13_3.jpg', '/static/img/tours/product_13_4.jpg', '/static/img/tours/product_13_1.jpg']
        },
        {
            'name': '진천 농다리 천년 돌다리 & 초평호 하늘다리 미르숲',
            'description': '고려 초기에 축조되어 천 년을 버텨온 신비로운 돌다리 농다리와 초평호 물안개 둘레길.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 41000,
            'member_discount_rate': 0.10,
            'recommendation_count': 460,
            'image_urls': ['/static/img/tours/product_14_2.jpg', '/static/img/tours/product_14_3.jpg', '/static/img/tours/product_14_4.jpg', '/static/img/tours/product_14_1.jpg']
        },
        {
            'name': '영동 와인터널 미식 투어 & 월류봉 달빛 석천계곡',
            'description': '포도와 와인의 고장 영동에서 즐기는 와인 시음과 한 폭의 산수화 같은 월류봉 봉우리 비경.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 55000,
            'member_discount_rate': 0.15,
            'recommendation_count': 520,
            'image_urls': ['/static/img/tours/product_15_2.jpg', '/static/img/tours/product_15_3.jpg', '/static/img/tours/product_15_4.jpg', '/static/img/tours/product_15_1.jpg']
        },
        {
            'name': '태안 천리포수목원 서해 바다정원 & 신두리 해안사구',
            'description': '1만 6천여 종의 식물이 서해 바다와 어우러진 수목원과 한국 유일의 신비로운 모래언덕 사구 탐험.',
            'region': RegionEnum.CHUNGCHEONG.value,
            'original_price': 59000,
            'member_discount_rate': 0.15,
            'recommendation_count': 780,
            'image_urls': ['/static/img/tours/product_16_2.jpg', '/static/img/tours/product_16_3.jpg', '/static/img/tours/product_16_4.jpg', '/static/img/tours/product_16_1.jpg']
        },

        # --- 추가 상품: [4] 전라 추가 (10개) ---
        {
            'name': '여수 오동도 동백숲길 & 해상케이블카 돌산대교 야경',
            'description': '푸른 바다 위 동백나무가 빼곡한 오동도와 바다를 건너는 케이블카에서 감상하는 여수 밤바다.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 72000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1180,
            'image_urls': ['/static/img/tours/product_19_1.jpg', '/static/img/tours/product_19_2.jpg', '/static/img/tours/product_19_3.jpg', '/static/img/tours/product_19_4.jpg']
        },
        {
            'name': '순천만국가정원 사계절 플라워 & 순천만습지 갈대숲',
            'description': '전 세계 정원을 모아놓은 대한민국 1호 국가정원과 황금빛 갈대밭이 끝없이 펼쳐지는 갯벌 생태 투어.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 65000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1050,
            'image_urls': ['/static/img/tours/product_20_1.jpg', '/static/img/tours/product_20_2.jpg', '/static/img/tours/product_20_3.jpg', '/static/img/tours/product_20_4.jpg']
        },
        {
            'name': '보성 녹차밭 대한다원 힐링 & 율포솔밭해변 해수녹차탕',
            'description': '초록빛 물결이 굽이치는 삼나무 숲속 차밭과 득량만 청정 해변에서 즐기는 피로회복 웰빙 코스.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 58000,
            'member_discount_rate': 0.10,
            'recommendation_count': 820,
            'image_urls': ['/static/img/tours/product_21_1.jpg', '/static/img/tours/product_21_2.jpg', '/static/img/tours/product_21_3.jpg', '/static/img/tours/product_21_4.jpg']
        },
        {
            'name': '담양 죽녹원 대나무숲 테라피 & 메타프로방스 문화마을',
            'description': '댓잎 사각거리는 청량한 죽림욕 산책과 이국적인 유럽풍 카페 마을에서 즐기는 감성 휴식.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 54000,
            'member_discount_rate': 0.10,
            'recommendation_count': 910,
            'image_urls': ['/static/img/tours/product_22_1.jpg', '/static/img/tours/product_22_2.jpg', '/static/img/tours/product_22_3.jpg', '/static/img/tours/product_22_4.jpg']
        },
        {
            'name': '전주 한옥마을 경기전 태조어진 & 자만벽화마을 산책',
            'description': '700여 채 한옥 골목길에서 한복을 입고 경기전 조선왕조 역사를 느끼며 맛있는 길거리 미식 여행.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 49000,
            'member_discount_rate': 0.10,
            'recommendation_count': 1100,
            'image_urls': ['/static/img/tours/product_23_1.jpg', '/static/img/tours/product_23_2.jpg', '/static/img/tours/product_23_3.jpg', '/static/img/tours/product_23_4.jpg']
        },
        {
            'name': '신안 퍼플섬 반월박지도 보랏빛 다리 & 자은도 백길해변',
            'description': '온 마을과 다리가 보라색으로 물든 이색 섬 투어와 분계 해변의 드넓은 백사장을 거니는 힐링.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 63000,
            'member_discount_rate': 0.15,
            'recommendation_count': 760,
            'image_urls': ['/static/img/tours/product_24_1.jpg', '/static/img/tours/product_24_2.jpg', '/static/img/tours/product_24_3.jpg', '/static/img/tours/product_24_4.jpg']
        },
        {
            'name': '남원 광한루원 춘향사랑정원 & 지리산 뱀사골 단풍계곡',
            'description': '성춘향과 이몽룡의 사랑이 깃든 누각과 지리산 청정 계곡의 옥빛 물웅덩이를 따라 걷는 코스.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 57000,
            'member_discount_rate': 0.10,
            'recommendation_count': 640,
            'image_urls': ['/static/img/tours/product_19_2.jpg', '/static/img/tours/product_19_3.jpg', '/static/img/tours/product_19_4.jpg', '/static/img/tours/product_19_1.jpg']
        },
        {
            'name': '목포 해상케이블카 유달산 횡단 & 근대역사문화거리',
            'description': '유달산 기암절벽과 고하도 바다를 넘나드는 국내 최장 케이블카와 목포 개항장 역사 투어.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 68000,
            'member_discount_rate': 0.15,
            'recommendation_count': 830,
            'image_urls': ['/static/img/tours/product_20_2.jpg', '/static/img/tours/product_20_3.jpg', '/static/img/tours/product_20_4.jpg', '/static/img/tours/product_20_1.jpg']
        },
        {
            'name': '완도 완도타워 다도해 뷰 & 신지명사십리 힐링 비치',
            'description': '다도해 청정 해상국립공원이 파노라마로 펼쳐지는 완도타워와 은빛 모래밭 해양치유 산책.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 61000,
            'member_discount_rate': 0.10,
            'recommendation_count': 560,
            'image_urls': ['/static/img/tours/product_21_2.jpg', '/static/img/tours/product_21_3.jpg', '/static/img/tours/product_21_4.jpg', '/static/img/tours/product_21_1.jpg']
        },
        {
            'name': '고흥 나로우주센터 과학관 & 쑥섬 바다 비밀정원',
            'description': '대한민국 우주 항공의 산실 나로우주센터와 야생화 만발한 바다 위 비밀정원 쑥섬 여행.',
            'region': RegionEnum.JEONLA.value,
            'original_price': 66000,
            'member_discount_rate': 0.15,
            'recommendation_count': 610,
            'image_urls': ['/static/img/tours/product_22_2.jpg', '/static/img/tours/product_22_3.jpg', '/static/img/tours/product_22_4.jpg', '/static/img/tours/product_22_1.jpg']
        },

        # --- 추가 상품: [5] 경북 추가 (10개) ---
        {
            'name': '경주 불국사 석굴암 신라천년 & 첨성대 동궁과월지 야경',
            'description': '유네스코 세계문화유산 신라 불교 예술의 정수와 야경이 아름다운 동궁과 월지 야간 투어.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 75000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1250,
            'image_urls': ['/static/img/tours/product_25_1.jpg', '/static/img/tours/product_25_2.jpg', '/static/img/tours/product_25_3.jpg', '/static/img/tours/product_25_4.jpg']
        },
        {
            'name': '안동 하회마을 부용대 나룻배 & 만휴정 원림 답사',
            'description': '600년 전통의 풍산 류씨 집성촌 고택 마을과 부용대 절벽, 낙동강변의 그림 같은 정자 탐방.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 58000,
            'member_discount_rate': 0.10,
            'recommendation_count': 840,
            'image_urls': ['/static/img/tours/product_26_1.jpg', '/static/img/tours/product_26_2.jpg', '/static/img/tours/product_26_3.jpg', '/static/img/tours/product_26_4.jpg']
        },
        {
            'name': '포항 호미곶 상생의손 해맞이 & 스페이스워크 환호공원',
            'description': '한반도 최동단 호미곶 바다 위 청동 손 조형물과 롤러코스터처럼 하늘을 걷는 스페이스워크 체험.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 62000,
            'member_discount_rate': 0.15,
            'recommendation_count': 990,
            'image_urls': ['/static/img/tours/product_27_1.jpg', '/static/img/tours/product_27_2.jpg', '/static/img/tours/product_27_3.jpg', '/static/img/tours/product_27_4.jpg']
        },
        {
            'name': '청송 주왕산 주산지 물안개 & 대전사 기암 협곡',
            'description': '물속에 잠긴 왕버들이 신비로운 분위기를 자아내는 주산지와 기암절벽 웅장한 주왕산 국립공원.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 59000,
            'member_discount_rate': 0.10,
            'recommendation_count': 720,
            'image_urls': ['/static/img/tours/product_28_1.jpg', '/static/img/tours/product_28_2.jpg', '/static/img/tours/product_28_3.jpg', '/static/img/tours/product_28_4.jpg']
        },
        {
            'name': '문경 문경새재 황톳길 맨발걷기 & 오픈세트장 사극체험',
            'description': '영남과 한양을 잇던 과거길 조령 삼관문 흙길을 맨발로 걷고 조선시대 드라마 촬영장을 둘러보는 코스.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 52000,
            'member_discount_rate': 0.10,
            'recommendation_count': 810,
            'image_urls': ['/static/img/tours/product_29_1.jpg', '/static/img/tours/product_29_2.jpg', '/static/img/tours/product_29_3.jpg', '/static/img/tours/product_29_4.jpg']
        },
        {
            'name': '영주 부석사 무량수전 배흘림기둥 & 소수서원 선비마을',
            'description': '소백산맥 봉우리들이 파도치는 절경의 부석사와 우리나라 최초의 사액서원에서 배우는 선비정신.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 54000,
            'member_discount_rate': 0.10,
            'recommendation_count': 690,
            'image_urls': ['/static/img/tours/product_30_1.jpg', '/static/img/tours/product_30_2.jpg', '/static/img/tours/product_30_3.jpg', '/static/img/tours/product_30_4.jpg']
        },
        {
            'name': '울진 불영사 계곡 드라이브 & 덕구온천 족욕 테라피',
            'description': '한국의 그랜드캐니언 불영계곡의 푸른 물줄기와 국내 유일의 자연용출 덕구온천 힐링.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 67000,
            'member_discount_rate': 0.15,
            'recommendation_count': 540,
            'image_urls': ['/static/img/tours/product_25_2.jpg', '/static/img/tours/product_25_3.jpg', '/static/img/tours/product_25_4.jpg', '/static/img/tours/product_25_1.jpg']
        },
        {
            'name': '영덕 블루로드 해맞이공원 바다산책 & 강구항 대게 미식',
            'description': '동해안 푸른 바다를 따라 조성된 해안 둘레길과 영덕 축산항 강구항의 풍성한 대게 미식.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 79000,
            'member_discount_rate': 0.15,
            'recommendation_count': 860,
            'image_urls': ['/static/img/tours/product_26_2.jpg', '/static/img/tours/product_26_3.jpg', '/static/img/tours/product_26_4.jpg', '/static/img/tours/product_26_1.jpg']
        },
        {
            'name': '봉화 백두대간 수목원 호랑이숲 & 분천역 산타마을',
            'description': '아시아 최대 규모의 국립수목원에서 백두산 호랑이를 만나고 동화 같은 산타마을의 낭만 기차역.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 61000,
            'member_discount_rate': 0.10,
            'recommendation_count': 630,
            'image_urls': ['/static/img/tours/product_27_2.jpg', '/static/img/tours/product_27_3.jpg', '/static/img/tours/product_27_4.jpg', '/static/img/tours/product_27_1.jpg']
        },
        {
            'name': '군위 화본역 레트로 감성 & 한밤마을 돌담길 산책',
            'description': '네티즌이 뽑은 가장 아름다운 간이역 화본역과 제주도를 닮은 제주식 돌담이 이어진 한밤마을.',
            'region': RegionEnum.GYEONGBUK.value,
            'original_price': 46000,
            'member_discount_rate': 0.10,
            'recommendation_count': 510,
            'image_urls': ['/static/img/tours/product_28_2.jpg', '/static/img/tours/product_28_3.jpg', '/static/img/tours/product_28_4.jpg', '/static/img/tours/product_28_1.jpg']
        },

        # --- 추가 상품: [6] 제주 추가 (10개) ---
        {
            'name': '제주 우도 성산일출봉 유람선 & 서빈백사 산호해변 투어',
            'description': '에메랄드빛 바다와 하얀 홍조단괴 백사장이 눈부신 섬 속의 섬 우도 일주 여행.',
            'region': RegionEnum.JEJU.value,
            'original_price': 78000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1350,
            'image_urls': ['/static/img/tours/product_31_1.jpg', '/static/img/tours/product_31_2.jpg', '/static/img/tours/product_31_3.jpg', '/static/img/tours/product_31_4.jpg']
        },
        {
            'name': '서귀포 주상절리대 해안 절벽 & 천지연폭포 아열대 숲',
            'description': '거대한 육각형 주상절리 바위 절벽에 부서지는 하얀 파도와 야경이 환상적인 천지연폭포.',
            'region': RegionEnum.JEJU.value,
            'original_price': 62000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1140,
            'image_urls': ['/static/img/tours/product_32_1.jpg', '/static/img/tours/product_32_2.jpg', '/static/img/tours/product_32_3.jpg', '/static/img/tours/product_32_4.jpg']
        },
        {
            'name': '구좌 세화해변 비취빛 바다 & 비자림 천년숲길 피톤치드',
            'description': '수령 500~800년 된 비자나무 수천 그루가 자생하는 태고의 숲과 아기자기한 세화 카페거리.',
            'region': RegionEnum.JEJU.value,
            'original_price': 69000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1220,
            'image_urls': ['/static/img/tours/product_33_1.jpg', '/static/img/tours/product_33_2.jpg', '/static/img/tours/product_33_3.jpg', '/static/img/tours/product_33_4.jpg']
        },
        {
            'name': '한림 협재해수욕장 비양도 뷰 & 금능 으뜸원해변 산책',
            'description': '은빛 모래와 비취빛 바다 너머로 비양도가 손에 잡힐 듯한 서쪽 최고의 노을 명소.',
            'region': RegionEnum.JEJU.value,
            'original_price': 58000,
            'member_discount_rate': 0.10,
            'recommendation_count': 1290,
            'image_urls': ['/static/img/tours/product_34_1.jpg', '/static/img/tours/product_34_2.jpg', '/static/img/tours/product_34_3.jpg', '/static/img/tours/product_34_4.jpg']
        },
        {
            'name': '조천 사려니숲길 삼나무 명상 & 산굼부리 억새 분화구',
            'description': '신성한 숲 사려니의 피톤치드 흙길을 걷고 가을빛 은빛 억새가 장관을 이루는 거대 분화구.',
            'region': RegionEnum.JEJU.value,
            'original_price': 65000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1080,
            'image_urls': ['/static/img/tours/product_35_1.jpg', '/static/img/tours/product_35_2.jpg', '/static/img/tours/product_35_3.jpg', '/static/img/tours/product_35_4.jpg']
        },
        {
            'name': '애월 한담해안산책로 투명카약 & 곽지과물해변 노을',
            'description': '깎아지른 해안 절벽을 따라 굽이치는 바다 산책로와 바닥이 훤히 보이는 투명 카약 체험.',
            'region': RegionEnum.JEJU.value,
            'original_price': 72000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1190,
            'image_urls': ['/static/img/tours/product_36_1.jpg', '/static/img/tours/product_36_2.jpg', '/static/img/tours/product_36_3.jpg', '/static/img/tours/product_36_4.jpg']
        },
        {
            'name': '표선 성읍민속마을 전통초가 & 제주민속촌 문화체험',
            'description': '제주 옛 산간마을의 가옥과 풍속이 생생히 살아있는 민속마을에서 즐기는 전통 제주 밥상.',
            'region': RegionEnum.JEJU.value,
            'original_price': 53000,
            'member_discount_rate': 0.10,
            'recommendation_count': 840,
            'image_urls': ['/static/img/tours/product_31_2.jpg', '/static/img/tours/product_31_3.jpg', '/static/img/tours/product_31_4.jpg', '/static/img/tours/product_31_1.jpg']
        },
        {
            'name': '중문 엉덩물계곡 유채꽃밭 & 여미지식물원 온실 투어',
            'description': '계곡을 가득 메운 샛노란 꽃밭과 전 세계 희귀 열대식물을 관람할 수 있는 식물원 힐링.',
            'region': RegionEnum.JEJU.value,
            'original_price': 61000,
            'member_discount_rate': 0.10,
            'recommendation_count': 920,
            'image_urls': ['/static/img/tours/product_32_2.jpg', '/static/img/tours/product_32_3.jpg', '/static/img/tours/product_32_4.jpg', '/static/img/tours/product_32_1.jpg']
        },
        {
            'name': '서귀포 정방폭포 해안 절경 & 올레시장 미식투어',
            'description': '폭포수가 바다로 직접 떨어지는 동양 유일의 해안폭포와 활기찬 전통시장의 맛있는 야식.',
            'region': RegionEnum.JEJU.value,
            'original_price': 56000,
            'member_discount_rate': 0.10,
            'recommendation_count': 1020,
            'image_urls': ['/static/img/tours/product_33_2.jpg', '/static/img/tours/product_33_3.jpg', '/static/img/tours/product_33_4.jpg', '/static/img/tours/product_33_1.jpg']
        },
        {
            'name': '안덕 카멜리아힐 동백수목원 & 산방산 용머리해안',
            'description': '전 세계 500여 종의 동백꽃이 피어나는 정원과 수천만 년 세월이 빚어낸 해안 사암 절벽.',
            'region': RegionEnum.JEJU.value,
            'original_price': 67000,
            'member_discount_rate': 0.15,
            'recommendation_count': 1130,
            'image_urls': ['/static/img/tours/product_34_2.jpg', '/static/img/tours/product_34_3.jpg', '/static/img/tours/product_34_4.jpg', '/static/img/tours/product_34_1.jpg']
        }
    ]
    sample_review_comments = [
        ("기대 이상으로 만족스러웠던 여행!", "가족들과 함께 다녀왔는데 코스가 정말 알차고 힐링 제대로 하고 왔습니다. 회원 할인받아서 가성비도 최고였어요!"),
        ("경치가 정말 장관이네요.", "사진보다 실물이 훨씬 아름답습니다. 가이드분도 친절하시고 일정이 무리 없어 부모님 모시고 가기 딱 좋습니다."),
        ("다음에 또 방문하고 싶어요.", "숙소와 연계된 코스도 좋고 특히 체험 프로그램이 인상 깊었습니다. 다음엔 친구들과 또 예약할게요!"),
        ("회원 혜택이 쏠쏠합니다.", "다른 여행사보다 회원 할인율이 높아서 기분 좋게 다녀왔습니다. 강력 추천합니다!"),
        ("잊지 못할 추억이 생겼습니다.", "답답한 도시를 벗어나 맑은 공기 마시며 즐겁게 힐링했습니다. 후기 믿고 갔는데 대만족이에요.")
    ]

    for p_info in products_data:
        json_urls = json.dumps(p_info['image_urls'], ensure_ascii=False)
        first_img = p_info['image_urls'][0]

        product = TourProduct.query.filter_by(name=p_info['name']).first()
        if not product:
            product = TourProduct(
                name=p_info['name'],
                description=p_info['description'],
                region=p_info['region'],
                #theme_id=p_info['theme'].id,
                original_price=p_info['original_price'],
                member_discount_rate=p_info['member_discount_rate'],
                recommendation_count=p_info['recommendation_count'],
                image_url=first_img,
                image_urls=json_urls
            )
            db.session.add(product)
            db.session.flush()

            # 상품별로 1~3개의 다채로운 후기 자동 등록
            num_reviews = random.randint(1, 3)
            for idx in range(num_reviews):
                reviewer = created_users[(idx + product.id) % len(created_users)]
                title, content = sample_review_comments[(idx + product.id) % len(sample_review_comments)]
                rating = 5 if idx == 0 else random.choice([4, 5])
                review = Review(
                    user_id=reviewer.id,
                    product_id=product.id,
                    title=f"[{product.region}] {title}",
                    content=content,
                    rating=rating
                )
                db.session.add(review)
        else:
            product.image_urls = json_urls
            product.image_url = first_img
            # ◀ [추가] 기존 상품 리뷰 자동 생성 (중복 방지 체크 포함)
            # 만약 해당 상품에 작성된 리뷰가 하나도 없는 경우에만 실행
            existing_review_exists = Review.query.filter_by(product_id=product.id).first()
            if not existing_review_exists:
                num_reviews = random.randint(1, 3)
                for idx in range(num_reviews):
                    reviewer = created_users[(idx + product.id) % len(created_users)]
                    title, content = sample_review_comments[(idx + product.id) % len(sample_review_comments)]
                    rating = 5 if idx == 0 else random.choice([4, 5])
                    
                    review = Review(
                        user_id=reviewer.id,
                        product_id=product.id,
                        title=f"[{product.region}] {title}",
                        content=content,
                        rating=rating
                    )
                    db.session.add(review)
    db.session.commit()
    total_count = TourProduct.query.count()

    # 4. 상품 구매 정보 (주문/결제) Seed 데이터 정의
    #    - 비회원(Guest) 상태로 생성/수정된 주문 정보
    #    - 로그인 회원(Member) 상태로 생성/수정된 주문 정보
    orders_data = [
        # --- [1] 비회원(Guest) 상태 주문 데이터 ---
        {
            'order_no': 'ORD-20260923064809-E3DB20',
            'user_username': None,
            'guest_name': '테스트고객',
            'guest_email': 'test@example.com',
            'guest_phone': '010-9999-8888',
            'product_name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'quantity': 2,
            'original_amount': 130000,
            'discount_amount': 0,
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': False,
            'created_at': datetime(2026, 9, 23, 6, 48, 9),
            'payment_method': 'CARD',
            'paid_amount': 130000,
            'transaction_id': 'TX-ORD-20260923064809-E3DB20',
            'paid_at': datetime(2026, 9, 23, 6, 48, 9)
        },
        {
            'order_no': 'ORD-20260923070325-0162C6',
            'user_username': None,
            'guest_name': '테스트고객',
            'guest_email': 'test@example.com',
            'guest_phone': '010-9999-8888',
            'product_name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'quantity': 2,
            'original_amount': 130000,
            'discount_amount': 0,
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': False,
            'created_at': datetime(2026, 9, 23, 7, 3, 25),
            'payment_method': 'CARD',
            'paid_amount': 130000,
            'transaction_id': 'TX-ORD-20260923070325-0162C6',
            'paid_at': datetime(2026, 9, 23, 7, 3, 25)
        },
        {
            'order_no': 'ORD-20260923072042-46A2A0',
            'user_username': None,
            'guest_name': '테스트고객',
            'guest_email': 'test@example.com',
            'guest_phone': '010-9999-8888',
            'product_name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'quantity': 2,
            'original_amount': 130000,
            'discount_amount': 0,
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': True,
            'created_at': datetime(2026, 9, 23, 7, 20, 42),
            'payment_method': 'CARD',
            'paid_amount': 130000,
            'transaction_id': 'TX-ORD-20260923072042-46A2A0',
            'paid_at': datetime(2026, 9, 23, 7, 20, 42)
        },
        {
            'order_no': 'ORD-20260923073004-063037',
            'user_username': None,
            'guest_name': '테스트고객',
            'guest_email': 'test@example.com',
            'guest_phone': '010-9999-8888',
            'product_name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'quantity': 2,
            'original_amount': 130000,
            'discount_amount': 0,
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': True,
            'created_at': datetime(2026, 9, 23, 7, 30, 4),
            'payment_method': 'CARD',
            'paid_amount': 130000,
            'transaction_id': 'TX-ORD-20260923073004-063037',
            'paid_at': datetime(2026, 9, 23, 7, 30, 4)
        },
        {
            'order_no': 'ORD-20260923073035-79D59A',
            'user_username': None,
            'guest_name': '테스트고객',
            'guest_email': 'test@example.com',
            'guest_phone': '010-9999-8888',
            'product_name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'quantity': 2,
            'original_amount': 130000,
            'discount_amount': 0,
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': True,
            'travel_date': '2026-10-06',
            'created_at': datetime(2026, 9, 23, 7, 30, 35),
            'payment_method': 'CARD',
            'paid_amount': 130000,
            'transaction_id': 'TX-ORD-20260923073035-79D59A',
            'paid_at': datetime(2026, 9, 23, 7, 30, 35)
        },
        {
            'order_no': 'ORD-20260923084202-B6D072',
            'user_username': None,
            'guest_name': '테스트고객',
            'guest_email': 'test@example.com',
            'guest_phone': '010-9999-8888',
            'product_name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'quantity': 2,
            'original_amount': 130000,
            'discount_amount': 0,
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': True,
            'travel_date': '2026-09-25',
            'created_at': datetime(2026, 9, 23, 8, 42, 2),
            'payment_method': 'CARD',
            'paid_amount': 130000,
            'transaction_id': 'TX-ORD-20260923084202-B6D072',
            'paid_at': datetime(2026, 9, 23, 8, 42, 2)
        },
        # --- [2] 로그인 회원(Member) 상태 주문 데이터 ---
        {
            'order_no': 'ORD-20260923084617-62642E',
            'user_username': 'hong',
            'guest_name': None,
            'guest_email': None,
            'guest_phone': None,
            'product_name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'quantity': 2,
            'original_amount': 130000,
            'discount_amount': 0,
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': True,
            'travel_date': '2026-09-26',
            'created_at': datetime(2026, 9, 23, 8, 46, 17),
            'payment_method': 'CARD',
            'paid_amount': 130000,
            'transaction_id': 'TX-ORD-20260923084617-62642E',
            'paid_at': datetime(2026, 9, 23, 8, 46, 17)
        },
        {
            'order_no': 'ORD-20260923085033-2725D1',
            'user_username': 'hong',
            'guest_name': None,
            'guest_email': None,
            'guest_phone': None,
            'product_name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'quantity': 2,
            'original_amount': 130000,
            'discount_amount': 0,
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': True,
            'travel_date': '2026-10-04',
            'created_at': datetime(2026, 9, 23, 8, 50, 33),
            'payment_method': 'CARD',
            'paid_amount': 130000,
            'transaction_id': 'TX-ORD-20260923085033-2725D1',
            'paid_at': datetime(2026, 9, 23, 8, 50, 33)
        },
        # 회원 우대 할인(15%) 및 PortOne 테스트 결제(1,000원) 적용 최신 주문 (hong)
        {
            'order_no': 'ORD-20260928112000-HONG01',
            'user_username': 'hong',
            'guest_name': None,
            'guest_email': None,
            'guest_phone': None,
            'product_name': '가평 아침고요수목원 & 남이섬 메타세쿼이아 낭만 힐링',
            'quantity': 2,
            'original_amount': 130000,
            'discount_amount': 19500,  # 15% 회원할인 적용 (인당 9,750원 할인)
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': True,
            'travel_date': '2026-10-08',
            'created_at': datetime(2026, 9, 28, 11, 20, 0),
            'payment_method': 'CARD',
            'paid_amount': 1000,       # PortOne 테스트 결제 금액 (1,000원)
            'transaction_id': 'payment-8aa7da59-1180-4c4e-9723-ed30e22b7ff4',
            'paid_at': datetime(2026, 9, 28, 11, 20, 5)
        },
        # 회원 우대 할인(10%) 적용 주문 (traveler_kim)
        {
            'order_no': 'ORD-20260928153000-KIM001',
            'user_username': 'traveler_kim',
            'guest_name': None,
            'guest_email': None,
            'guest_phone': None,
            'product_name': '수원 화성 성곽길 달빛 투어 & 플라잉 수원 열기구 체험',
            'quantity': 1,
            'original_amount': 45000,
            'discount_amount': 4500,   # 10% 회원할인 적용
            'status': 'COMPLETED',
            'agree_special': True,
            'agree_privacy': True,
            'agree_sensitive': True,
            'agree_location': False,
            'travel_date': '2026-10-10',
            'created_at': datetime(2026, 9, 28, 15, 30, 0),
            'payment_method': 'CARD',
            'paid_amount': 40500,
            'transaction_id': 'TX-ORD-20260928153000-KIM001',
            'paid_at': datetime(2026, 9, 28, 15, 30, 5)
        }
    ]

    for o_info in orders_data:
        order = Order.query.filter_by(order_no=o_info['order_no']).first()

        # 상품 조회 (이름으로 매칭, 없으면 1번 상품)
        product = TourProduct.query.filter_by(name=o_info['product_name']).first()
        if not product:
            product = TourProduct.query.first()

        # 회원 조회 (로그인 회원의 경우)
        user = None
        if o_info['user_username']:
            user = User.query.filter_by(user_id=o_info['user_username']).first()

        user_id_val = user.id if user else None
        qty = o_info.get('quantity', 1)
        orig_amt = o_info['original_amount']
        disc_amt = o_info['discount_amount']
        unit_price = (orig_amt - disc_amt) // qty if qty > 0 else orig_amt
        discount_applied = disc_amt // qty if qty > 0 else 0

        if not order:
            order = Order(
                order_no=o_info['order_no'],
                user_id=user_id_val,
                guest_name=o_info.get('guest_name'),
                guest_email=o_info.get('guest_email'),
                guest_phone=o_info.get('guest_phone'),
                original_amount=orig_amt,
                discount_amount=disc_amt,
                status=o_info.get('status', 'COMPLETED'),
                agree_special=o_info.get('agree_special', True),
                agree_privacy=o_info.get('agree_privacy', True),
                agree_sensitive=o_info.get('agree_sensitive', True),
                agree_location=o_info.get('agree_location', False),
                travel_date=o_info.get('travel_date', '2026-10-05'),
                created_at=o_info.get('created_at', datetime.now(timezone.utc))
            )
            db.session.add(order)
            db.session.flush()

            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=qty,
                unit_price=unit_price,
                discount_applied=discount_applied
            )
            db.session.add(order_item)

            payment = Payment(
                order_id=order.id,
                payment_method=o_info.get('payment_method', 'CARD'),
                paid_amount=o_info.get('paid_amount', orig_amt - disc_amt),
                transaction_id=o_info['transaction_id'],
                status='SUCCESS',
                paid_at=o_info.get('paid_at', o_info.get('created_at', datetime.now(timezone.utc)))
            )
            db.session.add(payment)
        else:
            # 기존 주문 정보 업데이트 (멱등성 보장)
            order.user_id = user_id_val
            order.guest_name = o_info.get('guest_name')
            order.guest_email = o_info.get('guest_email')
            order.guest_phone = o_info.get('guest_phone')
            order.original_amount = orig_amt
            order.discount_amount = disc_amt
            order.status = o_info.get('status', 'COMPLETED')
            order.agree_special = o_info.get('agree_special', True)
            order.agree_privacy = o_info.get('agree_privacy', True)
            order.agree_sensitive = o_info.get('agree_sensitive', True)
            order.agree_location = o_info.get('agree_location', False)
            order.travel_date = o_info.get('travel_date', '2026-10-05')
            if 'created_at' in o_info:
                order.created_at = o_info['created_at']

            item = order.items.first()
            if not item:
                item = OrderItem(
                    order_id=order.id,
                    product_id=product.id,
                    quantity=qty,
                    unit_price=unit_price,
                    discount_applied=discount_applied
                )
                db.session.add(item)
            else:
                item.product_id = product.id
                item.quantity = qty
                item.unit_price = unit_price
                item.discount_applied = discount_applied

            if not order.payment:
                payment = Payment(
                    order_id=order.id,
                    payment_method=o_info.get('payment_method', 'CARD'),
                    paid_amount=o_info.get('paid_amount', orig_amt - disc_amt),
                    transaction_id=o_info['transaction_id'],
                    status='SUCCESS',
                    paid_at=o_info.get('paid_at', order.created_at)
                )
                db.session.add(payment)
            else:
                order.payment.payment_method = o_info.get('payment_method', 'CARD')
                order.payment.paid_amount = o_info.get('paid_amount', orig_amt - disc_amt)
                order.payment.status = 'SUCCESS'

    db.session.commit()
    total_orders = Order.query.count()
    print(f"[Seed] 성공! 총 {total_count}개 관광 상품 및 {total_orders}개 주문/결제 데이터가 적재되었습니다.")

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
         seed_database()


