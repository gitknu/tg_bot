#ІМПОРТУЄМО БІБЛІОТЕКИ 👇👇👇

import telebot
from telebot import types
import twx.botapi

#ІМПОРТУЄМО БІБЛІОТЕКИ 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#ПРИКРІПЛЮЄМО КЛЮЧ БОТА 👇👇👇

bot = telebot.TeleBot('6092358205:AAFyRF_GyK7m7yB4PefOGXGPvFAktAGv4Jc')

#ПРИКРІПЛЮЄМО КЛЮЧ БОТА 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#СТАРТОВЕ ПОВІДОМЛЕННЯ 👇👇👇
     
@bot.message_handler(commands=['start'])
def start(message):
         markup = types.InlineKeyboardMarkup(row_width=2)
         markup.add(
         types.InlineKeyboardButton('Про нас 🎓', callback_data='Про_нас'),
         types.InlineKeyboardButton('Новини 📺', callback_data='Новини'),
         types.InlineKeyboardButton('Співробітники 👥', callback_data='Співробітники'),
         types.InlineKeyboardButton('Документи 📄', url='https://rebrand.ly/qaedu_gdrive'),
         types.InlineKeyboardButton('Інше 🔍', callback_data='Інше'),
         types.InlineKeyboardButton('Контакти 📞', callback_data='Контакти'),)
         video = open('logo_wide_gif.mp4', 'rb')
         bot.send_video(message.chat.id, video)
         bot.send_message(message.chat.id, 'Доброго дня! Вас вітає Телеграм-бот <a href="https://qaedu.knu.ua/">Відділу забезпечення якості освіти</a>. Тут Ви можете дізнатися необхідну інформацію, перейти на інші наші ресурси або просто <a href="https://rebrand.ly/qaedu_poll">залишити відгук</a>. \n\n <i>Бот не працює? Натисніть</i> \n/start', parse_mode='html', reply_markup=markup)

