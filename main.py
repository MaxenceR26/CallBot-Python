import vonage


class CallBot:
    def __init__(self):
        with open("private.key", 'r') as file:
            self.client = vonage.Client(
                application_id="YOUR APPLICATION ID",
                private_key=file.read(),
            )

        self.voice = vonage.Voice(self.client)

        self.response = self.voice.create_call({
            'to': [{'type': 'phone', 'number': "yourphonenumber"}],
            'from': {'type': 'phone', 'number': "yourphonenumber"},
            'ncco': [{'action': 'talk', 'text': 'Hello, my name is Maxence, and I am on call with you with a computer'}]
        })

        if self.response['status'] == 'started':
            print("L'appel a commencer !")
        else:
            print("L'appel n'a pas pus commencer !")


CallBot()
