import random


# Todas las cartas de excusa del juego
cartasExcusa = [
    {
        "Titulo": "Goblin Lerdo",
        "Descripcion": "Cuchi cuchi... Que lindo minino, se bueno y dame la patita",
    },
    {
        "Titulo": "La llave",
        "Descripcion": "Shalma-Ne, guardiana de las llaves de la Torre de la Hechiceria Oscura",
    },
    {
        "Titulo": "El otro Señor Oscuro",
        "Descripcion": "Maestro Karnaky, El Mago-Diablo y Kex, Discipulo de Pazuzu",
    },
    {
        "Titulo": "Chinchetas",
        "Descripcion": "El sabio Esagrod dice: ten cuidado con donde pones los pies...",
    },
    {
        "Titulo": "El comerciante tramposo",
        "Descripcion": "Gonat, el vendedor de basura, el mercader mas habil de Mor-Ankharas",
    },
    {
        "Titulo": "La isla salvaje",
        "Descripcion": "Las islas de plata, temperatura agradable, playas soleadas y mar en calma",
    },
    {
        "Titulo": "La espada soluble en agua",
        "Descripcion": "Nardaruss, la siniestra arma de Nya-Khebo",
    },
    {
        "Titulo": "La taberna",
        "Descripcion": "Ergus, propietario de la taberna del Loco que Grita",
    },
    {
        "Titulo": "El bosque oscuro",
        "Descripcion": "Bosque Salah-E-Diel, hogar de los elfos Drill",
    },
    {
        "Titulo": "El insecto molesto",
        "Descripcion": "Capitan Bolb Sisco, solo tu puedes salvar el multiverso",
    },
    {
        "Titulo": "El placido rio",
        "Descripcion": "Nineveh, el rio de los goblins",
    },
    {
        "Titulo": "La hierba del sueño",
        "Descripcion": "Caballo Loco, elfo de los bosques renegado y fumador empedernido de la hierba del sueño",
    },
    {
        "Titulo": "La momia",
        "Descripcion": "Aphotecymon XVII, el faraon",
    },
    {
        "Titulo": "El hombre viejo y rapaz",
        "Descripcion": "Esagrod, el viejo sabio con plumas",
    },
    {
        "Titulo": "El lugar equivocado",
        "Descripcion": "El paso del diablo",
    },
    {
        "Titulo": "Zombies!",
        "Descripcion": "Los siniestros sirvientes de Seth Amoth",
    },
    {
        "Titulo": "La elfa siniestra",
        "Descripcion": "Odium Kah, la glacial y misteriosa dama de las posibilidades",
    },
    {
        "Titulo": "La tropa prescindible",
        "Descripcion": "Los voluntariosos discipulos del senor oscuro",
    },
    {
        "Titulo": "El desolado desierto",
        "Descripcion": "Nefanko, el inhospito desierto de Kah-Nurek",
    },
    {
        "Titulo": "La belleza exotica",
        "Descripcion": "Nixel la silfide, virgen de las aguas",
    },
    {
        "Titulo": "El mapa",
        "Descripcion": "Otro de los innecesarios mapas de Gonat, el vendedor de basura",
    },
    {
        "Titulo": "La torre solitaria",
        "Descripcion": "La torre de Hechiceria Oscura, la secreta morada de Rigor Mortis",
    },
    {
        "Titulo": "La calavera",
        "Descripcion": "Tiembla, pues siempre tengo un ojo puesto en ti",
    },
    {
        "Titulo": "La cerveza enana",
        "Descripcion": "Guenzor Barbatrenzada, destilador de la mejor cerveza enana de Kathadin del Sur",
    },
    {
        "Titulo": "El tomo ululante",
        "Descripcion": "Tratado de magia negra, malvado y mendaz",
    },
    {
        "Titulo": "La puerta",
        "Descripcion": "La entrada parlante a la Torre Oscura",
    },
    {
        "Titulo": "La mazmorra oscura",
        "Descripcion": "Las sombrias prisiones entre dos mundos de Ghorn-Arra",
    },
    {
        "Titulo": "Oro!",
        "Descripcion": "Un goblin feliz es un goblin con una sonrisa reluciente",
    },
    {
        "Titulo": "El arbol milenario",
        "Descripcion": "Yrn-Dah-Uggil, el arbol sagrado de los elfos Drill",
    },
    {
        "Titulo": "La bola de cristal",
        "Descripcion": "Bardak el Negro, senor de los demonios",
    },
    {
        "Titulo": "El fantasma aterrador",
        "Descripcion": "Rey Thearsus IV, el fantasma del primer monarca unificador",
    },
    {
        "Titulo": "El cofre cerrado",
        "Descripcion": "Donde se rompen los suenos de los heroes",
    },
    {
        "Titulo": "La ciudad flotante",
        "Descripcion": "La ciudad libre de Kadath",
    },
    {
        "Titulo": "El hechicero del Este",
        "Descripcion": "Nak Nang-Klao, el mistico profesor de artes marciales de Ng Fang",
    },
    {
        "Titulo": "La pocion misteriosa",
        "Descripcion": "Otra de las enganosas pociones de Gonat, el vendedor de basura",
    },
    {
        "Titulo": "El templo en ruinas",
        "Descripcion": "Los sagrados lugares de la antigua religion de la Madre Tierra",
    },
    {
        "Titulo": "",
        "Descripcion": "",
    },
    {
        "Titulo": "",
        "Descripcion": "",
    },
    {
        "Titulo": "",
        "Descripcion": "",
    }
]
