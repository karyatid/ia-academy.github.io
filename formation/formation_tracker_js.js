/**
 * Formation IA Academy - Système de tracking de progression
 * Gère la progression, les quiz et la certification
 */

class FormationTracker {
    constructor() {
        this.storageKey = 'iaAcademyProgress';
        this.version = '1.0';
        this.init();
    }

    /**
     * Initialise le système de tracking
     */
    init() {
        if (!this.hasValidProgress()) {
            this.createInitialProgress();
        }
        this.upgradeIfNeeded();
        this.logAccess();
    }

    /**
     * Vérifie si des données de progression valides existent
     */
    hasValidProgress() {
        try {
            const data = localStorage.getItem(this.storageKey);
            if (!data) return false;
            
            const parsed = JSON.parse(data);
            return parsed && parsed.version && parsed.modules;
        } catch (e) {
            console.warn('Données de progression corrompues, réinitialisation...');
            return false;
        }
    }

    /**
     * Crée la structure initiale des données de progression
     */
    createInitialProgress() {
        const initialData = {
            version: this.version,
            student: {
                name: null,
                email: null,
                startDate: new Date().toISOString(),
                lastAccess: new Date().toISOString()
            },
            modules: {
                module1: {
                    id: 'fondamentaux',
                    title: 'Fondamentaux de l\'IA',
                    duration: 240, // 4 heures en minutes
                    completed: false,
                    completionDate: null,
                    timeSpent: 0,
                    quizScore: null,
                    quizDate: null,
                    sequences: {
                        overview: { completed: false, timeSpent: 0, visitDate: null },
                        introduction: { completed: false, timeSpent: 0, visitDate: null },
                        histoire: { completed: false, timeSpent: 0, visitDate: null },
                        types_safari: { completed: false, timeSpent: 0, visitDate: null },
                        quiz: { completed: false, timeSpent: 0, visitDate: null, score: null }
                    }
                },
                module2: {
                    id: 'prompting',
                    title: 'Art du Prompting',
                    duration: 360,
                    completed: false,
                    completionDate: null,
                    timeSpent: 0,
                    quizScore: null,
                    quizDate: null,
                    sequences: {
                        overview: { completed: false, timeSpent: 0, visitDate: null },
                        bases: { completed: false, timeSpent: 0, visitDate: null },
                        techniques_avancees: { completed: false, timeSpent: 0, visitDate: null },
                        atelier: { completed: false, timeSpent: 0, visitDate: null },
                        quiz: { completed: false, timeSpent: 0, visitDate: null, score: null }
                    }
                },
                module3: {
                    id: 'outils',
                    title: 'Outils IA Populaires',
                    duration: 360,
                    completed: false,
                    completionDate: null,
                    timeSpent: 0,
                    quizScore: null,
                    quizDate: null,
                    sequences: {
                        overview: { completed: false, timeSpent: 0, visitDate: null },
                        chatgpt: { completed: false, timeSpent: 0, visitDate: null },
                        comparatif: { completed: false, timeSpent: 0, visitDate: null },
                        workflow: { completed: false, timeSpent: 0, visitDate: null },
                        atelier: { completed: false, timeSpent: 0, visitDate: null }
                    }
                },
                module4: {
                    id: 'generative',
                    title: 'IA Générative',
                    duration: 420,
                    completed: false,
                    completionDate: null,
                    timeSpent: 0,
                    quizScore: null,
                    quizDate: null,
                    sequences: {
                        overview: { completed: false, timeSpent: 0, visitDate: null },
                        texte_scripts: { completed: false, timeSpent: 0, visitDate: null },
                        images: { completed: false, timeSpent: 0, visitDate: null },
                        audio_video: { completed: false, timeSpent: 0, visitDate: null },
                        projet_portfolio: { completed: false, timeSpent: 0, visitDate: null }
                    }
                },
                module5: {
                    id: 'automatisation',
                    title: 'Automatisation',
                    duration: 360,
                    completed: false,
                    completionDate: null,
                    timeSpent: 0,
                    quizScore: null,
                    quizDate: null,
                    sequences: {
                        overview: { completed: false, timeSpent: 0, visitDate: null },
                        introduction: { completed: false, timeSpent: 0, visitDate: null },
                        zapier: { completed: false, timeSpent: 0, visitDate: null },
                        make: { completed: false, timeSpent: 0, visitDate: null },
                        projet: { completed: false, timeSpent: 0, visitDate: null }
                    }
                },
                module6: {
                    id: 'casusage',
                    title: 'Cas d\'usage métier',
                    duration: 360,
                    completed: false,
                    completionDate: null,
                    timeSpent: 0,
                    quizScore: null,
                    quizDate: null,
                    sequences: {
                        overview: { completed: false, timeSpent: 0, visitDate: null },
                        identification: { completed: false, timeSpent: 0, visitDate: null },
                        implementation: { completed: false, timeSpent: 0, visitDate: null },
                        roadmap: { completed: false, timeSpent: 0, visitDate: null }
                    }
                },
                module7: {
                    id: 'ethique',
                    title: 'Éthique et sécurité',
                    duration: 300,
                    completed: false,
                    completionDate: null,
                    timeSpent: 0,
                    quizScore: null,
                    quizDate: null,
                    sequences: {
                        overview: { completed: false, timeSpent: 0, visitDate: null },
                        enjeux: { completed: false, timeSpent: 0, visitDate: null },
                        biais: { completed: false, timeSpent: 0, visitDate: null },
                        futur: { completed: false, timeSpent: 0, visitDate: null }
                    }
                },
                module8: {
                    id: 'projet',
                    title: 'Projet final',
                    duration: 360,
                    completed: false,
                    completionDate: null,
                    timeSpent: 0,
                    projectSubmitted: false,
                    projectScore: null,
                    sequences: {
                        overview: { completed: false, timeSpent: 0, visitDate: null },
                        brief: { completed: false, timeSpent: 0, visitDate: null },
                        conception: { completed: false, timeSpent: 0, visitDate: null },
                        realisation: { completed: false, timeSpent: 0, visitDate: null },
                        presentation: { completed: false, timeSpent: 0, visitDate: null }
                    }
                }
            },
            stats: {
                totalTimeSpent: 0,
                sessionsCount: 0,
                averageSessionTime: 0,
                completionRate: 0
            },
            certification: {
                eligible: false,
                generated: false,
                certificateId: null,
                issueDate: null,
                verificationCode: null
            }
        };

        this.saveProgress(initialData);
        console.log('📚 Formation IA Academy - Progression initialisée');
    }

