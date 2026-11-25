# 🌍 World Cities – løsningsforslag til økt 12

Alle oppgavene er løst i **ett prosjekt**, fordi hver oppgave bygger på den forrige.
I koden viser kommentarer som `# OPPGAVE 5` hvor hver oppgave er løst.

## 🚀 Kom i gang

1. Kopier `config_local.py.example` til `config_local.py` og fyll inn ditt eget passord.
2. Stopp andre Flask-servere på samme port (Ctrl + C).
3. Stå i denne mappen og kjør `python app.py`.
4. Åpne <http://127.0.0.1:5001/cities>. Vi bruker 5001 fordi AirPlay ofte bruker 5000 på Mac.

Testene trenger ikke database: `python -m unittest`

## 📁 Hvem gjør hva?

| Fil | Ansvar | Oppgaver |
|-----|--------|----------|
| `models.py` | Klassen `City` og reglene for en gyldig by | 2, 5 |
| `database.py` | All SQL | 3, 6, 7, 8, A |
| `app.py` | Rutene: tar imot forespørselen og velger svar | 4–8, A, B |
| `templates/` | HTML-en | 4 |
| `test_models.py` | Små tester av valideringen | 5 |

## 💡 Hvorfor er det løst slik?

### Oppgave 1 – Klargjøring
`.gitignore` i roten har `**/[Cc]onfig_local.py`. `**/` betyr alle mapper, og `[Cc]` dekker både stor
og liten C. Vi ignorerer også `__pycache__/`, fordi Python lager en kompilert kopi av
`config_local.py` der, **med passordet i**.

### Oppgave 2 – City
- `int()` i konstruktøren gjør at folketallet alltid er et tall, også om det kommer inn som tekst.
- `None` er lov som ID, fordi en ny by ikke har noen ID før MySQL har laget den.
- `if __name__ == "__main__":` gjør at testen bare kjører når vi starter `models.py` direkte.

### Oppgave 3 – get_city()
- `fetchone()` passer fordi ID er primærnøkkel: vi får én rad eller `None`.
- Rekkefølgen i `SELECT` må være lik rekkefølgen i konstruktøren. Bytter vi om på navn og distrikt,
  havner verdiene i feil attributt **uten feilmelding**.

### Oppgave 4 – Skjemaet
Én mal brukes til både ny og eksisterende by. `city_id` bestemmer overskrift, hvor skjemaet sendes,
og om ID og sletteknapp vises. Da slipper vi to nesten like filer.

### Oppgave 5 – Validering
Her bruker vi **objektorientering**: reglene for hva som er en gyldig by ligger i `City`, ikke i rutene.
- `@classmethod` (`City.from_form`) fungerer som en ekstra konstruktør. Vi trenger den fordi vi ikke har
  noe objekt ennå – det er nettopp det vi skal lage.
- `@staticmethod` (`City.is_country_code`) er en regel som ikke trenger noe objekt. Bysøket bruker den også.
- Ved feil bruker vi `raise ValueError(...)`, og ruten fanger den og svarer 400. Vi får altså enten en
  gyldig by eller en feil, aldri noe midt imellom.
- Reglene står ett sted og brukes av både `/add` og `/edit`. De kan testes uten Flask og MySQL.

### Oppgave 6 – insert_city()
ID er utelatt fordi MySQL lager den (`AUTO_INCREMENT`). `commit()` lagrer raden permanent.

### Oppgave 7 – update_city()
Fem `%s` og fem verdier i samme rekkefølge. ID står sist, fordi `WHERE` står sist.
Den hentes fra URL-en, så brukeren kan ikke endre den i skjemaet.

### Oppgave 8 – delete_city()
Trenger bare ID. At `City` fikk flere felter, endrer ikke hvordan vi finner raden.

### Ekstraoppgave A – Finnes landet?
`ZZZ` har riktig format, men er ikke et land. `city.CountryCode` er en fremmednøkkel til `country`, så
MySQL ville stoppet lagringen uansett. Ved å sjekke først kan vi svare med en tydelig 400.

