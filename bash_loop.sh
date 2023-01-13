#!/bin/bash

_NODE_NAMES=( \
"maroon" "olive" "green" "teal" "navy" "purple" "black" "silver" "white" "gray" "red" "yellow" "lime" "aqua" "blue" "fuchsia" \
"Leiy1uXu" "ooth3AiJ" "thieB6Qu" "pae2xeeP" "OVeej8sh" "jooroh4N" "Ibai1pha" "keeZ9phe" \
"eiYo3dae" "chu5Ziep" "Eevae6vo" "ulai8iiD" "Ieya7aic" "kaiJoa4r" "aVoh8aip" "achuph6I" \
"phee4Aip" "unah5Oe5" "daisei1E" "gaaD0oom" "Ooca4ouy" "eePhohr3" "Cheeh3Se" "Kie9iedo" \
"eZ5aCae5" "yokaeNg6" "Aeho6uTa" "foh7UTho" "iLeegh1A" "en0Bie9l" "quooQu3e" "naiS7aeb" \
"eeS4uotu" "wae4Ooye" "ho1eey5A" "Waquae0I" "ieth5Phe" "daeN1aew" "pee0Jer3" "aeteiC3m" \
"Egoox2ee" "poo0Ita3" "Acea2oof" "Quai8ush" "chahth7V" "chaeX6Ei" "AeM0aeng" "ohV3lu7e" \
"eeK1ieSo" "Uk1eng4S" "einahTh2" "PhieZ4om" "yanoh2Ju" "Gaethee6" "Eowoh0mo" "uCheung1" \
"eeMi2cei" "oGaux2Di" "Eihooj9a" "edeec8Ba" "woebaT7x" "aeg1Uo6N" "Zi3ahnga" "Eungeel9" \
"Beeyah7s" "ti2Aitai" "jah6Eetu" "Yohgahk3" "Eo3ieboy" "Aed2thie" "ih1Iilae" "ooThoh1s" \
"Wie7Aphe" "iBohh4ah" "woh0ohN0" "lui0Moru" "Yinie9Da" "De9foh5F" "Eilo7AeY" "Thoor8he" \
"Ohr0fa5c" "suSee1lo" "phoD5iu3" "Ahj3Ieco" "eeNg8ieb" "Aiyay7Ph" "EeJieph2" "gaJaTh2j" \
"Iej8ohti" "rou3ieG4" "we3Chooy" "pie1eiG6" "AeDe1Rie" "Aweo7dai" "zorahn4U" "Eeh6ok7w" \
"mi3Aiwue" "Na2nie8b" "OoXoL5ee" "pho6Agh0" "oht6Mahc" "Jooch4Ae" "thi1shuC" "ikohpuK4" \
"aK5aaqu1" "ahk8Noow" "vee0Soa4" "nauca5Ee" "OJi1queb" "ohH2Shie" "eaJ7chei" "HeiR6Mai" \
"eigo0Gu5" "Pof3iu3a" "uch7Ziti" "ieXoH4oo" "Ceiy1quo" "CaeV4eiS" "Ohpaix3U" "iech2Goo" \
"Iash7lee" "aiwaWia1" "ija1Ducu" "Ahr7liph" "gi2uWai6" "aePh6AhF" "wo4moo6Z" "aiv3WooY" \
"hoo0ooKu" "oP6ook3k" "ein3AhDa" "kookoo9I" "Igh8xoom" "dae7eo2I" "fieZ5nah" "vei2thaB" \
"PheiGh1v" "Evaeh8na" "Wa5ahthe" "iuN2xa7c" "sae8Lahp" "Nahnai7L" "eeLe1zai" "xiech5aS" \
"IeNikic5" "Faju9pom" "Shoj3loh" "aoB7main" "Shoive9l" "Dieth0ae" "she7AhP5" "Kahmae0A" \
"Fa6maedi" "Jii8ahpa" "ooGh9eap" "Je4goh5v" "Gah5ohS3" "eiShej6U" "yoh4Zaez" "vah2APiK" \
)
_YAGNA_API_PORT_BASE=17000
_GSB_PORT_BASE=18000
_NET_PORT_BASE=23000
_YAGNA_DATADIR_BASE="/home/ubuntu/.local/share/yagna-"
_DATA_DIR_BASE="/home/ubuntu/.local/share/ya-provider-"

_SUBNET="sdk"
_PAYMENT_NETWORK="testnet"

function launch_provider () {
  local i=$1
  local node_name=${_NODE_NAMES[i]}
  YAGNA_API_URL=http://0.0.0.0:$((_YAGNA_API_PORT_BASE+i))
  GSB_URL=tcp://127.0.0.1:$((_GSB_PORT_BASE+i))
  NODE_NAME=${node_name}
  YA_NET_BIND_URL=udp://0.0.0.0:$((_NET_PORT_BASE+i))
  YAGNA_DATADIR=${_YAGNA_DATADIR_BASE}${node_name}
  DATA_DIR=${_DATA_DIR_BASE}${node_name}
  golemsp run --payment-network ${_PAYMENT_NETWORK} --subnet ${_SUBNET}
}

launch_provider $1
