This little project aims at allowing voice command through Google Assistant to manipulate Orange TV.
Alexa should also work, but I did not try it.

You can shutdown the OrangeTV, switch over using channel number or its name. 
Note that switching to a channel automatically swith on the Orange TV (epg only).

Most of the informations on how to do it have been retrieve through orange community effort, 
reading this topic (https://communaute.orange.fr/t5/TV-par-ADSL-et-Fibre/API-pour-commander-le-decodeur-TV-depusi-une-tablette/td-p/43443/page/1). 
Long story short, it is possible to control the Orange TV with HTTP requests 
if they come from the same local network. This code just provide a http server that you need to run on your 
local network and expose to the internet (typically by doing a NAT redirection). 
Then, use ifttt.com to create 3 Applets.

# Get prepared

- Python 3
- Fixed IP for Orange TV (with default dns name : tvorange)
- Dynamic DNS to access your local network
- A computer (able to run python3, a Pi will do for example) with port 5000 exposed through NAT.

# Install and launch the server

```
git clone https://github.com/jm-cc/orangetv.git
cd orangetv
pip3 install .
```
This will install a tvorange executable, which may or may not be in your path.

Regardless of that, you can launch the server using :
`python3 -m orangetv.server`

# IFTTT Applets

You just need 3 Applets.

```
If 
(This) Google Assistant (or Alexa)
Then 
(That) Webhook
```

## Switch off
- URL : `http://<hostname>:<port>/switch_off`
- Method : GET

## Switch with channel name
- Say a phrase with a text ingredient
- URL :  `http://<hostname>:<port>/channel_name`
- Method : POST
- Content Type : text/plain
- Body : TextField (**Use Add ingredient!**)

## Switch with channel number
- Say a phrase with a number
- URL : `http://<hostname>:<port>/channel/#NumberField#` (Use **Add ingredient** for NumberField.)
- Method : GET