### Ekstraoppgave B – 404 eller 503?
`get_city()` gir `None` når byen mangler (404). En databasefeil er et unntak, og fanges av
`@app.errorhandler(Error)` (503). Den gjelder **alle** rutene, så vi slipper `try/except` i hver av dem.
`abort(404)` er ikke en databasefeil, og blir derfor ikke fanget her.

## 🗣️ Stopp og forklar

**Population sin vei (oppgave 4):** MySQL gir en tuple → `get_city()` sender `row[4]` til `City(...)` →
konstruktøren lagrer `self.population` → `show_city()` sender `population=city.population` →
Jinja setter verdien inn i `value="{{ population }}"`.

**Hvorfor må navnene stemme?** Jinja slår opp akkurat de navnene vi sender til `render_template()`.
Skriver vi `pop=` i Python og `{{ population }}` i malen, blir feltet tomt uten feilmelding.

**Hvorfor holder ikke HTML-validering (oppgave 5)?** Den kjører i nettleseren, og kan fjernes med
utviklerverktøyene eller omgås med for eksempel `curl`. HTML hjelper brukeren, Python beskytter dataene.

**Hvor skjer hva (oppgave 8)?** Skjemadata leses i `app.py` (`read_city_form`). `City` opprettes i
`database.py` når byen hentes fra databasen, og i `City.from_form()` når den kommer fra skjemaet.
All SQL kjøres i `database.py`.

**Hvorfor separate verdier til `execute()`?** Da behandles de alltid som data, aldri som SQL. Det hindrer
SQL-injeksjon, og et navn som `O'Brien` ødelegger ikke spørringen.

**Hvorfor `commit()`?** INSERT, UPDATE og DELETE skjer i en transaksjon. Uten `commit()` rulles
endringen tilbake når forbindelsen lukkes. SELECT endrer ingenting.

**Hvorfor POST?** HTML-skjemaer kan bare sende GET og POST, og GET skal aldri endre data. En lenke som
sletter med GET, kan bli åpnet ved et uhell eller av en søkerobot. HTTP-metoden og SQL-kommandoen er to
forskjellige ting.

**Hva gjør 303?** Den ber nettleseren gjøre en ny GET mot `/cities`. Da sender F5 ikke skjemaet på nytt,
og vi får ingen ekstra rad. Mønsteret heter *Post/Redirect/Get*.

**Hvorfor samme ID?** UPDATE endrer en rad som allerede finnes. Bare INSERT lager en ny ID.

## 🔀 Forskjeller fra fasit-PDF-en

| PDF-en | Her | Hvorfor |
|--------|-----|---------|
| Validering i `app.py`, returnerer `(values, error)` | `City.from_form()` og `ValueError` | Reglene hører til klassen |
| `get_cities()` gir tupler | Gir `City`-objekter | Samme mønster som i Fjordform |
| `try/except` bare i `/edit` | Én `errorhandler` | Gjelder alle rutene |
| Ingen øvre grense på folketall | Maks 2147483647 | Større tall får ikke plass i INT |

`get_cities()` er altså endret, selv om oppgave 3 ber om å beholde den. Vi henter alle fem kolonnene
fordi `City` trenger dem, og fordi ID-en gir oss lenker i listen.

## 🧪 Test selv

- [ ] Tomt navn, folketall -1 og landkode `NO` gir 400
- [ ] Landkode `ZZZ` gir 400
- [ ] ` nor ` sendt uten HTML-validering lagres som `NOR`
- [ ] Ny by under SWE vises når du søker etter SWE
- [ ] F5 etter lagring lager ingen ekstra rad
- [ ] Endring beholder ID-en
- [ ] `/city/ID` etter sletting gir 404
- [ ] GET mot `/edit/ID` og `/delete/ID` gir 405
- [ ] Stoppet MySQL gir 503

> ⚠️ Endre og slett bare byer du har lagt inn selv!
