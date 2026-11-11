# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
KAKAO = "https://open.kakao.com/o/snFgJ5Ci"

REVIEWS = [
    {
        "id": "v01",
        "date": "2026-08-21",
        "region": "서울 송파구",
        "car": "중형 세단",
        "service": "자살차량 특수청소",
        "filter": "suicide",
        "title": "송파 자살차량 특수청소 · 견인 후 실내 복원",
        "excerpt": "일반 견인이 어려운 오염 차량을 이동한 뒤, 시트와 공조까지 특수청소하고 인도했습니다.",
        "image": "service-01.jpg",
        "paras": [
            "카리셋 자살차량 특수청소 사례입니다. 현장 확인 후 일반 견인이 어려워 자살차량 견인으로 작업장까지 이동했습니다.",
            "시트 폼, 바닥 매트, 트림 안쪽, 공조 라인까지 오염이 스며 있어 표면 세차만으로는 냄새가 남는 상태였습니다. 분해가 필요한 부위를 확인한 뒤 약품 세척, 오존 탈취, 공조라인 세척을 순서대로 진행했습니다.",
            "작업 후 상태 확인을 거쳐 차량을 인도했습니다. 유가족 성함, 얼굴, 차량번호는 공개하지 않으며 작업 사진도 개인이 특정되지 않는 범위만 남깁니다.",
        ],
        "bullets": [
            "현장 출동 및 자살차량 견인",
            "실내 특수청소 · 차량 악취제거",
            "작업 후 인도",
        ],
        "facts": [
            ("차량 상태", "중형 세단. 일반 견인이 거부된 오염 차량으로, 실내 탑승이 어려운 상태였습니다."),
            ("오염 범위", "시트·바닥·트림·송풍구. 공조를 켜면 냄새가 다시 올라오는 구간까지 확인했습니다."),
            ("작업 과정", "현장 확인 → 견인 이동 → 내장재 분해 점검 → 오염 제거 → 오존 탈취 → 인도 전 확인"),
            ("사용 장비", "방호 장비, 특수 세정 약품, 오존 탈취기, 공조라인 세척 장비"),
            ("작업 결과", "실내 오염과 악취를 처리한 뒤 인도했습니다. 이후 보관·폐차 말소가 필요하면 이어서 안내합니다."),
            ("개인정보 보호", "성함·얼굴·차량번호는 올리지 않습니다. 지역·차종·작업 내용만 공개합니다."),
        ],
    },
    {
        "id": "v02",
        "date": "2026-07-14",
        "region": "경기 수원시",
        "car": "SUV",
        "service": "번개탄 차량 탈취",
        "filter": "charcoal",
        "title": "수원 번개탄 차량 탈취 · 공조라인 세척",
        "excerpt": "천장과 송풍구에 남은 그을음·냄새를 공조라인 세척과 연무 탈취로 처리했습니다.",
        "image": "service-03.jpg",
        "paras": [
            "카리셋 번개탄 차량 탈취 사례입니다. 표면 세차 후에도 에어컨을 켤 때마다 냄새가 재발한다고 하셔서, 천장·송풍구·공조라인과 필터까지 확인했습니다.",
            "그을음이 천장과 송풍구 주변에 남아 있었고, 시트 표면보다 공조 내부에서 냄새가 재발하는 형태였습니다. 공조라인 세척, 필터 교체, 오존 탈취를 함께 진행했습니다.",
            "냄새 재발 여부를 확인한 뒤 인도했습니다. 작업 기록은 차량 외관과 작업 범위 위주로만 남기고 번호판은 공개하지 않습니다.",
        ],
        "bullets": [
            "그을음·악취 범위 확인",
            "공조라인 세척 및 필터 교체",
            "번개탄 차량 탈취 후 인도",
        ],
        "facts": [
            ("차량 상태", "SUV. 겉 세차 후에도 에어컨 가동 시 냄새가 재발하는 상태였습니다."),
            ("오염 범위", "천장, 송풍구, 시트 표면, 공조 필터·라인"),
            ("작업 과정", "오염 범위 확인 → 그을음 제거 → 필터 교체 → 공조라인 세척 → 오존 탈취 → 재발 확인"),
            ("사용 장비", "공조 세척 장비, 필터 교체, 오존 탈취기, 특수 세정 약품"),
            ("작업 결과", "공조 가동 시 재발하던 냄새를 줄인 뒤 인도했습니다."),
            ("개인정보 보호", "차량번호·얼굴은 가리고, 지역·차종·작업 내용만 공개합니다."),
        ],
    },
    {
        "id": "v03",
        "date": "2026-06-03",
        "region": "부산 사상구",
        "car": "준중형 세단",
        "service": "고독사 차량 특수청소",
        "filter": "lonely",
        "title": "부산 고독사 차량 특수청소 후 폐차 말소 안내",
        "excerpt": "발견이 늦어진 차량의 내부 오염을 제거한 뒤, 복원보다 고인명의 폐차 말소가 맞다고 안내했습니다.",
        "image": "service-02.jpg",
        "paras": [
            "카리셋 고독사 차량 특수청소 사례입니다. 발견이 늦어진 준중형 세단으로, 시트와 내장재 깊숙이 오염이 배어 일반 세차로는 악취가 남는 상태였습니다.",
            "이동 후 시트·바닥·내장재의 오염 깊이를 확인하고 분해 세척과 탈취를 진행했습니다. 복원 비용과 잔존 가치를 함께 본 뒤, 재사용보다 고인명의 폐차 말소가 맞다고 안내했습니다.",
            "말소에 필요한 서류와 순서를 설명했고, 성함·차량번호는 후기에 올리지 않았습니다.",
        ],
        "bullets": [
            "고독사 차량 특수청소",
            "차량 악취제거",
            "고인명의 폐차 말소 안내",
        ],
        "facts": [
            ("차량 상태", "준중형 세단. 발견이 늦어 실내 오염이 깊고, 일반 세차로는 악취가 남는 상태였습니다."),
            ("오염 범위", "시트 폼, 바닥, 내장재 안쪽. 복원보다 처분이 유리한 수준으로 판단했습니다."),
            ("작업 과정", "이동 → 오염 깊이 확인 → 특수청소·탈취 → 복원/폐차 비교 안내 → 말소 서류 순서 안내"),
            ("사용 장비", "방호 장비, 특수 세정 약품, 오존 탈취기"),
            ("작업 결과", "내부 오염을 처리한 뒤 폐차 말소 방향을 안내했습니다."),
            ("개인정보 보호", "유가족 성함·얼굴·차량번호는 공개하지 않습니다."),
        ],
    },
    {
        "id": "v04",
        "date": "2026-05-19",
        "region": "대전 유성구",
        "car": "대형 세단",
        "service": "상속차량 보관",
        "filter": "storage",
        "title": "대전 상속차량 보관 · 한정승인 전 이동 보관",
        "excerpt": "상속 방향을 정하기 전, 고인 명의 차량을 이동·보관하고 이후 처분 순서를 안내했습니다.",
        "image": "service-06.jpg",
        "paras": [
            "카리셋 상속차량 보관 사례입니다. 한정승인 여부를 정하는 동안 대형 세단이 거리에 방치되지 않도록 먼저 이동·보관했습니다.",
            "보관 중 과태료·훼손·추가 오염을 막고, 단순승인·한정승인·상속포기 각각에서 가능한 다음 절차(특수청소, 폐차 말소, 계속 보관)를 구분해 설명했습니다.",
            "결정 전에는 명의 변경이나 처분을 서두르지 않도록 안내했습니다. 후기에는 지역·차종만 남깁니다.",
        ],
        "bullets": [
            "상속차량 보관을 위한 이동",
            "결정 전 안전 보관",
            "폐차 말소 · 특수청소 후속 안내",
        ],
        "facts": [
            ("차량 상태", "대형 세단. 상속 방향이 정해지기 전이라 바로 처분하지 않고 이동·보관이 필요했습니다."),
            ("오염 범위", "즉시 특수청소보다 방치 방지와 보관이 우선인 상황이었습니다."),
            ("작업 과정", "상담 → 이동 → 보관 → 상속 방향별 후속(특수청소·폐차 말소) 안내"),
            ("사용 장비", "오염 차량 이동이 가능한 견인·보관 동선"),
            ("작업 결과", "결정 전까지 안전하게 보관한 뒤, 이후 처분 순서를 안내했습니다."),
            ("개인정보 보호", "성함·얼굴·차량번호는 올리지 않고 지역·차종만 공개합니다."),
        ],
    },
]

