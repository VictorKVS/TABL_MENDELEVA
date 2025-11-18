
TABL_MENDELEVA/
│
├── app/
│   ├── main.py                 # Точка входа FastAPI
│   ├── config.py               # Настройки проекта (БД, пути)
│   │
│   ├── db/                     # База данных
│   │   ├── database.py         # Подключение SQLite
│   │   ├── models.py           # SQLAlchemy модели
│   │   ├── crud.py             # Функции для работы с БД
│   │   ├── seed.py             # Скрипт заполнения (118 элементов)
│   │   └── migrations/         # (на будущее)
│   │
│   ├── knowledge/              # База знаний (граф)
│   │   ├── graph.py            # API для графа
│   │   ├── relations.py        # Шаблоны связей
│   │   └── loaders/            # загрузчики данных
│   │
│   ├── vector/                 # RAG и эмбеддинги
│   │   ├── embeddings.py       # генерация эмбеддингов
│   │   ├── vector_store.py     # FAISS хранилище
│   │   └── texts/              # описания элементов
│   │
│   ├── api/                    # REST API
│   │   ├── elements.py         # /api/elements
│   │   ├── search.py           # /api/search
│   │   ├── graph.py            # /api/graph
│   │   └── router.py           # главный router
│   │
│   ├── templates/              # HTML-шаблоны (UI)
│   ├── static/                 # CSS, JS, картинки
│   └── utils/                  # вспомогательные функции
│
├── scripts/                    # CLI-скрипты
│   ├── init_db.py              # создать БД + загрузить элементы
│   └── rebuild_vectors.py      # пересоздать эмбеддинги
│
├── tests/                      # тесты
├──  TABL_MENDELEVA.V3.md -    # действующая версия  
│
├── README.md
├── requirements.txt
└── .env
