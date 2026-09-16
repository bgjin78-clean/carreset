(function () {
  const slides = Array.from(document.querySelectorAll(".hero-slide"));
  const dotsWrap = document.querySelector(".hero-dots");
  const prev = document.querySelector(".hero-prev");
  const next = document.querySelector(".hero-next");
  let index = 0;
  let timer;

  if (slides.length && dotsWrap) {
    slides.forEach((_, i) => {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("aria-label", i + 1 + "번째 슬라이드");
      if (i === 0) dot.classList.add("is-active");
      dot.addEventListener("click", () => go(i));
      dotsWrap.appendChild(dot);
    });

    function go(i) {
      slides[index].classList.remove("is-active");
      dotsWrap.children[index].classList.remove("is-active");
      index = (i + slides.length) % slides.length;
      slides[index].classList.add("is-active");
      dotsWrap.children[index].classList.add("is-active");
      restart();
    }

    function restart() {
      clearInterval(timer);
      timer = setInterval(() => go(index + 1), 7000);
    }

    prev?.addEventListener("click", () => go(index - 1));
    next?.addEventListener("click", () => go(index + 1));
    restart();
  }

  document.querySelectorAll(".faq-item").forEach((item) => {
    item.querySelector("button")?.addEventListener("click", () => {
      item.classList.toggle("is-open");
    });
  });

  const form = document.querySelector(".inquiry-form");
  const message = document.querySelector(".form-message");
  const EMAILJS_PUBLIC_KEY = "JKsVOKPtnWHIr2BCV";
  const EMAILJS_SERVICE_ID = "allbarunclean";
  const EMAILJS_TEMPLATE_ID = "template_b4ox5js";

  if (form && window.emailjs) {
    emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });
  }

  form?.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const services = Array.from(form.querySelectorAll('input[name="service"]:checked'))
      .map((input) => input.value);
    if (!services.length) {
      if (message) {
        message.classList.add("is-visible");
        message.textContent = "서비스를 하나 이상 선택해 주세요.";
      }
      return;
    }

    const region = form.region.value.trim();
    const phone = form.phone.value.trim();
    const car = form.car.value.trim() || "미기재";
    const memo = form.memo.value.trim();
    const body = [
      "[카리셋 홈페이지 상담 접수]",
      "",
      "카리셋(CARRESET) 사이트에서 접수된 차량 특수청소 상담입니다.",
      "",
      "■ 고객 연락처: " + phone,
      "■ 지역: " + region,
      "■ 차종: " + car,
      "■ 요청 서비스: " + services.join(", "),
      "",
      "■ 상황 설명",
      memo,
      "",
      "본 메일은 카리셋에서 올바른정리 상담 접수 메일로 전달합니다.",
      "회신·연락: 010-4393-2414 / 카카오 오픈채팅",
    ].join("\n");

    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn ? submitBtn.textContent : "";
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = "전송 중...";
    }
    if (message) {
      message.classList.remove("is-visible");
    }

    const params = {
      from_name: "카리셋 CARRESET",
      name: "카리셋 CARRESET",
      phone: phone,
      region: region,
      service: "카리셋 / " + services.join(", "),
      message: body,
    };

    if (!window.emailjs) {
      if (message) {
        message.classList.add("is-visible");
        message.textContent = "메일 전송 모듈을 불러오지 못했습니다. 010-4393-2414로 연락 주세요.";
      }
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
      return;
    }

    emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, params)
      .then(() => {
        form.reset();
        if (message) {
          message.classList.add("is-visible");
          message.textContent = "카리셋 명의로 상담 접수가 전달되었습니다. 확인 후 연락드리겠습니다.";
        }
      })
      .catch((err) => {
        console.error("EmailJS error:", err);
        if (message) {
          message.classList.add("is-visible");
          message.textContent = "전송에 실패했습니다. 급하시면 010-4393-2414 또는 카톡 상담을 이용해 주세요.";
        }
      })
      .finally(() => {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = originalText;
        }
      });
  });
})();
