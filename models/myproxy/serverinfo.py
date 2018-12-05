import random

blacklist = ["::1"] # v6 ip
class ServerInfo():
    def __init__(self, *args, **kwargs):
        self.server_list = ["http://127.0.0.1:5000/"]
        # self.server_list = ["http://127.0.0.1:5000/", "http://149.28.226.57"]

        self.blacklist = []
        return super().__init__(*args, **kwargs)


    def get_servers(self):
        return self.server_list


    def get_random_server(self):
        return self.server_list[random.randint(0, len(self.server_list)-1)]

    def get_blacklist(self):
        return self.blacklist
