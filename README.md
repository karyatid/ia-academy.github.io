# 🔧 Kit de Correction Formation IA

## 🚀 Installation rapide

1. **Télécharge les 3 fichiers** dans le dossier de ta formation :
   - `fix_formation.py` - Correction automatique complète
   - `quick_fix.py` - Modifications rapides
   - `test_quiz.py` - Testeur de quiz

2. **Ouvre un terminal** dans le dossier de ta formation

3. **Lance la correction complète** :
```bash
python fix_formation.py
```

## 📋 Ce qui sera corrigé automatiquement

### ✅ Encodage UTF-8
- Tous les caractères mal encodés (é, è, à, →, ←, emojis, etc.)
- Conversion automatique Latin-1 → UTF-8

### 🔗 Navigation
- Liens cassés entre les pages
- Structure de navigation module par module
- Boutons Précédent/Suivant

### 💾 Sauvegardes
- Création automatique de `.backup` avant modification
- Rapport JSON détaillé des corrections

## 🎯 Utilisation de Quick Fix

Pour des modifications rapides et spécifiques :

```bash
python quick_fix.py
```

**Options disponibles :**
1. Remplacer du texte partout
2. Corriger un lien spécifique  
3. Corriger tous les caractères spéciaux
4. Ajouter Google Analytics
5. Code personnalisé

## 🧪 Tester les Quiz

```bash
python test_quiz.py
```

Vérifie automatiquement :
- ✅ Structure HTML des quiz
- ✅ JavaScript fonctionnel
- ✅ Encodage des questions/réponses
- ✅ Logique de validation

## 💡 Workflow recommandé

### 1️⃣ **Première utilisation**
```bash
# Correction complète avec sauvegarde
python fix_formation.py

# Vérifier le rapport
cat correction_report.json
```

### 2️⃣ **Modifications ponctuelles**
```bash
# Pour un changement rapide
python quick_fix.py
# Choisir option 1 ou 2
```

### 3️⃣ **Après chaque modification**
```bash
# Tester les quiz
python test_quiz.py

# Ouvrir dans le navigateur pour vérifier
open dashboard.html  # Mac
start dashboard.html  # Windows
```

## 🆘 Problèmes fréquents et solutions

### ❌ "Module not found"
```bash
# Pas besoin de modules externes !
# Les scripts utilisent uniquement Python standard
```

### ❌ "Permission denied"
```bash
# Sur Mac/Linux, rendre exécutable
chmod +x fix_formation.py quick_fix.py test_quiz.py
```

### ❌ "Encoding error"
```bash
# Le script gère automatiquement UTF-8 et Latin-1
# Si problème persiste, contacte-moi !
```

## 📊 Structure des fichiers

```
formation-ia/
├── fix_formation.py        # Correction automatique complète
├── quick_fix.py           # Modifications rapides
├── test_quiz.py           # Testeur de quiz
├── correction_report.json # Rapport après correction
├── *.html.backup          # Sauvegardes automatiques
└── *.html                 # Fichiers corrigés
```

## 🎯 Exemples d'utilisation

### Corriger un lien cassé spécifique
```python
# Dans quick_fix.py, option 2
Ancien lien: fondamentaux_1_introduction.html
Nouveau lien: fondamentaux_1_introduction_1.html
```

### Remplacer du texte partout
```python
# Dans quick_fix.py, option 1
Texte à rechercher: Module 1 - Introduction
Remplacer par: Module 1 - Fondamentaux de l'IA
```

### Ajouter du CSS personnalisé
```python
# Dans quick_fix.py, option 5
# Puis taper :
from pathlib import Path
for f in Path(".").glob("*.html"):
    content = open(f, 'r', encoding='utf-8').read()
    if "</style>" in content:
        new_css = "\n/* Custom CSS */\n.my-class { color: blue; }\n</style>"
        content = content.replace("</style>", new_css)
        open(f, 'w', encoding='utf-8').write(content)
        print(f"CSS ajouté à {f.name}")
END
```

## 💬 Retour à Claude

Une fois les corrections appliquées, tu peux me dire :
- ✅ "J'ai lancé fix_formation.py, voici le rapport"
- ❌ "J'ai une erreur sur le fichier X"
- 💡 "Je voudrais aussi modifier Y"

Je pourrai alors :
1. Analyser le rapport de correction
2. Créer des scripts supplémentaires si besoin
3. T'aider avec des modifications spécifiques

## 🚀 Tips de Pro

1. **Toujours faire une sauvegarde manuelle** avant de grosses modifications :
   ```bash
   cp -r formation-ia formation-ia-backup-$(date +%Y%m%d)
   ```

2. **Tester sur un fichier d'abord** :
   ```bash
   # Modifier quick_fix.py pour tester sur un seul fichier
   # Remplacer *.html par fondamentaux_1_quiz_4.html
   ```

3. **Versionner avec Git** (optionnel mais recommandé) :
   ```bash
   git init
   git add .
   git commit -m "Avant correction automatique"
   python fix_formation.py
   git diff  # Voir tous les changements
   git commit -m "Correction encodage et liens"
   ```

---

💪 **Tu as maintenant tous les outils pour corriger ta formation "à la volée" !**

Besoin d'aide ? Reviens me voir avec le rapport de correction 😊
