# 2026 Antalya Pledges on AI - Form Collection

Formularz zaangażowania dla COP31 Antalya w trzech formatach: HTML, Gravity Forms i Google Forms.

## 📋 Dostępne formaty

### 1. HTML Form (Darmowy, uniwersalny)
- **Plik:** `cop31_pledges_interactive_form.html`
- **Hosting:** GitHub Pages, Netlify, Vercel (darmowe)
- **Zalety:** Nie wymaga pluginów, działa wszędzie
- **Link do live demo:** Wrzuć ten plik na GitHub Pages

### 2. Gravity Forms (Płatny plugin WordPress)
- **Plik:** `cop31_pledges_gravity_forms.json`
- **Jak używać:**
  1. Zainstaluj Gravity Forms w WordPress
  2. Idź do Forms → Gravity Forms → Import/Export
  3. Wgraj plik JSON
  4. Formularz pojawi się w liście form

### 3. Google Forms
- **Plik:** `create_cop31_google_form.gs`
- **Jak używać:**
  1. Idź do script.google.com
  2. Stwórz nowy Apps Script projekt
  3. Wklej zawartość pliku
  4. Uruchom funkcję `myFunction()`

---

## 🚀 Quick Start - GitHub Pages

### Opcja 1: Użyj tego repo (jeśli sforkowałeś)

```bash
# Wrzuć HTML do repo
cp cop31_pledges_interactive_form.html docs/index.html

# Włącz GitHub Pages w ustawieniach repo:
# Settings → Pages → Source: main branch /docs folder
```

**Link:** `https://username.github.io/repo-name/`

---

## 📱 Funkcje formularza

- ✅ 12 zobowiązań (A1-E3) w 6 sekcjach
- ✅ Dynamiczne pola: liczby, procenty, lata
- ✅ Zapis odpowiedzi jako JSON (pobiera plik)
- ✅ Responsywny design (mobile-friendly)
- ✅ Partner2Connect hyperlink
- ✅ Bez wymogów technicznych

---

## 📝 Zawartość sekcji

| Sekcja | Kod | Liczba zobowiązań |
|--------|-----|------------------|
| Pomiar, przejrzystość, odpowiedzialność | A | 3 |
| Infrastruktura | B | 3 |
| Projektowanie | C | 1 |
| Cyrkulacja i e-waste | D | 2 |
| AI dla akcji klimatycznej | E | 3 |

---

## 🔗 Dodatkowe pliki

- `build_gravity_forms_json.py` - Python script do generacji Gravity Forms JSON
- `build_microsoft_forms_import.py` - Python script do generacji Word (Microsoft Forms Quick Import)
- `build_cop31_interactive_pdf.py` - Python script do generacji interaktywnego PDF

---

## 💾 Format danych

Gdy użytkownik kliknie "Save responses", pobiera plik JSON:

```json
{
  "form": "2026 Antalya Pledges on AI",
  "organization": "My Organization Name",
  "savedAt": "2026-09-14T10:15:00.000Z",
  "responses": {
    "org-name": "My Organization",
    "org-type": "Government",
    "a1-number": 20,
    "a1-date": 2030,
    ...
  }
}
```

---

## ❓ Pytania?

Formularz jest w pełni responsywny i działa bez backendu. Wszystkie dane są przetwarzane lokalnie w przeglądarce.

**Partner2Connect:** https://www.itu.int/partner2connect/