LIST_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>차량 작업후기 | 카리셋 특수</title>
  <meta name="description" content="카리셋 차량 작업후기. 자살차량 특수청소, 고독사 차량, 번개탄 탈취, 견인, 상속차량 보관, 폐차 말소 사례를 공개합니다. 010-4393-2414">
  <meta name="keywords" content="차량 작업후기, 자살차량 특수청소 후기, 고독사 차량, 번개탄 탈취, 카리셋">
  <meta name="author" content="카리셋 CARRESET">
  <meta name="robots" content="noindex, follow">
  <meta name="googlebot" content="noindex, follow">
  <meta name="Yeti" content="noindex, follow">
  <link rel="canonical" href="https://www.special.carreset.kr/reviews/index.html">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:site_name" content="카리셋 특수">
  <meta property="og:title" content="차량 작업후기 | 카리셋 특수">
  <meta property="og:description" content="자살차량 특수청소, 고독사 차량, 번개탄 탈취, 상속차량 보관 작업 사례">
  <meta property="og:url" content="https://www.special.carreset.kr/reviews/index.html">
  <meta property="og:image" content="https://www.special.carreset.kr/images/schema-vehicle.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@700;900&display=swap">
  <link rel="stylesheet" href="../css/style.css?v=21">
  <link rel="icon" href="../images/favicon.ico">
  <script type="application/ld+json">
  {list_schema}
  </script>
