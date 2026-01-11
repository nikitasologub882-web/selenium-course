# locators.py
# XPath локаторы для страницы https://hyperskill.org/courses

# ========================
# HEADER элементы
# ========================

# Логотип Hyperskill в хедере
LOGO = ("xpath", "//header//a[@href='/']")

# Кнопка "Catalog" в навигации
CATALOG_BUTTON = ("xpath", "//a[contains(text(), 'Catalog')]")

# Кнопка "Pricing" в навигации
PRICING_BUTTON = ("xpath", "//a[contains(text(), 'Pricing')]")

# Кнопка "For Business" в навигации
FOR_BUSINESS_BUTTON = ("xpath", "//a[contains(text(), 'For Business')]")

# Кнопка "Sign in" в хедере
SIGN_IN_BUTTON = ("xpath", "//button[contains(text(), 'Sign in')]")

# Кнопка "Start for free" в хедере
START_FOR_FREE_BUTTON = ("xpath", "//button[contains(text(), 'Start for free')]")

# Кнопка меню (гамбургер) для мобильной версии
MENU_BUTTON = ("xpath", "//button[contains(@class, 'nav-link')]//*[contains(@data-component-name, 'ph-list')]")

# ========================
# BODY - Основные элементы
# ========================

# Главный заголовок "What do you want to learn today?"
MAIN_TITLE = ("xpath", "//h1[contains(text(), 'What do you want to learn today?')]")

# Подзаголовок под главным заголовком
SUB_TITLE = ("xpath", "//p[contains(text(), 'Select a course that fits your interests')]")

# ========================
# Категории курсов (фильтры)
# ========================

# Кнопка "Most popular" (активная категория)
MOST_POPULAR_CATEGORY = ("xpath", "//a[contains(@class, 'active') and contains(text(), 'Most popular')]")

# Кнопка "All courses"
ALL_COURSES_CATEGORY = ("xpath", "//a[contains(text(), 'All courses')]")

# Кнопка "Python"
PYTHON_CATEGORY = ("xpath", "//a[contains(text(), 'Python')]")

# Кнопка "Java"
JAVA_CATEGORY = ("xpath", "//a[contains(text(), 'Java')]")

# Кнопка "Kotlin & Android"
KOTLIN_CATEGORY = ("xpath", "//a[contains(text(), 'Kotlin & Android')]")

# Кнопка "AI Coding Tools"
AI_CODING_TOOLS_CATEGORY = ("xpath", "//a[contains(text(), 'AI Coding Tools')]")

# Кнопка "✨ AI Engineering"
AI_ENGINEERING_CATEGORY = ("xpath", "//a[contains(text(), '✨ AI Engineering')]")

# Кнопка "Web Dev"
WEB_DEV_CATEGORY = ("xpath", "//a[contains(text(), 'Web Dev')]")

# Кнопка "Backend"
BACKEND_CATEGORY = ("xpath", "//a[contains(text(), 'Backend')]")

# Кнопка "DevOps"
DEVOPS_CATEGORY = ("xpath", "//a[contains(text(), 'DevOps')]")

# Кнопка "Data Science & Analysis"
DATA_SCIENCE_CATEGORY = ("xpath", "//a[contains(text(), 'Data Science & Analysis')]")

# Кнопка "ML & Math"
ML_MATH_CATEGORY = ("xpath", "//a[contains(text(), 'ML & Math')]")

# Кнопка "SQL and Databases"
SQL_DATABASES_CATEGORY = ("xpath", "//a[contains(text(), 'SQL and Databases')]")

# Кнопка "Go & C++"
GO_CPP_CATEGORY = ("xpath", "//a[contains(text(), 'Go & C++')]")

# ========================
# Карточки курсов
# ========================

# Первая карточка курса "Python Developer"
FIRST_COURSE_CARD = ("xpath", "(//div[contains(@class, 'track-card')])[1]")

# Заголовок первой карточки курса
FIRST_COURSE_TITLE = ("xpath", "(//h5[contains(@class, 'leading-tight')])[1]")

