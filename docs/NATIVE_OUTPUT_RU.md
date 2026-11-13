# Captured native Codex response — 2026-11-11

Generated from installed skills and the native Scout MCP connection using three synthetic profiles. Only the local search ID is redacted. The original wording, including the SumUp precedence inconsistency documented in [the review](OUTPUT_QUALITY.md), is retained. This is test output, not personalized advice for the real user.

---

Нативный Scout MCP работает: `get_scout_status`, `get_saved_results` и `refine_shortlist` успешно вызваны для поиска `[LOCAL_SEARCH_ID]`. Получены **10 вакансий**; новые или платные поиски не запускались. Оценки ниже относятся только к синтетическим профилям.

Источник — сохранённые объявления Apify, наблюдавшиеся **11.11.2026 в 15:13 UTC**, с датами публикации 5–11 ноября. Их текущая открытость независимо не проверена.

**product_mid_remote_germany — сначала investigate; безусловного приоритета нет.**

| Решение | Вакансия и доказательства |
|---|---|
| **Investigate** | [Kaufland — Product Analyst, Mobile App](https://www.linkedin.com/jobs/view/4488681762/). SQL/Python и A/B-тесты подтверждены профилем; remote внутри Германии прямо разрешён. Однако требуются 2–3 года продуктовой аналитики приложения и понимание mobile analytics — такой опыт не установлен. Adobe Analytics указан как предпочтение. |
| **Investigate** | [ablefy — Data Analyst, Mid level](https://www.linkedin.com/jobs/view/4480031765/). Четыре года, SQL и Python соответствуют части требований. Data modeling, warehouse, event tracking и AI-инструменты не подтверждены; remote из Германии в тексте не установлен. |
| **Investigate, ниже** | [Pennylane — Senior Product Analyst](https://www.linkedin.com/jobs/view/4444702320/). Есть релевантная продуктовая аналитика, SQL и дашборды; указаны 5–6 лет, dbt и event-based платформы — профиль этого полностью не подтверждает. Remote в Европе зависит от команды и роли, поэтому условия для Германии требуют уточнения. |
| **Deprioritize** | [Voodoo — Senior Game Data Analyst](https://www.linkedin.com/jobs/view/4479537318/): требуются 4+ года именно игровой аналитики, которых профиль не устанавливает. [SumUp — Senior Product Analyst](https://www.linkedin.com/jobs/view/4487169531/): совпадение аналитических задач перевешивает явный конфликт с обязательным remote — работа office-first в Берлине. |

Право работать в Германии без спонсорства **заявлено в синтетическом профиле**.

**gaming_senior_remote — prioritize Voodoo, с уточнением оформления.**

| Решение | Вакансия и доказательства |
|---|---|
| **Prioritize** | [Voodoo — Senior Game Data Analyst, Paper.io 2](https://www.linkedin.com/jobs/view/4479537318/). Требования 4+ лет gaming analytics, SQL, Python/R, A/B-тесты и работа с продуктовой командой прямо поддержаны шестью годами опыта. Монетизация, поведение игроков и дашборды совпадают с задачами. Разрешён full remote в CET ±3 часа; оформление из Германии и спонсорство отдельно не подтверждены. Ежедневное применение AI и создание автоматизаций в профиле не установлены. |
| **Investigate как альтернативу** | [Kaufland — Product Analyst, Mobile App](https://www.linkedin.com/jobs/view/4488681762/). Mobile games, SQL/Python и эксперименты дают переносимый опыт; remote внутри Германии разрешён. Следует уточнить переход в retail-приложение и соответствие уровня роли; это не Game Data Analyst. |
| **Deprioritize** | [SumUp](https://www.linkedin.com/jobs/view/4487169531/) — office-first; [Sonova — Manager Data Analytics](https://www.linkedin.com/jobs/view/4472711447/) — hybrid в Берлине или Stäfa. Оба формата конфликтуют с обязательным remote, а задачи находятся вне игровой аналитики. |

Потребность в спонсорстве и право этого кандидата работать в Германии **неизвестны**.

**junior_reporting — приоритетных Junior Data Analyst в наборе нет.**

| Решение | Вакансия и доказательства |
|---|---|
| **Investigate** | [UX & Usability Analyst — Jobs-im-Allgäu.de](https://www.linkedin.com/jobs/view/4487483431/). Текст называет June Fund GmbH и допускает смену профессии: UX-опыт желателен, но необязателен. Задачи включают отчёты и анализ обратной связи; стажировка даёт частичное соответствие. Это смежная UX-роль: нужно уточнить работодателя, работу в Берлине и визовое спонсорство. |
| **Deprioritize** | [Sonova](https://www.linkedin.com/jobs/view/4472711447/): Excel/Power BI совпадают, но требуются минимум пять лет и SQL. [SumUp](https://www.linkedin.com/jobs/view/4487169531/): нужны продвинутый SQL и самостоятельные эксперименты. [ablefy](https://www.linkedin.com/jobs/view/4480031765/): 3–5 лет, SQL, Python и владение проектами. Эти требования не подтверждены шестимесячной стажировкой. |

Обязательное для junior визовое спонсорство **нигде в сохранённых текстах не подтверждено**; молчание работодателя не означает отказ.

В остальных объявлениях также есть существенные расхождения: [Berliner Verlag](https://www.linkedin.com/jobs/view/4485841162/) требует 3–5 лет Product Owner/Manager и управления agile-командами; [Zalando](https://www.linkedin.com/jobs/view/4486213928/) — 5+ лет, Tableau/Databricks; [Schumacher](https://www.linkedin.com/jobs/view/4461901236/) — SKU-аналитику, статистическое моделирование и запись в Snowflake. Оснований поднять их выше выбранных вариантов нет.

**Результат проверки качества:** фильтр `workplace=remote` вернул 0, исключив все 10 записей с `unknown`, хотя тексты содержат remote-условия. Лексический рейтинг поднял senior-роли для junior из-за Excel/Power BI; итоговая оценка выше исправляет этот порядок по требованиям. Рейтинг — детерминированная эвристика, не вероятность интервью. Числовая зарплата во всех объявлениях отсутствует; соответствие зарплатным ожиданиям неизвестно.