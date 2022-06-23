from mycroft import MycroftSkill, intent_file_handler


class Roadtripmusic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('roadtripmusic.intent')
    def handle_roadtripmusic(self, message):
        self.speak_dialog('roadtripmusic')


def create_skill():
    return Roadtripmusic()

