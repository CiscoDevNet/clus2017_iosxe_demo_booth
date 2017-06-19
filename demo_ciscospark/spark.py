import requests
from requests.auth import HTTPBasicAuth
import requests.packages.urllib3
import json

proxies = {
	"http":"http://173.36.224.108:8080",
	"https":"https://173.36.224.108:8080"
}

def create_room(room_name, token):
	
	requests.packages.urllib3.disable_warnings()

	headers = {'Authorization':'Bearer '+token,
				'Content-Type':'application/json'}
	body = json.dumps({'title':room_name})

	resp = requests.post('https://api.ciscospark.com/v1/rooms',
	verify=False,headers=headers,data=body)

	print resp

def list_rooms(token):
	
	requests.packages.urllib3.disable_warnings()

	headers = {'Authorization':'Bearer '+token,
				'Content-Type':'application/json'}
	resp = requests.get('https://api.ciscospark.com/v1/rooms',
	verify=False,headers=headers)

	return resp

def get_room_id(room_name, token):

	requests.packages.urllib3.disable_warnings()

	id = ""

	headers = {'Authorization':'Bearer '+token,
				'Content-Type':'application/json'}
	resp = requests.get('https://api.ciscospark.com/v1/rooms',
	verify=False,headers=headers,proxies=proxies)

	if resp.status_code == 200:
		
		rooms = json.loads(resp.text)['items']

		for room in rooms:
			if room['title'] == room_name:
				id = room['id']

	return id

def list_messages(room_id, token):

	requests.packages.urllib3.disable_warnings()

	headers = {'Authorization':'Bearer '+token,
				'Content-Type':'application/json'}
	resp = requests.get('https://api.ciscospark.com/v1/messages?roomId={}'.format(room_id),
						verify=False,headers=headers)
	return resp.text

def post_message(message_text, room_id, token):

	requests.packages.urllib3.disable_warnings()

	headers = {'Authorization':'Bearer '+token,
				'Content-Type':'application/json'}

	body = json.dumps({'roomId':room_id,'text':message_text})

	resp = requests.post('https://api.ciscospark.com/v1/messages',
	verify=False,headers=headers,data=body,proxies=proxies)

	return resp

def post_message_with_image(message_text, img_url, room_id, token):

	requests.packages.urllib3.disable_warnings()

	headers = {'Authorization':'Bearer '+token,
				'Content-Type':'application/json'}

	body = json.dumps({'roomId':room_id,'text':message_text, 'files':img_url})

	resp = requests.post('https://api.ciscospark.com/v1/messages',
	verify=False,headers=headers,data=body)

	return resp

def cleanup_room(room_id, token):

	requests.packages.urllib3.disable_warnings()

	messages = json.loads(list_messages(room_id, token))

	headers = {'Authorization':'Bearer '+token,
				'Content-Type':'application/json'}

	for message in messages['items']:

		resp = requests.delete('https://api.ciscospark.com/v1/messages/{}'.format(message['id']),
					verify=False,headers=headers)
		print resp.status_code



def main():

	room=get_room_id('jeff test room')
	print post_message('Testing 6:32pm',room).status_code
	list_messages(room)

if __name__ == "__main__":

	main()