    /**
     * Met à niveau les données si nécessaire
     */
    upgradeIfNeeded() {
        const data = this.getProgress();
        if (data.version !== this.version) {
            // Logique de migration ici si besoin
            data.version = this.version;
            this.saveProgress(data);
        }
    }

    /**
     * Récupère les données de progression
     */
    getProgress() {
        try {
            const data = localStorage.getItem(this.storageKey);
            return data ? JSON.parse(data) : null;
        } catch (e) {
            console.error('Erreur lecture progression:', e);
            return null;
        }
    }

    /**
     * Sauvegarde les données de progression
     */
    saveProgress(data) {
        try {
            data.student.lastAccess = new Date().toISOString();
            localStorage.setItem(this.storageKey, JSON.stringify(data));
            return true;
        } catch (e) {
            console.error('Erreur sauvegarde progression:', e);
            return false;
        }
    }

    /**
     * Enregistre l'accès à une séquence
     */
    trackSequenceVisit(moduleId, sequenceId, timeSpent = 0) {
        const data = this.getProgress();
        if (!data || !data.modules[moduleId]) return false;

        const sequence = data.modules[moduleId].sequences[sequenceId];
        if (sequence) {
            sequence.visitDate = new Date().toISOString();
            sequence.timeSpent = Math.max(sequence.timeSpent, timeSpent);
            sequence.completed = true;

            // Met à jour le temps total du module
            data.modules[moduleId].timeSpent += timeSpent;
            data.stats.totalTimeSpent += timeSpent;

            this.checkModuleCompletion(data, moduleId);
            this.updateStats(data);
            this.saveProgress(data);

            console.log(`✅ Séquence ${sequenceId} du ${moduleId} visitée`);
            return true;
        }
        return false;
    }

    /**
     * Sauvegarde le résultat d'un quiz
     */
    saveQuizResult(moduleId, score, timeSpent = 0) {
        const data = this.getProgress();
        if (!data || !data.modules[moduleId]) return false;

        data.modules[moduleId].quizScore = score;
        data.modules[moduleId].quizDate = new Date().toISOString();
        
        // Met à jour la séquence quiz si elle existe
        if (data.modules[moduleId].sequences.quiz) {
            data.modules[moduleId].sequences.quiz.completed = true;
            data.modules[moduleId].sequences.quiz.score = score;
            data.modules[moduleId].sequences.quiz.visitDate = new Date().toISOString();
            data.modules[moduleId].sequences.quiz.timeSpent = timeSpent;
        }

        data.modules[moduleId].timeSpent += timeSpent;
        data.stats.totalTimeSpent += timeSpent;

        this.checkModuleCompletion(data, moduleId);
        this.checkCertificationEligibility(data);
        this.updateStats(data);
        this.saveProgress(data);

        console.log(`📊 Quiz ${moduleId} complété avec ${score}%`);
        
        // Backup automatique si score élevé
        if (score >= 80) {
            this.scheduleAutoBackup();
        }

        return true;
    }

