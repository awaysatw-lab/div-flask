from datetime import datetime, timedelta
from sqlalchemy import inspect
from pybo import db
from pybo.models import TimeDeal

def seed_time_deals():
    try:
        inspector = inspect(db.engine)
        if not inspector.has_table('time_deal'):
            return
    except Exception:
        return

    print("🌱 데이터베이스에 국내 타임딜 테스트 데이터를 등록하는 중...")

    # [수정] 2. 메인 타임딜 데이터 (해외 시드니 -> 국내 제주도)
    main_deal = TimeDeal(
        product_type='main',
        airline='[대한항공]',
        title='제주 프리미엄 감성 숙소 & 에어카텔 3/4일',
        hashtags='#감성독채 #우도 보트투어 #한라산 트레킹 #돌문화공원',
        description='푸른 바다와 유채꽃향기, 온전한 휴식을 선물하는 제주 🍊',
        price=349000,
        end_date=datetime.now() + timedelta(days=4, hours=8, minutes=51),  # 약 4일 후 마감
        image_file='jeju.jpg',  # static/img/jeju.jpg 이미지 매칭
        badge1='에어카텔 풀패키지',
        badge2='특급호텔 1박 업그레이드'
    )

    # [수정] 3. 서브 타임딜 데이터 1 (해외 마나도 -> 국내 울릉도)
    sub_deal1 = TimeDeal(
        product_type='sub',
        airline='[크루즈선박]',
        title='울릉도/독도 대형 크루즈 힐링 여행 3일 🌊',
        hashtags='#독도입도 #울릉도육로관광 #명이나물정식',
        description='대형 크루즈로 멀미 없이 편안하게 떠나는 신비의 섬',
        price=289000,
        end_date=datetime.now() + timedelta(days=3),
        image_file='ulleung.jpg',  # static/img/ulleung.jpg 이미지 매칭
        badge1='독도관광 포함',
        badge2='전일정 식사제공'
    )

    # [수정] 4. 서브 타임딜 데이터 2 (해외 도야마 -> 국내 부산/경주)
    sub_deal2 = TimeDeal(
        product_type='sub',
        airline='[KTX고속열차]',
        title='부산/경주 역사문화 탐방 온천 투어 3일',
        hashtags='#해운대캡슐열차 #경주황리단길 #야경투어',
        description='과거와 현재가 공존하는 낭만 가득 영남권 코스',
        price=199000,
        end_date=datetime.now() + timedelta(days=3),
        image_file='busan.jpg',  # static/img/busan.jpg 이미지 매칭
        badge1='KTX 왕복포함',
        badge2='5성급 온천호텔'
    )

    # 5. DB에 저장
    db.session.add(main_deal)
    db.session.add(sub_deal1)
    db.session.add(sub_deal2)
    db.session.commit()
    print("✅ 국내 타임딜 테스트 데이터 자동 등록 완료!")
