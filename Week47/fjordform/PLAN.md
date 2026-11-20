# 🏋️ Fjordform – plan for økta

Vi bygger et lite medlemssystem for treningssenteret **Fjordform** i Flask og MySQL.
Resepsjonen skal kunne registrere **produkter** (medlemskap), **kunder** og **ansatte**
uten å åpne DataGrip.

Vi har ca. **to timer**. Derfor er SQL-skriptene og hele frontenden (HTML-maler og CSS)
laget på forhånd, så vi kan bruke tiden på Python-koden.

---

## ✅ Ferdig fra start

| Fil | Hva den er |
|-----|------------|
| [`fjordform_setup.sql`](fjordform_setup.sql) | Lager databasen `fjordform` med tabellene `product`, `employee` og `customer` |
| [`seed.sql`](seed.sql) | Valgfrie testdata, i tilfelle vi går tom for tid |
| [`templates/`](templates) | Alle HTML-sidene. Felles oppsett ligger i `base.html`, og de andre sidene bruker `{% extends %}` |
| [`static/css/style.css`](static/css/style.css) | Stylingen for hele appen |

## 🛠️ Det vi koder sammen

| Fil | Innhold |
|-----|---------|
| `models.py` | Klassene `models.py`, `Customer` og `Employee` |
| `database.py` | Alle SQL-spørringene, med `%s`-parametre og `commit()` |
| `app.py` | Rutene: GET for å hente data, POST for å endre data |
| `config_local.py` | Tilkoblingen til databasen. **Skal ikke til GitHub** |
| `config_local.py.example` | Mal for `config_local.py`, uten ekte passord |

---

## ⏱️ Tidsplan

| Del | Innhold | Ca. tid |
|-----|---------|---------|
| Oppsett | Kjør `fjordform_setup.sql` i DataGrip og koble appen til databasen | 10 min |
| Del 1 | Produkter: vis, legg til, endre, slett | 35 min |
| Del 2 | Kunder, med JOIN og nedtrekksliste for produkt | 45 min |
| Del 3 | Ansatte, på egen hånd | 20 min |
| Del 4 | Legg inn data via appen og test | 10 min |

---

## 🧭 Rutene

Alle tre delene følger samme mønster. Slik ser det ut for produkter:

| Rute | Metode | Gjør | Svar |
|------|--------|------|------|
| `/products` | GET | Lister alle produkter | 200 |
| `/product/<id>` | GET | Viser ett produkt i skjemaet | 200, eller 404 hvis det ikke finnes |
| `/product/add` | GET, POST | Viser skjema og lagrer nytt produkt | 303 til listen, 400 ved ugyldig input |
| `/product/<id>/edit` | POST | Endrer et produkt | 303 til listen, 400 ved ugyldig input |
| `/product/<id>/delete` | POST | Sletter et produkt | 303 til listen, 409 hvis det er i bruk |

Kunder bruker `/customers` og `/customer/...`, og ansatte bruker `/employees` og `/employee/...`.

---

## 📋 Steg for steg

### Oppsett
1. Åpne DataGrip og kjør `fjordform_setup.sql`.
2. Sjekk at `SELECT * FROM product;` gir null rader og ingen feil.
3. Kopier `config_local.py.example` til `config_local.py` og fyll inn ditt eget passord.

### Del 1 – Produkter
Bygg og test i denne rekkefølgen: **liste → legg til → vis → endre → slett**.
1. `models.py`: klassen `models.py` med `id`, `name`, `description` og `monthly_price`.
2. `database.py`: `get_products()`, `get_product(id)`, `insert_product(...)`, `update_product(...)` og `delete_product(id)`.
3. `app.py`: de fem rutene. Alle endringer avsluttes med `redirect("/products", code=303)`.
4. Validering i Flask: navn 1–50 tegn, beskrivelse maks 200 tegn, og pris er et tall større enn 0. Ved feil svarer vi `400`.