    /**
     * Marque un projet comme soumis (Module 8)
     */
    submitProject(score = null) {
        const data = this.getProgress();
        if (!data) return false;

        data.modules.module8.projectSubmitted = true;
        data.modules.module8.projectScore = score;
        data.modules.module8.completionDate = new Date().toISOString();
        data.modules.module8.completed = true;

        this.checkCertificationEligibility(data);
        this.updateStats(data);
        this.saveProgress(data);

        console.log('🎯 Projet final soumis !');
        return true;
    }

    /**
     * Vérifie si un module est complété
     */
    checkModuleCompletion(data, moduleId) {
        const module = data.modules[moduleId];
        if (!module) return;

        const sequences = Object.values(module.sequences);
        const allSequencesCompleted = sequences.every(seq => seq.completed);

        // Conditions spéciales pour certains modules
        let moduleCompleted = false;
        
        if (moduleId === 'module8') {
            // Module 8 nécessite le projet soumis
            moduleCompleted = allSequencesCompleted && module.projectSubmitted;
        } else if (module.quizScore !== null) {
            // Modules avec quiz nécessitent quiz réussi + séquences
            moduleCompleted = allSequencesCompleted && module.quizScore >= 70;
        } else {
            // Modules sans quiz nécessitent juste toutes les séquences
            moduleCompleted = allSequencesCompleted;
        }

        if (moduleCompleted && !module.completed) {
            module.completed = true;
            module.completionDate = new Date().toISOString();
            console.log(`🎉 Module ${moduleId} complété !`);
        }
    }

    /**
     * Vérifie l'éligibilité à la certification
     */
    checkCertificationEligibility(data) {
        const modules = Object.values(data.modules);
        
        // Tous les modules doivent être complétés
        const allModulesCompleted = modules.every(m => m.completed);
        
        // Tous les quiz doivent être réussis (sauf module 3 et 8 qui n'en ont pas)
        const quizModules = ['module1', 'module2', 'module4', 'module5', 'module6', 'module7'];
        const allQuizPassed = quizModules.every(moduleId => {
            const module = data.modules[moduleId];
            return module.quizScore !== null && module.quizScore >= 70;
        });

        // Projet final soumis
        const projectSubmitted = data.modules.module8.projectSubmitted;

        const wasEligible = data.certification.eligible;
        data.certification.eligible = allModulesCompleted && allQuizPassed && projectSubmitted;

        if (data.certification.eligible && !wasEligible) {
            console.log('🎓 Éligible pour la certification !');
            this.scheduleAutoBackup();
        }
    }

    /**
     * Génère un certificat de formation
     */
    generateCertificate(studentName, studentEmail) {
        const data = this.getProgress();
        
        if (!data.certification.eligible) {
            return { success: false, error: 'Non éligible pour la certification' };
        }

        if (data.certification.generated) {
            return { 
                success: true, 
                certificateId: data.certification.certificateId,
                issueDate: data.certification.issueDate,
                verificationCode: data.certification.verificationCode
            };
        }

        // Génère les identifiants uniques
        const certificateId = this.generateCertificateId();
        const verificationCode = this.generateVerificationCode();

        // Met à jour les données étudiant
        data.student.name = studentName;
        data.student.email = studentEmail;

        // Génère le certificat
        data.certification.generated = true;
        data.certification.certificateId = certificateId;
        data.certification.issueDate = new Date().toISOString();
        data.certification.verificationCode = verificationCode;

        this.saveProgress(data);

        console.log('🎓 Certificat généré:', certificateId);

        return {
            success: true,
            certificateId,
            issueDate: data.certification.issueDate,
            verificationCode,
            studentName,
            studentEmail
        };
    }

    /**
     * Met à jour les statistiques
     */
    updateStats(data) {
        data.stats.sessionsCount++;
        
        const completedModules = Object.values(data.modules).filter(m => m.completed).length;
        data.stats.completionRate = Math.round((completedModules / 8) * 100);
        
        if (data.stats.sessionsCount > 0) {
            data.stats.averageSessionTime = Math.round(data.stats.totalTimeSpent / data.stats.sessionsCount);
        }
    }