#СТАРТОВЕ ПОВІДОМЛЕННЯ 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#ПОЧАТОК 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Початок' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
         telebot.types.InlineKeyboardButton('Про нас 🎓', callback_data='Про_нас'),
         telebot.types.InlineKeyboardButton('Новини 📺', callback_data='Новини'),
         telebot.types.InlineKeyboardButton('Співробітники 👥', callback_data='Співробітники'),
         telebot.types.InlineKeyboardButton('Документи 📄', url='https://rebrand.ly/qaedu_gdrive'),
         telebot.types.InlineKeyboardButton('Інше 🔍', callback_data='Інше'),
         telebot.types.InlineKeyboardButton('Контакти 📞', callback_data='Контакти'),)
    video = open('logo_wide_gif.mp4', 'rb')
    bot.send_photo(query.message.chat.id, video)
    bot.send_message(chat_id=query.message.chat.id,
                     text='Доброго дня! Вас вітає Телеграм-бот <a href="https://qaedu.knu.ua">Відділу забезпечення якості освіти </a>. Тут Ви можете дізнатися необхідну інформацію, перейти на інші наші ресурси або просто <a href="https://rebrand.ly/qaedu_poll">залишити відгук</a> \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)        

#ПОЧАТОК 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#ПРО НАС 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Про_нас' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('Контакти 📞', callback_data='Контакти'),
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'))
    video = open('promo_beta_viddil.mp4', 'rb')
    bot.send_video(query.message.chat.id, video)    
    bot.send_message(chat_id=query.message.chat.id,
                     text='<b>Що таке Відділ забезпечення якості освіти?</b> \n\n✅ Ми відділ, який координує функціонування системи забезпечення якості освіти на рівні Університету. \n\n📈 Наша команда прагне впроваджувати в Університеті найновіші досягнення у сфері забезпечення якості освіти. \n\n🧐 <b><i>Чим займається відділ забезпечення якості освіти?</i></b> \n- консультує структурні підрозділи з питань формування освітніх програм та здійснює їх внутрішню експертизу; \n- бере участь у підготовці до процедур зовнішнього забезпечення якості; \n- надає консультативну допомогу, координує та здійснює моніторинг діяльності структурних підрозділів щодо питань якості освіти. \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)        

#ПРО НАС 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#СПІВРОБІТНИКИ 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Співробітники' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('Білоус О.', callback_data='У розробці'),
telebot.types.InlineKeyboardButton('Суздаль Ю.', callback_data='У розробці'),
telebot.types.InlineKeyboardButton('Захарова Ю.', callback_data='У розробці'),
telebot.types.InlineKeyboardButton('Хруцька О.', callback_data='У розробці'),
telebot.types.InlineKeyboardButton('Контакти 📞', callback_data='Контакти'),
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'))
    photo = open('d_v_sh.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='Очолює відділ Щеглюк Дарія Василівна. Інформацію щодо інших співробітників Ви можете знайти нижче. \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)        

#СПІВРОБІТНИКИ 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#КОЛЕКТИВ (БІЛОУС О.) 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Білоус О.' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'),
telebot.types.InlineKeyboardButton('Назад ↩️', callback_data='Співробітники'))
    photo = open('worker_name.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='▶️ <u>ПІБ</u>: <b>Білоус О. По-батькові</b> \n\n▶️ <u>Посада</u>: <i>Інженер</i> \n\n▶️ <u>Володіє навичками</u>: \n(що вміє, та переважно чим займається, у відділі) \n\n- Створення додатків (на Python); \n- Розробка веб-сервісів (на PHP і JS); \n- Встановлення та налаштування спеціалізованого ПЗ для подальшого користування спеціалістом. \n\n▶️ <u>Із яких питань може допомогти</u>: \n(яка користь від цього комусь поза межами відділу) \n- Проконсультувати щодо базових основ програмування; \n- Проінформувати щодо наявного технічного забезпечення відділу.  \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)        

#КОЛЕКТИВ (БІЛОУС О.) 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#КОЛЕКТИВ (СУЗДАЛЬ Ю.) 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Суздаль Ю.' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'),
telebot.types.InlineKeyboardButton('Назад ↩️', callback_data='Співробітники'))
    photo = open('worker_name.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='▶️ <u>ПІБ</u>: <b>Суздаль Ю. По-батькові</b> \n\n▶️ <u>Посада</u>: <i>Інженер</i> \n\n▶️ <u>Володіє навичками</u>: \n(що вміє, та переважно чим займається, у відділі) \n\n- Створення додатків (на Python); \n- Розробка веб-сервісів (на PHP і JS); \n- Встановлення та налаштування спеціалізованого ПЗ для подальшого користування спеціалістом. \n\n▶️ <u>Із яких питань може допомогти</u>: \n(яка користь від цього комусь поза межами відділу) \n- Проконсультувати щодо базових основ програмування; \n- Проінформувати щодо наявного технічного забезпечення відділу.  \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)        

#КОЛЕКТИВ (СУЗДАЛЬ Ю.) 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#КОЛЕКТИВ (ЗАХАРОВА Ю.) 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Захарова Ю.' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'),
telebot.types.InlineKeyboardButton('Назад ↩️', callback_data='Співробітники'))
    photo = open('worker_name.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='▶️ <u>ПІБ</u>: <b>Захарова Ю. По-батькові</b> \n\n▶️ <u>Посада</u>: <i>Інженер</i> \n\n▶️ <u>Володіє навичками</u>: \n(що вміє, та переважно чим займається, у відділі) \n\n- Створення додатків (на Python); \n- Розробка веб-сервісів (на PHP і JS); \n- Встановлення та налаштування спеціалізованого ПЗ для подальшого користування спеціалістом. \n\n▶️ <u>Із яких питань може допомогти</u>: \n(яка користь від цього комусь поза межами відділу) \n- Проконсультувати щодо базових основ програмування; \n- Проінформувати щодо наявного технічного забезпечення відділу.  \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)        

