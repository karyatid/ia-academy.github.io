# Formation IA V4 — CLAUDE.md

## Description du projet

Formation complète sur l'Intelligence Artificielle, composée de fichiers HTML organisés par modules, avec des scripts Python de maintenance.

## Structure des modules

| Module | Préfixe | Contenu |
|--------|---------|---------|
| 1 | `fondamentaux_1_` | Fondamentaux de l'IA (histoire, introduction, types, quiz) |
| 2 | `prompting_2_` | Prompting (bases, techniques avancées, atelier, quiz) |
| 3 | `outils_3_` | Outils IA (ChatGPT, Claude, autres, atelier) |
| 4 | `generative_4_` | IA Générative (texte, image, audio, vidéo, workflows) |
| 5 | `automatisation_5_` | Automatisation (Make, Zapier, projet) |
| 6 | `casusage_6_` | Cas d'usage (éducation, marketing, productivité) |
| 7 | `ethique_7_` | Éthique IA (enjeux, biais, futur) |
| 8 | `projet_8_` | Projet final |

## Fichiers principaux

- `index.html` — Page d'accueil / point d'entrée
- `dashboard.html` — Tableau de bord de la formation
- `fix_formation.py` — Correction automatique complète (encodage + navigation)
- `quick_fix.py` — Modifications rapides et ciblées
- `test_quiz.py` — Testeur de quiz HTML
- `correction_report.json` — Rapport des corrections appliquées

## Conventions et règles

- Encodage : **UTF-8** obligatoire pour tous les fichiers HTML
- Convention de nommage : `module_numéro_sujet_ordre.html` (ex: `fondamentaux_1_quiz_4.html`)
- Les scripts Python n'utilisent que la bibliothèque standard (pas de pip install)

## Commandes utiles

```bash
# Correction complète avec sauvegarde
python fix_formation.py

# Modification rapide et ciblée
python quick_fix.py

# Tester les quiz
python test_quiz.py

# Ouvrir le dashboard
open dashboard.html
```

## Points d'attention

- Toujours vérifier l'encodage UTF-8 lors de modifications de fichiers HTML
- Les liens de navigation entre pages suivent la convention de nommage des fichiers
- Tester les quiz après toute modification JavaScript
- Créer un backup manuel avant des modifications massives
