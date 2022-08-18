import aiogram
import threading
import aminofix
import json
import os
import asyncio
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, Message
from aiogram.utils import executor
TOKEN_Telegram = "5597440969:AAFBH7if6Y9UJeW4MF87uDjLsaXoBRi0P9Q"

class Form(StatesGroup):
	name = State()
	coinis = State()
	coinsend = State()
	links = State()
	linkcommi = State()
	sendpass = State()
	sendid = State()
	device = State()
	start = State()


client = Bot(TOKEN_Telegram, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(client, storage=storage)

profile = {
	"email": "none",
	"password": "none",
	"coinsend1": 0,
	"link": "none",
	"linkcomm": 0,
	"password1": "none",
	"sendpassadm": "none",
	"id": 0,
	"deviceid": "none"
}

@dp.message_handler()
async def mess(message: Message):
	content = str(message.text).split(" ")
	user_Id = str(message.from_user.id)
	if content[0][0] == "/":
		if content[0][1:] == "start":
			await message.reply(f"чтобы отправить монеты напишите /send\nчтобы получить айди соо зайдите в бота и напишите /id\nbot: @Aminoid_bot\nваш айди: {user_Id}\nчтобы отменить действие напишите /back\nчтобы ввести девайс айди напишите(обязательно) /device")
			await Form.start.set()
@dp.message_handler(state=Form.start)
async def mess(message: Message):
	ct = message.text.lower()
	content = str(message.text).split(" ")
	user_Id = str(message.from_user.id)
	user_name = message.from_user['username']
	chat_Id = message.chat.id
	reg = os.listdir()
	mes = State()
	if (f"{user_Id}.json") not in reg:
		with open(f"{user_Id}.json", "w") as file:
			json.dump(profile, file)
			
	with open(f"{user_Id}.json", "r") as file:
			profile_info = json.load(file)
	
	if content[0][0] == "/":
		if content[0][1:] == "passadmsend":
			await Form.sendpass.set()
			await message.reply("здраствуйте админ! айди получателя:")
			
	if content[0][0] == "/":
		if content[0][1:] == "send":
			if profile_info["password1"] == "none":
				await message.reply("чтобы купить ключ верефикации напишите нам: @Redpiar")
			elif profile_info["password1"] == "almaz":
				await message.reply("вы получили доступ!")
				await Form.name.set()
				await message.reply("напишите почту аккаунта с которой будем кидать монеты:")
			elif profile_info["password1"] == "divolo":
				await message.reply("вы получили доступ!")
				await Form.name.set()
				await message.reply("напишите почту аккаунта с которой будем кидать монеты:")
			elif profile_info["password1"] == "zerro":
				await message.reply("вы получили доступ!")
				await Form.name.set()
				await message.reply("напишите почту аккаунта с которой будем кидать монеты:")
			elif profile_info["password1"] == "die":
				await message.reply("вы получили доступ!")
				await Form.name.set()
				await message.reply("напишите почту аккаунта с которой будем кидать монеты:")
			elif profile_info["password1"] == "gold":
				await message.reply("вы получили доступ!")
				await Form.name.set()
				await message.reply("напишите почту аккаунта с которой будем кидать монеты:")
			
	if content[0][0] == "/":
		if content[0][1:] == "device":
			await Form.device.set()
			await message.reply("введите девайс айди(чтобы получить помощь пишите нам: @Redpiar ):")

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        content = str(message.text).split(" ")
        data['name'] = message.text
        data['coinis'] = message.text
        named = data['name']
        coiniss = data['coinis']
        content = str(message.text).split(" ")
        user_Id = str(message.from_user.id)
        with open(f"{user_Id}.json", "r") as file:
        	profile_info = json.load(file)
        	profile_info["email"] = f"{named}"
        	with open(f"{user_Id}.json", "w") as file:
        		json.dump(profile_info, file)
        		
        await message.reply(named)
        await Form.coinis.set()
        await message.reply("пароль от аккаунта(если ничего не произошло, то вы получили ошибку): ")
        

@dp.message_handler(state=Form.coinis)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
    	content = str(message.text).split(" ")
    	user_Id = str(message.from_user.id)
    	with open(f"{user_Id}.json", "r") as file:
        	profile_info = json.load(file)
    	data['name']=message.text
    	data['coinis']=message.text
    	named=data['name']
    	coiniss=data['coinis']
    	profile_info["password"]=f"{coiniss}"
    	with open(f"{user_Id}.json", "w") as file:
    		json.dump(profile_info, file)
    	email = profile_info["email"]
    	passwor = profile_info["password"]
    	profile_info["password"]=f"{coiniss}"
    	with open(f"{user_Id}.json", "w") as file:
    		json.dump(profile_info, file)
    	await message.reply("обработка...")
    	await asyncio.sleep(5)
    	await message.reply(f"{email}\n{passwor}")
    	
    	await Form.coinsend.set()
    	await message.reply("отправьте количество монет которые кинем: ")
    	if content[0][0] == "/":
        	if content[0][1:] == "back":
        		await message.reply("напишите почту аккаунта с которой будем кидать монеты:")
        		await Form.name.set()
@dp.message_handler(state=Form.coinsend)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
    	user_Id = str(message.from_user.id)
    	with open(f"{user_Id}.json", "r") as file:
        	profile_info = json.load(file)
    	data['name']=message.text
    	data['coinis']=message.text
    	data['coinsend']=message.text
    	hueta = data['coinsend']
    	profile_info["coinsend1"]=f"{hueta}"
    	with open(f"{user_Id}.json", "w") as file:
    		json.dump(profile_info, file)
    	email=profile_info["email"]
    	passwor=profile_info["password"]
    	aminocoin=profile_info["coinsend1"]
    	await message.reply("обработка...")
    	await asyncio.sleep(5)
    	await Form.linkcommi.set()
    	await message.reply(f"отправьте айди на соо: ")

@dp.message_handler(state=Form.linkcommi)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
    	user_Id = str(message.from_user.id)
    	with open(f"{user_Id}.json", "r") as file:
        	profile_info = json.load(file)
    	data['name']=message.text
    	data['coinis']=message.text
    	data['coinsend']=message.text
    	data['linkcommi']=message.text
    	comm = data['linkcommi']
    	profile_info["linkcomm"]=f"{comm}"
    	with open(f"{user_Id}.json", "w") as file:
    		json.dump(profile_info, file)
    	await message.reply("обработка...")
    	await asyncio.sleep(5)
    	await Form.links.set()
    	await message.reply("скиньте ссылку на вип профиль: ")

@dp.message_handler(state=Form.links)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
    	data["device"] = message.text
    	user_Id = str(message.from_user.id)
    	with open(f"{user_Id}.json", "r") as file:
    		profile_info = json.load(file)
    	comm = profile_info["linkcomm"]
    	with open(f"{user_Id}.json", "w") as file:
    		json.dump(profile_info, file)
    	linkcomm=data["linkcommi"]
    	hueta=data['coinsend']
    	data["links"] = message.text
    	linksi=data["links"]
    	email=profile_info["email"]
    	device_Id=data["device"]
    	passwor=profile_info["password"]
    	aminocoin=profile_info["coinsend1"]
    	linkcommin=profile_info["linkcomm"]
    	sendemino = int(aminocoin)
    	await message.reply("обработка...")
    	client = aminofix.Client(deviceId=device_Id)
    	client.login(email=email, password=passwor)
    	client.join_community(comId=f"{comm}")
    	await message.reply("зашли в соо...")
    	code = client.get_from_code(linksi)
    	comId = code.comIdPost
    	userId = code.objectId
    	subclient = aminofix.SubClient(comId, profile=client.profile)
    	await message.reply("отправляется...\nэто может занять время если большая сумма")
    	while sendemino > 0:
    		sendemino -= 500
    		threading.Thread(target=subclient.subscribe, args=(userId, )).start()
    	await asyncio.sleep(0)
    	await message.reply("напишите почту аккаунта с которой будем отсылать монеты:")
    	await Form.name.set()

@dp.message_handler(state=Form.sendpass)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
    	user_Id = str(message.from_user.id)
    	with open(f"{user_Id}.json", "r") as file:
    		profile_info = json.load(file)
    	data["sendpass"] = message.text
    	sendid = data["sendpass"]
    	profile_info["id"] = f"{sendid}"
    	with open(f"{user_Id}.json", "w") as file:
    		json.dump(profile_info, file)
    	await Form.sendid.set()
    	await message.reply("введите пароль который отправим: ")
    		

@dp.message_handler(state=Form.sendid)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
    	content = str(message.text).split(" ")
    	user_Id = str(message.from_user.id)
    	with open(f"{user_Id}.json", "r") as file:
    		profile_info = json.load(file)
    	data["sendid"] = message.text
    	id = data["sendid"]
    	profile_info["sendpassadm"] = f"{id}"
    	with open(f"{user_Id}.json", "w") as file:
    		json.dump(profile_info, file)
    	passsend = profile_info["sendpassadm"]
    	idsend = profile_info["id"]
    	with open(f"{idsend}.json", "w") as file:
    		json.dump(profile_info, file)
    	profile_info["password1"] = f"{passsend}"
    	with open(f"{idsend}.json", "w") as file:
    		json.dump(profile_info, file)
    	if content[0][0] == "/":
    		if content[0][1:] == "send":
    			await Form.name.set()
    			await message.reply("напишите почту аккаунта с которой будем кидать монеты:")
    		

@dp.message_handler(state=Form.device)
async def process_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['device'] = message.text
		user_Id = str(message.from_user.id)
		with open(f"{user_Id}.json", "r") as file:
			profile_info = json.load(file)
		device = data["device"]
		profile_info["deviceid"] = f"{device}"
		with open(f"{user_Id}.json", "w") as file:
		  		json.dump(profile_info, file)
		  		await Form.start.set()
    		

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)