#КОЛЕКТИВ (ЗАХАРОВА Ю.) 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#КОЛЕКТИВ (ХРУЦЬКА О.) 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Хруцька О.' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'),
telebot.types.InlineKeyboardButton('Назад ↩️', callback_data='Співробітники'))
    photo = open('worker_name.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='▶️ <u>ПІБ</u>: <b>Хруцька О. По-батькові</b> \n\n▶️ <u>Посада</u>: <i>Інженер</i> \n\n▶️ <u>Володіє навичками</u>: \n(що вміє, та переважно чим займається, у відділі) \n\n- Створення додатків (на Python); \n- Розробка веб-сервісів (на PHP і JS); \n- Встановлення та налаштування спеціалізованого ПЗ для подальшого користування спеціалістом. \n\n▶️ <u>Із яких питань може допомогти</u>: \n(яка користь від цього комусь поза межами відділу) \n- Проконсультувати щодо базових основ програмування; \n- Проінформувати щодо наявного технічного забезпечення відділу.  \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)        

#КОЛЕКТИВ (ХРУЦЬКА О.) 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#НОВИНИ 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Новини' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('Дізнатися ще 👉', url='https://fb.com/department.quality/posts/pfbid02ycXBwMBhHhgfv3opRpahXhpgaAvrXGkMk94Qk8nVgdzTeE5RwgRLudU5AdJQWRghl'),
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'))
    photo = open('news.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='📺 З 13 лютого по 8 березня відбулася активна фаза другої хвилі навчання за програмою підвищення кваліфікації «Роль гарантів освітніх програм у розбудові внутрішньої системи забезпечення якості вищої освіти». Підготовку пройшли 179 зареєстрованих осіб, серед яких гаранти освітніх програм Київського національного університету імені Тараса Шевченка, а також особи, які беруть участь в адмініструванні освітніх програм в структурних підрозділах. \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)

#НОВИНИ 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#ІНШЕ 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Інше' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('Гаранту ОП', callback_data='Гаранту ОП'),
telebot.types.InlineKeyboardButton('НПП', callback_data='НПП'),
telebot.types.InlineKeyboardButton('Здобувачу', callback_data='Здобувачу'),
telebot.types.InlineKeyboardButton('Стейкхолдеру', callback_data='Стейкхолдеру'),
telebot.types.InlineKeyboardButton('Гугл Диск ☁️', url='https://rebrand.ly/qaedu_gdrive'),
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'))
    photo = open('other.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='Не знайшли необхідну інформацію в інших розділах? Тоді можливо вона саме тут! \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)

#ІНШЕ 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#ГАРАНТУ ОП 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Гаранту ОП' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('Гугл Диск ☁️', url='https://rebrand.ly/qaedu_gdrive'),
telebot.types.InlineKeyboardButton('Назад ↩️', callback_data='Інше'))
    photo = open('_garant.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='У цьому розділі ви можете знайти необхідну для <b>гарантів освітніх програм</b>. Зокрема, дізнатися про <a href="https://www.fb.com/department.quality/posts/pfbid04Bgz7TWvU9TPs5ua6o7ALaqC1DQKMNFyB363gPLGQp8kY9VcXDbCu9U1xFqnma16l?__cft__[0]=AZXFLznEK4AvWCFjZ2mHVSvVkAmeFpbrQk4kNqnnPsbAb689a6rmiti0m65Y-2oX3O3Md--sZe7-gqLYl3u_ss4tQVy5PV67PGc8Ywzs-gncDx0Mje4IsOtNiVo39i5CF3AodZAYZSyghQ7aRm-PbnT6koyxYpDcKcvH6dvIhLQ_OBQdaXkTK0cOmARx-yYfDTLg6pu5eMLUCU20dwVnL7Ds&__tn__=%2CO%2CP-R">моніторинг якості освіти</a>. \n\nОкрім цього, ознайомитися з діяльністю <a href="https://fb.com/KNUprofessionals/">КНУ Professionals</a>. \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)