</head>
<body data-root=".." data-section="reviews" data-page="reviews/index.html">
  <div data-layout="header"></div>
  <section class="page-hero">
    <div class="inner">
      <p class="crumb"><a href="../index.html">홈</a> · 작업후기 · 차량 작업후기</p>
      <h1>차량 작업후기</h1>
      <p>각 사례에는 차량 상태, 오염 범위, 작업 과정, 사용 장비, 결과, 개인정보 보호 조치를 적습니다. 유가족 성함·얼굴·차량번호는 공개하지 않으며, 작업 사진은 제공해 주신 경우에만 번호판을 가리고 올립니다.</p>
    </div>
  </section>
  <div class="inner page-wrap">
    <div data-layout="side"></div>
    <article class="page-content">
      <div class="review-filters" role="tablist">
        <button type="button" class="is-active" data-filter="all">전체</button>
        <button type="button" data-filter="suicide">자살차량 특수청소</button>
        <button type="button" data-filter="lonely">고독사 차량</button>
        <button type="button" data-filter="charcoal">번개탄 탈취</button>
        <button type="button" data-filter="storage">보관 · 말소</button>
      </div>
      <div class="review-grid">
        {cards}
      </div>
      <div class="page-cta">
        <p>작업 사진과 지역·차종을 알려주시면 차량 작업후기에 올려 드립니다. 개인이 드러나는 내용은 올리지 않습니다.</p>
        <div class="inquiry-actions">
          <a class="btn-solid" href="tel:01043932414">전화로 후기 문의</a>
          <a class="btn-kakao" href="{kakao}" target="_blank" rel="noopener noreferrer">카톡으로 후기 문의</a>
        </div>
      </div>
    </article>
  </div>
  <div data-layout="footer"></div>
  <script src="../js/layout.js?v=21"></script>
  <script src="../js/main.js?v=21"></script>
</body>
</html>
"""

DETAIL_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | 카리셋 특수 작업후기</title>
  <meta name="description" content="{excerpt} 카리셋 차량 작업후기. 010-4393-2414">
  <meta name="keywords" content="{service}, 차량 작업후기, 카리셋">
  <meta name="author" content="카리셋 CARRESET">
  <meta name="robots" content="noindex, follow">
  <meta name="googlebot" content="noindex, follow">
  <meta name="Yeti" content="noindex, follow">
  <link rel="canonical" href="https://www.special.carreset.kr/reviews/{id}.html">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:site_name" content="카리셋 특수">
  <meta property="og:title" content="{title} | 카리셋 특수">
  <meta property="og:description" content="{excerpt}">
  <meta property="og:url" content="https://www.special.carreset.kr/reviews/{id}.html">
  <meta property="og:image" content="https://www.special.carreset.kr/images/{image}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@700;900&display=swap">
  <link rel="stylesheet" href="../css/style.css?v=21">
  <link rel="icon" href="../images/favicon.ico">
  <script type="application/ld+json">
  {json_ld}
  </script>
</head>
<body data-root=".." data-section="reviews" data-page="reviews/{id}.html">
  <div data-layout="header"></div>
  <section class="page-hero">
    <div class="inner">
      <p class="crumb"><a href="../index.html">홈</a> · <a href="index.html">작업후기</a> · {service}</p>
      <h1>{title}</h1>
      <p>{region} · {car} · {date}</p>
    </div>
  </section>
  <div class="inner page-wrap">
    <div data-layout="side"></div>
    <article class="page-content">
      <div class="review-hero">
        <img src="../images/{image}" alt="{service} 작업후기" width="1280" height="720">
      </div>
      <p class="review-kicker">{service}</p>
      {paras}
      <dl class="review-facts">
        {facts}
      </dl>
      <ul>
        {bullets}
      </ul>
      <nav class="related-keywords" aria-label="다른 작업후기">
        <h3>다른 차량 작업후기</h3>
        {related}
        <a href="https://carreset.kr/">카리셋 본 사이트</a>
      </nav>
      <div class="page-cta">
        <p>비슷한 차량 작업이 필요하시면 카리셋 전국 24시간 상담 010-4393-2414로 연락 주세요.</p>
        <div class="inquiry-actions">
          <a class="btn-solid" href="tel:01043932414">전화 상담하기</a>
          <a class="btn-kakao" href="{kakao}" target="_blank" rel="noopener noreferrer">카톡 상담하기</a>
          <a class="btn-ghost" href="index.html">후기 목록</a>
        </div>
      </div>
    </article>
  </div>
  <div data-layout="footer"></div>
  <script src="../js/layout.js?v=21"></script>
  <script src="../js/main.js?v=21"></script>
</body>
</html>
"""


