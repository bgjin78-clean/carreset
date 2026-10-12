(function () {
  const KAKAO = "https://open.kakao.com/o/snFgJ5Ci";
  const TEL = "01043932414";
  const TEL_VIEW = "010-4393-2414";

  const MENU = [
    {
      id: "keepsake",
      label: "유품정리",
      href: "keepsake/index.html",
      groups: [
        {
          title: "서비스 안내",
          items: [
            { label: "유품정리의 이해", href: "keepsake/understanding.html" },
            { label: "고인유품정리", href: "keepsake/deceased.html" },
            { label: "고독사 유품정리", href: "keepsake/lonely.html" },
            { label: "무연고 유품정리", href: "keepsake/unclaimed.html" },
            { label: "요양병원입소 집정리", href: "keepsake/hospital.html" },
          ],
        },
        {
          title: "보관 · 인수",
          items: [
            { label: "유품 보관", href: "keepsake/storage.html" },
            { label: "유품 인수인계", href: "keepsake/handover.html" },
          ],
        },
        {
          title: "접수",
          items: [{ label: "유품정리 서비스 접수", href: "index.html#inquiry" }],
        },
      ],
    },
    {
      id: "cleaning",
      label: "특수청소",
      href: "cleaning/index.html",
      groups: [
        {
          title: "현장 유형",
          items: [
            { label: "고독사 특수청소", href: "cleaning/lonely.html" },
            { label: "극단적 선택 특수청소", href: "cleaning/suicide.html" },
            { label: "변사사건 특수청소", href: "cleaning/unattended.html" },
            { label: "강력범죄 현장 특수청소", href: "cleaning/crime.html" },
            { label: "쓰레기집 청소", href: "cleaning/hoarding.html" },
          ],
        },
        {
          title: "복원 · 분쟁",
          items: [
            { label: "악취제거 · 오염제거", href: "cleaning/odor.html" },
            { label: "살균 소독", href: "cleaning/disinfect.html" },
            { label: "비전문업체 피해 복원", href: "cleaning/restore.html" },
            { label: "유가족 / 임대인 분쟁", href: "cleaning/dispute.html" },
          ],
        },
        {
          title: "접수",
          items: [{ label: "특수청소 서비스 접수", href: "index.html#inquiry" }],
        },
      ],
    },
    {
      id: "vehicle",
      label: "사망자차량",
      href: "vehicle/index.html",
      groups: [
        {
          title: "특수청소",
          items: [
            { label: "자살차량 특수청소", href: "vehicle/suicide.html" },
            { label: "고독사 차량 특수청소", href: "vehicle/lonely.html" },
            { label: "번개탄 차량 탈취", href: "vehicle/charcoal.html" },
            { label: "차량 악취제거", href: "vehicle/odor.html" },
            { label: "차량 실내 복원", href: "vehicle/restore.html" },
          ],
        },
        {
          title: "이동 · 보관",
          items: [
            { label: "자살차량 견인", href: "vehicle/tow.html" },
            { label: "상속차량 보관", href: "vehicle/storage.html" },
          ],
        },
        {
          title: "행정 · 처분",
          items: [
            { label: "고인명의 폐차 말소", href: "vehicle/scrap.html" },
            { label: "고인차량 수출", href: "vehicle/export.html" },
            { label: "금융 · 저당 상담", href: "vehicle/finance.html" },
            { label: "유산 · 상속 상담", href: "vehicle/inherit.html" },
            { label: "기업제휴", href: "vehicle/partner.html" },
          ],
        },
        {
          title: "접수",
          items: [{ label: "사망자차량 서비스 접수", href: "index.html#inquiry" }],
        },
      ],
    },
    {
      id: "reviews",
      label: "작업후기",
      href: "reviews/index.html",
      groups: [
        {
          title: "차량 작업후기",
          items: [
            { label: "전체 보기", href: "reviews/index.html" },
            { label: "자살차량 특수청소", href: "reviews/index.html#suicide" },
            { label: "고독사 차량", href: "reviews/index.html#lonely" },
            { label: "번개탄 탈취", href: "reviews/index.html#charcoal" },
            { label: "보관 · 말소", href: "reviews/index.html#storage" },
          ],
        },
        {
          title: "접수",
          items: [{ label: "후기 등록 문의", href: "index.html#inquiry" }],
        },
      ],
    },
    {
      id: "inquiry",
      label: "상담문의",
      href: "index.html#inquiry",
      groups: [
        {
          title: "상담",
          items: [
            { label: "전화 상담 010-4393-2414", href: "tel:01043932414" },
            { label: "카톡 상담", href: "https://open.kakao.com/o/snFgJ5Ci" },
            { label: "온라인 접수", href: "index.html#inquiry" },
          ],
        },
      ],
    },
  ];

  function rootPath() {
    return document.body.getAttribute("data-root") || ".";
  }

  function url(path) {
    if (!path) return "#";
    if (path.startsWith("http") || path.startsWith("tel:")) return path;
    const root = rootPath().replace(/\/$/, "");
    return root + "/" + path.replace(/^\//, "");
  }

  function headerHTML() {
    const items = MENU.map((section) => {
      const cols = section.groups
        .map((group) => {
          const links = group.items
            .map((item) => `<li><a href="${url(item.href)}">${item.label}</a></li>`)
            .join("");
          return `<div class="mega-col"><h4>${group.title}</h4><ul>${links}</ul></div>`;
        })
        .join("");
      return `
        <li class="has-mega">
          <a href="${url(section.href)}">${section.label}</a>
          <div class="mega">
            <div class="mega-inner">${cols}</div>
          </div>
        </li>`;
    }).join("");

    return `
      <header class="site-header">
        <div class="inner header-top">
          <a class="logo" href="${url("index.html")}">
            <img src="${url("images/logo.png")}" alt="카리셋 자살차량 특수청소">
            <span class="logo-ko">카리셋</span>
            <span class="logo-bar" aria-hidden="true"></span>
            <span class="logo-en">CARRESET</span>
          </a>
          <div class="header-phone">
            <em>대표번호</em>
            <a href="tel:${TEL}">${TEL_VIEW}</a>
          </div>
          <button class="menu-toggle" type="button" aria-label="메뉴 열기">
            <span></span><span></span><span></span>
          </button>
        </div>
        <nav class="site-nav">
          <ul class="nav-list inner">${items}</ul>
        </nav>
      </header>`;
  }

  function footerHTML() {
    return `
      <footer class="site-footer">
        <div class="inner">
          <div class="footer-top">
            <div class="footer-brand">
              <a class="logo" href="${url("index.html")}">
                <img src="${url("images/logo.png")}" alt="카리셋 자살차량 특수청소">
                <span class="logo-ko">카리셋</span>
                <span class="logo-bar" aria-hidden="true"></span>
                <span class="logo-en">CARRESET</span>
              </a>
              <p>카리셋 자살차량 특수청소 · 고독사 차량 · 번개탄 탈취 · 상속차량 보관 · 폐차말소 · 유품정리</p>
            </div>
            <div>
              <p>24시간 상담</p>
              <a class="footer-phone" href="tel:${TEL}">${TEL_VIEW}</a>
            </div>
          </div>
          <p class="footer-copy">
            상호 : 카리셋 / 대표 : 입력 예정 / 사업자등록번호 : 입력 예정<br>
            주소 : 입력 예정 / 이메일 : 입력 예정 / 개인정보보호책임자 : 입력 예정<br>
            대표번호 : ${TEL_VIEW}<br>
            본 사이트는 카리셋 특수청소 전용 페이지입니다. <a href="https://carreset.kr/">카리셋 본 사이트</a><br>
            © 2026 CARRESET. All rights reserved.
          </p>
          <nav class="footer-keywords" aria-label="주요 키워드">
            <a href="${url("reviews/index.html")}">차량 작업후기</a>
            <a href="${url("vehicle/suicide.html")}">자살차량 특수청소</a>
            <a href="${url("vehicle/suicide.html")}">자살차량청소</a>
            <a href="${url("vehicle/lonely.html")}">고독사 차량 특수청소</a>
            <a href="${url("vehicle/charcoal.html")}">번개탄 차량 탈취</a>
            <a href="${url("vehicle/odor.html")}">차량 악취제거</a>
            <a href="${url("vehicle/tow.html")}">자살차량 견인</a>
            <a href="${url("vehicle/storage.html")}">상속차량 보관</a>
            <a href="${url("vehicle/scrap.html")}">고인명의 폐차 말소</a>
            <a href="${url("keepsake/index.html")}">유품정리</a>
            <a href="${url("keepsake/deceased.html")}">고인유품정리</a>
            <a href="${url("keepsake/lonely.html")}">고독사 유품정리</a>
            <a href="${url("cleaning/index.html")}">특수청소</a>
            <a href="${url("cleaning/lonely.html")}">고독사 특수청소</a>
            <a href="${url("cleaning/hoarding.html")}">쓰레기집 청소</a>
          </nav>
        </div>
      </footer>
      <div class="float-call">
        <a class="float-kakao" href="${KAKAO}" target="_blank" rel="noopener noreferrer">카톡<br>상담</a>
        <a href="tel:${TEL}">전화<br>상담</a>
      </div>`;
  }

  function sideHTML(sectionId, currentHref) {
    const section = MENU.find((item) => item.id === sectionId);
    if (!section) return "";
    const groups = section.groups
      .map((group) => {
        const links = group.items
          .map((item) => {
            const active = item.href === currentHref ? ' class="is-active"' : "";
            return `<li><a${active} href="${url(item.href)}">${item.label}</a></li>`;
          })
          .join("");
        return `<h4>${group.title}</h4><ul>${links}</ul>`;
      })
      .join("");
    return `<aside class="page-side"><a class="side-title" href="${url(section.href)}">${section.label}</a>${groups}</aside>`;
  }

  function bindNav() {
    const toggle = document.querySelector(".menu-toggle");
    const nav = document.querySelector(".site-nav");
    toggle?.addEventListener("click", () => nav?.classList.toggle("is-open"));
    document.querySelectorAll(".nav-list > li > a").forEach((link) => {
      link.addEventListener("click", (event) => {
        if (window.innerWidth > 768) return;
        const item = link.parentElement;
        if (item.querySelector(".mega")) {
          event.preventDefault();
          item.classList.toggle("is-open");
        }
      });
    });
  }

  const headerMount = document.querySelector("[data-layout='header']");
  const footerMount = document.querySelector("[data-layout='footer']");
  if (headerMount) headerMount.outerHTML = headerHTML();
  if (footerMount) footerMount.outerHTML = footerHTML();

  const sideMount = document.querySelector("[data-layout='side']");
  if (sideMount) {
    sideMount.outerHTML = sideHTML(
      document.body.getAttribute("data-section"),
      document.body.getAttribute("data-page")
    );
  }

  bindNav();
  window.CARRESET_MENU = MENU;
})();
