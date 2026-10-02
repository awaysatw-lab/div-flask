from datetime import datetime, timedelta
from sqlalchemy import inspect
from pybo import db
from pybo.models import TimeDeal

def seed_time_deals():
    # 1. 이미 데이터가 있는지 검사 (중복 등록 방지)
    try:
        # DB 테이블이 아직 생성되지 않은 상태(flask db init, migrate 등)에서는 건너뜁니다.
        inspector = inspect(db.engine)
        if not inspector.has_table('time_deal'):
            return

        # 1. 이미 데이터가 있는지 검사 (중복 등록 방지)
        if TimeDeal.query.first() is not None:
            return
    except Exception:
        return

    print("🌱 데이터베이스에 타임딜 테스트 데이터를 등록하는 중...")

    # 2. 메인 타임딜 데이터 (호주 시드니)
    main_deal = TimeDeal(
        product_type='main',
        airline='[아시아나항공]',
        title='호주 시드니 | 멜버른 6/7일',
        hashtags='#오페라하우스 내부 #블루마운틴 시닉 #포트스테판 사막썰매 #돌핀크루즈',
        description='도시의 낭만과 대자연의 호흡, 한 번에 만나는 호주 🦘',
        price=1649000,
        end_date=datetime.now() + timedelta(days=4, hours=8, minutes=51),  # 지금부터 약 4일 후 마감
        image_file='sydney.jpg',
        badge1='블루마운틴 시닉4콤보',
        badge2='시드니타워'
    )

    # 3. 서브 타임딜 데이터 1 (마나도)
    sub_deal1 = TimeDeal(
        product_type='sub',
        airline='[이스타항공]',
        title='마나도 5일 - NDC리조트 VS 베스트웨스턴 ✈️',
        hashtags='#풀패키지 #스노클링 #힐링여행',
        description='숨겨진 천국의 휴양지, 마나도',
        price=629000,
        end_date=datetime.now() + timedelta(days=3),
        image_file='manado.jpg',  # 적절한 이미지 파일명
        badge1='나인mile랜드',
        badge2='부나켄 호핑투어'
    )

    # 4. 서브 타임딜 데이터 2 (도야마)
    sub_deal2 = TimeDeal(
        product_type='sub',
        airline='[진에어]',
        title='도야마/알펜루트 온천 4/5일',
        hashtags='#온천여행 #알펜루트 #황홀한대자연',
        description='설산과 온천을 동시에 즐기는 힐링 코스',
        price=1699000,
        end_date=datetime.now() + timedelta(days=3),
        image_file='danang.jpg',  # 기존 이미지 양식 활용
        badge1='도야마 직항',
        badge2='호시노리조트 증정'
    )

    # 5. DB에 저장
    db.session.add(main_deal)
    db.session.add(sub_deal1)
    db.session.add(sub_deal2)
    db.session.commit()
    print("✅ 타임딜 테스트 데이터 자동 등록 완료!")
