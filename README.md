# 🎬 Movie API

Projekt REST API oparty na FastAPI do zarządzania informacjami o filmach. Zawiera obsługę bazy danych PostgreSQL, testy jednostkowe oraz konfigurację CI/CD z użyciem GitHub Actions.

## 🔧 Technologie

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pytest](https://docs.pytest.org/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Uvicorn](https://www.uvicorn.org/)

# Movie API Project

## Aktualizacja

Projekt został zaktualizowany do:

- **SQLAlchemy 2.0** — nowy sposób deklaracji modeli i zarządzania bazą
- **Pydantic v2** — zmiany w konfiguracji modeli (np. `ConfigDict` zamiast klasy `Config`)

Dzięki temu kod jest zgodny z najnowszymi wersjami bibliotek i łatwiejszy w utrzymaniu.

---

## Wymagania

- Python 3.11+
- PostgreSQL
- Pozostałe zależności z `requirements.txt`

---

## 📦 Instalacja lokalna

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/ciborowskigrzegorz-bit/movie-api.git
cd movie-api
```

### 2. Utwórz i aktywuj środowisko

```bash
python3.11 -m venv venv
source venv/bin/activate  # macOS/Linux
# lub
venv\Scripts\activate  # Windows
```

### 3. Instalacja zależności

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Uruchomienie aplikacji

Upewnij się, że masz dostęp do działającej bazy PostgreSQL. Następnie:

```bash
uvicorn app.main:app --reload
```

API będzie dostępne pod: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Testy

```bash
pytest
```

Testy znajdują się w katalogu `tests/`.

---

## ⚙️ CI/CD (GitHub Actions)

Projekt zawiera konfigurację workflow (`.github/workflows/python-tests.yml`) uruchamiającą testy automatycznie przy pushu lub pull requeście.

---

## 📁 Struktura projektu

```
movie-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routers.py
│   └── database.py
├── tests/
│   └── test_movies.py
├── requirements.txt
├── .github/
│   └── workflows/
│       └── python-tests.yml
└── README.md
```

---
## 🌍 Demo online

Aplikacja dostępna publicznie na:

🔗 https://movie-api.onrender.com

---

## 📝 TODO / Plany rozwoju

- [ ] Dodanie autoryzacji JWT
- [ ] Filtrowanie i paginacja wyników
- [ ] Obsługa recenzji filmów
- [x] Deployment na Render lub Vercel

---

## 👨‍💻 Autor

Projekt stworzony przez **Grzegorz Ciborowski**  
🔗 GitHub: [ciborowskigrzegorz-bit](https://github.com/ciborowskigrzegorz-bit)

---

## 📄 Licencja

MIT © 2025
