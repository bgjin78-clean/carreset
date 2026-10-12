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
            "시트, 바닥, 트림, 공조 라인에 스며든 오염을 제거한 뒤 오존 탈취를 진행했습니다. 유가족 요청에 따라 개인이 특정되지 않도록 사진과 성함은 공개하지 않습니다.",
            "작업 후 상태 확인을 거쳐 차량을 인도했으며, 이후 보관이나 폐차 말소가 필요하면 이어서 안내할 수 있습니다.",
        ],
        "bullets": [
            "현장 출동 및 자살차량 견인",
            "실내 특수청소 · 차량 악취제거",
            "작업 후 인도",
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
            "카리셋 번개탄 차량 탈취 사례입니다. 표면 세차 후에도 에어컨을 켤 때마다 냄새가 재발한다고 하셔서, 공조라인과 필터까지 확인했습니다.",
            "천장·송풍구·시트에 남은 그을음을 제거하고 필터 교체, 오존 탈취를 진행했습니다. 작업 사진은 차량 외관과 작업 장면 위주로만 남깁니다.",
            "냄새 재발 여부를 확인한 뒤 인도했습니다.",
        ],
        "bullets": [
            "그을음·악취 범위 확인",
            "공조라인 세척 및 필터 교체",
            "번개탄 차량 탈취 후 인도",
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
            "카리셋 고독사 차량 특수청소 사례입니다. 시트와 내장재 깊숙이 오염이 배어 있어 일반 세차로는 악취가 남았습니다.",
            "이동 후 분해가 필요한 부위까지 확인하고 오염 제거와 탈취를 진행했습니다. 차량 잔존 가치와 오염 정도를 보고 폐차 말소 방향을 함께 상담했습니다.",
            "고인명의 폐차 말소에 필요한 서류와 순서를 안내했습니다.",
        ],
        "bullets": [
            "고독사 차량 특수청소",
            "차량 악취제거",
            "고인명의 폐차 말소 안내",
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
            "카리셋 상속차량 보관 사례입니다. 한정승인 여부를 정하는 동안 차량이 방치되지 않도록 먼저 이동·보관했습니다.",
            "보관 중 과태료나 추가 오염을 막고, 단순승인·한정승인·상속포기 각각에서 가능한 다음 절차를 설명했습니다.",
            "이후 폐차 말소나 특수청소가 필요하면 같은 흐름으로 이어갈 수 있습니다.",
        ],
        "bullets": [
            "상속차량 보관을 위한 이동",
            "결정 전 안전 보관",
            "폐차 말소 · 특수청소 후속 안내",
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
  <meta name="robots" content="index, follow">
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
  <link rel="stylesheet" href="../css/style.css?v=18">
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
      <p>자살차량 특수청소, 고독사 차량, 번개탄 탈취, 견인, 상속차량 보관, 폐차 말소 사례입니다. 유가족 개인정보는 공개하지 않습니다.</p>
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
  <script src="../js/layout.js?v=18"></script>
  <script src="../js/main.js?v=18"></script>
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
  <meta name="robots" content="index, follow">
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
  <link rel="stylesheet" href="../css/style.css?v=18">
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
      <ul>
        {bullets}
      </ul>
      <nav class="related-keywords" aria-label="다른 작업후기">
        <h3>다른 차량 작업후기</h3>
        {related}
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
  <script src="../js/layout.js?v=18"></script>
  <script src="../js/main.js?v=18"></script>
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
            related=related,
            json_ld=json_ld,
            **{k: v for k, v in item.items() if k not in ("paras", "bullets")},
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
