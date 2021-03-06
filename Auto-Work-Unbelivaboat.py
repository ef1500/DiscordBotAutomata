# Auto Work for Unbelievaboat
# Written by ef1500

import requests
import time
import sys

class yuzu:

    def __init__(self, token, channel, message):
        self.token = token
        self.channel_id = channel
        self.message = message
        self.headers = {'Authorization': token}


    def _generate_message(self, m1):
        return m1


    def execute(self):
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': self._generate_message(self.message)})


def main():
    if len(sys.argv) < 3:
        print(f'Usage: py {sys.argv[0]} <TOKEN> <CHANNEL ID> "MESSAGE"')
        sys.exit()

    token = sys.argv[1]
    channel_id = sys.argv[2]
    message = sys.argv[3]

    epicness = yuzu(token, channel_id, message)
    n = 0
    while n < 100000:
        epicness.execute()
        time.sleep(1812)
        n+=1

if __name__ == '__main__':
    main()

# Best Regards,
#            ~ef1500
#
#             :*******************
#             :M$$MV***********V$M
#               *N$I*          :IF
#                 VN$M*
#                  :V$$I*
#                    *I$$F:
#                      *M$$V           :VFVV*
#                      :VF*:            *VVN$M:
#                    *VV*                  :M$M:
#                 :*V*:                     *N$I:
#               :VV*            :V:          V$$F:
#             *FV*::::::::::::::V$*         V$NN$F:
#            *$$$$$$$$$$$$$$$$$$$$*        *$N**$$V
#             ::::::::::::::::::::        *$N*  V$$*
#                                        *N$*    V$N*
#                                       *$N*      V$N*
#                                      *N$*        F$N*
#                                      :*:          ***
