from .. import loader, utils 


def register(cb):
	cb(KickAllMod())

class KickAllMod(loader.Module):
	"""Ломаем все."""
	strings = {'name': 'УбиваторНахуй'}

	async def ubitcmd(self, message):
		"""Что блять не понятного? Используй .ubit  <s>, чтобы кикнуть всех с чата. Это клон kickall я просто зделал для себя"""
		args = utils.get_args_raw(message) 
		silent = False
		if 's' in args: 
			silent = True
			await message.delete()
		else: await message.edit('✝️Молитесь за чат😌 [ Вам пизда ] ')
		users = await message.client.get_participants(message.chat_id,aggressive=True)
		count = 0
		for user in users:
			try:
				if user.id != message.from_id:
					await message.client.kick_participant(message.chat_id, user.id)
					count += 1
			except: pass
		if silent == True:
			chat = await message.client.get_entity(message.to_id) 
			await message.client.send_message('me', f'<b>В чате "{chat.title}" снесено {count} грешников.</b>')
		else: await message.edit(f'<b>Кикнуто {count} пользователей.</b>')
