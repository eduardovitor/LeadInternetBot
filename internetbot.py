import slack
import os
import speedtest

SLACK_TOKEN=os.environ["SLACK_TOKEN"]
CHANNEL="#internet-bot"

try:
    st = speedtest.Speedtest()
    down_speed = st.download()
    down_speed_megabits= str(round(down_speed/1000000, 2))
    msg="Olá eu sou o NetBot \n" + "A velocidade atual da internet do Lead é de {} Mbps".format(down_speed_megabits)
    client = slack.WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel=CHANNEL,text=msg)
except:
    msg="Olá eu sou o NetBot \n" + "Não consegui calcular a velocidade da internet devido a uma falha no meu servidor"
    client = slack.WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel=CHANNEL,text=msg)

