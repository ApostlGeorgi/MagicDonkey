import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 

token = "vk1.a.uqqH8l7UAu6ld8oCpBsVtsf6M4jpU3VxLEe_TQvru5vaoVl1tNXeOe5GVO4q03zsva6gxcLTOIGpxn6Lfa-hCeJJZJq5o6ZBQGGHrtwx_WTtTPj3O1HFeUA2xxOxnsiWn8WPnweS1BoYoGab9c7v1adgsrWso1XdRaIe56B8T6MvmYbvZHVFUb2rOnbh8iGHLEO6xrADhwpVjRwdTGak_w"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
botLongPool = VkBotLongPoll(vk, 227770673, 25)

def writeUserMsg(from_id, peer_id, random_id, message):
    vk.method('messages.send', {'user_id': from_id, 
                                'message': message, 
                                'random_id' : random_id,
                                'peer_id': peer_id})

    
def writeChatMsg(from_id, peer_id, random_id, message):
    vk.method('messages.send', {'from_id': from_id, 
                                'message': message, 
                                'random_id' : random_id,
                                'peer_id': peer_id})

def listenMessage():
        # Основной цикл
    for event in botLongPool.listen():
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW:
        
            # Если оно имеет метку для меня( то есть бота)
            if event.from_chat:  
                if(event.object.message['text'].lower().find('каст') != -1):          
                    writeChatMsg(event.object.message['from_id'],
                                event.object.message['peer_id'], 
                                event.object.message['random_id'], 
                                'ты не достоин кастовать')
                      
                if(event.object.message['text'].lower().find('кида') != -1):          
                    writeChatMsg(event.object.message['from_id'],
                                event.object.message['peer_id'], 
                                event.object.message['random_id'], 
                                'Кидай столовые принадлежности: ' + str(random.randint(1, 20)))
                    
            elif event.from_user:
                writeUserMsg(event.object.message['from_id'],
                             event.object.message['peer_id'], 
                             event.object.message['random_id'], 
                             event.object.message['text'])

            
        else:
             writeUserMsg(event.object.message['from_id'],
                             event.object.message['peer_id'], 
                             event.object.message['random_id'], 
                             'иди нахуй')


listenMessage()