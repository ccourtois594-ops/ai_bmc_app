import streamlit as st
import openai
import os
from datetime import datetime
import json
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
url = "http://www.netsquad.cc"
openai_api_key = os.getenv("OPENAI_API_KEY", ""),
# Configuration de la page
st.set_page_config(
    page_title="Business Model Canvas",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre principal
st.markdown ("Retour à Pro_ia NetSquad (%s)" % url)
st.title("🎯 Business Model Canva + marques+ prompt logo")
st.markdown("Transformez vos idées en Business Model complet")

# Sidebar pour la configuration
with st.sidebar:
    st.header("Configuration")
    
    # Clé API OpenAI
    #openai_api_key = st.text_input(
     #   "Clé API OpenAI",
    #  value=os.getenv("OPENAI_API_KEY", ""),
     #   type="password",
      #  help="Entrez votre clé API OpenAI ou configurez-la dans le fichier .env"
    #)
    
    # Modèle OpenAI
    model_choice = st.selectbox(
        "Modèle OpenAI",
        ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
        index=0,
        help="Choisissez le modèle OpenAI à utiliser"
    )
    
    # Niveau de détail
    detail_level = st.selectbox(
        "Niveau de détail",
        ["Basique", "Détaillé", "Très détaillé"],
        index=1,
        help="Niveau de détail souhaité pour le post"
    )
    
    # Horizon temporel
    Clientele = st.selectbox(
        "Clientèle",
        ["Régionale", "Nationale", "Internationale"],
        index=0,
        help="Zone d'activité"
    )

# Fonction pour générer la todo list
def generate_todo_list(goal, detail_level, Clientele, api_key, model):
    """Génère un post linkedin détaillée basée sur le prompt"""
    
    # Configuration du client OpenAI
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))
    
    # Définition du niveau de détail
    detail_prompts = {
        "Basique": "Crée un Business Model Canvas simple avec les étapes principales",
        "Détaillé": "Crée un Business Model Canvas détaillé avec des sources",
        "Très détaillé": "Crée un Business Model Canvas très détaillée avec des sources, des chiffres et statistiques, des ressources pour aller plus loin"
    }
    
    # Prompt principal
    prompt = f"""
    Tu es un spécialiste de la création d'entreprise, du Marketing et de l'innovation.
tu dois réaliser un business model canvas de haut niveau, détaillé et original, en fonction de l'activité décrite dans {{ $json.message}} }}.
pour chaque activité, tu décriras le modèle idéal pour :
** offre et proposition de valeur
tu décriras aussi précisément que possible l'offre proposée dans cette activité, en la décrivant sous forme de punchline marketing percutante, utilisable comme baseline pour un logo
Formule une proposition de valeur claire, concise et différenciante 
pour notre entreprise. Utilise un angle orienté client, pas auto￾centré.
Structure ta réponse selon ce format : "Pour [client type], qui 
[problème ou frustration], nous offrons [solution], qui permet 
[bénéfice clé]". Propose 3 variantes adaptées à des cibles 
différentes (client final, prescripteur, décideur).
** segments clients
tu définiras l'ensemble des segments de clientèle susceptible de représenter 80% de la clientèle compte tenu de l'activité
** relations clients
tu définiras les types de relations clients qui sont pertinents compte tenu de l'activité, des segments clients, et des innovations récentes, rentables et attractives  dans ce domaine
** canaux de distributions
tu définiras les cinq canaux de distribution les plus adaptés à l'activité
** activités clés
tu listera les dix activités clés de cette activité, incluant les taches administratives nécessaires
** partenaires stratégique
tu listeras les dix partenaires clés de cette activité, fournisseurs de materiel, de conseils, ou partenaires commercial possibles.
** ressources clés
tu listeras les 10 ressources clés nécessaires pour pouvoir réaliser l'activité, incluant les investissements, les savoirs faire et compétences, les processus de production
** revenus
tu listeras les sources de revenus récurrentes précises, leur mode de calcul,les tarifs moyens constatés sur le marché
** dépenses
compte tenu des éléments plus haut, tu listeras les 20 principales dépenses nécessaires, incluant infrastructures, investissements, locaux, energie, licences et location de logiciels, salaires, charges et tout autre élément nécessaire à l'activité.
Tu établiras un budget prévisionnel sous forme de tableau, avec une approximation des coûts réaliste pour chaque poste et un total des dépenses nécessaires, scalé pour l'activité normale
** Nom de marque
tu proposeras dix noms de marque réellement originales et percutantes, mémorisables facilement et exprimant clairment les éléments précédents.
** prompt
tu écriras un prompt destiné à générer une identité visuelle forte et efficace, percutant, original, et exprimant au mieux les éléments précédents, susceptible de devenir un game changer et de se démarquer des concurrents.
** SWOT
Fais une analyse SWOT détaillée de cet entreprise en te basant 
sur son marché, son offre et ses ambitions. Identifie les éléments à 
fort impact stratégique, pas les généralités.
Structure ta réponse dans un tableau à 4 colonnes : Forces, 
Faiblesses, Opportunités, Menaces. Termine par une synthèse de 5 
lignes qui résume les 3 leviers prioritaires à activer et les 2 risques 
majeurs à surveiller pour nourrir la réflexion du COMEX
** Roadmap
Structure une roadmap stratégique sur 12 mois, découpée en 3 
grandes phases : court terme (1-3 mois), moyen terme (4-8 mois), 
long terme (9-12 mois). Pour chaque phase, détaille les objectifs 
visés, les livrables clés, et les éventuels prérequis.
Présente le tout dans un tableau 3 colonnes : Phase / Objectifs / 
Livrables. Termine par une synthèse avec les 3 jalons majeurs à 
suivre et les indicateurs associés.
** Pitch
Rédige un pitch oral de 2 minutes pour présenter notre stratégie à 
un investisseur, un partenaire ou un COMEX externe. Le pitch doit 
être clair, crédible et engageant.
Structure-le en 4 blocs : 1) Contexte et enjeux, 2) Vision et ambition 
à 3 ans, 3) Stratégie et feuille de route, 4) Différenciation et facteurs 
clés de succès. 350 mots max.
** Scenarios de developpement
Propose 3 scénarios stratégiques de développement pour mon 
entreprise à horizon 3 ans. Chaque scénario doit inclure les 
objectifs visés, les opportunités à saisir, les risques associés et les 
conditions de réussite.
Rends-les comparables en les structurant sous forme de tableau ou 
de liste à puces, et termine par une recommandation argumentée 
sur le scénario le plus pertinent selon notre contexte.
** Avantage concurrentiel
Identifie les éléments qui constituent aujourd'hui un avantage 
concurrentiel réel sur le marché. Aide-moi à distinguer les atouts 
perçus vs ceux réellement différenciants.
Présente-les dans une liste structurée avec : 1) l'atout, 2) son 
impact business, 3) comment le renforcer ou mieux le valoriser."
** KPI
Propose une liste de 8 à 10 KPI stratégiques à suivre 
mensuellement pour piloter notre stratégie. Classe-les par catégorie 
: performance business, engagement client, structuration interne.
Présente-les dans un tableau avec : nom du KPI, formule de calcul, 
fréquence de suivi, responsable associé.
** Stakeholders
Établis une carte des parties prenantes clés de notre stratégie 
(internes et externes). Pour chacune, indique son rôle, son niveau 
d'influence et les actions à mener pour l'impliquer.
Structure ta réponse dans un tableau 4 colonnes : Partie prenante / 
Rôle / Influence / Action recommandée.


    OBJECTIF : {goal}
    
    {detail_prompts[detail_level]} pour écrire ce prompt.

    Structure ta réponse comme suit :
    
    ## 📋 Business Model Canvas pour: "{goal}"
    
    **Clientele :** {Clientele}
    **Complexité :** [Simple/Moyenne/Élevée]
    
    ## Post crée : 
    """
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Tu es un expert en planification de projets et en productivité. Tu fournis des plans d'action détaillés et réalisables."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=4096
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Erreur lors de la génération : {str(e)}"

