#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎯 QUICK FIX - Modifications rapides sur les fichiers HTML
==========================================================
"""

import os
import sys
from pathlib import Path

class QuickFix:
    def __init__(self):
        self.changes_count = 0
        
    def replace_in_files(self, pattern, replacement, file_pattern="*.html"):
        """Remplace un pattern dans tous les fichiers correspondants"""
        files = list(Path(".").glob(file_pattern))
        
        print(f"🔍 Recherche de '{pattern}' dans {len(files)} fichiers...")
        
        for filepath in files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if pattern in content:
                    new_content = content.replace(pattern, replacement)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    occurrences = content.count(pattern)
                    self.changes_count += occurrences
                    print(f"  ✅ {filepath.name}: {occurrences} remplacements")
                    
            except Exception as e:
                print(f"  ❌ Erreur dans {filepath.name}: {e}")
        
        print(f"\n✨ Total: {self.changes_count} modifications effectuées")
    
    def fix_specific_link(self, old_link, new_link):
        """Corrige un lien spécifique dans tous les fichiers"""
        print(f"🔗 Correction du lien: {old_link} → {new_link}")
        self.replace_in_files(f'href="{old_link}"', f'href="{new_link}"')
    
    def add_to_all_files(self, selector, content, position="after"):
        """Ajoute du contenu avant/après un sélecteur dans tous les fichiers"""
        files = list(Path(".").glob("*.html"))
        
        for filepath in files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                if selector in html_content:
                    if position == "after":
                        new_content = html_content.replace(selector, selector + "\n" + content)
                    else:  # before
                        new_content = html_content.replace(selector, content + "\n" + selector)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"  ✅ {filepath.name}: contenu ajouté")
                    
            except Exception as e:
                print(f"  ❌ Erreur dans {filepath.name}: {e}")

def main():
    qf = QuickFix()
    
    print("╔════════════════════════════════════════════════════╗")
    print("║        🎯 QUICK FIX - MODIFICATIONS RAPIDES        ║")
    print("╚════════════════════════════════════════════════════╝")
    print("\nQue voulez-vous faire ?")
    print("1. Remplacer du texte dans tous les fichiers")
    print("2. Corriger un lien spécifique")
    print("3. Corriger tous les caractères spéciaux")
    print("4. Ajouter un tracker Analytics")
    print("5. Modification personnalisée")
    
    choice = input("\nVotre choix (1-5): ")
    
    if choice == "1":
        pattern = input("Texte à rechercher: ")
        replacement = input("Remplacer par: ")
        qf.replace_in_files(pattern, replacement)
        
    elif choice == "2":
        old_link = input("Ancien lien: ")
        new_link = input("Nouveau lien: ")
        qf.fix_specific_link(old_link, new_link)
        
    elif choice == "3":
        # Corrections rapides des caractères les plus courants
        fixes = [
            ('Ã©', 'é'), ('Ã¨', 'è'), ('Ã ', 'à'), ('â†'', '→'), 
            ('â†', '←'), ('âœ"', '✓'), ('ðŸ', '🏆'), ('ðŸš€', '🚀')
        ]
        for bad, good in fixes:
            qf.replace_in_files(bad, good)
            
    elif choice == "4":
        # Exemple d'ajout de Google Analytics
        analytics_code = """
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR_ID');
</script>"""
        qf.add_to_all_files("</head>", analytics_code, position="before")
        
    elif choice == "5":
        print("\n📝 Mode personnalisé - Entrez votre code Python:")
        print("(Tapez 'END' sur une ligne seule pour terminer)")
        
        code_lines = []
        while True:
            line = input()
            if line == "END":
                break
            code_lines.append(line)
        
        code = "\n".join(code_lines)
        try:
            exec(code)
            print("✅ Code exécuté avec succès")
        except Exception as e:
            print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()
