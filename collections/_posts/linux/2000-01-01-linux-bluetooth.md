---
title: "Linux: Bluetooth"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00
categories:
  - IT

tags:
  - python
  - pycharm
  - jupyter
  - package
  - pandas

---

Inicialmente encontrar os dispositivos conectados

```bash
pactl list | grep -Pzo '.*bluez_card(.*\n)*'
```

<br>

É possível ver que a latência é de zero. Vamos alterar essa configuração!

```bash
# Comando Padrão
pactl set-port-latency-offset <NAME> <PORT> <BUFFER_SIZE_MICROSECONDS>

# Comando Ajustado com as variáveis!
pactl set-port-latency-offset bluez_card.E8_07_BF_01_4D_CD headset-output 50000
```

<br>

Reiniciar o _bluetooth_

```bash
sudo service bluetooth restart
```

<br>

# Referências

- [A2DP on PulseAudio - terrible choppy/skipping audio](https://askubuntu.com/questions/475987/a2dp-on-pulseaudio-terrible-choppy-skipping-audio)
- https://askubuntu.com/questions/589885/automatically-switch-sound-output-device-to-bluetooth-headset-force-to-a2dp-pr
- https://sandalov.org/blog/2146/
