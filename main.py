import asyncio

from decouple import config
from telethon import TelegramClient

# Identifiant de l'application disponible depuis (my.telegram.org)
API_ID = config("API_ID")
# Clé secrète de ton application disponible aussi depuis (my.telegram.org)
API_HASH = config("API_HASH")
# Le numéros de telephone du compte Telegram (format : +22700000000)
PHONE_NUMBER = config("PHONE_NUMBER")

# Le point d'entrée, il represente la connexion à Telegram
client = TelegramClient('session', API_ID, API_HASH)

async def main():
    # Ouvre la connexion, et créer le fichier de session
    async with client:
        # Recuperation des tous les echanges, grace a la methode 'get_dialogs()',
        # elle renvoie une liste
        dialogs = await client.get_dialogs()
        # Filtré les dialogs par archivé
        achived = await client.get_dialogs(archived=True)
        # Filtré les dialogs par non archivé
        non_achived = await client.get_dialogs(archived=False)
        print('\n\n')
        print(f'Archived {'=' * 20}')
        # parcourir la list, et effectuer l'action de suppression sur chaque element dialog
        for i, dialog in enumerate(achived):
            # toutes les echanges non archivées, seront supprimées
            await client.delete_dialog(dialog)
            # Attendre un delai de 5 second entre chaque suppression, pour eviter le FloodWaitError
            await asyncio.sleep(5)
            print(f'{i} - {dialog.name} has successfully deleted')

        #     Enfin, desarchivé les discussions dans le dossier archivé
        for i, dialog in enumerate(achived):
            await client.edit_folder(dialog, 0)
            print(f'{i} - {dialog.name} has unarchived')

        print('=' * 20)
        print('\n\n')


asyncio.run(main())