# Бейдж "Certificate" на первой карточке
FIRST_COURSE_CERTIFICATE_BADGE = ("xpath", "(//span[contains(@class, 'badge-warning')])[1]")

# Рейтинг первой карточки курса
FIRST_COURSE_RATING = ("xpath", "(//div[contains(@class, 'text-xl')])[1]")

# Количество проектов в первой карточке
FIRST_COURSE_PROJECTS_COUNT = ("xpath", "(//span[contains(@class, 'track-statistics')]//span[contains(text(), 'projects')])[1]")

# Количество часов в первой карточке
FIRST_COURSE_HOURS_COUNT = ("xpath", "(//span[contains(@class, 'track-statistics')]//span[contains(text(), 'hours')])[1]")

# Описание первой карточки курса
FIRST_COURSE_DESCRIPTION = ("xpath", "(//span[contains(@class, 'track-description')])[1]")

# Логотип JetBrains Academy в первой карточке
FIRST_COURSE_PROVIDER_LOGO = ("xpath", "(//img[@alt='JetBrains Academy'])[1]")

# Текст "already learning" в первой карточке
FIRST_COURSE_LEARNING_COUNT = ("xpath", "(//div[contains(text(), 'already learning')])[1]")

# Все карточки курсов
ALL_COURSE_CARDS = ("xpath", "//div[contains(@class, 'track-card')]")

# ========================
# Вторая карточка курса "Introduction to Java"
# ========================

SECOND_COURSE_CARD = ("xpath", "(//div[contains(@class, 'track-card')])[2]")
SECOND_COURSE_TITLE = ("xpath", "(//h5[contains(@class, 'leading-tight')])[2]")
SECOND_COURSE_RATING = ("xpath", "(//div[contains(@class, 'text-xl')])[2]")

# ========================
# Третья карточка курса "Python Fundamentals with Practical Projects"
# ========================

THIRD_COURSE_CARD = ("xpath", "(//div[contains(@class, 'track-card')])[3]")
THIRD_COURSE_TITLE = ("xpath", "(//h5[contains(@class, 'leading-tight')])[3]")

# ========================
# FOOTER элементы
# ========================

# Раздел "Languages" в футере
FOOTER_LANGUAGES_SECTION = ("xpath", "//footer//span[contains(text(), 'Languages')]")

# Ссылка "Python" в футере
FOOTER_PYTHON_LINK = ("xpath", "//footer//a[contains(text(), 'Python')]")

# Ссылка "Java" в футере
FOOTER_JAVA_LINK = ("xpath", "//footer//a[contains(text(), 'Java')]")

# Раздел "Career paths" в футере
FOOTER_CAREER_PATHS_SECTION = ("xpath", "//footer//span[contains(text(), 'Career paths')]")

# Ссылка "Web Dev" в футере
FOOTER_WEB_DEV_LINK = ("xpath", "//footer//a[contains(text(), 'Web Dev')]")

# Раздел "Resources" в футере
FOOTER_RESOURCES_SECTION = ("xpath", "//footer//div[contains(text(), 'Resources')]")

# Ссылка "Blog" в футере
FOOTER_BLOG_LINK = ("xpath", "//footer//a[contains(text(), 'Blog')]")

# Ссылка "University" в футере
FOOTER_UNIVERSITY_LINK = ("xpath", "//footer//a[contains(text(), 'University')]")

# Ссылка "Guide" в футере
FOOTER_GUIDE_LINK = ("xpath", "//footer//a[contains(text(), 'Guide')]")

# Раздел "Subscription" в футере
FOOTER_SUBSCRIPTION_SECTION = ("xpath", "//footer//div[contains(text(), 'Subscription')]")

# Ссылка "For Business" в футере
FOOTER_FOR_BUSINESS_LINK = ("xpath", "//footer//a[contains(text(), 'For Business')]")

# Ссылка "Pricing" в футере
FOOTER_PRICING_LINK = ("xpath", "//footer//a[contains(text(), 'Pricing')]")

