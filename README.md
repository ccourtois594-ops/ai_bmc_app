# 🎯 AI BMC

Une application web Python qui utilise l'intelligence artificielle d'OpenAI pour transformer vos proejts en Business Model Canvas détaillés et réalisables.

## ✨ Fonctionnalités

- **Génération automatique de BMC** basée sur votre activité
- **Niveaux de détail personnalisables** (Basique, Détaillé, Très détaillé)
- **Interface intuitive** avec Streamlit
- **Export des BMC** en TXT et JSON
- **Support de plusieurs modèles OpenAI** (GPT-5, GPT-3.5-turbo etc...)

## 🚀 Installation et utilisation

### Prérequis
- Python 3.8+
- Une clé API OpenAI

### Installation

1. Clonez ou téléchargez ce projet
2. Créez un environnement virtuel :
   ```bash
   uv venv
   ```
3. Activez l'environnement virtuel :
   ```bash
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
4. Installez les dépendances :
   ```bash
   uv pip install -r requirements.txt
   ```

### Lancement de l'application

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : http://localhost:8501

## 🔧 Configuration

### Clé API OpenAI
1. Obtenez votre clé API sur [OpenAI Platform](https://platform.openai.com/)
2. Entrez-la dans la sidebar de l'application

### Paramètres personnalisables
- **Modèle OpenAI** : Choisissez entre GPT-4o, GPT-4o-mini ou GPT-3.5-turbo
- **Niveau de détail** : Ajustez la granularité des tâches générées
- **Horizon temporel** : Définissez la durée prévue pour votre projet

## 📝 Exemple d'utilisation

1. **Décrivez votre activine ** :
   ```
   "Une activité de Boucher-charcutier à Angers"
   ```

2. **Configurez les paramètres** :
   - Niveau : Détaillé
   - Modèle : GPT-4o-mini

3. **Générez votre plan** et obtenez :
   - Vue d'ensemble du projet
   - BMC détaillées 
   - Estimations de temps
   - Ressources nécessaires
   - Critères de réussite
   - Gestion des risques
   - prompt pour logo


## 💾 Export et sauvegarde

- **Format TXT** : Pour lecture et impression
- **Format JSON** : Pour intégration avec d'autres outils
- **Historique intégré** : Accès aux plans précédents

## 🔒 Sécurité

- Votre clé API n'est pas stockée localement
- Les données restent privées (pas de sauvegarde sur serveur externe)
- Communication sécurisée avec l'API OpenAI

## 🛠️ Développement

### Structure du projet
```
ai_goal_planner_web_app/
├── app.py              # Application principale Streamlit
├── requirements.txt    # Dépendances Python
└── README.md          # Documentation
```

### Personnalisation
L'application peut être facilement étendue :
- Nouveaux formats d'export
- Intégrations avec d'autres APIs
- Templates personnalisés
- Modes de collaboration

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier selon vos besoins.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer la documentation
- Partager vos retours d'expérience

---


🤖 Généré avec l'assistance de Memex - [memex.tech](https://memex.tech)
