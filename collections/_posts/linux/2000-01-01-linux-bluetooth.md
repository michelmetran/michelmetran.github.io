---
title: "Linux: <i>bluetooth</i>"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00
toc: false
classes: wide
categories:
  - IT
tags:
  - bluetooth
  - hardware
  - sound
---

Em um dado momento o meu fone de ouvido, _bluetooth_, passou a apresentar problemas na conexão com o Sistema Operacional Ubuntu.
Dessa forma, visando solucionar o problema, após pesquisar, fiz o seguinte:

Inicialmente encontrar os dispositivos conectados:

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
- [Automatically switch sound output device to Bluetooth headset & force to A2DP profile on connection](https://askubuntu.com/questions/589885/automatically-switch-sound-output-device-to-bluetooth-headset-force-to-a2dp-pr)
- [Auto switch to A2DP bluetooth device when connected in Ubuntu](https://sandalov.org/blog/2146/)