# Раздел "Hyperskill" в футере
FOOTER_HYPERSKILL_SECTION = ("xpath", "//footer//div[contains(text(), 'Hyperskill')]")

# Ссылка "About" в футере
FOOTER_ABOUT_LINK = ("xpath", "//footer//a[contains(text(), 'About')]")

# Раздел "Support" в футере
FOOTER_SUPPORT_SECTION = ("xpath", "//footer//div[contains(text(), 'Support')]")

# Ссылка "Help Center" в футере
FOOTER_HELP_CENTER_LINK = ("xpath", "//footer//a[contains(text(), 'Help Center')]")

# Ссылка "Terms" в футере
FOOTER_TERMS_LINK = ("xpath", "//footer//a[contains(text(), 'Terms')]")

# Кнопка "Full catalog" в футере
FOOTER_FULL_CATALOG_BUTTON = ("xpath", "//footer//a[contains(text(), 'Full catalog')]")

# Логотип Google Play в футере
FOOTER_GOOGLE_PLAY = ("xpath", "//footer//img[contains(@alt, 'Google Play')]")

# Логотип App Store в футере
FOOTER_APP_STORE = ("xpath", "//footer//img[contains(@alt, 'App Store')]")

# Иконка Reddit в соцсетях
SOCIAL_REDDIT = ("xpath", "//footer//a[@title='Hyperskill on Reddit']")

# Иконка Facebook в соцсетях
SOCIAL_FACEBOOK = ("xpath", "//footer//a[@title='Hyperskill on Facebook']")

# Иконка LinkedIn в соцсетях
SOCIAL_LINKEDIN = ("xpath", "//footer//a[@title='Hyperskill on Linkedin']")

# Иконка Discord в соцсетях
SOCIAL_DISCORD = ("xpath", "//footer//a[@title='Hyperskill on Discord']")

# Иконка Instagram в соцсетях
SOCIAL_INSTAGRAM = ("xpath", "//footer//a[@title='Hyperskill on Instagram']")

# Иконка TikTok в соцсетях
SOCIAL_TIKTOK = ("xpath", "//footer//a[@title='Hyperskill on TikTok']")

# Иконка YouTube в соцсетях
SOCIAL_YOUTUBE = ("xpath", "//footer//a[@title='Hyperskill on YouTube']")

# ========================
# Дополнительные элементы
# ========================

# Количество проектов в бейджах (например, "6" в "Most popular")
CATEGORY_BADGE_COUNT = ("xpath", "(//span[contains(@class, 'badge-count')])[1]")

# Ссылка на полный курс Python Developer
PYTHON_DEVELOPER_LINK = ("xpath", "//a[contains(@href, '/courses/2-python-developer')]")

# Ссылка на курс Introduction to Java
JAVA_INTRODUCTION_LINK = ("xpath", "//a[contains(@href, '/courses/8-introduction-to-java')]")

# Ссылка на курс Python Fundamentals
PYTHON_FUNDAMENTALS_LINK = ("xpath", "//a[contains(@href, '/courses/6-introduction-to-python')]")

# Ссылка на курс Kotlin Core
KOTLIN_CORE_LINK = ("xpath", "//a[contains(@href, '/courses/18-kotlin-core')]")

# Ссылка на курс Java Backend Developer
JAVA_BACKEND_LINK = ("xpath", "//a[contains(@href, '/courses/12-java-backend-developer-spring-boot')]")

# Ссылка на курс Introduction to Frontend
FRONTEND_INTRODUCTION_LINK = ("xpath", "//a[contains(@href, '/courses/125-introduction-to-frontend')]")

# ========================
# Мета-элементы
# ========================

# Meta description страницы
META_DESCRIPTION = ("xpath", "//meta[@name='description']")

# Meta title страницы
META_TITLE = ("xpath", "//title")

# Schema.org структурированные данные
SCHEMA_DATA = ("xpath", "//script[@type='application/ld+json']")