def main() -> None:
    folder = ROOT / "reviews"
    folder.mkdir(exist_ok=True)

    cards = []
    for item in REVIEWS:
        cards.append(
            f'''<a class="review-card" href="{item["id"]}.html" data-type="{item["filter"]}">
          <div class="review-media"><img src="../images/{item["image"]}" alt="{item["service"]}"></div>
          <p class="review-kicker">{item["service"]}</p>
          <h2>{item["title"]}</h2>
          <p>{item["excerpt"]}</p>
          <span class="review-meta">{item["region"]} · {item["date"]}</span>
        </a>'''
        )

    list_schema = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "카리셋 차량 작업후기",
            "url": "https://www.special.carreset.kr/reviews/index.html",
            "mainEntity": {
                "@type": "ItemList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "url": "https://www.special.carreset.kr/reviews/" + item["id"] + ".html",
                        "name": item["title"],
                    }
                    for i, item in enumerate(REVIEWS)
                ],
            },
        },
        ensure_ascii=False,
    )

    (folder / "index.html").write_text(
        LIST_TEMPLATE.format(cards="\n        ".join(cards), kakao=KAKAO, list_schema=list_schema),
        encoding="utf-8",
    )
    print("wrote reviews/index.html")

    for item in REVIEWS:
        related = "\n        ".join(
            f'<a href="{other["id"]}.html">{other["service"]}</a>'
            for other in REVIEWS
            if other["id"] != item["id"]
        )
        json_ld = json.dumps(
            {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": item["title"],
                "datePublished": item["date"],
                "dateModified": item["date"],
                "description": item["excerpt"],
                "image": "https://www.special.carreset.kr/images/" + item["image"],
                "author": {
                    "@type": "Organization",
                    "name": "카리셋 CARRESET",
                    "url": "https://www.special.carreset.kr/",
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "카리셋 CARRESET",
                    "url": "https://www.special.carreset.kr/",
                },
                "mainEntityOfPage": "https://www.special.carreset.kr/reviews/" + item["id"] + ".html",
            },
            ensure_ascii=False,
        )
        html = DETAIL_TEMPLATE.format(
            kakao=KAKAO,
            paras="\n      ".join(f"<p>{p}</p>" for p in item["paras"]),
            bullets="\n        ".join(f"<li>{b}</li>" for b in item["bullets"]),
            facts="\n        ".join(
                f"<div><dt>{label}</dt><dd>{text}</dd></div>"
                for label, text in item.get("facts", [])
            ),
            related=related,
            json_ld=json_ld,
            **{k: v for k, v in item.items() if k not in ("paras", "bullets", "facts")},
        )
        (folder / f"{item['id']}.html").write_text(html, encoding="utf-8")
        print("wrote reviews/" + item["id"] + ".html")

    js_items = [
        {
            "id": item["id"],
            "title": item["title"],
            "service": item["service"],
            "region": item["region"],
            "date": item["date"],
            "excerpt": item["excerpt"],
            "image": item["image"],
            "href": "reviews/" + item["id"] + ".html",
        }
        for item in REVIEWS
    ]
    (ROOT / "js" / "reviews-data.js").write_text(
        "window.CARRESET_REVIEWS = "
        + json.dumps(js_items, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print("wrote js/reviews-data.js")


if __name__ == "__main__":
    main()