🧪 **Test:** Legg inn «Testprodukt», endre prisen og slett det. Sjekk i DataGrip etter hvert steg.

### Del 2 – Kunder
Samme mønster som for produkter, men med fire nye ting:
1. **JOIN:** `get_customers()` henter produktnavnet med `JOIN product p ON p.id = c.product_id`.
2. **Nedtrekksliste:** Skjemaet viser produktene fra `get_products()`.
3. **Mer validering:** e-post må inneholde `@`, telefon er valgfri, og en tom telefon lagres som `None`.
4. **Feilhåndtering:** Fang `IntegrityError`.
   - errno `1062`: e-posten finnes fra før, og vi svarer `409`.
   - errno `1451`: produktet er i bruk og kan ikke slettes, og vi svarer `409`.

🧪 **Test:** To kunder med samme e-post skal gi 409. Et produkt som har kunder skal ikke kunne slettes.

### Del 3 – Ansatte (på egen hånd)
- Felter: `first_name`, `last_name`, `role` og `email`.
- `role` må være én av *Resepsjon*, *Personlig trener*, *Gruppeinstruktør* eller *Daglig leder*.
  Lag lista **én gang** i Python, og bruk den både i nedtrekkslista og i valideringen.

### Del 4 – Legg inn data
Bruk bare appen, ikke DataGrip:
1. Tre produkter: Basic, Personlig trener og Gruppetrening.
2. Minst to ansatte.
3. Minst fem kunder, fordelt på produktene.

Kontroller resultatet i DataGrip:

```sql
SELECT p.name, COUNT(*) AS customers
FROM customer c
JOIN product p ON p.id = c.product_id
GROUP BY p.name;
```

---

## ☑️ Sjekkliste

- [ ] Produkter, kunder og ansatte kan vises, legges til, endres og slettes
- [ ] Tomt navn, ugyldig e-post og pris under null gir 400
- [ ] Dobbel e-post (kunde og ansatt) gir 409
- [ ] Et produkt som har kunder kan ikke slettes, og vi får 409 i stedet for en krasj
- [ ] `/customer/9999` gir 404
- [ ] Alle endringer lander på listen via 303
- [ ] Ingen SQL med f-strenger eller `+`, bare `%s`-parametre

---

## 🌿 Git-repetisjon

```bash
git switch -c fjordform          # ny branch
git status                       # hva er endret?
git add Week47/fjordform         # legg til bare det vi vil ha med
git commit -m "Add product routes to Fjordform"
git push -u origin fjordform     # første push av en ny branch
```

Deretter lager vi en **pull request** på GitHub og merger den inn i `main`.

> ⚠️ Sjekk at `config_local.py` **ikke** er med i commiten. `.gitignore` skal stoppe den,
> men det er lurt å se over `git status` før du committer.

---

## 🚀 For dem som blir raske

**Nivå 2**
- Søk i kundelista med `/customers?q=...` og `LIKE`
- Personlig trener på kunden (`trainer_id`, `LEFT JOIN`)
- Meldinger med `flash()`. `base.html` viser dem allerede!

**Nivå 3**
- Statistikkside `/stats` med `GROUP BY` og `SUM`
- Sidedeling av kundelista med `LIMIT` og `OFFSET`

---

## 💭 Refleksjonsspørsmål

1. Hvorfor bruker vi POST og ikke GET for å slette en kunde?
2. Hva skjer i databasen hvis du glemmer `commit()` etter en INSERT?
3. Hvorfor svarer vi med 303 redirect etter lagring, i stedet for å vise siden direkte?
4. Hva er forskjellen på `%s`-parametre og en f-streng? Hva kan skje hvis noen skriver
   `x'; DROP TABLE customer; --` som fornavn?
5. HTML-skjemaet har `required` og `maxlength`. Hvorfor validerer vi likevel i Flask?
6. Hva hindrer `FOREIGN KEY` i å skje, og hvorfor er det bedre at Flask fanger feilen enn at appen krasjer?
