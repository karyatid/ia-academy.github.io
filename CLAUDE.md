# IA Academy — CLAUDE.md

## Vue d'ensemble du projet

Dépôt GitHub Pages (`karyatid/ia-academy.github.io`) contenant deux composants :

1. **Site vitrine** (racine) — Page marketing statique en français ciblant TPE/PME, freelances et particuliers
2. **Formation** (`formation/`) — Formation complète sur l'IA, 8 modules, fichiers HTML organisés par module

## Architecture

```
/                           ← Site vitrine (point d'entrée GitHub Pages)
├── index.html              ← Page d'accueil du site vitrine
├── programme.html
├── a-propos.html
├── blog.html
├── article.html
├── contact.html
├── assets/css/design-system.css
└── formation/              ← Tous les contenus de formation
    ├── index.html          ← Dashboard / point d'entrée de la formation
    ├── assets/css/main.css
    └── [modules 1–8]
```

## Site vitrine

**Stack** : HTML + CSS custom properties + Tailwind CDN + vanilla JS. Aucun build system.

- Design token principal : `--color-primary: #E8600A` (orange)
- Chaque page HTML embarque sa propre config Tailwind (`<script id="tailwind-config">`)
- Navigation active : classe `.nav-active` / `.nav-default` (définie dans `design-system.css`)
- Typo : **Manrope** (titres + body) + **Inter** (labels) via Google Fonts

## Formation

### Modules

| Module | Préfixe | Contenu |
|--------|---------|---------|
| 1 | `fondamentaux_1_` | Fondamentaux de l'IA |
| 2 | `prompting_2_` | Prompting |
| 3 | `outils_3_` | Outils IA |
| 4 | `generative_4_` | IA Générative |
| 5 | `automatisation_5_` | Automatisation |
| 6 | `casusage_6_` | Cas d'usage |
| 7 | `ethique_7_` | Éthique IA |
| 8 | `projet_8_` | Projet final |

### Conventions formation

- Encodage : **UTF-8** obligatoire
- Nommage : `module_numéro_sujet_ordre.html` (ex: `fondamentaux_1_quiz_4.html`)
- Tous les liens internes sont relatifs entre fichiers du dossier `formation/`

## TODO — À faire (non urgent)

- [ ] **Logo** : créer un logo unifié pour la marque (site vitrine + formation utilisent des noms différents — à harmoniser)
- [ ] **Lien logo formation → site vitrine** : dans tous les fichiers de formation, le logo pointe vers `index.html` (dashboard formation). À terme, le faire pointer vers `../index.html` (site vitrine) ou prévoir une navigation retour.
- [ ] **CTA site vitrine → formation** : ajouter un bouton "Accéder à la formation" dans le hero du site vitrine pointant vers `formation/index.html`
- [ ] **Nom unifié** : harmoniser le nom de la formation et de la société sur tous les supports

## Développement local

Ouvrir directement les fichiers HTML dans un navigateur. Aucune installation requise.