# Interface principale
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Décrivez votre activité")
    
    # Zone de saisie de l'objectif
    goal_input = st.text_area(
        "Décrivez votre activité",
        placeholder="Ex: Une activité d'automatisation IA avec N8N, un traiteur spécialisé dans les plats asiatiques, un SAAS pour générer des videos performantes, etc.",
        height=150,
        help="Décrivez votre activité de manière claire et précise"
    )
    
    # Bouton de génération
    generate_button = st.button(
        "🚀 Générer le Business Model Canvas",
        type="primary",
        use_container_width=True
    )

with col2:
    st.header("💡 Conseils")
    st.info(
        """
        **Pour un meilleur résultat :**
        
        ✅ Soyez spécifique dans votre activité
        
        ✅ Mentionnez le contexte (personnel, professionnel, etc.)
        
        ✅ Précisez les clientèles visées et vos spécificités
        
        ✅ Indiquez l'objectif de votre activité """
    )

    st.header("💡 Evolution ")
    st.info(
        """   
        Cet agent peut facilement être adapté, en amont en automatisant la recherche de projets viraux dans votre métier,  
        et en aval pour générer automatiquement le logo et l'identité visuelle        """
    )
    st.header("⚠️ Pour me soutenir ")
    st.info(
        """   
        Pour soutenir ce site,  vous pouvez donner 10€, ce qui permettra de le péréniser
        https://pay.sumup.com/b2c/QZMH6LCX 
        """
    )
    
    st.header("📊 Historique")
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    if st.session_state.history:
        for i, item in enumerate(reversed(st.session_state.history[-5:])):
            with st.expander(f"Objectif {len(st.session_state.history)-i}"):
                st.write(f"**{item['goal'][:50]}...**")
                st.write(f"*{item['timestamp']}*")
    else:
        st.write("Aucun historique pour le moment")

