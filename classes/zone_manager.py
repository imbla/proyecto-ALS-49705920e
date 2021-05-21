zones = {
    "intro" : {
            "es": {
                 "name": "intro, parte 1",
                 "text": "2050. Las plantas han mutado de manera extrema debido a varios factores, todos culpa del gobierno. El polen se ha incrementado, convirtiendose en la nueva especie dominante del planeta.",
                 "image": "images/ciudad.jpeg",
                 "options": {"continuar": "intro1"}
             },
            "en": {
                 "name": "intro, part 1",
                 "text": "2050. Plants have mutated in an extreme way due to several factors, all of them involving the government. Pollen has increased to the point of becoming Earth's new dominant species.",
                 "image": "images/ciudad.jpeg",
                 "options": {"continue": "intro1"}
             }
        },
   "intro1" : {
            "es": {
                 "name": "intro, parte 2",
                 "text": "La civilizacion humana continua, porque mala hierba nunca muere. La gente con alergia al polen ha sido declarada como prescindible, debido a su tendencia a ser consumidos por el polen mas rapido que el resto de humanos.",
                 "image": "images/ciudad.jpeg",
                 "options": {"continuar": "intro2"}
             },
            "en": {
                 "name": "intro, part 2",
                 "text": "Human civilization continues because we are reaaally stubborn. People with pollen allergies have been deemed as disposable, due to their lower resistance to pollen compared to non-allergic humans.",
                 "image": "images/ciudad.jpeg",
                 "options": {"continue": "intro2"}
             }
        },
   "intro2" : {
            "es": {
                 "name": "almacen",
                 "text": "Dicha gente alergica es abandonada en cuidades viejas. Tu eres uno de ellos. Te acabas de despertar en medio de un almacen. Todas las cajas estan rotas o vacias, anulando cualquier logica de videojuego que se les pudiera aplicar.",
                 "image": "images/almacen.jpeg",
                 "options": {"salir por la ventana": "almacen_ventana","salir por la puerta": "almacen_puerta","no hacer nada": "almacen_esperar"}
             },
            "en": {
                 "name": "storage",
                 "text": "Said allergic people have been left behind on old cities. You are one of them. You have woken up in a storage. All the crates are broken or empty, cancelling all videogame logic that you could apply to them",
                 "image": "images/almacen.jpeg",
                 "options": {"exit through the window": "almacen_ventana","exit through the door": "almacen_puerta","do nothing": "almacen_esperar"}
             }
        },
   "almacen_esperar" : {
            "es": {
                 "name": "almacen",
                 "text": "Decides permanecer en el almacen. Notas unos periodicos convenientemente tirados en el suelo. Las noticias tratan sobre gente quejica protestando sobre demasiado polen y sobre canciones nuevas, la mas popular siendo 'AAAAAAAAAAAAAAAAHHHHHHH'.",
                 "image": "images/almacen.jpeg",
                 "options": {"salir por la ventana": "almacen_ventana","salir por la puerta": "almacen_puerta","no hacer nada": "almacen_esperar"}
             },
            "en": {
                 "name": "storage",
                 "text": "You decide to do nothing. You notice some conveniently placed newspapers in the floor. The news focus on whiny people complaining about too much pollen and the new songs, the most popular being 'AAAAAAAAAAAAAAAAHHHHHHH'",
                 "image": "images/almacen.jpeg",
                 "options": {"exit through the window": "almacen_ventana","exit through the door": "almacen_puerta","do nothing": "almacen_esperar"}
             }
        },
   "almacen_ventana" : {
            "es": {
                 "name": "ventana",
                 "text": "Pese a la presecia de una puerta, decides salir por la ventana. Al cuerno la logica, esto es una zona post-apocaliptica! La ventana da a una calle lo suficientemente abandonada como para intimidarte.",
                 "image": "images/calle.jpeg",
                 "options": {"volver al almacen": "almacen_esperar","avanzar": "calle_persona_alergica"}
             },
            "en": {
                 "name": "window",
                 "text": "Despite the presence of a door, you decide to exit through the window. Screw logic, this is a post-apocalyptic wasteland! The window leads to a street, which is abandoned enough to feel sinister.",
                 "image": "images/calle.jpeg",
                 "options": {"go back to the storage": "almacen_esperar","go forward": "calle_persona_alergica"}
             }
        },
   "calle_persona_alergica" : {
            "es": {
                 "name": "calle",
                 "text": "Una persona siniestra bloquea el camino. Notas que es victima del polen, ya que 34% de su masa corporal es moco. ",
                 "image": "images/calle.jpeg",
                 "options": {"hablar con el desconocido": "desconocido_charla","rodear al desconocido y avanzar": "helicoptero_gobierno","volver atras": "almacen_ventana"}
             },
            "en": {
                 "name": "street",
                 "text": "A sinister peron blocks the path forward. You notice they are a victim of the pollen since 34% of their bodyweight has become snot.",
                 "image": "images/calle.jpeg",
                 "options": {"talk to the stranger": "desconocido_charla","walk arround the stranger and move forward": "helicoptero_gobierno","go back": "almacen_ventana"}
             }
        },
   "desconocido_charla" : {
            "es": {
                 "name": "desconcido amocarrado",
                 "text": "El desconocido intenta comunicarse, pero solo logra emitir sonidos nasales interrumpidos por estornudos cada 2.1468794 segundos.",
                 "image": "images/calle.jpeg",
                 "options": {"hablar con el desconocido": "desconocido_charla","rodear al desconocido y avanzar": "helicoptero_gobierno","volver atras": "almacen_ventana"}
             },
            "en": {
                 "name": "stranger with a cold",
                 "text": "The stranger tries talking with you, but they only manage to make nasal noises interrumpted by a sneeze every 2.1468794 seconds.",
                 "image": "images/calle.jpeg",
                 "options": {"talk to the stranger": "desconocido_charla","walk arround the stranger and move forward": "helicoptero_gobierno","go back": "almacen_ventana"}
             }
        },
   "helicoptero_gobierno" : {
            "es": {
                 "name": "helicoptero",
                 "text": "Un helicoptero es visible a lo lejos. Tiene el simbolo del gobierno pro-supremacia-nasal, los culpables de esta situacion.",
                 "image": "images/helicoptero.jpeg",
                 "options": {"insultarles": "helicoptero_ataque","avanzar sigilosamente": "pabellon"}
             },
            "en": {
                 "name": "helicopter",
                 "text": "A helicopter can be seen in the distance. It has the pro-nasal-supremacy government's symbol, the ones to blame for all of this.",
                 "image": "images/helicoptero.jpeg",
                 "options": {"insult them": "helicoptero_ataque","go forward stealthily": "pabellon"}
             }
        },
    "helicoptero_ataque": {
        "es": {
            "name": "te han pillado...",
            "text": "Insultas a los pilotos del helicoptero con una diversidad espectacular de palabrotas. Responden enviando a soldados contra ti. Antes de que puedas reaccionar, te dan un golpe en la cabeza. Antes de desmayarte, les oyes decir algo sobre gente alergica...",
            "image": "images/helicoptero.jpeg",
            "options": {"continuar": "intro2"}
        },
        "en": {
            "name": "they found you...",
            "text": "You insult the helicopter's pilots with an impressive variety of swear words. They reply by sending soldiers at you. Before you can react, one of them hits you in the head. Before fainting, you hear them saying something about allergic people..",
            "image": "images/helicoptero.jpeg",
            "options": {"continue": "intro2"}
        }
    },
    "pabellon": {
        "es": {
            "name": "Pabellon",
            "text": "Entras a un pabellon lleno de gente amocarrada. Te estan mirando. Quieren preguntarte algo, o al menos es lo que das entendido. El moco les hace dificil hablar.",
            "image": "images/pabellon.jpeg",
            "options": {"hablar": "pregunta1","volver atras": "calle_persona_alergica"}
        },
        "en": {
            "name": "Pavilion",
            "text": "You enter a pavillion filled with allergic people. They stare at you. They want to ask you something, or that's what you understand. The snot makes speaking hard for them.",
            "image": "images/pabellon.jpeg",
            "options": {"talk with them": "pregunta1","go back": "calle_persona_alergica"}
        }
    },
    "pregunta_mal": {
        "es": {
            "name": "Pabellon",
            "text": "Has respondido mal. Los desconocidos expresan su decepcion con sonidos nasales tristes.",
            "image": "images/pabellon.jpeg",
            "options": {"continuar": "pabellon"}
        },
        "en": {
            "name": "Pavilion",
            "text": "You answer is wrong. The strangers express their disappointment with sad nasal noises.",
            "image": "images/pabellon.jpeg",
            "options": {"continue": "pabellon"}
        }
    },
    "pregunta1": {
        "es": {
            "name": "Quiz",
            "text": "'Por que los desconocidos de la carretera llevan armaduras?'",
            "image": "images/pabellon.jpeg",
            "options": {"para combate": "pregunta_mal", "por moda": "pregunta2", "por comodidad": "pregunta_mal"}
        },
        "en": {
            "name": "Quiz",
            "text": "'Why do the road strangers wear armor?'",
            "image": "images/pabellon.jpeg",
            "options": {"for combat": "pregunta_mal", "for fashion": "pregunta2", "for comfiness": "pregunta_mal"}
        }
    },
    "pregunta2": {
        "es": {
            "name": "Quiz",
            "text": "'Por que nos abandono el gobierno?'",
            "image": "images/pabellon.jpeg",
            "options": {"alergias": "pregunta3", "mocos": "pregunta_mal", "tos": "pregunta_mal", "estornudos": "pregunta_mal"}
        },
        "en": {
            "name": "Quiz",
            "text": "'Why do the road strangers wear armor?'",
            "image": "images/pabellon.jpeg",
            "options": {"allergies": "pregunta3", "snot": "pregunta_mal", "cough": "pregunta_mal", "sneezing": "pregunta_mal"}
        }
    },
    "pregunta3": {
        "es": {
            "name": "Quiz",
            "text": "'A donde llevan los tuneles del metro abandonado'",
            "image": "images/pabellon.jpeg",
            "options": {"al bosque": "pregunta_mal", "al hospital": "pregunta_mal", "a varios sitios": "final3", "a la calle": "pregunta_mal", "aqui": "pregunta_mal"}
        },
        "en": {
            "name": "Quiz",
            "text": "'Where do the abandonned metro's tunnel lead to?'",
            "image": "images/pabellon.jpeg",
            "options": {"the forest": "pregunta_mal", "the hospital": "pregunta_mal", "several places": "final3", "the street": "pregunta_mal", "here": "pregunta_mal"}
        }
    },
    "final3": {
        "es": {
            "name": "FINAL 3 de 3  -  Rey de los Alergicos",
            "text": "Tras completar un desafio intelectual de dudosa calidad, eres coronado rey. Tu reinado dura unos cuantos minutos antes de que el polen te consuma, pero fueron unos minutos bastante alegres.",
            "image": "images/rey.jpeg",
            "options": {}
        },
        "en": {
            "name": "ENDING 3 of 3  -  King of the Allergic",
            "text": "After beating an intelectual challenge of doubtful quality, you are crowned king. You rule last a few minutes before you are consumed by the pollen, but they were some neat minutes.",
            "image": "images/rey.jpeg",
            "options": {}
        }
    },
    "almacen_puerta": {
        "es": {
            "name": "Carretera",
            "text": "Sales a la calle. Un grupo de gente con armaduras se acerca conduciendo un coche especialmente ruidoso. No parecen muy amigables...",
            "image": "images/carretera.jpeg",
            "options": {"huir": "parque", "luchar": "guarida", "volver atras": "almacen_esperar"}
        },
        "en": {
            "name": "Carretera",
            "text": "You are in the street. Several people with armor driving an espeacially noisy car are coming closer. They don't look very friendly...",
            "image": "images/carretera.jpeg",
            "options": {"run away": "parque", "fight": "guarida", "go back": "almacen_esperar"}
        }
    },
    "guarida": {
        "es": {
            "name": "Guarida",
            "text": "La pelea dura 14 segundos, el tiempo que necesitaron para dejarte inconsciente despues de que intentaras atacarles. Te despiertas en su guarida. Uno de ellos enta cerca de ti, pero no te presta atencion.",
            "image": "images/guarida.jpeg",
            "options": {"huir sigilosamente": "barrio", "hablar con el bandido": "batallita1"}
        },
        "en": {
            "name": "Lair",
            "text": "The fight lasts 14 seconds, the time need by them to leave you unconscious after you tried attacking them. You wake up in their lair. One of them is near you, but they don't pay attention to you.",
            "image": "images/guarida.jpeg",
            "options": {"flee stealthily": "barrio", "talk with the bandit": "batallita1"}
        }
    },
    "batallita1": {
        "es": {
            "name": "Guarida",
            "text": "Le preguntas al bandido que van ha hacer contigo. 'Pues no se, tu atacaste primero, asi que esto es mas o menos una medida de seguridad. Me recuerda a una vez que estaba en la mili...'",
            "image": "images/guarida.jpeg",
            "options": {"continuar": "batallita2"}
        },
        "en": {
            "name": "Lair",
            "text": "You ask the bandit what are they going to do with you. 'I don't know, you kinda attacked first, so this is some sort of cautionary protocol. It reminds me of that time when I was in the Navy...'",
            "image": "images/guarida.jpeg",
            "options": {"continue": "batallita2"}
        }
    },
    "batallita2": {
        "es": {
            "name": "Guarida",
            "text": "El bandido continua hablando sobre la mili. Han pasado 3 horas. Todas sus historias tienen que ver con el ejercito intentando detonar el polen.",
            "image": "images/guarida.jpeg",
            "options": {"continuar": "batallita3"}
        },
        "en": {
            "name": "Lair",
            "text": "The bandit keeps talking about their time in the Navy. 3 hours have passed. All of their stories are related to the army trying to blow the pollen up.",
            "image": "images/guarida.jpeg",
            "options": {"continue": "batallita3"}
        }
    },
    "batallita3": {
        "es": {
            "name": "Guarida",
            "text": "16 horas. Ya no reconoces el sonido de las palabras. Todas suenan igual, y deletran m-i-l-i.",
            "image": "images/guarida.jpeg",
            "options": {"continuar": "disculpa"}
        },
        "en": {
            "name": "Lair",
            "text": "16 hours. You can't recognize the sound of words. All sound the same, and spell n-a-v-y.",
            "image": "images/guarida.jpeg",
            "options": {"continue": "disculpa"}
        }
    },
    "disculpa": {
        "es": {
            "name": "Guarida",
            "text": "Ya no puedes mas. Le pides al bandido que pare. 'Bandido? Ah, la armadura... solo la llevamos por moda post-apocaliptica. Tambien somos alergicos abandonados. Perdona por el susto, puedes salir si quieres. Esto me recuerda a aquella vez que...'",
            "image": "images/guarida.jpeg",
            "options": {"SALIR YA": "barrio"}
        },
        "en": {
            "name": "Lair",
            "text": "You can't take it anymore. You ask the bandit to stop. 'Bandit? Oh, the armor... we only wear them for post-apocalyptic fashion. We are also abandonned allergics! Sorry about this, you can leave if you want. Hey, this reminds me of that one time...'",
            "image": "images/guarida.jpeg",
            "options": {"LEAVE NOW": "barrio"}
        }
    },
    "barrio": {
        "es": {
            "name": "Barrio residencial",
            "text": "Llegas a un barrio residencial. Una victima del polen descansa en un banco. Te esta mirando. Puedes ver un camino hacia un bosque a lo lejos.",
            "image": "images/barrio.jpeg",
            "options": {"hablar con el desconocido": "batallitasB", "ir al bosque": "bosque1", "caminar sin rumbo": "parque"}
        },
        "en": {
            "name": "Residential area",
            "text": "You arrive to a residential area. One victim of the pollen rest in a bench. They stare at you. You can see a path to the forest in the distance.",
            "image": "images/barrio.jpeg",
            "options": {"talk with the stranger": "batallitasB", "go to the forest": "bosque1", "wander around": "parque"}
        }
    },
    "batallitasB": {
        "es": {
            "name": "Barrio residencial",
            "text": "Antes de que puedas decir algo, el desconocido comienza a hablar. Su boca esta tan seca que todo lo que entiendes es 'hrdsjubcdhau', junto a varias palabrotas.",
            "image": "images/barrio.jpeg",
            "options": {"hablar con el desconocido": "batallitasB", "ir al bosque": "bosque1", "caminar sin rumbo": "parque"}
        },
        "en": {
            "name": "Residential area",
            "text": "Before you can say anything, the strangers begins talking. Their mouth is so dry that all you can understand is 'hrdsjubcdhau', alongside several swear words.",
            "image": "images/barrio.jpeg",
            "options": {"talk with the stranger": "batallitasB", "go to the forest": "bosque1", "wander around": "parque"}
        }
    },
    "bosque1": {
        "es": {
            "name": "Bosque",
            "text": "Entras en el bosque. Un silencio siniestro te da la bienvenida.",
            "image": "images/bosque.jpeg",
            "options": {"avanzar": "bosque2", "retroceder": "barrio"}
        },
        "en": {
            "name": "Forest",
            "text": "You enter the forest. A sinister silence greets you.",
            "image": "images/bosque.jpeg",
            "options": {"go forward": "bosque2", "go back": "barrio"}
        }
    },
    "bosque2": {
        "es": {
            "name": "Bosque",
            "text": "Sigues caminando. Los unicos animales que sobreviven aqui son abejas. No reaccionan a tu presencia.",
            "image": "images/bosque.jpeg",
            "options": {"avanzar": "bosque3", "retroceder": "bosque1"}
        },
        "en": {
            "name": "Forest",
            "text": "You keep walking. The only animals that live here are bees. They don't react to your presence.",
            "image": "images/bosque.jpeg",
            "options": {"go forward": "bosque3", "go back": "bosque1"}
        }
    },
    "bosque3": {
        "es": {
            "name": "Bosque",
            "text": "Pierna izquierta, pierna derecha, pierna izquierta, pierna derecha, pierna izquierta, siesta de 4 horas...",
            "image": "images/bosque.jpeg",
            "options": {"avanzar": "bosque4", "retroceder": "bosque2"}
        },
        "en": {
            "name": "Forest",
            "text": "Left leg, right leg, left leg, right leg, left leg, right leg, left leg, 4 hour nap...",
            "image": "images/bosque.jpeg",
            "options": {"go forward": "bosque4", "go back": "bosque2"}
        }
    },
    "bosque4": {
        "es": {
            "name": "Bosque",
            "text": "La salida esta cerca.",
            "image": "images/bosque.jpeg",
            "options": {"avanzar": "bosque5", "retroceder": "bosque3"}
        },
        "en": {
            "name": "Forest",
            "text": "The exit is near.",
            "image": "images/bosque.jpeg",
            "options": {"go forward": "bosque5", "go back": "bosque3"}
        }
    },
    "bosque5": {
        "es": {
            "name": "Bosque",
            "text": "Vale, me equivoque. Perdon.",
            "image": "images/bosque.jpeg",
            "options": {"avanzar": "final2", "retroceder": "bosque4"}
        },
        "en": {
            "name": "Forest",
            "text": "Oh, I was wrong. Sorry.",
            "image": "images/bosque.jpeg",
            "options": {"go forward": "final2", "go back": "bosque4"}
        }
    },
    "final2": {
        "es": {
            "name": "FINAL 2 de 3 - Al fin un lugar decente.",
            "text": "Llegas a un refugio abandonado. En el, encuentras una mascarilla que logra protegerte del polen. Decides quedarte. El resto de tu vida es tranquilo y lleno de siestas.",
            "image": "images/refugio.jpeg",
            "options": {}
        },
        "en": {
            "name": "ENDING 2 of 3 - A nice place at least.",
            "text": "You arrive to an abandonned shelter. You find a face mask that protects you from the pollen there. You decide to stay. The rest of you life is calm and full of naps.",
            "image": "images/refugio.jpeg",
            "options": {}
        }
    },
   "parque" : {
            "es": {
                 "name": "Parque",
                 "text": "Llegas a un parque tranquilo. Si no fuera por las cantidades industriales de polen, seria una vista agradable. Puedes ver la entrada a una estacion de metro cerca.",
                 "image": "images/parque.jpeg",
                 "options": {"continuar": "metro"}
             },
            "en": {
                 "name": "Park",
                 "text": "You arrive at a quiet park. It would be a nice view, but the industrial amounts of pollen kinda ruin it. You can see the entrance to a subway station nearby.",
                 "image": "images/parque.jpeg",
                 "options": {"continue": "metro"}
             }
        },
   "metro" : {
            "es": {
                 "name": "Tuneles",
                 "text": "Entras en el metro. No hay ningun tren a la vista, y la via esta cerrada. Sin embargo, 2 tuneles estan abiertos...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunel A": "tunelA","tunel B": "tunelB","volver atras": "parque"}
             },
            "en": {
                 "name": "Tunnels",
                 "text": "You enter the subway. The train is out of service, but 2 tunnels are open...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunnel A": "tunelA","tunnel B": "tunelB","go back": "parque"}
             }
        },
   "tunelA" : {
            "es": {
                 "name": "Tuneles",
                 "text": "Atraviesas el tunel. Encuentras 2 tuneles abiertos...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunel X": "tunelX","tunel J": "tunelJ", "volver atras": "metro"}
             },
            "en": {
                 "name": "Tunnels",
                 "text": "You cross the tunnel and find 2 open tunnels...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunnel X": "tunelX","tunnel J": "tunelJ", "go back": "metro"}
             }
        },
   "tunelB" : {
            "es": {
                 "name": "Tuneles",
                 "text": "Atraviesas el tunel. Encuentras 2 tuneles abiertos...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunel W": "tunelW","tunel Z": "tunelJ", "volver atras": "metro"}
             },
            "en": {
                 "name": "Tunnels",
                 "text": "You cross the tunnel and find 2 open tunnels...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunnel W": "tunelW","tunnel Z": "metro", "go back": "metro"}
             }
        },
   "tunelX" : {
            "es": {
                 "name": "Tuneles",
                 "text": "Atraviesas el tunel. Encuentras 2 tuneles abiertos...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunel C": "salida","tunel W": "tunelW", "volver atras": "tunelA"}
             },
            "en": {
                 "name": "Tunnels",
                 "text": "You cross the tunnel and find 2 open tunnels...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunnel C": "salida","tunnel W": "tunelW", "go back": "tunelA"}
             }
        },
   "tunelJ" : {
            "es": {
                 "name": "Tuneles",
                 "text": "Atraviesas el tunel. Encuentras 2 tuneles abiertos...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunel F": "calle_persona_alergica","tunel B": "tunelB", "volver atras": "tunelA"}
             },
            "en": {
                 "name": "Tunnels",
                 "text": "You cross the tunnel and find 2 open tunnels...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunnel F": "calle_persona_alergica","tunel B": "tunnelB", "go back": "tunelA"}
             }
        },
   "tunelW" : {
            "es": {
                 "name": "Tuneles",
                 "text": "Atraviesas el tunel. Encuentras 2 tuneles abiertos...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunel P": "tunelP","tunel J": "tunelJ", "volver atras": "tunelB"}
             },
            "en": {
                 "name": "Tunnels",
                 "text": "You cross the tunnel and find 2 open tunnels...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunnel P": "tunelP","tunnel J": "tunelJ", "go back": "tunelB"}
             }
        },
   "tunelP" : {
            "es": {
                 "name": "Tuneles",
                 "text": "Atraviesas el tunel. Encuentras 2 tuneles abiertos...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunel Q": "bosque3","tunel Z": "metro", "volver atras": "tunelB"}
             },
            "en": {
                 "name": "Tunnels",
                 "text": "You cross the tunnel and find 2 open tunnels...",
                 "image": "images/tunel.jpeg",
                 "options": {"tunnel Q": "bosque3","tunnel Z": "metro", "go back": "tunelB"}
             }
        },
   "salida" : {
            "es": {
                 "name": "FINAL 1 de 3 - Tu ultima gran huida",
                 "text": "El tunel te lleva a una salida fuera de la cuidad condenada. Varia gente no-alergica te mira sorprendido. Eres consumido por el polen poco despues, pero esta experiencia lleva a los no-alergicos a iniciar una revolucion contra en gobierno pro-supremacia-nasal. El resto es historia.",
                 "image": "images/salida.jpeg",
                 "options": {}
             },
            "en": {
                 "name": "ENDING 1 of 3 - You last great escape",
                 "text": "The tunnel takes you to an exit outside the condemned city. Several non-allergic people look at you surprised. You are consumed by the pollen short afterwards, but this experience leads the non-allergic to starting a revolution agaisnt the pro-nasal-supremacy government. The rest is history.",
                 "image": "images/salida.jpeg",
                 "options": {}
             }
        },
   "game_over" : {
            "es": {
                 "name": "GAME OVER",
                 "text": "Has respirado demasiado polen. Tu nariz produce tanto moco que engordas 17 kilos. Tu respiracion se reduce a intentos desesperados de bostezar. Tu muerte es anunciada por estornudos extremdamente ruidosos. Y luego, silencio.",
                 "image": "images/muerte.jpeg",
                 "options": {}
             },
            "en": {
                 "name": "GAME OVER",
                 "text": "You have breathed too much pollen. You nose generates so much snot that now you weight 17kg more. Your breathing is reduced to desesperate yawning attemps. You death is announced by really loud sneezes. And then, silence.",
                 "image": "images/muerte.jpeg",
                 "options": {}
             }
        }
}
