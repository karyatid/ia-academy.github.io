#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 TEST QUIZ - Vérificateur automatique de quiz
===============================================
"""

import re
import json
from pathlib import Path
from datetime import datetime

class QuizTester:
    def __init__(self):
        self.quiz_files = []
        self.issues = []
        self.stats = {
            "total_files": 0,
            "valid_quizzes": 0,
            "issues_found": 0,
            "encoding_issues": 0,
            "js_issues": 0,
            "structure_issues": 0
        }
    
    def find_quiz_files(self):
        """Trouve tous les fichiers de quiz"""
        # Patterns pour identifier les quiz
        quiz_patterns = ['*quiz*.html', '*test*.html', '*evaluation*.html']
        
        for pattern in quiz_patterns:
            self.quiz_files.extend(Path(".").glob(pattern))
        
        # Éliminer les doublons
        self.quiz_files = list(set(self.quiz_files))
        self.stats["total_files"] = len(self.quiz_files)
        
        print(f"📚 {len(self.quiz_files)} fichiers de quiz trouvés")
        return self.quiz_files
    
    def check_encoding(self, filepath):
        """Vérifie l'encodage du fichier"""
        issues = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Vérifier les caractères mal encodés
            bad_chars = ['Ã©', 'Ã¨', 'Ã ', 'â†'', 'â†', 'âœ"', 'ðŸ']
            for char in bad_chars:
                if char in content:
                    issues.append(f"Caractère mal encodé trouvé: {char}")
                    self.stats["encoding_issues"] += 1
                    
        except UnicodeDecodeError:
            issues.append("Fichier pas en UTF-8")
            self.stats["encoding_issues"] += 1
            
        return issues
    
    def check_quiz_structure(self, filepath):
        """Vérifie la structure HTML du quiz"""
        issues = []
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Vérifications de base
        checks = {
            "quiz-container": "Container de quiz manquant",
            "quiz-question": "Questions de quiz manquantes",
            "quiz-option": "Options de réponse manquantes",
            "data-answer": "Attributs de réponse manquants"
        }
        
        for element, error_msg in checks.items():
            if element not in content:
                issues.append(error_msg)
                self.stats["structure_issues"] += 1
        
        # Vérifier les boutons
        if "startQuiz" not in content and "quiz" in filepath.name.lower():
            issues.append("Bouton de démarrage du quiz manquant")
        
        return issues
    
    def check_javascript(self, filepath):
        """Vérifie le JavaScript du quiz"""
        issues = []
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Patterns JavaScript essentiels pour un quiz
        js_patterns = {
            r"(let|var|const)\s+currentQuestion": "Variable currentQuestion manquante",
            r"(let|var|const)\s+score": "Variable score manquante",
            r"addEventListener\s*\(": "Event listeners manquants",
            r"function\s+(startQuiz|selectAnswer|nextQuestion)": "Fonctions de quiz manquantes"
        }
        
        for pattern, error_msg in js_patterns.items():
            if not re.search(pattern, content):
                if "quiz" in filepath.name.lower():
                    issues.append(error_msg)
                    self.stats["js_issues"] += 1
        
        # Vérifier les erreurs JavaScript communes
        js_errors = [
            (r"getElementByID", "Erreur: getElementByID au lieu de getElementById"),
            (r"\.innerHtml", "Erreur: innerHtml au lieu de innerHTML"),
            (r"documnet\.", "Typo: 'documnet' au lieu de 'document'"),
            (r"cosole\.", "Typo: 'cosole' au lieu de 'console'")
        ]
        
        for pattern, error_msg in js_errors:
            if re.search(pattern, content, re.IGNORECASE):
                issues.append(error_msg)
                self.stats["js_issues"] += 1
        
        return issues
    
    def check_quiz_logic(self, filepath):
        """Vérifie la logique du quiz"""
        issues = []
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Compter les questions et réponses
        questions = len(re.findall(r'class="quiz-question"', content))
        correct_answers = len(re.findall(r'data-answer="correct"', content))
        
        if questions > 0:
            if correct_answers == 0:
                issues.append("Aucune réponse correcte définie")
            elif correct_answers != questions:
                issues.append(f"Incohérence: {questions} questions mais {correct_answers} réponses correctes")
        
        # Vérifier la cohérence des IDs
        id_pattern = r'id="([^"]+)"'
        ids = re.findall(id_pattern, content)
        duplicates = [id for id in ids if ids.count(id) > 1]
        
        if duplicates:
            unique_duplicates = list(set(duplicates))
            issues.append(f"IDs dupliqués: {', '.join(unique_duplicates[:5])}")
        
        return issues
    
    def generate_fix_script(self, filepath, issues):
        """Génère un script de correction pour les problèmes trouvés"""
        fixes = []
        
        for issue in issues:
            if "mal encodé" in issue:
                fixes.append("# Correction de l'encodage")
                fixes.append("python fix_formation.py")
                
            elif "manquant" in issue.lower():
                fixes.append(f"# Ajouter l'élément manquant : {issue}")
                
            elif "Typo" in issue:
                typo_match = re.search(r"'([^']+)' au lieu de '([^']+)'", issue)
                if typo_match:
                    fixes.append(f"# Corriger le typo")
                    fixes.append(f"python quick_fix.py")
                    fixes.append(f"# Option 1: Remplacer '{typo_match.group(1)}' par '{typo_match.group(2)}'")
        
        return "\n".join(fixes) if fixes else None
    
    def test_file(self, filepath):
        """Teste un fichier de quiz complet"""
        print(f"\n🔍 Test de : {filepath.name}")
        print("-" * 40)
        
        all_issues = []
        
        # Tests d'encodage
        encoding_issues = self.check_encoding(filepath)
        if encoding_issues:
            print("  ❌ Problèmes d'encodage:")
            for issue in encoding_issues:
                print(f"     - {issue}")
            all_issues.extend(encoding_issues)
        else:
            print("  ✅ Encodage OK")
        
        # Tests de structure
        structure_issues = self.check_quiz_structure(filepath)
        if structure_issues:
            print("  ❌ Problèmes de structure:")
            for issue in structure_issues:
                print(f"     - {issue}")
            all_issues.extend(structure_issues)
        else:
            print("  ✅ Structure HTML OK")
        
        # Tests JavaScript
        js_issues = self.check_javascript(filepath)
        if js_issues:
            print("  ⚠️  Problèmes JavaScript:")
            for issue in js_issues:
                print(f"     - {issue}")
            all_issues.extend(js_issues)
        else:
            print("  ✅ JavaScript OK")
        
        # Tests de logique
        logic_issues = self.check_quiz_logic(filepath)
        if logic_issues:
            print("  ⚠️  Problèmes de logique:")
            for issue in logic_issues:
                print(f"     - {issue}")
            all_issues.extend(logic_issues)
        else:
            print("  ✅ Logique OK")
        
        # Générer script de correction si nécessaire
        if all_issues:
            self.stats["issues_found"] += len(all_issues)
            self.issues.append({
                "file": str(filepath),
                "issues": all_issues
            })
            
            fix_script = self.generate_fix_script(filepath, all_issues)
            if fix_script:
                print("\n  💡 Script de correction suggéré:")
                print("  " + fix_script.replace("\n", "\n  "))
        else:
            self.stats["valid_quizzes"] += 1
            print("\n  🎉 Quiz valide et fonctionnel !")
        
        return len(all_issues) == 0
    
    def run(self):
        """Lance tous les tests"""
        print("╔════════════════════════════════════════════════════╗")
        print("║        🧪 TEST DES QUIZ - FORMATION IA             ║")
        print("╚════════════════════════════════════════════════════╝")
        
        # Trouver les fichiers
        self.find_quiz_files()
        
        if not self.quiz_files:
            print("\n❌ Aucun fichier de quiz trouvé")
            return
        
        # Tester chaque fichier
        for filepath in sorted(self.quiz_files):
            self.test_file(filepath)
        
        # Rapport final
        self.generate_report()
    
    def generate_report(self):
        """Génère le rapport final"""
        print("\n" + "="*60)
        print("📊 RAPPORT FINAL DES TESTS")
        print("="*60)
        
        print(f"\n✅ Quiz valides : {self.stats['valid_quizzes']}/{self.stats['total_files']}")
        
        if self.stats['issues_found'] > 0:
            print(f"⚠️  Problèmes trouvés : {self.stats['issues_found']}")
            print(f"   - Encodage : {self.stats['encoding_issues']}")
            print(f"   - Structure : {self.stats['structure_issues']}")
            print(f"   - JavaScript : {self.stats['js_issues']}")
            
            print("\n📝 Fichiers à corriger en priorité:")
            for item in self.issues[:5]:  # Top 5 des fichiers problématiques
                filename = Path(item['file']).name
                issue_count = len(item['issues'])
                print(f"   - {filename} ({issue_count} problèmes)")
        else:
            print("\n🎉 Tous les quiz sont fonctionnels !")
        
        # Sauvegarder le rapport
        report = {
            "timestamp": datetime.now().isoformat(),
            "stats": self.stats,
            "issues": self.issues
        }
        
        report_file = Path("quiz_test_report.json")
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Rapport détaillé sauvegardé : {report_file}")
        
        # Recommandations
        if self.stats['encoding_issues'] > 0:
            print("\n💡 Recommandation : Lancer 'python fix_formation.py' pour corriger l'encodage")
        
        if self.stats['js_issues'] > 0:
            print("💡 Recommandation : Vérifier le code JavaScript dans les fichiers problématiques")

def main():
    tester = QuizTester()
    tester.run()
    
    # Proposer une correction automatique si des problèmes sont trouvés
    if tester.stats['issues_found'] > 0:
        print("\n" + "="*60)
        response = input("Voulez-vous lancer la correction automatique ? (o/n): ")
        if response.lower() in ['o', 'oui', 'y', 'yes']:
            import subprocess
            print("\n🔧 Lancement de la correction automatique...")
            subprocess.run([sys.executable, "fix_formation.py"])
            
            print("\n🔄 Relance des tests après correction...")
            tester2 = QuizTester()
            tester2.run()

if __name__ == "__main__":
    main()
