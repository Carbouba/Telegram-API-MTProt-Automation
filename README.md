# Telegram API MTProto Automation

## Sources & Documentation
- [Telethon Documentation](https://docs.telethon.dev/)
- [Telegram API — my.telegram.org](https://my.telegram.org)
- [python-decouple](https://pypi.org/project/python-decouple/)

---

## Introduction

J'ai ouvert mon application Telegram apres plusieurs d'inactivité, je me suis rendu compte que j'ai un grand nombre d'echange et de groupes dont je ne connais meme pas ou dont j'ai été ajouté automatioquement
je me suis rendu dans les parametre ou  j'ai défini l'action de geste de glissement d'échange pour supprimer l'échange,
mais je me suis vite rendu compte que  j'été entrain d'effectuer une tâche répétitive, en plus  j'ai vraiment pas de temps à perdre
j'ai au moins plus 500 échange, et je ne souhaite en garder que quelques uns, j'ai pas non plus envie de changer de compte ni de perdre certains échanges en supprimante compte.
Je me suis poser la question : comment  résoudre ça avec python ?

J'ai fais mes recherche concerant la creation de Bot Telegram avec Python, et je suis tomber sur la bibliotheque Telethon.
Une bibliothèque Python qui utilise l'API MTProto de Telegram. 
Elle  permet de gérer son compte comme si on  étais dans l'appli, on peut :
- Lister tous les echanges
- Supprimer les echanges
- Envoyer/recuper des message
Quasiment tous ce qui est possible depuis l'application Telegram lui meme.
C'est alors que j'ai ecrit ce script qui ma permis en quelques seconds, et avec quelques ligne de code, de supprimer instantanement plus 500 echnanges en direct,
- ce qui impression, ce que j'ai gardé l'application Telegram ouvert sur mon Windows, et j'assite au spectacle, les echange sont supprimer en direct, je le vois depuis l'application, elle disparaissent une a une sous mes yeux.

C'est ce qui me plais avec Python, ça polyvalence, et surtout en terme d'automatisation, ça c'est n'sst qu'un ecript, mais les possiblitées qu'aoofre Python vont au-delas. 

---

## Prérequis

- Python >= 3.8
- Un compte Telegram actif
- Les clés API Telegram (`API_ID` et `API_HASH`)

### Obtenir les clés API

Rendez-vous sur [https://my.telegram.org](https://my.telegram.org) et connectez-vous avec votre numéro de téléphone au format international : `+22700000000`

1. Cliquez sur **"API development tools"**
2. Remplissez le formulaire (nom et plateforme quelconques)
3. Récupérez votre **App api_id** et **App api_hash**

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Carbouba/Telegram-API-MTProt-Automation.git
cd Telegram-API-MTProt-Automation
```

### 2. Créer un environnement virtuel

**Sur Windows :**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Sur Linux/macOS :**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Mettre à jour pip

```bash
python -m pip install --upgrade pip
```

### 4. Installer les dépendances

```bash
pip install telethon python-decouple
```

---

## Configuration

Copiez le fichier `.env_example` et renommez-le `.env` :

```bash
cp .env_example .env
```

Remplissez vos vrais identifiants dans `.env` :

```
API_ID=remplacez_par_votre_api_id
API_HASH=remplacez_par_votre_api_hash
PHONE_NUMBER=+22700000000
```

> ⚠️ Ne partagez jamais votre fichier `.env`. Il est déjà inclus dans le `.gitignore`.

---

## Utilisation

Lancez le script :

**Sur Windows :**
```bash
python main.py
```

**Sur Linux/macOS :**
```bash
python3 main.py
```

Lors du premier lancement, Telegram vous enverra un code de vérification par SMS. Saisissez-le dans le terminal. Une fois authentifié, un fichier `session.session` est créé — vous n'aurez plus à ressaisir votre numéro.

---

## Avertissement

- Ce script agit sur votre **vrai compte Telegram**
- La suppression d'un échange est **irréversible**
- Un délai de 5 secondes est imposé entre chaque suppression pour éviter le blocage par Telegram (`FloodWaitError`)
- Utilisez ce script de manière responsable et conformément aux [conditions d'utilisation de Telegram](https://telegram.org/tos)

Le code permettant de supprimé les echanges est commenté, vous pouvez le decommenté si vous le voulez.
Pour commencé, utilisez ce code pour obtenir vos propres informations pour confirmé la connexion
`me = await client.get_me()`
Pour plus de detail sur les methodes, visitez la doc officielle 

[Telethon Documentation](https://docs.telethon.dev/)
---

## Structure du projet

```
Telegram-API-MTProt-Automation/
├── main.py          # Script principal
├── .env             # Variables d'environnement (non versionné)
├── .env_example     # Modèle de configuration
├── .gitignore       # Fichiers exclus de Git
├── requirements.txt # Dépendances Python
└── README.md        # Documentation
```

---

## Auteur

**Boubacar Sani** — [GitHub](https://github.com/Carbouba)