#ГАРАНТУ ОП 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#НПП 👇👇👇

@bot.callback_query_handler(func=lambda x: 'НПП' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('Гугл Диск ☁️', url='https://rebrand.ly/qaedu_gdrive'),
telebot.types.InlineKeyboardButton('Назад ↩️', callback_data='Інше'))
    photo = open('_npp.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='У цьому розділі ви можете знайти необхідну для <b>навчально-педагогічних працівників</b>. Зокрема, переглянути інформацію про посадові інструкції: \n\n👉 <a href="http://senate.univ.kiev.ua/wp-content/uploads/2022/05/%D0%9F%D0%BE%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F-%D0%BF%D1%80%D0%BE-%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA-%D1%80%D0%BE%D0%B7%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F-%D1%96-%D0%B7%D0%B0%D1%82%D0%B2%D0%B5%D1%80%D0%B4%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F-%D0%BF%D0%BE%D1%81%D0%B0%D0%B4%D0%BE%D0%B2%D0%B8%D1%85-%D1%96%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D1%96%D0%B9.pdf">Положення про порядок розроблення і затвердження посадових інструкцій</a> \n\nТакож дізнатися більше про <a href="https://bit.ly/3ocQq1u">академічну доброчесність</a>.\n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)

#НПП 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#ЗДОБУВАЧУ 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Здобувачу' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('Гугл Диск ☁️', url='https://rebrand.ly/qaedu_gdrive'),
telebot.types.InlineKeyboardButton('Назад ↩️', callback_data='Інше'))
    photo = open('_zdobuvach.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='У цьому розділі ви можете знайти необхідну для <b>здобувачів освіти</b>. Зокрема, ознайомитися із тими <a href="http://www.univ.kiev.ua/ua/student-life">можливостями</a>, які надає Київський національний університет студентству. \n\nТакож дізнатися більше про <a href="https://bit.ly/3ocQq1u">академічну доброчесність</a>. \n\nОкрім цього, ознайомитися з нашими дописами щодо таких тем, як: \n\n👉 <a href="https://bit.ly/41kvNzk">Студентоцентризм</a> \n\n👉 <a href="https://bit.ly/41fRJeB">Вільний вибір дисциплін</a>. \n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)

#ЗДОБУВАЧУ 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#СТЕЙКХОЛДЕРУ 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Стейкхолдеру' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('Гугл Диск ☁️', url='https://rebrand.ly/qaedu_gdrive'),
telebot.types.InlineKeyboardButton('Назад ↩️', callback_data='Інше'))
    photo = open('_stakeholder.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='У цьому розділі ви можете знайти необхідну для <b>стейкхолдерів</b>. Зокрема, ознайомитися із положенням про раду роботодавців: \n\n👉 <a href="http://senate.univ.kiev.ua/wp-content/uploads/2020/07/%D0%9F%D0%BE%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F-%D0%BF%D1%80%D0%BE-%D1%80%D0%B0%D0%B4%D0%B8-%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D0%BE%D0%B4%D0%B0%D0%B2%D1%86%D1%96%D0%B2-%D0%9A%D0%9D%D0%A3.pdf">Положення про Раду роботодавців</a>.\n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)

#СТЕЙКХОЛДЕРУ 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#КОНТАКТИ 👇👇👇

