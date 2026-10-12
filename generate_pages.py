# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KAKAO = "https://open.kakao.com/o/snFgJ5Ci"

PAGES = [
    {
        "section": "keepsake",
        "file": "index.html",
        "page": "keepsake/index.html",
        "title": "유품정리",
        "lead": "유가족의 뜻에 맞춰 고인의 물건을 정리하고, 보관과 인수인계까지 함께합니다.",
        "h2": "유품정리는 물건 정리만이 아닙니다",
        "paras": [
            "카리셋 유품정리는 유가족의 요청 범위에 맞춰 고인유품정리, 고독사 유품정리, 요양병원입소 집정리, 무연고 유품 보관을 진행합니다.",
            "갑작스러운 이별 앞에서 유품을 손대는 일은 마음과 시간이 모두 필요합니다. 현장 특수청소나 사망자차량 처리가 필요하면 함께 연계합니다.",
        ],
        "bullets": [
            "유가족이 지정한 범위만 정리합니다",
            "중요 서류, 사진, 유품은 따로 분류합니다",
            "필요 시 보관과 인수인계를 함께 진행합니다",
            "현장 특수청소가 필요하면 차량·주거 작업을 연계합니다",
        ],
    },
    {
        "section": "keepsake",
        "file": "understanding.html",
        "page": "keepsake/understanding.html",
        "title": "유품정리의 이해",
        "lead": "무엇을 남기고, 무엇을 정리할지 정하는 일부터 유품정리는 시작됩니다.",
        "h2": "먼저 범위와 순서를 정합니다",
        "paras": [
            "유품정리는 청소와 다릅니다. 고인과 가족의 흔적이 담긴 물건을 함부로 버릴 수 없고, 법적·행정적으로 남겨야 할 서류도 있습니다.",
            "카리셋은 작업 전에 유가족과 정리 범위, 보관이 필요한 물건, 폐기 대상, 작업 순서를 함께 확인합니다. 마음이 준비되지 않은 경우에는 급하지 않은 물건부터 나눠 진행할 수 있습니다.",
        ],
        "bullets": [
            "상담 단계에서 현장 상황과 희망 범위를 듣습니다",
            "중요 유품과 일반 정리 대상을 구분합니다",
            "특수청소가 필요한 공간은 별도 안내합니다",
        ],
    },
    {
        "section": "keepsake",
        "file": "deceased.html",
        "page": "keepsake/deceased.html",
        "title": "고인유품정리",
        "lead": "유가족의 의뢰에 맞춰 돌아가신 고인의 유품을 정리합니다.",
        "h2": "남길 것과 정리할 것을 함께 나눕니다",
        "paras": [
            "고인의 옷, 생활용품, 사진, 서류는 유가족마다 의미가 다릅니다. 카리셋은 일괄 폐기보다 분류를 우선합니다.",
            "원하시면 가족이 보기 어려운 공간부터 대신 정리하고, 남겨야 할 물건은 상자 단위로 구분해 전달합니다.",
        ],
        "bullets": [
            "주거 공간, 창고, 차량 내부 유품을 구분해 정리",
            "서류·통장·인감 등 행정 관련 물건 별도 분류",
            "원하시는 경우 사진 기록 후 진행",
        ],
    },
    {
        "section": "keepsake",
        "file": "lonely.html",
        "page": "keepsake/lonely.html",
        "title": "고독사 유품정리",
        "lead": "발견이 늦어진 현장의 유품은 위생 처리와 분류를 함께 진행합니다.",
        "h2": "특수청소와 유품정리를 한 흐름으로",
        "paras": [
            "고독사 현장은 단순 정리만으로 끝나지 않는 경우가 많습니다. 오염된 물건과 남겨야 할 유품을 구분한 뒤, 필요한 공간은 특수청소로 이어갑니다.",
            "임대인, 관리사무소, 유가족이 각각 확인해야 할 사항이 다를 수 있어 작업 전 역할과 범위를 분명히 합니다.",
        ],
        "bullets": [
            "오염 유무에 따라 폐기와 보관을 나눕니다",
            "악취·오염이 있는 공간은 특수청소를 연계합니다",
            "중요 유품은 별도 포장해 전달합니다",
        ],
    },
    {
        "section": "keepsake",
        "file": "unclaimed.html",
        "page": "keepsake/unclaimed.html",
        "title": "무연고 유품정리",
        "lead": "연고자를 바로 찾기 어려운 경우에도 중요한 유품은 남겨 두고 정리합니다.",
        "h2": "함부로 버리지 않습니다",
        "paras": [
            "무연고 사망 또는 연고 확인이 늦어지는 현장에서는 신분증, 서류, 사진, 귀중품을 먼저 구분해 보관하는 것이 중요합니다.",
            "카리셋은 바로 폐기할 수 없는 물건을 따로 정리하고, 이후 인수 주체가 정해지면 인계할 수 있도록 돕습니다.",
        ],
        "bullets": [
            "신원·행정 관련 물건 우선 분류",
            "보관이 필요한 유품과 폐기 대상 구분",
            "인수 주체 확인 후 인계",
        ],
    },
    {
        "section": "keepsake",
        "file": "hospital.html",
        "page": "keepsake/hospital.html",
        "title": "요양병원입소 집정리",
        "lead": "요양병원 입소 전, 거주하시던 집의 물건을 정리해 드립니다.",
        "h2": "앞으로의 생활을 위한 정리입니다",
        "paras": [
            "입소 준비는 시간이 촉박한 경우가 많습니다. 가져갈 물건, 보관할 물건, 정리할 물건을 나눠 가족의 부담을 덜어 드립니다.",
            "나중에 다시 집으로 돌아올 가능성을 남겨 두고 싶다면, 전부 비우지 않고 필요한 공간만 정리하는 방식으로도 진행합니다.",
        ],
        "bullets": [
            "입소에 필요한 생활용품 우선 분류",
            "가구·가전 이동 또는 보관 상담",
            "빈집 관리가 필요하면 범위에 맞춰 정리",
        ],
    },
    {
        "section": "keepsake",
        "file": "storage.html",
        "page": "keepsake/storage.html",
        "title": "유품 보관",
        "lead": "바로 결정하기 어려운 유품은 분류한 뒤 보관할 수 있습니다.",
        "h2": "시간이 필요한 유품을 맡기실 수 있습니다",
        "paras": [
            "상속, 가족 간 협의, 마음이 정리되는 데는 시간이 필요합니다. 당장 폐기하기 어려운 물건은 따로 구분해 보관 상담을 진행합니다.",
            "차량 유품과 주거 유품이 함께 있는 경우에는 각각의 보관 방식을 안내합니다.",
        ],
        "bullets": [
            "중요 유품 우선 분류 후 보관 상담",
            "상속 절차가 끝날 때까지 필요한 물건 보존",
            "차량 보관이 필요하면 사망자차량 서비스와 연계",
        ],
    },
    {
        "section": "keepsake",
        "file": "handover.html",
        "page": "keepsake/handover.html",
        "title": "유품 인수인계",
        "lead": "정리한 유품을 유가족 또는 지정하신 분께 구분해 전달합니다.",
        "h2": "무엇을 전달했는지 남깁니다",
        "paras": [
            "작업이 끝난 뒤에도 유품이 어디에 있는지 알 수 있어야 합니다. 카리셋은 남겨 드릴 물건과 정리한 범위를 구분해 인계합니다.",
            "여러 가족이 나눠 가져가야 하는 경우에는 상자·품목 단위로 구분해 전달할 수 있습니다.",
        ],
        "bullets": [
            "인계 대상과 보관 대상을 구분해 전달",
            "중요 서류와 귀중품은 별도 확인",
            "이후 특수청소나 차량 처리가 남으면 이어서 안내",
        ],
    },
    {
        "section": "cleaning",
        "file": "index.html",
        "page": "cleaning/index.html",
        "title": "특수청소",
        "lead": "고독사, 극단적 선택, 변사사건 등 일반 청소로 해결할 수 없는 현장을 처리합니다.",
        "h2": "특수청소는 눈에 보이는 오염만 지우는 일이 아닙니다",
        "paras": [
            "카리셋 특수청소는 고독사 특수청소, 극단적 선택 현장, 변사사건, 강력범죄 현장, 쓰레기집 청소처럼 일반 청소로 해결할 수 없는 오염을 원인부터 다룹니다.",
            "주거 현장과 자살차량 특수청소, 고독사 차량이 함께 있는 경우에도 한 흐름으로 상담합니다.",
        ],
        "bullets": [
            "고독사 특수청소 · 극단적 선택 · 변사 · 강력범죄 현장",
            "쓰레기집 청소, 악취제거, 비전문업체 피해 복원",
            "살균 소독과 임대인·유가족 분쟁 상담",
        ],
    },
    {
        "section": "cleaning",
        "file": "lonely.html",
        "page": "cleaning/lonely.html",
        "title": "고독사 특수청소",
        "lead": "고독사 특수청소로 발견이 늦어진 현장의 오염과 악취를 처리합니다.",
        "h2": "고독사 특수청소는 위생 처리와 공간 복원을 함께 봅니다",
        "paras": [
            "카리셋 고독사 특수청소는 바닥, 벽, 가구, 공조 시설까지 번진 오염을 원인부터 다룹니다. 표면만 닦는 고독사청소로는 악취가 다시 올라오는 경우가 많습니다.",
            "오염물 제거, 살균 소독, 오존 탈취 후 고독사 유품정리와 고독사 차량 특수청소가 필요하면 함께 안내합니다.",
        ],
        "bullets": [
            "오염물 제거 및 폐기",
            "살균 · 소독, 오존 탈취",
            "유품정리와 차량 처리 연계",
        ],
    },
    {
        "section": "cleaning",
        "file": "suicide.html",
        "page": "cleaning/suicide.html",
        "title": "극단적 선택 특수청소",
        "lead": "극단적 선택 현장 특수청소와 자살차량 특수청소를 구분해 진행합니다.",
        "h2": "극단적 선택 특수청소는 가족이 보지 않아도 되는 일을 대신합니다",
        "paras": [
            "카리셋 극단적 선택 특수청소는 현장 출동부터 오염 제거, 악취탈취, 복원까지 필요한 범위를 조용히 진행합니다.",
            "차량 내부에서 발생한 경우에는 자살차량 특수청소로 이어지고, 주거 현장은 고독사 특수청소·유품정리와 연계할 수 있습니다.",
        ],
        "bullets": [
            "현장 출동 및 오염 범위 확인",
            "특수 약품과 장비로 원인 제거",
            "주거와 차량을 구분해 처리",
        ],
    },
    {
        "section": "cleaning",
        "file": "unattended.html",
        "page": "cleaning/unattended.html",
        "title": "변사사건 현장",
        "lead": "변사 현장은 수사·행정 절차 이후 위생 처리가 필요합니다.",
        "h2": "절차가 끝난 뒤의 현장을 정리합니다",
        "paras": [
            "변사사건 현장은 관계 기관의 확인이 끝난 뒤에야 청소를 시작할 수 있습니다. 카리셋은 그 이후 단계에서 오염 제거와 공간 복원을 진행합니다.",
            "임대주택인 경우 원상회복 범위도 함께 상담합니다.",
        ],
        "bullets": [
            "관계 기관 확인 이후 작업",
            "오염 제거, 살균, 탈취",
            "원상회복이 필요하면 범위 안내",
        ],
    },
    {
        "section": "cleaning",
        "file": "crime.html",
        "page": "cleaning/crime.html",
        "title": "강력범죄 현장",
        "lead": "범죄 피해 현장은 심리적 부담과 위생 문제가 함께 남습니다.",
        "h2": "현장을 다시 생활 가능한 상태로",
        "paras": [
            "강력범죄 현장은 눈에 보이는 흔적뿐 아니라 보이지 않는 오염과 냄새까지 남을 수 있습니다. 카리셋은 전문 장비로 오염을 제거하고 살균·탈취를 진행합니다.",
            "피해자와 유가족이 국가 지원 제도를 안내받을 수 있도록, 필요한 경우 관련 연락처도 함께 안내합니다.",
        ],
        "bullets": [
            "혈흔 · 체액 등 특수 오염 제거",
            "살균 · 소독 및 악취 제거",
            "작업 범위는 사전 협의 후 진행",
        ],
    },
    {
        "section": "cleaning",
        "file": "hoarding.html",
        "page": "cleaning/hoarding.html",
        "title": "쓰레기집 청소",
        "lead": "쓰레기집 청소는 적치물 반출과 악취·해충 처리, 공간 복원까지 이어집니다.",
        "h2": "쓰레기집 청소는 버리는 일로 끝나지 않습니다",
        "paras": [
            "카리셋 쓰레기집 청소는 적치물만 반출하고 끝내지 않습니다. 바닥과 벽면, 배수, 해충, 악취까지 남아 있는 경우가 많습니다.",
            "반출, 세척, 살균 소독, 탈취 순서로 공간이 다시 사용될 수 있게 돕습니다.",
        ],
        "bullets": [
            "폐기물 분류 및 반출",
            "악취 · 해충 원인 제거",
            "살균 · 소독 후 생활 공간 복원",
        ],
    },
    {
        "section": "cleaning",
        "file": "odor.html",
        "page": "cleaning/odor.html",
        "title": "악취 · 오염 제거",
        "lead": "냄새는 공기 중에만 있지 않습니다. 스며든 원인을 제거해야 사라집니다.",
        "h2": "방향제로는 해결되지 않습니다",
        "paras": [
            "사망 현장이나 장기 방치된 공간의 악취는 자재 안쪽까지 배어 있습니다. 향으로 가리면 시간이 지나 다시 올라옵니다.",
            "카리셋은 오염원을 제거하고 오존 탈취, 약품 처리, 필요 시 자재 교체로 냄새의 원인을 다룹니다.",
        ],
        "bullets": [
            "오염원 확인 및 제거",
            "오존 탈취 · 전문 약품 처리",
            "재발 가능성이 높은 자재는 교체 상담",
        ],
    },
    {
        "section": "cleaning",
        "file": "disinfect.html",
        "page": "cleaning/disinfect.html",
        "title": "살균 · 소독",
        "lead": "눈에 보이지 않는 세균과 바이러스까지 처리합니다.",
        "h2": "청소 다음 단계가 살균입니다",
        "paras": [
            "오염물을 제거한 뒤에도 세균과 곰팡이가 남을 수 있습니다. 카리셋은 작업 공간에 맞는 살균·소독을 진행합니다.",
            "차량 실내와 주거 공간이 함께 오염된 경우에는 각각의 방식에 맞춰 처리합니다.",
        ],
        "bullets": [
            "오염 제거 후 살균 · 소독",
            "공조 · 환기 경로 점검",
            "작업 후 주의사항 안내",
        ],
    },
    {
        "section": "cleaning",
        "file": "restore.html",
        "page": "cleaning/restore.html",
        "title": "비전문업체 피해 복원",
        "lead": "제대로 끝나지 않은 현장은 악취와 오염이 다시 올라올 수 있습니다.",
        "h2": "미완료 작업을 이어서 마무리합니다",
        "paras": [
            "표면만 닦고 끝난 현장, 폐기물이 남은 현장, 냄새가 재발한 현장은 추가로 금전적·정신적 피해가 생깁니다.",
            "카리셋은 현재 상태를 다시 진단하고, 남은 오염과 악취를 원인부터 처리합니다.",
        ],
        "bullets": [
            "기존 작업 상태 재진단",
            "남은 오염 · 악취 원인 제거",
            "필요 시 자재 복원 및 재작업",
        ],
    },
    {
        "section": "cleaning",
        "file": "dispute.html",
        "page": "cleaning/dispute.html",
        "title": "유가족 / 임대인 분쟁",
        "lead": "현장 처리 비용과 원상회복 범위를 둘러싼 갈등을 줄이도록 돕습니다.",
        "h2": "범위와 기록을 분명히 합니다",
        "paras": [
            "임대주택에서 고독사나 변사가 발생하면 유가족과 임대인 사이에 비용, 원상회복, 퇴거 시점을 두고 다툼이 생기기도 합니다.",
            "카리셋은 어느 한쪽을 대신해 다투는 입장이 아니라, 현장 상태와 필요한 작업 범위를 확인하고 양측이 판단할 수 있게 안내합니다.",
        ],
        "bullets": [
            "현장 상태와 작업 범위 확인",
            "원상회복에 필요한 항목 안내",
            "작업 전후 상태를 구분해 설명",
        ],
    },
    {
        "section": "vehicle",
        "file": "index.html",
        "page": "vehicle/index.html",
        "title": "사망자차량",
        "lead": "자살차량 · 고독사 차량의 특수청소부터 견인, 보관, 폐차 · 말소까지 한 흐름으로 진행합니다.",
        "h2": "사망자차량은 옮기는 것으로 끝나지 않습니다",
        "paras": [
            "카리셋 사망자차량 서비스는 자살차량 특수청소, 고독사 차량 특수청소, 번개탄 차량 탈취, 자살차량 견인, 상속차량 보관, 고인명의 폐차 말소를 한 흐름으로 진행합니다.",
            "단순승인, 한정승인, 상속포기에 따라 보관과 처분 방향이 달라질 수 있어 먼저 상황을 듣고 맞는 순서를 제안합니다.",
        ],
        "bullets": [
            "특수청소 · 탈취 · 실내 복원",
            "견인 · 이동 · 장기 보관",
            "폐차 · 말소 · 수출 · 금융 상담",
        ],
    },
    {
        "section": "vehicle",
        "file": "suicide.html",
        "page": "vehicle/suicide.html",
        "title": "자살차량 특수청소",
        "lead": "자살차량 특수청소, 견인, 오염제거, 탈취, 보관, 폐차말소까지 한 흐름으로 진행합니다.",
        "h2": "자살차량 특수청소는 일반 세차로 해결되지 않습니다",
        "paras": [
            "카리셋 자살차량 특수청소는 극단적 선택이 발생한 차량의 시트, 바닥, 트림, 공조 라인까지 스며든 오염을 처리합니다. 일반 세차나 견인이 거부되는 경우에도 현장 출동부터 진행합니다.",
            "자살차량 견인 후 특수청소, 차량 악취제거, 상속차량 보관, 고인명의 폐차 말소 중 필요한 다음 단계를 상황에 맞게 안내합니다.",
            "카리셋은 현장 사진으로 오염 범위를 가늠한 뒤 일반 견인이 가능한지부터 안내합니다. 작업 후에는 차량 작업후기에 지역·차종만 남기고 공개할 수 있습니다.",
        ],
        "bullets": [
            "자살차량 특수청소 · 오염 범위 확인",
            "자살차량 견인 · 이동",
            "악취제거, 보관, 폐차 말소 상담",
        ],
    },
    {
        "section": "vehicle",
        "file": "lonely.html",
        "page": "vehicle/lonely.html",
        "title": "고독사 차량 특수청소",
        "lead": "고독사 차량 특수청소로 발견이 늦어진 차량의 오염과 악취를 처리합니다.",
        "h2": "고독사 차량은 시간이 지날수록 내부 오염이 깊습니다",
        "paras": [
            "카리셋 고독사 차량 특수청소는 시트 폼, 카펫, 내장재 깊숙이 밴 오염과 악취를 제거합니다. 차량 안에서 발견이 늦어진 경우 일반 세차로는 냄새가 다시 올라오는 경우가 많습니다.",
            "복원이 가능한지, 폐차 말소가 맞는지는 오염 정도와 차량 가치를 보고 함께 상담합니다. 필요하면 자살차량 견인과 상속차량 보관으로 이어갑니다.",
        ],
        "bullets": [
            "내부 오염도 진단",
            "시트 · 내장재 분해 세척 또는 교체 상담",
            "복원 가능 여부에 따른 보관 · 폐차 안내",
        ],
    },
    {
        "section": "vehicle",
        "file": "charcoal.html",
        "page": "vehicle/charcoal.html",
        "title": "번개탄 차량 탈취",
        "lead": "그을음과 일산화탄소 냄새가 밴 실내를 원인부터 제거합니다.",
        "h2": "번개탄 차량 탈취는 천장과 공조까지 함께 봅니다",
        "paras": [
            "카리셋 번개탄 차량 탈취는 천장, 유리, 송풍구, 시트에 남은 그을음과 냄새를 원인부터 제거합니다. 표면 세차만으로는 공조를 켤 때마다 냄새가 재발합니다.",
            "공조라인 세척, 필터 교체, 오존 탈취를 포함해 차량 악취제거와 실내 복원까지 이어서 진행할 수 있습니다.",
        ],
        "bullets": [
            "그을음 · 악취 범위 확인",
            "공조라인 세척 및 필터 교체",
            "오존 탈취와 실내 복원",
        ],
    },
    {
        "section": "vehicle",
        "file": "odor.html",
        "page": "vehicle/odor.html",
        "title": "차량 악취제거",
        "lead": "차량 악취제거로 시트와 내장재 안쪽까지 스며든 냄새를 제거합니다.",
        "h2": "차량 악취제거는 숨은 경로를 찾아야 합니다",
        "paras": [
            "카리셋 차량 악취제거는 자살차량, 고독사 차량, 번개탄 차량처럼 일반 세차로 없어지지 않는 냄새를 원인부터 처리합니다.",
            "시트 폼, 안전벨트, 바닥 매트, 에어컨 내부까지 확인하고 약품, 스팀, 오존, 필요 시 부품 교체로 재발을 줄입니다.",
        ],
        "bullets": [
            "악취 원인 부위 점검",
            "특수 약품 · 오존 탈취",
            "재발 위험이 큰 부품 교체 상담",
        ],
    },
    {
        "section": "vehicle",
        "file": "restore.html",
        "page": "vehicle/restore.html",
        "title": "실내 복원",
        "lead": "손상된 내장재를 점검하고 필요 시 교체 · 복원합니다.",
        "h2": "청소 다음에 복원 여부를 판단합니다",
        "paras": [
            "오염이 심한 시트나 천장재는 세척만으로 원래 상태를 되돌리기 어렵습니다. 카리셋은 세척으로 가능한 범위와 교체가 필요한 범위를 구분해 제안합니다.",
            "상속 차량의 경우 복원 비용과 잔존 가치를 함께 보고 방향을 정할 수 있습니다.",
        ],
        "bullets": [
            "내장재 손상 · 변색 확인",
            "세척 복원 또는 교체 제안",
            "작업 후 상태 확인 및 인도",
        ],
    },
    {
        "section": "vehicle",
        "file": "tow.html",
        "page": "vehicle/tow.html",
        "title": "자살차량 견인",
        "lead": "자살차량 견인, 고독사 차량 이동 등 일반 견인이 어려운 차량을 출동해 옮깁니다.",
        "h2": "자살차량 견인은 일반 견인과 다릅니다",
        "paras": [
            "카리셋 자살차량 견인은 오염이 심하거나 사망자 명의라 일반 견인·정비가 거부되는 차량을 현장 확인 후 이동합니다.",
            "보관소나 작업장으로 옮긴 뒤 자살차량 특수청소, 상속차량 보관, 폐차 말소를 이어갈 수 있습니다.",
        ],
        "bullets": [
            "현장 출동 및 안전 조치",
            "보관소 · 작업장 이동",
            "이동 후 상태 확인 및 다음 단계 안내",
        ],
    },
    {
        "section": "vehicle",
        "file": "storage.html",
        "page": "vehicle/storage.html",
        "title": "상속차량 보관",
        "lead": "상속차량 보관으로 한정승인·상속포기 결정 전 고인 명의 자동차를 안전하게 맡기실 수 있습니다.",
        "h2": "상속차량 보관은 결정을 미루는 시간이 필요할 때 씁니다",
        "paras": [
            "카리셋 상속차량 보관은 단순승인·한정승인·상속포기 여부를 정하는 동안 고인 명의 차량이 방치되지 않도록 이동·보관합니다.",
            "보관 중 과태료, 훼손, 추가 오염을 막고, 이후 고인명의 폐차 말소나 특수청소 방향을 안내합니다.",
        ],
        "bullets": [
            "단순승인 · 한정승인 · 상속포기에 맞춘 보관",
            "오염 차량의 이동 후 보관",
            "보관 중 폐차 · 말소 · 매각 방향 상담",
        ],
    },
    {
        "section": "vehicle",
        "file": "scrap.html",
        "page": "vehicle/scrap.html",
        "title": "고인명의 폐차 말소",
        "lead": "고인명의 폐차 말소, 서류 확인부터 말소 등록까지 대행 상담합니다.",
        "h2": "고인명의 폐차 말소는 오염·서류·저당부터 확인합니다",
        "paras": [
            "카리셋 고인명의 폐차 말소는 오염으로 폐차가 거부된 차량도 이동·특수청소 후 절차를 안내합니다.",
            "사망자 차량 폐차에 필요한 서류와 순서를 유가족 상황에 맞춰 설명하고, 상속차량 보관이 먼저 필요하면 함께 진행합니다.",
        ],
        "bullets": [
            "폐차 가능 여부 확인",
            "필요 서류 안내",
            "말소 등록 대행 상담",
        ],
    },
    {
        "section": "vehicle",
        "file": "export.html",
        "page": "vehicle/export.html",
        "title": "고인차량 수출",
        "lead": "복원 후 수출이 가능한 차량은 처분 방향을 함께 검토합니다.",
        "h2": "모든 차량이 수출 대상은 아닙니다",
        "paras": [
            "차량 상태, 사고 이력, 잔존 가치, 서류 조건에 따라 수출이 가능한 경우와 폐차가 맞는 경우가 나뉩니다.",
            "카리셋은 무리하게 수출을 권하지 않고, 현재 상태에서 가능한 처분 방법을 설명합니다.",
        ],
        "bullets": [
            "차량 상태 및 서류 확인",
            "수출 · 폐차 · 보관 중 선택 상담",
            "후속 행정 절차 안내",
        ],
    },
    {
        "section": "vehicle",
        "file": "finance.html",
        "page": "vehicle/finance.html",
        "title": "금융 · 저당 상담",
        "lead": "할부, 리스, 저당이 남은 차량도 상황에 맞는 방향을 안내합니다.",
        "h2": "남은 채무와 차량 처리를 같이 봅니다",
        "paras": [
            "고인 명의 차량에 할부나 저당이 남아 있으면 청소나 폐차만으로 끝나지 않습니다. 금융사 확인이 필요한 경우가 있습니다.",
            "카리셋은 법률 대리를 하지 않는 범위에서, 필요한 확인 사항과 진행 순서를 안내합니다.",
        ],
        "bullets": [
            "할부 · 리스 · 저당 여부 확인 안내",
            "처리 전 필요한 서류 설명",
            "특수청소 · 보관 · 폐차와 연계한 순서 제안",
        ],
    },
    {
        "section": "vehicle",
        "file": "inherit.html",
        "page": "vehicle/inherit.html",
        "title": "유산 · 상속 상담",
        "lead": "단순승인, 한정승인, 상속포기에 따라 차량 처리 방향이 달라집니다.",
        "h2": "상속 방향이 정해지기 전에도 차량은 움직일 수 있습니다",
        "paras": [
            "차량은 상속 재산에 포함됩니다. 방향을 정하기 전에 함부로 명의를 바꾸거나 처분하면 문제가 생길 수 있습니다.",
            "카리셋은 법률 판단을 대신하지 않습니다. 대신 차량을 안전하게 보관하고, 각 방향에서 가능한 후속 조치를 설명합니다.",
        ],
        "bullets": [
            "단순승인 · 한정승인 · 상속포기별 차량 처리 안내",
            "결정 전 장기 보관",
            "필요 시 법률 상담 연계 안내",
        ],
    },
    {
        "section": "vehicle",
        "file": "partner.html",
        "page": "vehicle/partner.html",
        "title": "기업제휴",
        "lead": "금융사, 법무, 보험, 청소 현장에서 사망자 차량 처리를 함께할 수 있습니다.",
        "h2": "현장 처리가 필요한 기관과 협력합니다",
        "paras": [
            "사망자 명의 차량은 한 업체만의 일로 끝나지 않는 경우가 많습니다. 견인, 보관, 특수청소, 행정 처리가 동시에 필요합니다.",
            "카리셋은 제휴 문의에 대해 업무 범위와 진행 방식을 안내합니다.",
        ],
        "bullets": [
            "금융 · 보험 · 법무 현장 연계 상담",
            "전국 출동 및 차량 특수청소",
            "보관 · 폐차 · 말소 후속 처리",
        ],
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{seo_title}</title>
  <meta name="description" content="{seo_desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="카리셋 CARRESET">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://www.special.carreset.kr/{page}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:site_name" content="카리셋 특수">
  <meta property="og:title" content="{seo_title}">
  <meta property="og:description" content="{seo_desc}">
  <meta property="og:url" content="https://www.special.carreset.kr/{page}">
  <meta property="og:image" content="https://www.special.carreset.kr/images/{og_image}">
  <meta property="og:image:width" content="1280">
  <meta property="og:image:height" content="720">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{seo_title}">
  <meta name="twitter:description" content="{seo_desc}">
  <meta name="twitter:image" content="https://www.special.carreset.kr/images/{og_image}">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@700;900&display=swap">
  <link rel="stylesheet" href="../css/style.css?v=18">
  <link rel="icon" href="../images/favicon.ico">
  <script type="application/ld+json">
  {json_ld}
  </script>
</head>
<body data-root=".." data-section="{section}" data-page="{page}">
  <div data-layout="header"></div>
  <section class="page-hero">
    <div class="inner">
      <p class="crumb"><a href="../index.html">홈</a> · <a href="../{section}/index.html">{section_label}</a> · {h1}</p>
      <h1>{h1}</h1>
      <p>{lead}</p>
    </div>
  </section>
  <div class="inner page-wrap">
    <div data-layout="side"></div>
    <article class="page-content">
      <h2>{h2}</h2>
      <p>{seo_line}</p>
      {paras}
      <ul>
        {bullets}
      </ul>
      <nav class="related-keywords" aria-label="관련 키워드">
        <h3>함께 찾는 키워드</h3>
        {related}
      </nav>
      <div class="page-cta">
        <p>카리셋 전국 24시간 상담 010-4393-2414. 지금 상황을 말씀해 주시면 필요한 절차부터 안내드립니다.</p>
        <div class="inquiry-actions">
          <a class="btn-solid" href="tel:01043932414">전화 상담하기</a>
          <a class="btn-kakao" href="{kakao}" target="_blank" rel="noopener noreferrer">카톡 상담하기</a>
          <a class="btn-ghost" href="../index.html#inquiry">온라인 접수</a>
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

LABELS = {"keepsake": "유품정리", "cleaning": "특수청소", "vehicle": "사망자차량"}
SECTION_IMAGE = {
    "keepsake": "schema-keepsake.jpg",
    "cleaning": "schema-cleaning.jpg",
    "vehicle": "schema-vehicle.jpg",
}

RELATED_DEFAULT = [
    ("자살차량 특수청소", "vehicle/suicide.html"),
    ("고독사 차량 특수청소", "vehicle/lonely.html"),
    ("번개탄 차량 탈취", "vehicle/charcoal.html"),
    ("상속차량 보관", "vehicle/storage.html"),
    ("고인명의 폐차 말소", "vehicle/scrap.html"),
    ("유품정리", "keepsake/index.html"),
    ("고독사 특수청소", "cleaning/lonely.html"),
    ("특수청소", "cleaning/index.html"),
    ("차량 작업후기", "reviews/index.html"),
]

RELATED_BY_PAGE = {
    "vehicle/suicide.html": [
        ("자살차량청소", "vehicle/suicide.html"),
        ("자살차량 견인", "vehicle/tow.html"),
        ("차량 악취제거", "vehicle/odor.html"),
        ("고독사 차량 특수청소", "vehicle/lonely.html"),
        ("상속차량 보관", "vehicle/storage.html"),
        ("고인명의 폐차 말소", "vehicle/scrap.html"),
        ("유품정리", "keepsake/index.html"),
        ("차량 작업후기", "reviews/index.html"),
    ],
    "vehicle/lonely.html": [
        ("고독사 차량", "vehicle/lonely.html"),
        ("자살차량 특수청소", "vehicle/suicide.html"),
        ("차량 악취제거", "vehicle/odor.html"),
        ("고독사 특수청소", "cleaning/lonely.html"),
        ("고독사 유품정리", "keepsake/lonely.html"),
        ("상속차량 보관", "vehicle/storage.html"),
        ("차량 작업후기", "reviews/index.html"),
    ],
    "vehicle/charcoal.html": [
        ("번개탄 탈취", "vehicle/charcoal.html"),
        ("차량 악취제거", "vehicle/odor.html"),
        ("차량 실내 복원", "vehicle/restore.html"),
        ("자살차량 특수청소", "vehicle/suicide.html"),
        ("차량 작업후기", "reviews/index.html"),
    ],
    "keepsake/index.html": [
        ("고인유품정리", "keepsake/deceased.html"),
        ("고독사 유품정리", "keepsake/lonely.html"),
        ("요양병원입소 집정리", "keepsake/hospital.html"),
        ("고독사 특수청소", "cleaning/lonely.html"),
        ("자살차량 특수청소", "vehicle/suicide.html"),
    ],
    "cleaning/index.html": [
        ("고독사 특수청소", "cleaning/lonely.html"),
        ("고독사청소", "cleaning/lonely.html"),
        ("쓰레기집 청소", "cleaning/hoarding.html"),
        ("극단적 선택 특수청소", "cleaning/suicide.html"),
        ("유품정리", "keepsake/index.html"),
        ("자살차량 특수청소", "vehicle/suicide.html"),
    ],
}

SEO = {
    "keepsake/index.html": {
        "h1": "유품정리",
        "seo_title": "유품정리 · 고인유품정리 · 고독사 유품정리 | 카리셋 특수",
        "seo_desc": "카리셋 유품정리. 고인유품정리, 고독사 유품정리, 요양병원입소 집정리, 유품 보관과 인수인계를 전국 상담합니다. 010-4393-2414",
        "keywords": "유품정리, 고인유품정리, 고독사 유품정리, 카리셋, 집정리",
        "seo_line": "카리셋 유품정리는 고인유품정리, 고독사 유품정리, 무연고 유품, 요양병원입소 집정리를 유가족 요청 범위에 맞춰 진행합니다.",
        "og_image": "schema-keepsake.jpg",
    },
    "keepsake/understanding.html": {
        "keywords": "유품정리의 이해, 유품정리, 고인유품정리, 카리셋",
        "seo_line": "유품정리는 청소와 다릅니다. 카리셋은 남길 유품과 정리 범위를 유가족과 먼저 정한 뒤 고인유품정리와 특수청소가 필요한 공간을 구분합니다.",
    },
    "keepsake/deceased.html": {
        "h1": "고인유품정리",
        "seo_title": "고인유품정리 | 카리셋 특수",
        "seo_desc": "카리셋 고인유품정리. 유가족 의뢰에 맞춰 고인 유품을 분류하고 정리합니다. 전국 상담 010-4393-2414",
        "keywords": "고인유품정리, 유품정리, 카리셋",
        "seo_line": "카리셋 고인유품정리는 남길 유품과 정리할 물건을 구분해, 유가족이 보시기에 부담스러운 공간을 대신 정리합니다.",
    },
    "keepsake/lonely.html": {
        "h1": "고독사 유품정리",
        "seo_title": "고독사 유품정리 | 카리셋 특수",
        "seo_desc": "카리셋 고독사 유품정리. 발견이 늦어진 현장의 유품 분류와 특수청소를 함께 진행합니다. 010-4393-2414",
        "keywords": "고독사 유품정리, 고독사청소, 유품정리, 카리셋",
        "seo_line": "카리셋 고독사 유품정리는 오염 유품과 보관 유품을 나눈 뒤, 필요하면 고독사 특수청소와 고독사 차량 특수청소까지 연계합니다.",
    },
    "keepsake/unclaimed.html": {
        "keywords": "무연고 유품정리, 유품정리, 카리셋",
        "seo_line": "카리셋 무연고 유품정리는 신분증·서류·사진·귀중품을 먼저 구분해 보관하고, 인수 주체가 정해지면 인계합니다.",
    },
    "keepsake/hospital.html": {
        "keywords": "요양병원입소 집정리, 집정리, 유품정리, 카리셋",
        "seo_line": "카리셋 요양병원입소 집정리는 가져갈 물건, 보관할 물건, 정리할 물건을 나눠 입소 준비를 돕습니다.",
    },
    "keepsake/storage.html": {
        "keywords": "유품 보관, 유품정리, 카리셋",
        "seo_line": "카리셋 유품 보관은 상속이나 가족 협의가 끝날 때까지 바로 결정하기 어려운 물건을 분류해 보관 상담합니다.",
    },
    "keepsake/handover.html": {
        "keywords": "유품 인수인계, 유품정리, 카리셋",
        "seo_line": "카리셋 유품 인수인계는 남겨 드릴 물건과 정리한 범위를 구분해 유가족 또는 지정하신 분께 전달합니다.",
    },
    "cleaning/index.html": {
        "h1": "특수청소",
        "seo_title": "특수청소 · 고독사청소 · 쓰레기집 청소 | 카리셋 특수",
        "seo_desc": "카리셋 특수청소. 고독사 특수청소, 극단적 선택, 변사사건, 쓰레기집 청소, 악취제거, 살균소독을 전국 상담합니다. 010-4393-2414",
        "keywords": "특수청소, 고독사청소, 고독사 특수청소, 쓰레기집 청소, 카리셋",
        "seo_line": "카리셋 특수청소는 고독사 특수청소, 극단적 선택 현장, 변사사건, 강력범죄 현장, 쓰레기집 청소의 오염 제거와 살균·탈취를 진행합니다.",
        "og_image": "schema-cleaning.jpg",
    },
    "cleaning/lonely.html": {
        "h1": "고독사 특수청소",
        "seo_title": "고독사 특수청소 · 고독사청소 | 카리셋 특수",
        "seo_desc": "카리셋 고독사 특수청소. 발견이 늦어진 현장의 오염 제거, 악취제거, 살균소독을 진행합니다. 010-4393-2414",
        "keywords": "고독사 특수청소, 고독사청소, 특수청소, 카리셋",
        "seo_line": "카리셋 고독사 특수청소는 바닥·벽·가구에 스며든 오염과 악취를 제거하고, 고독사 유품정리와 고독사 차량 특수청소가 필요하면 함께 안내합니다.",
    },
    "cleaning/suicide.html": {
        "h1": "극단적 선택 특수청소",
        "seo_title": "극단적 선택 특수청소 · 자살현장 청소 | 카리셋 특수",
        "seo_desc": "카리셋 극단적 선택 특수청소. 주거와 차량 오염 제거, 악취탈취를 전국 24시간 상담합니다. 010-4393-2414",
        "keywords": "극단적 선택 특수청소, 자살현장 청소, 특수청소, 카리셋",
        "seo_line": "카리셋은 극단적 선택 특수청소와 자살차량 특수청소를 구분해, 유가족이 보시지 않아도 되는 처리를 대신합니다.",
    },
    "cleaning/unattended.html": {
        "h1": "변사사건 특수청소",
        "keywords": "변사사건 특수청소, 변사 현장 청소, 특수청소, 카리셋",
        "seo_line": "카리셋 변사사건 특수청소는 관계 기관 확인 이후 오염 제거, 살균, 탈취, 원상회복 범위를 안내합니다.",
    },
    "cleaning/crime.html": {
        "h1": "강력범죄 현장 특수청소",
        "keywords": "강력범죄 현장 특수청소, 특수청소, 카리셋",
        "seo_line": "카리셋 강력범죄 현장 특수청소는 혈흔·체액 등 특수 오염 제거와 살균 소독, 악취제거를 진행합니다.",
    },
    "cleaning/hoarding.html": {
        "h1": "쓰레기집 청소",
        "seo_title": "쓰레기집 청소 | 카리셋 특수",
        "seo_desc": "카리셋 쓰레기집 청소. 적치물 반출, 악취·해충 처리, 살균소독까지 진행합니다. 010-4393-2414",
        "keywords": "쓰레기집 청소, 쓰레기집, 특수청소, 카리셋",
        "seo_line": "카리셋 쓰레기집 청소는 폐기물 반출만으로 끝내지 않고 바닥·벽면·배수·해충·악취까지 처리해 공간이 다시 쓰일 수 있게 합니다.",
    },
    "cleaning/odor.html": {
        "h1": "악취제거 · 오염제거",
        "keywords": "악취제거, 오염제거, 특수청소, 카리셋",
        "seo_line": "카리셋 악취제거는 방향제로 가리지 않고, 자재 안쪽까지 밴 오염원을 제거한 뒤 오존 탈취와 약품 처리를 진행합니다.",
    },
    "cleaning/disinfect.html": {
        "h1": "살균 소독",
        "keywords": "살균 소독, 특수청소, 카리셋",
        "seo_line": "카리셋 살균 소독은 오염물 제거 다음 단계로, 주거 현장과 차량 실내에 맞는 방식으로 진행합니다.",
    },
    "cleaning/restore.html": {
        "keywords": "비전문업체 피해 복원, 특수청소, 카리셋",
        "seo_line": "카리셋은 표면만 닦고 끝난 현장, 냄새가 재발한 현장을 다시 진단하고 남은 오염과 악취를 원인부터 처리합니다.",
    },
    "cleaning/dispute.html": {
        "keywords": "유가족 임대인 분쟁, 고독사 특수청소, 카리셋",
        "seo_line": "고독사·변사 현장의 비용과 원상회복 범위를 둘러싼 갈등을 줄이도록, 카리셋은 현장 상태와 작업 범위를 확인해 안내합니다.",
    },
    "vehicle/index.html": {
        "h1": "사망자차량 특수청소",
        "seo_title": "사망자차량 특수청소 · 자살차량 · 상속차량 보관 | 카리셋 특수",
        "seo_desc": "카리셋 사망자차량 처리. 자살차량 특수청소, 고독사 차량, 번개탄 탈취, 상속차량 보관, 폐차 말소를 전국 24시간 상담합니다. 010-4393-2414",
        "keywords": "사망자차량, 자살차량 특수청소, 상속차량 보관, 고인명의 폐차, 카리셋",
        "seo_line": "카리셋 사망자차량 서비스는 자살차량 특수청소, 고독사 차량 특수청소, 견인, 상속차량 보관, 고인명의 폐차 말소를 한 흐름으로 진행합니다.",
        "og_image": "schema-vehicle.jpg",
    },
    "vehicle/suicide.html": {
        "h1": "카리셋 자살차량 특수청소",
        "seo_title": "카리셋 자살차량 특수청소 · 견인 · 악취제거",
        "seo_desc": "카리셋 자살차량 특수청소. 현장 출동, 견인, 오염제거, 악취탈취, 보관, 폐차말소까지 전국 24시간 상담합니다. 010-4393-2414",
        "keywords": "자살차량 특수청소, 자살차량청소, 자살차량 견인, 차량 특수청소, 카리셋",
        "seo_line": "카리셋 자살차량 특수청소(자살차량청소)는 일반 세차로 해결되지 않는 내부 오염을 제거하고, 자살차량 견인부터 보관·폐차 말소까지 이어서 안내합니다.",
        "og_image": "service-01.jpg",
    },
    "vehicle/lonely.html": {
        "h1": "고독사 차량 특수청소",
        "seo_title": "고독사 차량 특수청소 · 악취제거 | 카리셋 특수",
        "seo_desc": "카리셋 고독사 차량 특수청소. 발견이 늦어진 차량의 오염 제거와 악취탈취, 보관·폐차를 상담합니다. 010-4393-2414",
        "keywords": "고독사 차량, 고독사 차량 특수청소, 차량 악취제거, 카리셋",
        "seo_line": "카리셋 고독사 차량 특수청소는 시트와 내장재 깊숙이 밴 오염·악취를 제거하고, 복원 또는 폐차 방향을 함께 상담합니다.",
        "og_image": "service-02.jpg",
    },
    "vehicle/charcoal.html": {
        "h1": "번개탄 차량 탈취",
        "seo_title": "번개탄 차량 탈취 · 냄새제거 | 카리셋 특수",
        "seo_desc": "카리셋 번개탄 차량 탈취. 그을음과 악취, 공조라인 오염을 제거하고 실내 탈취를 진행합니다. 010-4393-2414",
        "keywords": "번개탄 차량, 번개탄 탈취, 차량 냄새제거, 카리셋",
        "seo_line": "카리셋 번개탄 차량 탈취는 천장·송풍구·시트에 남은 그을음과 냄새를 공조라인 세척과 연무 탈취로 처리합니다.",
        "og_image": "service-03.jpg",
    },
    "vehicle/storage.html": {
        "h1": "상속차량 보관",
        "seo_title": "상속차량 보관 · 고인명의 자동차 보관 | 카리셋 특수",
        "seo_desc": "카리셋 상속차량 보관. 한정승인·상속포기 결정 전 고인 명의 차량을 안전하게 보관합니다. 010-4393-2414",
        "keywords": "상속차량 보관, 상속자동차 보관, 고인명의 차량 보관, 카리셋",
        "seo_line": "카리셋 상속차량 보관은 단순승인·한정승인·상속포기 결정 전, 고인 명의 자동차를 이동·보관한 뒤 폐차 말소 방향을 안내합니다.",
        "og_image": "service-06.jpg",
    },
    "vehicle/scrap.html": {
        "h1": "고인명의 폐차 말소",
        "seo_title": "고인명의 폐차 말소 · 사망자 차량 폐차 | 카리셋 특수",
        "seo_desc": "카리셋 고인명의 폐차 말소 대행. 폐차 거부 차량, 서류·저당 확인부터 말소 등록까지 상담합니다. 010-4393-2414",
        "keywords": "고인명의 폐차, 사망자 차량 폐차, 말소 대행, 카리셋",
        "seo_line": "카리셋 고인명의 폐차 말소는 오염으로 폐차가 거부된 차량도 이동·특수청소 후 말소 절차를 안내합니다.",
        "og_image": "service-07.jpg",
    },
    "vehicle/tow.html": {
        "h1": "자살차량 견인",
        "seo_title": "자살차량 견인 · 사망자차량 이동 | 카리셋 특수",
        "seo_desc": "카리셋 전국 자살차량 견인·이동. 일반 견인이 어려운 오염 차량도 출동해 보관·특수청소 장소로 옮깁니다. 010-4393-2414",
        "keywords": "자살차량 견인, 사망자차량 견인, 차량 이동, 카리셋",
        "seo_line": "카리셋 자살차량 견인은 고독사 차량 등 일반 견인이 거부되는 차량을 안전하게 이동한 뒤 특수청소와 보관을 이어갑니다.",
        "og_image": "service-05.jpg",
    },
    "vehicle/odor.html": {
        "h1": "차량 악취제거",
        "seo_title": "차량 악취제거 · 특수 오염 제거 | 카리셋 특수",
        "seo_desc": "카리셋 차량 악취제거. 시트·내장재·공조까지 스며든 냄새와 오염의 원인을 제거합니다. 010-4393-2414",
        "keywords": "차량 악취제거, 차량 냄새제거, 차량 특수청소, 카리셋",
        "seo_line": "카리셋 차량 악취제거는 자살차량·고독사 차량·번개탄 차량처럼 일반 세차로 없어지지 않는 냄새를 원인부터 처리합니다.",
        "og_image": "service-04.jpg",
    },
    "vehicle/restore.html": {
        "h1": "차량 실내 복원",
        "keywords": "차량 실내 복원, 차량 특수청소, 카리셋",
        "seo_line": "카리셋 차량 실내 복원은 세척으로 가능한 범위와 시트·천장재 교체가 필요한 범위를 구분해 제안합니다.",
        "og_image": "service-09.jpg",
    },
    "vehicle/export.html": {
        "keywords": "고인차량 수출, 고인명의 폐차, 카리셋",
        "seo_line": "카리셋은 고인차량 수출이 가능한 경우와 폐차가 맞는 경우를 차량 상태·서류 조건에 따라 구분해 안내합니다.",
    },
    "vehicle/finance.html": {
        "keywords": "금융 저당 상담, 고인명의 폐차, 상속차량 보관, 카리셋",
        "seo_line": "할부·리스·저당이 남은 고인 명의 차량은 특수청소나 폐차만으로 끝나지 않습니다. 카리셋은 필요한 확인 사항과 순서를 안내합니다.",
    },
    "vehicle/inherit.html": {
        "keywords": "유산 상속 상담, 상속차량 보관, 카리셋",
        "seo_line": "카리셋 유산·상속 상담은 법률 판단을 대신하지 않고, 단순승인·한정승인·상속포기 전 차량을 안전하게 보관하는 방법을 설명합니다.",
    },
    "vehicle/partner.html": {
        "keywords": "기업제휴, 자살차량 특수청소, 사망자차량, 카리셋",
        "seo_line": "카리셋은 금융·보험·법무·청소 현장에서 필요한 사망자차량 견인, 특수청소, 보관, 폐차 말소 업무 범위를 안내합니다.",
    },
}


def related_html(page: str) -> str:
    items = RELATED_BY_PAGE.get(page, RELATED_DEFAULT)
    links = [
        f'<a href="../{href}">{label}</a>'
        for label, href in items
        if href != page
    ]
    return "\n        ".join(links)


def seo_for(item: dict) -> dict:
    extra = SEO.get(item["page"], {})
    title = item["title"]
    lead = item["lead"]
    return {
        "h1": extra.get("h1", title),
        "seo_title": extra.get("seo_title", f"{title} | 카리셋 특수"),
        "seo_desc": extra.get(
            "seo_desc",
            f"카리셋 {title}. {lead} 전국 24시간 상담 010-4393-2414.",
        ),
        "keywords": extra.get("keywords", f"{title}, 카리셋"),
        "seo_line": extra.get(
            "seo_line",
            f"카리셋 {title} 안내입니다. 전국 24시간 상담 010-4393-2414.",
        ),
        "og_image": extra.get("og_image", SECTION_IMAGE[item["section"]]),
    }


def json_ld(item: dict, seo: dict) -> str:
    import json

    section = item["section"]
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "name": seo["h1"],
                "provider": {
                    "@type": "LocalBusiness",
                    "name": "카리셋 CARRESET",
                    "telephone": "+82-10-4393-2414",
                    "url": "https://www.special.carreset.kr/",
                },
                "areaServed": "KR",
                "url": f"https://www.special.carreset.kr/{item['page']}",
                "image": {
                    "@type": "ImageObject",
                    "url": f"https://www.special.carreset.kr/images/{seo['og_image']}",
                    "width": 1280,
                    "height": 720,
                },
                "description": seo["seo_desc"],
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "홈",
                        "item": "https://www.special.carreset.kr/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": LABELS[section],
                        "item": f"https://www.special.carreset.kr/{section}/index.html",
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": seo["h1"],
                        "item": f"https://www.special.carreset.kr/{item['page']}",
                    },
                ],
            },
        ],
    }
    return json.dumps(data, ensure_ascii=False)


def main() -> None:
    for item in PAGES:
        folder = ROOT / item["section"]
        folder.mkdir(exist_ok=True)
        seo = seo_for(item)
        paras = "\n      ".join(f"<p>{p}</p>" for p in item["paras"])
        bullets = "\n        ".join(f"<li>{b}</li>" for b in item["bullets"])
        html = TEMPLATE.format(
            title=item["title"],
            lead=item["lead"],
            section=item["section"],
            page=item["page"],
            section_label=LABELS[item["section"]],
            h1=seo["h1"],
            h2=item["h2"],
            paras=paras,
            bullets=bullets,
            kakao=KAKAO,
            seo_title=seo["seo_title"],
            seo_desc=seo["seo_desc"],
            keywords=seo["keywords"],
            seo_line=seo["seo_line"],
            og_image=seo["og_image"],
            json_ld=json_ld(item, seo),
            related=related_html(item["page"]),
        )
        (folder / item["file"]).write_text(html, encoding="utf-8")
        print("wrote", item["page"])


if __name__ == "__main__":
    main()
