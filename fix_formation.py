#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔧 FIX FORMATION IA - Outil de correction automatique
=====================================================
Corrige automatiquement :
- Les problèmes d'encodage UTF-8
- Les liens cassés entre les pages
- La structure de navigation
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
import shutil

class FormationFixer:
    def __init__(self, folder_path="."):
        self.folder_path = Path(folder_path)
        self.files = list(self.folder_path.glob("*.html"))
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "files_processed": 0,
            "encoding_fixes": 0,
            "links_fixed": 0,
            "errors": []
        }
        
        # Mapping des caractères mal encodés
        self.encoding_fixes = {
            'Ã©': 'é', 'Ã¨': 'è', 'Ãª': 'ê', 'Ã ': 'à', 'Ã¢': 'â',
            'Ã´': 'ô', 'Ã®': 'î', 'Ã¯': 'ï', 'Ã§': 'ç', 'Ã¹': 'ù',
            'Ã»': 'û', 'Å"': 'œ', 'Ã€': 'À', 'Ãˆ': 'È', 'Ã‰': 'É',
            'ÃŠ': 'Ê', 'Ã"': 'Ô', 'Ã‡': 'Ç', 'â€™': "'", 'â€œ': '"',
            'â€': '"', 'â€"': '—', 'â€"': '–', 'â€¦': '…', 'â€¢': '•',
            'â†'': '→', 'â†': '←', 'âœ"': '✓', 'âœ…': '✅', 'âŒ': '❌',
            'ðŸ': '🏆', 'ðŸŽ¯': '🎯', 'ðŸš€': '🚀', 'ðŸ"': '🔍', 'ðŸ'¡': '💡',
            'ðŸŽ‰': '🎉', 'ðŸ"Š': '📊', 'ðŸ"š': '📚', 'ðŸ—ºï¸': '🗺️',
            'ðŸ§ ': '🧠', 'ðŸ"®': '🔮', 'ðŸ› ï¸': '🛠️', 'ðŸŽ®': '🎮',
            'ðŸ"'': '🔒', 'ðŸ†˜': '🆘', 'ðŸ"—': '🔗', 'ðŸ"±': '📱',
            'ðŸ–¼ï¸': '🖼️', 'ðŸŽ¬': '🎬', 'ðŸŽ§': '🎧', 'ðŸ"§': '🔧'
        }
        
        # Structure de navigation correcte
        self.navigation_structure = {
            # Module 1 - Fondamentaux
            "fondamentaux_1_overview.html": {
                "prev": "dashboard.html",
                "next": "fondamentaux_1_introduction_1.html"
            },
            "fondamentaux_1_introduction_1.html": {
                "prev": "fondamentaux_1_overview.html",
                "next": "fondamentaux_1_histoire_2.html"
            },
            "fondamentaux_1_histoire_2.html": {
                "prev": "fondamentaux_1_introduction_1.html",
                "next": "fondamentaux_1_types_safari_3.html"
            },
            "fondamentaux_1_types_safari_3.html": {
                "prev": "fondamentaux_1_histoire_2.html",
                "next": "fondamentaux_1_quiz_4.html"
            },
            "fondamentaux_1_quiz_4.html": {
                "prev": "fondamentaux_1_types_safari_3.html",
                "next": "prompting_2_overview.html"
            },
            
            # Module 2 - Prompting
            "prompting_2_overview.html": {
                "prev": "fondamentaux_1_quiz_4.html",
                "next": "prompting_2_bases_1.html"
            },
            "prompting_2_bases_1.html": {
                "prev": "prompting_2_overview.html",
                "next": "prompting_2_techniques_avancees_2.html"
            },
            "prompting_2_techniques_avancees_2.html": {
                "prev": "prompting_2_bases_1.html",
                "next": "prompting_2_atelier_3.html"
            },
            "prompting_2_atelier_3.html": {
                "prev": "prompting_2_techniques_avancees_2.html",
                "next": "prompting_2_quiz_4.html"
            },
            "prompting_2_quiz_4.html": {
                "prev": "prompting_2_atelier_3.html",
                "next": "outils_3_overview.html"
            },
            
            # Module 3 - Outils
            "outils_3_overview.html": {
                "prev": "prompting_2_quiz_4.html",
                "next": "outils_3_chatgpt_1a.html"
            },
            "outils_3_chatgpt_1a.html": {
                "prev": "outils_3_overview.html",
                "next": "outils_3_chatgpt_1b.html"
            },
            "outils_3_chatgpt_1b.html": {
                "prev": "outils_3_chatgpt_1a.html",
                "next": "outils_3_chatgpt_1c.html"
            },
            "outils_3_chatgpt_1c.html": {
                "prev": "outils_3_chatgpt_1b.html",
                "next": "outils_3_chatgpt_1d.html"
            },
            "outils_3_chatgpt_1d.html": {
                "prev": "outils_3_chatgpt_1c.html",
                "next": "outils_3_claude_2.html"
            },
            "outils_3_claude_2.html": {
                "prev": "outils_3_chatgpt_1d.html",
                "next": "outils_3_autres_3.html"
            },
            "outils_3_autres_3.html": {
                "prev": "outils_3_claude_2.html",
                "next": "outils_3_atelier_4.html"
            },
            "outils_3_atelier_4.html": {
                "prev": "outils_3_autres_3.html",
                "next": "generative_4_overview.html"
            },
            
            # Module 4 - IA Générative
            "generative_4_overview.html": {
                "prev": "outils_3_atelier_4.html",
                "next": "generative_4_texte_scripts_1.html"
            },
            "generative_4_texte_scripts_1.html": {
                "prev": "generative_4_overview.html",
                "next": "generative_4_scripts_claude_1b.html"
            },
            "generative_4_scripts_claude_1b.html": {
                "prev": "generative_4_texte_scripts_1.html",
                "next": "generative_4_subtitles_tools_1c.html"
            },
            "generative_4_subtitles_tools_1c.html": {
                "prev": "generative_4_scripts_claude_1b.html",
                "next": "generative_4_midjourney_debutant_2a.html"
            },
            "generative_4_midjourney_debutant_2a.html": {
                "prev": "generative_4_subtitles_tools_1c.html",
                "next": "generative_4_midjourney_2a.html"
            },
            "generative_4_midjourney_2a.html": {
                "prev": "generative_4_midjourney_debutant_2a.html",
                "next": "generative_4_dalle_alternatives_2b.html"
            },
            "generative_4_dalle_alternatives_2b.html": {
                "prev": "generative_4_midjourney_2a.html",
                "next": "generative_4_workflows_visuels_2c.html"
            },
            "generative_4_workflows_visuels_2c.html": {
                "prev": "generative_4_dalle_alternatives_2b.html",
                "next": "generative_4_audio_3a.html"
            },
            "generative_4_audio_3a.html": {
                "prev": "generative_4_workflows_visuels_2c.html",
                "next": "generative_4_video_3b.html"
            },
            "generative_4_video_3b.html": {
                "prev": "generative_4_audio_3a.html",
                "next": "generative_4_sync_3c.html"
            },
            "generative_4_sync_3c.html": {
                "prev": "generative_4_video_3b.html",
                "next": "generative_4_projet_portfolio_4.html"
            },
            "generative_4_projet_portfolio_4.html": {
                "prev": "generative_4_sync_3c.html",
                "next": "automatisation_5_overview.html"
            },
            
            # Module 5 - Automatisation
            "automatisation_5_overview.html": {
                "prev": "generative_4_projet_portfolio_4.html",
                "next": "automatisation_5_introduction_1.html"
            },
            "automatisation_5_introduction_1.html": {
                "prev": "automatisation_5_overview.html",
                "next": "automatisation_5_zapier_2.html"
            },
            "automatisation_5_zapier_2.html": {
                "prev": "automatisation_5_introduction_1.html",
                "next": "automatisation_5_make_3.html"
            },
            "automatisation_5_make_3.html": {
                "prev": "automatisation_5_zapier_2.html",
                "next": "automatisation_5_projet_4.html"
            },
            "automatisation_5_projet_4.html": {
                "prev": "automatisation_5_make_3.html",
                "next": "casusage_6_overview.html"
            },
            
            # Module 6 - Cas d'usage
            "casusage_6_overview.html": {
                "prev": "automatisation_5_projet_4.html",
                "next": "casusage_6_education_1.html"
            },
            "casusage_6_education_1.html": {
                "prev": "casusage_6_overview.html",
                "next": "casusage_6_marketing_2.html"
            },
            "casusage_6_marketing_2.html": {
                "prev": "casusage_6_education_1.html",
                "next": "casusage_6_productivite_3.html"
            },
            "casusage_6_productivite_3.html": {
                "prev": "casusage_6_marketing_2.html",
                "next": "sequence_6_4_etude_cas.html"
            },
            "sequence_6_4_etude_cas.html": {
                "prev": "casusage_6_productivite_3.html",
                "next": "ethique_7_overview.html"
            },
            
            # Module 7 - Éthique
            "ethique_7_overview.html": {
                "prev": "sequence_6_4_etude_cas.html",
                "next": "ethique_7_enjeux_1a.html"
            },
            "ethique_7_enjeux_1a.html": {
                "prev": "ethique_7_overview.html",
                "next": "ethique_7_enjeux_1b.html"
            },
            "ethique_7_enjeux_1b.html": {
                "prev": "ethique_7_enjeux_1a.html",
                "next": "ethique_7_biais_2.html"
            },
            "ethique_7_biais_2.html": {
                "prev": "ethique_7_enjeux_1b.html",
                "next": "ethique_7_futur_3.html"
            },
            "ethique_7_futur_3.html": {
                "prev": "ethique_7_biais_2.html",
                "next": "projet_8_overview.html"
            },
            
            # Module 8 - Projet
            "projet_8_overview.html": {
                "prev": "ethique_7_futur_3.html",
                "next": "quiz_parcours_module8.html"
            },
            "quiz_parcours_module8.html": {
                "prev": "projet_8_overview.html",
                "next": "parcours_a_mini_agence.html"
            },
            "parcours_a_mini_agence.html": {
                "prev": "quiz_parcours_module8.html",
                "next": "parcours_b_solution_metier.html"
            },
            "parcours_b_solution_metier.html": {
                "prev": "parcours_a_mini_agence.html",
                "next": "parcours-c-ecosysteme-ia.html"
            },
            "parcours-c-ecosysteme-ia.html": {
                "prev": "parcours_b_solution_metier.html",
                "next": "dashboard.html"
            }
        }
    
    def fix_encoding(self, content):
        """Corrige les problèmes d'encodage UTF-8"""
        original_content = content
        fixes_count = 0
        
        for bad_char, good_char in self.encoding_fixes.items():
            if bad_char in content:
                content = content.replace(bad_char, good_char)
                fixes_count += 1
        
        if fixes_count > 0:
            print(f"  ✅ {fixes_count} corrections d'encodage appliquées")
            self.report["encoding_fixes"] += fixes_count
            
        return content
    
    def fix_navigation_links(self, content, filename):
        """Corrige les liens de navigation"""
        if filename in self.navigation_structure:
            nav_info = self.navigation_structure[filename]
            fixes_count = 0
            
            # Pattern pour trouver les liens de navigation
            patterns = [
                # Liens précédents
                (r'href="[^"]*"([^>]*btn-secondary[^>]*>.*?(?:←|â†|Précédent|Module \d+))',
                 f'href="{nav_info["prev"]}"\\1'),
                # Liens suivants  
                (r'href="[^"]*"([^>]*btn-primary[^>]*>.*?(?:→|â†'|Suivant|Module \d+))',
                 f'href="{nav_info["next"]}"\\1'),
            ]
            
            for pattern, replacement in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                    fixes_count += 1
            
            if fixes_count > 0:
                print(f"  ✅ {fixes_count} liens de navigation corrigés")
                self.report["links_fixed"] += fixes_count
                
        return content
    
    def verify_links(self, content, filename):
        """Vérifie que tous les liens pointent vers des fichiers existants"""
        broken_links = []
        link_pattern = r'href="([^"#][^"]*\.html)"'
        
        for match in re.finditer(link_pattern, content):
            link = match.group(1)
            if not link.startswith('http'):
                link_path = self.folder_path / link
                if not link_path.exists():
                    broken_links.append(link)
        
        if broken_links:
            print(f"  ⚠️  Liens cassés détectés : {', '.join(broken_links)}")
            self.report["errors"].append({
                "file": str(filename),
                "broken_links": broken_links
            })
        
        return broken_links
    
    def process_file(self, filepath):
        """Traite un fichier HTML"""
        print(f"\n📄 Traitement de : {filepath.name}")
        
        try:
            # Créer une sauvegarde
            backup_path = filepath.with_suffix('.html.backup')
            if not backup_path.exists():
                shutil.copy2(filepath, backup_path)
                print(f"  💾 Sauvegarde créée : {backup_path.name}")
            
            # Lire le fichier avec le bon encodage
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(filepath, 'r', encoding='latin-1') as f:
                    content = f.read()
                print(f"  ⚠️  Fichier en Latin-1, conversion UTF-8")
            
            # Appliquer les corrections
            content = self.fix_encoding(content)
            content = self.fix_navigation_links(content, filepath.name)
            broken_links = self.verify_links(content, filepath.name)
            
            # Écrire le fichier corrigé
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✅ Fichier corrigé et sauvegardé")
            self.report["files_processed"] += 1
            
        except Exception as e:
            error_msg = f"Erreur lors du traitement de {filepath.name}: {str(e)}"
            print(f"  ❌ {error_msg}")
            self.report["errors"].append({"file": str(filepath), "error": str(e)})
    
    def run(self):
        """Lance le processus de correction"""
        print("="*60)
        print("🚀 DÉBUT DE LA CORRECTION DE LA FORMATION IA")
        print("="*60)
        
        if not self.files:
            print("❌ Aucun fichier HTML trouvé dans le dossier")
            return
        
        print(f"\n📊 {len(self.files)} fichiers HTML trouvés")
        
        for filepath in self.files:
            self.process_file(filepath)
        
        # Générer le rapport
        self.generate_report()
    
    def generate_report(self):
        """Génère un rapport des corrections"""
        print("\n" + "="*60)
        print("📋 RAPPORT DE CORRECTION")
        print("="*60)
        
        print(f"✅ Fichiers traités : {self.report['files_processed']}")
        print(f"🔤 Corrections d'encodage : {self.report['encoding_fixes']}")
        print(f"🔗 Liens corrigés : {self.report['links_fixed']}")
        
        if self.report["errors"]:
            print(f"\n⚠️  Erreurs rencontrées : {len(self.report['errors'])}")
            for error in self.report["errors"]:
                if "broken_links" in error:
                    print(f"  - {error['file']}: liens cassés -> {', '.join(error['broken_links'])}")
                else:
                    print(f"  - {error['file']}: {error.get('error', 'Erreur inconnue')}")
        
        # Sauvegarder le rapport JSON
        report_file = self.folder_path / "correction_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.report, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Rapport détaillé sauvegardé : {report_file}")
        print("\n✨ Correction terminée avec succès !")

def main():
    import sys
    
    # Déterminer le dossier à traiter
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print("╔════════════════════════════════════════════════════╗")
    print("║     🔧 FIX FORMATION IA - OUTIL DE CORRECTION     ║")
    print("╚════════════════════════════════════════════════════╝")
    
    # Confirmation avant de lancer
    print(f"\n📂 Dossier à traiter : {os.path.abspath(folder)}")
    response = input("\n⚠️  Des sauvegardes seront créées. Continuer ? (o/n) : ")
    
    if response.lower() in ['o', 'oui', 'y', 'yes']:
        fixer = FormationFixer(folder)
        fixer.run()
    else:
        print("❌ Correction annulée")

if __name__ == "__main__":
    main()