@bot.callback_query_handler(func=lambda x: 'Контакти' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('Вебсайт 💻', url='https://qaedu.knu.ua'),
telebot.types.InlineKeyboardButton('Телеграм ✈️', url='https://t.me/qaedu_bot'),
telebot.types.InlineKeyboardButton('Фейсбук 📘', url='https://fb.com/department.quality'),
telebot.types.InlineKeyboardButton('Гугл Диск ☁️', url='https://rebrand.ly/qaedu_gdrive'),
telebot.types.InlineKeyboardButton('Співробітники 👥', callback_data='Співробітники'),
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'))
    bot.send_message(chat_id=query.message.chat.id,
                     text='👇 Нижче подано короткі посилання на наші ресурси (у двох варіантах - посилання та кнопки, обирайте зручніший для себе)\n\n💻 Вебсайт - qaedu.knu.ua\n\n🤖 Цей ТГ-бот - t.me/qaedu_bot\n\n📘 Фейсбук - fb.com/department.quality\n\n☁️ Гугл Диск - rebrand.ly/qaedu_gdrive\n\n✉️ Електронна скринька:\ndepartment_quality@univ.net.ua\n\n📞 Телефонні номери відділу:\n+38(044)239-34-21 \n(а також +38(044)239-37-21)\n\n📍 Знайти нас можна у каб. 223\n(у Червоному корпусі КНУ, що на мапі)\n\n <i>Бот не працює? Натисніть</i> \n/start',
                     parse_mode='html', 
                     reply_markup=step_kb)
    bot.send_location(query.message.chat.id, 50.4420116, 30.5111119)
    bot.send_contact(query.message.chat.id, phone_number=380442393421, first_name='ВЗЯО', last_name='...3421')
    bot.send_contact(query.message.chat.id, phone_number=380442393721, first_name='ВЗЯО', last_name='...3721')
    bot.send_message(chat_id=query.message.chat.id, text='👆 Вище подано короткі посилання на наші ресурси (у двох варіантах - посилання та кнопки, обирайте зручніший для себе) \n\n <i>Бот не працює? Натисніть</i> \n/start', parse_mode='html')

#КОНТАКТИ 👆👆👆


# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#У РОЗРОБЦІ 👇👇👇

@bot.callback_query_handler(func=lambda x: 'У розробці' in x.data)
def exec_step_1(query: telebot.types.CallbackQuery):
    bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  reply_markup=None)
    step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    step_kb.add(
telebot.types.InlineKeyboardButton('На початок 🏠', callback_data='Початок'),
telebot.types.InlineKeyboardButton('Назад ↩️', callback_data='Співробітники'))
    photo = open('nothing.png', 'rb')
    bot.send_photo(query.message.chat.id, photo)
    bot.send_message(chat_id=query.message.chat.id,
                     text='Перепрошуємо, але наразі ця частина боту перебуває в розробці. Ви можете натиснути /start аби повернутися на початок або скористатися кнопками нижче',
                     parse_mode='html', 
                     reply_markup=step_kb)        

#У РОЗРОБЦІ 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =


#ЗАЛИШИТИ СВІЙ НОМЕР БОТУ (початок) 👇👇👇

@bot.message_handler(commands=['mobile'])
def mobile_phone(message):
         kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
         btn1 = types.KeyboardButton(text='☎ Залишити номер телефону ☎', request_contact=True)
         kb.add(btn1)
         photo = open('other.png', 'rb')
         bot.send_photo(message.chat.id, photo)
         bot.send_message(message.chat.id, '📞 Натисність кнопку в нижньому меню аби залишити свій контакт. \n\n <i>Бот не працює? Натисніть</i> \n/start \n\n👇 👇 👇', parse_mode='html', reply_markup=kb)

#ЗАЛИШИТИ СВІЙ НОМЕР БОТУ (початок) 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#ЗАЛИШИТИ СВІЙ НОМЕР БОТУ (кінець) 👇👇👇

@bot.message_handler(content_types=['contact'])
def phone_got(message):
         phone_num_message = bot.send_message(message.chat.id, message.contact.phone_number)
         bot.forward_message(chat_id="-991334486", from_chat_id=message.chat.id, message_id=message.id)
         bot.delete_message(message.chat.id, phone_num_message.id)
         rm_kb = telebot.types.ReplyKeyboardRemove() 
         photo = open('other.png', 'rb')
         bot.send_photo(message.chat.id, photo)
         bot.send_message(message.chat.id, '😊 Дякуємо! Ми зконтактуємо за першої нагоди! \n\n <i>Натисніть</i> /start <i>аби повернутися на початкове меню</i>', parse_mode='html', reply_markup=rm_kb)