    /**
     * Exporte les données de progression
     */
    exportProgress() {
        const data = this.getProgress();
        if (!data) return null;

        const exportData = {
            ...data,
            exportDate: new Date().toISOString(),
            exportVersion: this.version
        };

        const blob = new Blob([JSON.stringify(exportData, null, 2)], {
            type: 'application/json'
        });

        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `ia-academy-progress-${new Date().toISOString().split('T')[0]}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        console.log('📦 Progression exportée');
        return exportData;
    }

    /**
     * Importe des données de progression
     */
    importProgress(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            
            reader.onload = (e) => {
                try {
                    const importedData = JSON.parse(e.target.result);
                    
                    // Validation basique
                    if (!importedData.modules || !importedData.version) {
                        reject(new Error('Fichier de progression invalide'));
                        return;
                    }

                    // Sauvegarde l'ancien progress
                    const oldData = this.getProgress();
                    localStorage.setItem(this.storageKey + '_backup', JSON.stringify(oldData));

                    // Importe les nouvelles données
                    this.saveProgress(importedData);
                    console.log('📥 Progression importée avec succès');
                    resolve(importedData);

                } catch (error) {
                    reject(new Error('Erreur lors de l\'import: ' + error.message));
                }
            };

            reader.onerror = () => reject(new Error('Erreur de lecture du fichier'));
            reader.readAsText(file);
        });
    }

    /**
     * Sauvegarde automatique par email
     */
    scheduleAutoBackup() {
        setTimeout(() => {
            const data = this.getProgress();
            const backupData = JSON.stringify(data, null, 2);
            
            const subject = encodeURIComponent('Sauvegarde Formation IA Academy');
            const body = encodeURIComponent(`
Bonjour,

Voici votre sauvegarde automatique de progression de la Formation IA Academy.

Progression: ${data.stats.completionRate}%
Dernière connexion: ${new Date(data.student.lastAccess).toLocaleString()}

Pour restaurer cette progression:
1. Ouvrez la formation IA Academy
2. Accédez aux paramètres
3. Utilisez la fonction "Importer la progression"
4. Copiez-collez les données ci-dessous dans un fichier .json

Données de progression:
${backupData}

Bonne formation !
L'équipe IA Academy
            `);

            window.open(`mailto:?subject=${subject}&body=${body}`);
        }, 2000);
    }

    /**
     * Génère un ID unique de certificat
     */
    generateCertificateId() {
        const timestamp = Date.now().toString(36);
        const random = Math.random().toString(36).substr(2, 5);
        return `IA2024-${timestamp}-${random}`.toUpperCase();
    }

    /**
     * Génère un code de vérification
     */
    generateVerificationCode() {
        return Math.random().toString(36).substr(2, 8).toUpperCase();
    }

    /**
     * Enregistre l'accès à la formation
     */
    logAccess() {
        const data = this.getProgress();
        data.student.lastAccess = new Date().toISOString();
        this.saveProgress(data);
    }

    /**
     * Obtient un résumé de la progression
     */
    getProgressSummary() {
        const data = this.getProgress();
        if (!data) return null;

        return {
            completionRate: data.stats.completionRate,
            totalTimeSpent: data.stats.totalTimeSpent,
            modulesCompleted: Object.values(data.modules).filter(m => m.completed).length,
            quizAverage: this.calculateQuizAverage(data),
            certificationEligible: data.certification.eligible,
            certificateGenerated: data.certification.generated
        };
    }

    /**
     * Calcule la moyenne des quiz
     */
    calculateQuizAverage(data) {
        const scores = Object.values(data.modules)
            .map(m => m.quizScore)
            .filter(score => score !== null);
        
        if (scores.length === 0) return 0;
        return Math.round(scores.reduce((sum, score) => sum + score, 0) / scores.length);
    }

    /**
     * Remet à zéro la progression
     */
    resetProgress() {
        if (confirm('⚠️ Êtes-vous sûr de vouloir remettre à zéro votre progression ? Cette action est irréversible.')) {
            localStorage.removeItem(this.storageKey);
            this.createInitialProgress();
            console.log('🔄 Progression remise à zéro');
            return true;
        }
        return false;
    }
}

// Instance globale du tracker
window.formationTracker = new FormationTracker();

// Fonctions utilitaires globales pour les pages
window.trackQuiz = (moduleId, score, timeSpent) => {
    return window.formationTracker.saveQuizResult(moduleId, score, timeSpent);
};

window.trackSequence = (moduleId, sequenceId, timeSpent) => {
    return window.formationTracker.trackSequenceVisit(moduleId, sequenceId, timeSpent);
};

window.getFormationProgress = () => {
    return window.formationTracker.getProgressSummary();
};

window.exportFormationProgress = () => {
    return window.formationTracker.exportProgress();
};

console.log('🚀 Formation Tracker initialisé !');