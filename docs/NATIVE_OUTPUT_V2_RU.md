# Native Codex + installed Skills + Scout 0.2 — 2026-11-11

Fresh ephemeral Codex process; 10 completed native MCP calls against the same cached search; no paid search or refresh. Model wording below is preserved. All profiles are synthetic. This capture uses current lexical versus adjusted scores; comparison with v0.1 is in the Scout before/after report.

**Обоснованного `prioritize` нет ни для одного профиля.** Scout v0.2 ранжировал одну сохранённую выборку из 10 вакансий для всех трёх кандидатов с указанными полями. `heuristic_score` — лексическое соответствие; `ranking_score` учитывает ограничения и пробелы в доказательствах. Это не вероятность интервью.

| Синтетический профиль | Лучшие варианты: lexical → ranking | Рекомендация, конфликты и критические неизвестные | Цитаты из кэша |
|---|---|---|---|
| **Product mid**, 4 года, remote DE | [Kaufland — Product Analyst, Mobile App](https://www.linkedin.com/jobs/view/4488681762/): **90 → 84**. [Pennylane — Senior Product Analyst](https://www.linkedin.com/jobs/view/4444702320/): **80 → 58** | **Сначала уточнить (`investigate`).** Kaufland прямо допускает remote из Германии; SQL/Python и эксперименты подтверждены профилем, но опыт мобильной аналитики не подтверждён. Adobe Analytics — предпочтение. У Pennylane нужно уточнить senior scope, dbt/Amplitude и применимость условной удалёнки. | Kaufland: “working remotely (within Germany)”; “2-3 years in Product Analytics, working with an app”; “preferably with Adobe Analytics”. Pennylane: “Depending on the teams and the requirements of the position”. |
| **Gaming senior**, 6 лет, remote DE | [Voodoo — Senior Game Data Analyst](https://www.linkedin.com/jobs/view/4479537318/): **100 → 90**. После remote-фильтра следующий — Kaufland: **44 → 26** | **Сначала уточнить (`investigate`).** У Voodoo прямо совпадают игровой опыт, SQL/Python, A/B testing, монетизация и поведение игроков. Однако возможность найма из DE и необходимость/доступность sponsorship неизвестны. Kaufland дальше от целевой игровой роли. | Voodoo: “4+ years in analytical roles within gaming”; “full remote within CET time ±3h”. **Часовой пояс не подтверждает допустимую страну найма.** |
| **Junior reporting**, 0,5 года, sponsorship нужен | [June Fund — UX & Usability Analyst](https://www.linkedin.com/jobs/view/4487483431/): **20 → 8**. Лексический лидер [Sonova — Manager Data Analytics](https://www.linkedin.com/jobs/view/4472711447/): **60 → 0** | June Fund — только **исследовать**: UX отличается от Junior Data Analyst, sponsorship неизвестен; Excel/Power BI не доказывают UX-компетенции. Sonova — **понизить приоритет (`deprioritize`)**: обязательные 5 лет против 0,5; SQL не подтверждён. В целом подходящего приоритета нет. | June Fund: “Berufserfahrung im UX-Bereich ist von Vorteil, aber nicht zwingend erforderlich.” Sonova: “At least 5 years of experience”; “Hands-on experience with Power BI, SQL and Excel”. |

Канонические навыки, возвращённые Scout:

- **Product:** `SQL`, `Python`, `A/B testing`, `dashboards`.
- **Gaming:** `SQL`, `Python`, `A/B testing`, `monetization`, `player behavior`.
- **Junior:** `Excel`, `Power BI`.

Локальный `refine_shortlist(workplace="remote")` оставил **4 из 10** вакансий для каждого удалённого профиля. Неизвестный формат исключается фильтром, но это не доказательство отсутствия удалёнки. Показательный конфликт: [SumUp — Senior Product Analyst](https://www.linkedin.com/jobs/view/4487169531/) у product-профиля получил **90 → 0**, поскольку текст прямо говорит “office-first setup”.

**Работодатель и публикатор разделены:** для June Fund поле `employer` — **June Fund GmbH**, а `publisher` и исходное `source_company` — **Jobs-im-Allgäu.de**. Основание — “June Fund GmbH – Mehrere Mitarbeiter gesucht!”; это утверждение описания, идентичность не проверена. Фильтр работодателя June Fund вернул **1** запись, по имени публикатора — **0**.

Ручная проверка выявляет ограничения автоматического разбора: альтернативы вроде “Snowflake, Postgres, or Redshift” нельзя превращать в требование владеть всеми системами. Sonova прямо называет роль **individual contributor**, поэтому слово Manager не доказывает управление людьми. Верхняя граница опыта не является максимумом; отсутствие навыка кандидата в тексте вакансии не означает дефицит кандидата.

Источник — сохранённые наблюдения Apify от **11.11.2026, 15:13 UTC**; даты публикаций в кэше — 5–11 ноября. Актуальность открытых позиций не проверялась. Зарплата не указана; порог кандидатов неизвестен. Новых поисков, refresh, браузинга и обращений к Notion не было.