#ЗАЛИШИТИ СВІЙ НОМЕР БОТУ (кінець) 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#БОТ НЕ ВІДПОВІДАЄ НА ТЕКСТОВІ ПОВІДОМЛЕННЯ 👇👇👇

#(для перевірки id групи - додати туди бота Get My ID)

@bot.message_handler()
def get_user_text(message):
   if message.text == "":
     bot.send_message(message.chat.id, '🤔 Ви щось написали? \n\n😧 На жаль, у функціоналі цього боту немає відповіді на питання у текстовій формі. \n\n🙂 Однак, Ви можете залишити номер телефону для контакту із Вами. \n\n☎ Для цього натисність на команту нижче:\n👉 /mobile 👈 \n\n🙅 Якщо Ви не хочете ділитися контактом, то можете діяти за наступним алгоритмом: \n\n 1. Почати наново \n 2. Перейти в розділ "Контакти" \n 3. Звязатися зі співробітниками \n (аби вони надали Вам відповідь) \n\n👉 Аби почати наново - натисніть, будь ласка, на /start \n\n✍ Також Ви можете <a href="https://rebrand.ly/qaedu_poll">залишити відгук</a>, якщо жоден із варіантів вище не є прийнятним.', parse_mode='html')
     bot.forward_message(chat_id="-991334486", from_chat_id=message.chat.id, message_id=message.id)
   else:
     bot.send_message(message.chat.id, '🤔 Ви щось написали? \n\n😧 На жаль, у функціоналі цього боту немає відповіді на питання у текстовій формі. \n\n🙂 Однак, Ви можете залишити номер телефону для контакту із Вами. \n\n☎ Для цього натисність на команту нижче:\n👉 /mobile 👈 \n\n🙅 Якщо Ви не хочете ділитися контактом, то можете діяти за наступним алгоритмом: \n\n 1. Почати наново \n 2. Перейти в розділ "Контакти" \n 3. Звязатися зі співробітниками \n (аби вони надали Вам відповідь) \n\n👉 Аби почати наново - натисніть, будь ласка, на /start \n\n✍ Також Ви можете <a href="https://rebrand.ly/qaedu_poll">залишити відгук</a>, якщо жоден із варіантів вище не є прийнятним.', parse_mode='html')
     bot.forward_message(chat_id="-991334486", from_chat_id=message.chat.id, message_id=message.id)

#БОТ НЕ ВІДПОВІДАЄ НА ТЕКСТОВІ ПОВІДОМЛЕННЯ 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =

#БОТ ПРАЦЮЄ ПОСТІЙНО 👇👇👇

bot.polling(none_stop=True)

#БОТ ПРАЦЮЄ ПОСТІЙНО 👆👆👆

# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =
# = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / = / =


# @bot.message_handler(commands=['starter'])
# def starter(message):
#          markup = types.ReplyKeyboardMarkup(row_width=2)
#          markup.add(
#          types.KeyboardButton('Button1'),
#          types.KeyboardButton('Button2'),
#          types.KeyboardButton('Button3'),
#          types.KeyboardButton('Button4'))
#          video = open('logo_wide_gif.mp4', 'rb')
#          bot.send_video(message.chat.id, video)
#          bot.send_message(message.chat.id, 'Доброго дня! Вас вітає Телеграм-бот <a href="https://qaedu.knu.ua">Відділу забезпечення якості освіти </a>. Тут Ви можете дізнатися необхідну інформацію, перейти на інші наші ресурси або просто <a href="https://rebrand.ly/qaedu_poll">залишити відгук</a> \n\n <i>Бот не працює? Натисніть</i> /start', parse_mode='html', reply_markup=markup)

