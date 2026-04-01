#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FIX QUIZ DISPLAY BUG - Corrige l'affichage prématuré des réponses
================================================================
Supprime le 'display: block' des classes .quiz-feedback.correct et .quiz-feedback.incorrect
car le JavaScript gère déjà l'affichage avec style.display = 'block'
"""

import os
import re
from pathlib import Path
from datetime import datetime
import shutil

class QuizDisplayFixer:
    def __init__(self, folder_path="."):
        self.folder_path = Path(folder_path)
        self.files = list(self.folder_path.glob("*.html"))
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "files_processed": 0,
            "quiz_bugs_fixed": 0,
            "errors": []
        }
    
    def fix_quiz_css(self, content):
        """Corrige le CSS des quiz pour ne pas afficher les réponses immédiatement"""
        fixes_count = 0
        
        # Pattern 1: Supprimer display: block de .quiz-feedback.correct
        pattern1 = r'(\.quiz-feedback\.correct\s*\{[^}]*?)display:\s*block;'
        if re.search(pattern1, content, re.DOTALL):
            content = re.sub(pattern1, r'\1', content, flags=re.DOTALL)
            fixes_count += 1
            print("  [OK] Corrigé: .quiz-feedback.correct")
        
        # Pattern 2: Supprimer display: block de .quiz-feedback.incorrect
        pattern2 = r'(\.quiz-feedback\.incorrect\s*\{[^}]*?)display:\s*block;'
        if re.search(pattern2, content, re.DOTALL):
            content = re.sub(pattern2, r'\1', content, flags=re.DOTALL)
            fixes_count += 1
            print("  [OK] Corrigé: .quiz-feedback.incorrect")
        
        if fixes_count > 0:
            self.report["quiz_bugs_fixed"] += fixes_count
            
        return content, fixes_count
    
    def process_file(self, filepath):
        """Traite un fichier HTML"""
        try:
            # Vérifier si le fichier contient un quiz
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'quiz-feedback' not in content:
                return  # Pas de quiz dans ce fichier
            
            print(f"\n[FICHIER] {filepath.name}")
            
            # Créer une sauvegarde
            backup_path = filepath.with_suffix('.html.quiz_backup')
            if not backup_path.exists():
                shutil.copy2(filepath, backup_path)
                print(f"  [BACKUP] Sauvegarde créée")
            
            # Appliquer les corrections
            content, fixes = self.fix_quiz_css(content)
            
            if fixes > 0:
                # Écrire le fichier corrigé
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"  [OK] {fixes} bug(s) CSS corrigé(s)")
                self.report["files_processed"] += 1
            else:
                print(f"  [INFO] Aucun bug détecté")
            
        except Exception as e:
            print(f"  [ERREUR] {str(e)}")
            self.report["errors"].append({"file": str(filepath), "error": str(e)})
    
    def run(self):
        """Lance le processus de correction"""
        print("=" * 70)
        print("FIX QUIZ DISPLAY BUG - CORRECTION DES RÉPONSES AFFICHÉES PRÉMATURÉMENT")
        print("=" * 70)
        
        if not self.files:
            print("[ERREUR] Aucun fichier HTML trouvé")
            return
        
        print(f"\n[INFO] {len(self.files)} fichiers HTML trouvés")
        print("[INFO] Recherche des fichiers avec quiz...")
        
        for filepath in self.files:
            self.process_file(filepath)
        
        self.generate_report()
    
    def generate_report(self):
        """Génère un rapport des corrections"""
        print("\n" + "=" * 70)
        print("RAPPORT DE CORRECTION")
        print("=" * 70)
        
        print(f"[OK] Fichiers avec quiz traités : {self.report['files_processed']}")
        print(f"[OK] Bugs CSS corrigés : {self.report['quiz_bugs_fixed']}")
        
        if self.report["errors"]:
            print(f"\n[ATTENTION] Erreurs rencontrées : {len(self.report['errors'])}")
            for error in self.report["errors"]:
                print(f"  - {error['file']}: {error.get('error', 'Erreur')}")
        
        print("\n[SOLUTION] Le JavaScript gère maintenant l'affichage des feedbacks avec:")
        print("  → document.querySelector('.quiz-feedback.correct').style.display = 'block';")
        print("\n[TERMINÉ] Les quiz n'affichent plus les réponses au chargement ! ✓")

def main():
    import sys
    
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print("FIX QUIZ DISPLAY BUG")
    print("=" * 40)
    print(f"Dossier : {os.path.abspath(folder)}")
    
    response = input("\nLancer la correction des quiz ? (o/n) : ")
    
    if response.lower() in ['o', 'oui', 'y', 'yes']:
        fixer = QuizDisplayFixer(folder)
        fixer.run()
    else:
        print("Correction annulée")

if __name__ == "__main__":
    main()