# Génération du plan d'action
if generate_button:
    if not openai_api_key:
        st.error("⚠️ Veuillez entrer votre clé API OpenAI dans la sidebar")
    elif not goal_input.strip():
        st.error("⚠️ Veuillez décrire votre projet")
    else:
        with st.spinner("🤖 Génération du Business Model Canva en cours..."):
            # Génération de la todo list
            todo_list = generate_todo_list(
                goal_input, 
                detail_level, 
                openai_api_key,
                Clientele,
                model_choice
            )
            
            # Affichage du résultat
            st.header("📋 Votre Busines Model Canva")
            st.markdown(todo_list)
            
            # Sauvegarde dans l'historique
            st.session_state.history.append({
                'goal': goal_input,
                'plan': todo_list,
                'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M"),
                'detail_level': detail_level,
            })
            
            # Boutons d'actions
            # col1, col2, col3 = st.columns(3)
            #
            # with col1:
            #     if st.button("📄 Copier le plan"):
            #         st.success("Plan copié ! (vous pouvez maintenant le coller ailleurs)")
            #
            # with col2:
            #     # Bouton de téléchargement
            #     st.download_button(
            #         label="💾 Télécharger (TXT)",
            #         data=todo_list,
            #         file_name=f"plan_action_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
            #         mime="text/plain"
            #     )
            #
            # with col3:
            #     # Bouton de téléchargement JSON
            #     plan_data = {
            #         'objective': goal_input,
            #         'plan': todo_list,
            #         'parameters': {
            #             'detail_level': detail_level,
            #             'Audience': Audience,
            #             'model': model_choice
            #         },
            #         'timestamp': datetime.now().isoformat()
            #     }
            #
            #     st.download_button(
            #         label="📊 Télécharger (JSON)",
            #         data=json.dumps(plan_data, ensure_ascii=False, indent=2),
            #         file_name=f"plan_action_{datetime.now().strftime('%Y%m%d_%H%M')}.json",
            #         mime="application/json"
            #     )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        🎯 AI BMC - Transformez vos idées en Business Model Canva Complet
    </div>
    """,
    unsafe_allow_html=True
)