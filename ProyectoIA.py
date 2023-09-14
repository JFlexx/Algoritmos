# Proyecto de Inteligencia Artifcial

# Declaracion de las distancias NO reales de las estaciones

disEstacionesShinjuku = {"Yoyogi" : 0.676, "Shin-okubo" : 1.3, "Ochanomizu":11.3}

disEstacionesYoyogi = {"Shinjuku" : 0.676, "Harajuku" : 1.3, "Sendagaya":1}

disEstacionesHarayuku = {"Yoyogi" : 1.3, "Shibuya" : 1.6}

disEstacionesShibuya = {"Harajuku" : 1.6, "Ebisu" : 1.5}

disEstacionesEbisu = {"Shibuya" : 1.5, "Meguro" : 3.5}

disEstacionesMeguru = {"Ebisu" : 3.5, "Gotanda" : 1}

disEstacionesGotanda = {"Meguro": 1, "Osaki":0.93}

disEstacionesOsaki = {"Gotanda":0.93, "Shinagawa":1.6}     #OSAKI -> GOTANDA REDONDEADO

disEstacionesShinagawa = {"Osaki":1.6,"Tamachi":2.2}

disEstacionesTamachi = {"Shinagawa":2.2, "Hamamatsucho":1.4}

disEstacionesHamamatsucho = {"Tamachi":1.4, "Shimbashi":1.2}

disEstacionesShimbashi = {"Hamamatsucho":1.2, "Yurakucho":1.1}

disEstacionesYurakucho = {"Shimbashi":1.1, "Tokyo":0.80}        #YURAKUCHO -> TOKYO  REDONDEADO

disEstacionesTokyo = {"Yurakucho":0.80, "Kanda":1.3, "Ochanomizu":2.7}       

disEstacionesKanda = {"Tokyo":1.3, "Akihabara":0.77}        #KANDA -> AKIHABARA REDONDEADO

disEstacionesAkihabara = {"Kanda":0.77, "Okachimachi":0.97, "Suidobashi":2}     

disEstacionesOkachimachi = {"Akihabara":0.97, "Ueno":0.78}      #OKACHIMACHI -> UENO REDONDEADO

disEstacionesUeno = {"Okachimachi":0.78, "Uguisudani":0.98}     #UENO -> UGUISUDANI REDONDEADO

disEstacionesUguisudani = {"Ueno":0.98, "Nippori":1.1}

disEstacionesNippori = {"Uguisudani":1.1, "Nishi-nippori":0.58}     #NIPPORI -> NISHI-NIPPORI REDONDEADO

disEstacionesNishiNippori = {"Nippori":0.58, "Tabata":0.82}         #NISHI-NIPPORI -> TABATA REDONDEADO

disEstacionesTabata = {"Nishi-nippori":0.82, "Komagome":1.5}

disEstacionesKomagome = {"Tabata":1.5, "Sugamo":0.79}               #KOMAGOME -> SUGAMO REDONDEADO

disEstacionesSugamo = {"Komagome":0.79, "Otsuka":1.1}

disEstacionesOtsuka = {"Sugamo":1.1, "Ikebukuro":1.9}

disEstacionesIkebukuro = {"Otsuka":1.9, "Mejiro":1.1}

disEstacionesMejiro = {"Ikebukuro":1.1, "Takadanobaba":0.99}    # MEJIRO -> TAKADANOBABA REDONDEADO

disEstacionesTakadanobaba = {"Mejiro":0.99, "Shin-okubo":1.3}

disEstacionesShinOkubo = {"Takadanobaba":1.3, "Shinjuku":1.3}

disEstacionesSendagaya = {"Yoyogi":1, "Shinanomachi":0.89}

disEstacionesShinanomachi = {"Sendagaya":0.89, "Yotsuya":1.1}

disEstacionesYotsuya = {"Shinanomachi":1.1, "Ichigaya":0.91}

disEstacioneesIchigaya = {"Yotsuya":0.91, "Iidabashi":1.6}

disEstacionesIidabashi = {"Ichigaya":1.6, "Suidobashi":0.99}

disEstacionesSuidobashi = {"Iidabashi":0.99, "Ochanomizu":1.1, "Akihabara":2}

disEstacionesOchanomizu = {"Suidobashi":1.1, "Shinjuku":11.3, "Tokyo":2.7}

# ********************************************************************

disEstaciones = {"Shinjuku":disEstacionesShinjuku, "Yoyogi":disEstacionesYoyogi, "Harajuku":disEstacionesHarayuku, "Shibuya":disEstacionesShibuya, "Ebisu":disEstacionesEbisu,
                  "Meguro":disEstacionesMeguru, "Gotanda":disEstacionesGotanda, "Osaki":disEstacionesOsaki, "Shinagawa":disEstacionesShinagawa, "Tamachi":disEstacionesTamachi,
                  "Hamamatsucho":disEstacionesHamamatsucho, "Shimbashi":disEstacionesShimbashi, "Yurakucho":disEstacionesYurakucho, "Tokyo":disEstacionesTokyo, "Kanda":disEstacionesKanda,
                  "Akihabara":disEstacionesAkihabara, "Okachimachi":disEstacionesOkachimachi, "Ueno":disEstacionesUeno, "Uguisudani":disEstacionesUguisudani, "Nippori":disEstacionesNippori,
                  "Nishi-nippori":disEstacionesNishiNippori, "Tabata":disEstacionesTabata, "Komagome":disEstacionesKomagome, "Sugamo":disEstacionesSugamo, "Otsuka":disEstacionesOtsuka,
                  "Ikebukuro":disEstacionesIkebukuro, "Mejiro":disEstacionesMejiro, "Takadanobaba":disEstacionesTakadanobaba, "Shin-okubo":disEstacionesShinOkubo, "Sendagaya":disEstacionesSendagaya,
                  "Shinanomachi":disEstacionesShinanomachi, "Yotsuya":disEstacionesYotsuya, "Ichigaya":disEstacioneesIchigaya, "Iidabashi":disEstacionesIidabashi, "Suidobashi":disEstacionesSuidobashi,
                  "Ochanomizu":disEstacionesOchanomizu
                 }

# Declaracion de las distancias reales

disAereaShinjuku = {
                    "Shinjuku":0, "Yoyogi":0.558, "Harajuku":2.16, "Shibuya":3.53, "Ebisu":4.86, "Meguro":6.34, "Gotanda":7.34, "Osaki":8.18, "Shinagawa":7.64,
                    "Tamachi":6.49, "Hamamatsucho":6, "Shimbashi":5.84, "Yurakucho":5.91, "Tokyo":6.14, "Kanda":6.38, "Akihabara":6.61, "Okachimachi":7,
                    "Ueno":7.46, "Uguisudani":7.84, "Nippori":7.64, "Nishi-nippori":7.63, "Tabata":7.68, "Komagome":6.7, "Sugamo":6, "Otsuka":5.32, "Ikebukuro":4.53,
                    "Mejiro":3.54, "Takadanobaba":2.58, "Shin-okubo":1.29, "Sendagaya":1.35, "Shinanomachi":2.1, "Yotsuya":2.72, "Ichigaya":3.15, "Iidabashi":4.25,
                    "Suidobashi":4.95, "Ochanomizu":5.93
                    }

# ********************************************************************

disAereaYoyogi = {
                    "Shinjuku":0.558, "Yoyogi":0, "Harajuku":1.39, "Shibuya":2.84, "Ebisu":4.18, "Meguro":5.64, "Gotanda":6.68, "Osaki":7.47, "Shinagawa":6.98,
                    "Tamachi":5.91, "Hamamatsucho":5.91, "Shimbashi":5.44, "Yurakucho":5.58, "Tokyo":5.87, "Kanda":6.28, "Akihabara":6.6, "Okachimachi":7.09,
                    "Ueno":7.59, "Uguisudani":8.05, "Nippori":7.91, "Nishi-nippori":7.92, "Tabata":8.05, "Komagome":7.13, "Sugamo":6.46, "Otsuka":5.84, "Ikebukuro":5.15,
                    "Mejiro":4.18, "Takadanobaba":3.2, "Shin-okubo":1.95, "Sendagaya":0.878, "Shinanomachi":1.71, "Yotsuya":2.59, "Ichigaya":3.11, "Iidabashi":4.4,
                    "Suidobashi":5.07, "Ochanomizu":5.9
                 }

# ********************************************************************

disAereaHarajuku = {
                    "Shinjuku":2.16, "Yoyogi":1.39, "Harajuku":0, "Shibuya":1.39, "Ebisu":2.71, "Meguro":4.19, "Gotanda":5.25, "Osaki":6.07, "Shinagawa":5.66,
                    "Tamachi":4.86, "Hamamatsucho":5.15, "Shimbashi":4.97, "Yurakucho":5.38, "Tokyo":5.84, "Kanda":6.55, "Akihabara":7, "Okachimachi":7.65,
                    "Ueno":8.15, "Uguisudani":8.82, "Nippori":8.82, "Nishi-nippori":8.9, "Tabata":9.15, "Komagome":8.32, "Sugamo":7.7, "Otsuka":7.19, "Ikebukuro":6.6,
                    "Mejiro":5.65, "Takadanobaba":4.68, "Shin-okubo":3.43, "Sendagaya":1.4, "Shinanomachi":1.9, "Yotsuya":3, "Ichigaya":3.62, "Iidabashi":5.11,
                    "Suidobashi":5.73, "Ochanomizu":6.44
                    }

# ********************************************************************

disAereaShibuya = {
                    "Shinjuku":3.53, "Yoyogi":2.84, "Harajuku":1.39, "Shibuya":0, "Ebisu":1.47, "Meguro":2.95, "Gotanda":4.05, "Osaki":4.9, "Shinagawa":4.7,
                    "Tamachi":4.35, "Hamamatsucho":5.02, "Shimbashi":5.21, "Yurakucho":5.85, "Tokyo":6.45, "Kanda":7.3, "Akihabara":7.85, "Okachimachi":8.6,
                    "Ueno":9.25, "Uguisudani":9.86, "Nippori":9.98, "Nishi-nippori":10.1, "Tabata":10.38, "Komagome":9.65, "Sugamo":9.05, "Otsuka":8.55, "Ikebukuro":8,
                    "Mejiro":7.05, "Takadanobaba":6.07, "Shin-okubo":4.8, "Sendagaya":2.72, "Shinanomachi":2.98, "Yotsuya":4.05, "Ichigaya":4.8, "Iidabashi":6.3,
                    "Suidobashi":6.78, "Ochanomizu":7.4
                    }

# ********************************************************************

disAereaEbisu = {
                    "Shinjuku":4.86, "Yoyogi":4.18, "Harajuku":2.71, "Shibuya":1.47, "Ebisu":0, "Meguro":1.51, "Gotanda":2.62, "Osaki":3.4, "Shinagawa":3.36,
                    "Tamachi":3.46, "Hamamatsucho":4.43, "Shimbashi":4.89, "Yurakucho":5.72, "Tokyo":6.4, "Kanda":7.52, "Akihabara":8.1, "Okachimachi":8.98,
                    "Ueno":9.66, "Uguisudani":10.39, "Nippori":10.57, "Nishi-nippori":10.76, "Tabata":11.18, "Komagome":10.53, "Sugamo":10, "Otsuka":9.6, "Ikebukuro":9.18,
                    "Mejiro":8.26, "Takadanobaba":7.32, "Shin-okubo":6.08, "Sendagaya":3.84, "Shinanomachi":3.82, "Yotsuya":4.77, "Ichigaya":5.42, "Iidabashi":6.91,
                    "Suidobashi":7.31, "Ochanomizu":7.72
                }

# ********************************************************************

disAereaMeguru = {
                    "Shinjuku":6.34, "Yoyogi":5.64, "Harajuku":4.19, "Shibuya":4.19, "Ebisu":1.51, "Meguro":0, "Gotanda":1.13, "Osaki":1.95, "Shinagawa":2.18,
                    "Tamachi":3.15, "Hamamatsucho":4, "Shimbashi":5.25, "Yurakucho":6.22, "Tokyo":7, "Kanda":8.14, "Akihabara":8.82, "Okachimachi":9.8,
                    "Ueno":10.5, "Uguisudani":11.22, "Nippori":11.58, "Nishi-nippori":11.8, "Tabata":12.25, "Komagome":11.75, "Sugamo":11.25, "Otsuka":10.9, "Ikebukuro":10.62,
                    "Mejiro":9.72, "Takadanobaba":8.78, "Shin-okubo":7.55, "Sendagaya":5.25, "Shinanomachi":5.12, "Yotsuya":5.95, "Ichigaya":6.55, "Iidabashi":8.02,
                    "Suidobashi":8.3, "Ochanomizu":8.5
                }

# ********************************************************************

disAereaGotanda = {
                    "Shinjuku":7.34, "Yoyogi":6.68, "Harajuku":5.25, "Shibuya":4.05, "Ebisu":2.62, "Meguro":1.13, "Gotanda":0, "Osaki":1.13, "Shinagawa":1.39,
                    "Tamachi":3.07, "Hamamatsucho":4.44, "Shimbashi":5.46, "Yurakucho":6.48, "Tokyo":7.28, "Kanda":8.46, "Akihabara":9.19, "Okachimachi":10.16,
                    "Ueno":10.93, "Uguisudani":11.68, "Nippori":12.11, "Nishi-nippori":12.4, "Tabata":12.9, "Komagome":12.46, "Sugamo":12.01, "Otsuka":11.76, "Ikebukuro":11.76,
                    "Mejiro":10.67, "Takadanobaba":9.77, "Shin-okubo":8.57, "Sendagaya":6.2, "Shinanomachi":6.01, "Yotsuya":6.68, "Ichigaya":7.29, "Iidabashi":8.63,
                    "Suidobashi":8.86, "Ochanomizu":8.98
                }

# ********************************************************************

disAereaOsaki = {
                    "Shinjuku":8.18, "Yoyogi":7.47, "Harajuku":6.07, "Shibuya":4.9, "Ebisu":3.4, "Meguro":1.95, "Gotanda":1.13, "Osaki":0, "Shinagawa":1.33,
                    "Tamachi":3.37, "Hamamatsucho":4.75, "Shimbashi":5.8, "Yurakucho":6.87, "Tokyo":7.67, "Kanda":8.87, "Akihabara":9.64, "Okachimachi":10.62,
                    "Ueno":11.37, "Uguisudani":12.17, "Nippori":12.62, "Nishi-nippori":12.94, "Tabata":13.49, "Komagome":13.08, "Sugamo":12.62, "Otsuka":12.45, "Ikebukuro":12.29,
                    "Mejiro":11.43, "Takadanobaba":10.54, "Shin-okubo":9.34, "Sendagaya":6.99, "Shinanomachi":6.73, "Yotsuya":7.37, "Ichigaya":7.94, "Iidabashi":9.27,
                    "Suidobashi":9.42, "Ochanomizu":9.46
                }

# ********************************************************************

disAereaShinagawa = {
                        "Shinjuku" : 7.64, "Yoyogi" : 6.98, "Harajuku" : 5.66, "Shibuya" : 4.7, "Ebisu" : 3.36,
                        "Meguro" : 2.18, "Gotanda" : 1.39, "Osaki" : 1.33, "Shinagawa" : 0, "Tamachi" : 2.08,
                        "Hamamatsucho" : 3.42, "Shimbashi" : 4.55, "Yurakucho" : 5.79, "Tokyo" : 6.4, "Kanda" : 7.6,
                        "Akihabara" : 8.38, "Okachimachi" : 9.38, "Ueno" : 10.2, "Uguisudani" : 10.95, "Nippori" : 11.45,
                        "Nishi-nippori" : 11.8, "Tabata" : 12.35, "Komagome" : 12.05, "Sugamo" : 11.7, "Otsuka" : 11.55,
                        "Ikebukuro" : 11.52, "Mejiro" : 10.71, "Takadanobaba" : 9.86, "Shin-okubo" : 8.76,
                        "Sendagaya" : 6.38, "Shinanomachi" : 6, "Yotsuya" : 6.45, "Ichigaya" : 6.96,
                        "Iidabashi" : 8.2, "Suidobashi" : 8.3, "Ochanomizu" : 8.24
                    }

# ********************************************************************

disAereaTamachi =  {
                        "Shinjuku" : 6.49, "Yoyogi" : 5.91, "Harajuku" : 4.86, "Shibuya" : 4.35, "Ebisu" : 3.46,
                        "Meguro" : 3.15, "Gotanda" : 3.07, "Osaki" : 3.37, "Shinagawa" : 2.08, "Tamachi" : 0,
                        "Hamamatsucho" : 1.38, "Shimbashi" : 2.5, "Yurakucho" : 3.52, "Tokyo" : 4.32, "Kanda" : 5.55,
                        "Akihabara" : 6.3, "Okachimachi" : 7.3, "Ueno" : 8.08, "Uguisudani" : 8.85, "Nippori" : 9,
                        "Nishi-nippori" : 9.75, "Tabata" : 10.35, "Komagome" : 10.1, "Sugamo" : 9.77, "Otsuka" : 9.74,
                        "Ikebukuro" : 9.89, "Mejiro" : 9.61, "Takadanobaba" : 8.43, "Shin-okubo" : 7.48,
                        "Sendagaya" : 5.15, "Shinanomachi" : 4.54, "Yotsuya" : 4.76, "Ichigaya" : 5.15,
                        "Iidabashi" : 6.27, "Suidobashi" : 6.28, "Ochanomizu" : 6.18
                    }

# ********************************************************************

disAereaHamamatsucho = {
                            "Shinjuku":6, "Yoyogi":5.91, "Harajuku":5.15, "Shibuya":5.02, "Ebisu":4.43,
                            "Meguro":4, "Gotanda":4.44, "Osaki":4.75, "Shinagawa":3.42, "Tamachi":1.38,
                            "Hamamatsucho":0, "Shimbashi":1.38, "Yurakucho":2.33, "Tokyo":3.01, "Kanda":4.24,
                            "Akihabara":4.99, "Okachimachi":6.01, "Ueno":6.79, "Uguisudani":7.59, "Nippori":8.18,
                            "Nishi-nippori":8.57, "Tabata":9.21, "Komagome":9.07, "Sugamo":8.83, "Otsuka":8.9,
                            "Ikebukuro":9.25, "Mejiro":8.62, "Takadanobaba":7.99, "Shin-okubo":7.21,
                            "Sendagaya":5.04, "Shinanomachi":4.31, "Yotsuya":4.2, "Ichigaya":4.42,
                            "Iidabashi":5.31, "Suidobashi":5.2, "Ochanomizu":4.95
                        }

# ********************************************************************

disAereaShimbashi = {
                        "Shinjuku":5.84, "Yoyogi":5.44, "Harajuku":4.97, "Shibuya":5.21, "Ebisu":4.89,
                        "Meguro":5.25, "Gotanda":5.46, "Osaki":5.8, "Shinagawa":4.55, "Tamachi":2.5,
                        "Hamamatsucho":1.38, "Shimbashi":0, "Yurakucho":1.06, "Tokyo":1.82, "Kanda":3.05,
                        "Akihabara":3.8, "Okachimachi":4.8, "Ueno":5.6, "Uguisudani":6.38, "Nippori":6.95,
                        "Nishi-nippori":7.34, "Tabata":7.98, "Komagome":7.88, "Sugamo":7.65, "Otsuka":7.77,
                        "Ikebukuro":8.22, "Mejiro":7.66, "Takadanobaba":7.12, "Shin-okubo":6.49,
                        "Sendagaya":4.55, "Shinanomachi":3.75, "Yotsuya":3.35, "Ichigaya":3.42,
                        "Iidabashi":4.15, "Suidobashi":3.99, "Ochanomizu":7.32
                    }

# ********************************************************************

disAereaYurakucho = {
                        "Shinjuku":5.91, "Yoyogi":5.58, "Harajuku":5.38, "Shibuya":5.85, "Ebisu":5.72,
                        "Meguro":6.22, "Gotanda":6.48, "Osaki":6.87, "Shinagawa":5.79, "Tamachi":3.52,
                        "Hamamatsucho":2.33, "Shimbashi":1.06, "Yurakucho":0, "Tokyo":0.8, "Kanda":2.02,
                        "Akihabara":2.77, "Okachimachi":3.78, "Ueno":4.56, "Uguisudani":5.35, "Nippori":5.96,
                        "Nishi-nippori":6.36, "Tabata":7.03, "Komagome":7, "Sugamo":6.84, "Otsuka":7.05,
                        "Ikebukuro":7.67, "Mejiro":7.22, "Takadanobaba":6.79, "Shin-okubo":6.34,
                        "Sendagaya":4.71, "Shinanomachi":3.88, "Yotsuya":3.2, "Ichigaya":3.04,
                        "Iidabashi":3.42, "Suidobashi":3.13, "Ochanomizu":2.73
                    }

# ********************************************************************

disAereaTokyo = {
                    "Shinjuku":6.14, "Yoyogi":5.87, "Harajuku":5.84, "Shibuya":6.45, "Ebisu":6.4,
                    "Meguro":7, "Gotanda":7.28, "Osaki":7.67, "Shinagawa":6.4, "Tamachi":4.32,
                    "Hamamatsucho":3.01, "Shimbashi":1.82, "Yurakucho":0.8, "Tokyo":0, "Kanda":1.24,
                    "Akihabara":1.98, "Okachimachi":3, "Ueno":3.78, "Uguisudani":4.58, "Nippori":5.24,
                    "Nishi-nippori":5.65, "Tabata":6.35, "Komagome":6.42, "Sugamo":6.32, "Otsuka":6.62,
                    "Ikebukuro":7.39, "Mejiro":7.03, "Takadanobaba":6.71, "Shin-okubo":6.37,
                    "Sendagaya":5.05, "Shinanomachi":4.22, "Yotsuya":3.4, "Ichigaya":3.04,
                    "Iidabashi":3.06, "Suidobashi":2.62, "Ochanomizu":2.04
                }

# ********************************************************************

disAereaKanda = {
                    "Shinjuku":6.38, "Yoyogi":6.28, "Harajuku":6.55, "Shibuya":7.3, "Ebisu":7.52,
                    "Meguro":8.14, "Gotanda":8.46, "Osaki":8.87, "Shinagawa":7.6, "Tamachi":5.55,
                    "Hamamatsucho":4.24, "Shimbashi":3.05, "Yurakucho":2.02, "Tokyo":1.24, "Kanda":0,
                    "Akihabara":0.75, "Okachimachi":1.78, "Ueno":2.55, "Uguisudani":3.36, "Nippori":4.04,
                    "Nishi-nippori":4.48, "Tabata":5.23, "Komagome":5.42, "Sugamo":5.44, "Otsuka":5.89,
                    "Ikebukuro":6.86, "Mejiro":6.66, "Takadanobaba":6.51, "Shin-okubo":6.48,
                    "Sendagaya":5.52, "Shinanomachi":4.75, "Yotsuya":3.73, "Ichigaya":3.2,
                    "Iidabashi":2.6, "Suidobashi":1.94, "Ochanomizu":0.98
                }

# ********************************************************************

disAereaAkihabara = {
                        "Shinjuku" : 6.61,"Yoyogi" : 6.6 ,"Harajuku": 7,"Shibuya" : 7.85,"Ebisu" : 8.1,
                        "Meguro": 8.82,"Gotanda" : 9.19,"Osaki" : 9.64,"Shinagawa" : 8.38,"Tamachi" : 6.3,
                        "Hamamatsucho" : 4.99,"Shimbashi" : 3.8,"Yurakucho":2.77, "Tokyo" : 1.98,"Kanda" : 0.75,
                        "Okachimachi":1.03,"Ueno": 1.8,"Uguisudani":2.6,"Nippori": 3.32,"Nishi-nippori":3.78,
                        "Tabata":4.56,"Komagome":4.84, "Sugamo":4.95,"Otsuka":5.49,"Ikebukuro":6.6,
                        "Mejiro":6.5,"Takadanobaba":6.46,"Shin-okubo":6.57,"Sendagaya":5.9,"Shinanomachi":5.18,
                        "Yotsuya":4.56,"Ichigaya":3.49,"Iidabashi":2.57,"Suidobashi":1.81,"Ochanomizu":0.715,
                        "Akihabara":0
                    }

# ********************************************************************

disAereaOkachimachi = {
                        "Shinjuku": 7, "Yoyogi": 7.09, "Harajuku": 7.65, "Shibuya":8.6, "Ebisu": 8.98,
                        "Meguro": 9.8, "Gotanda": 10.16, "Osaki": 10.62, "Shinagawa": 9.38, "Tamachi":7.3,
                        "Hamamatsucho": 6.01, "Shimbashi": 4.8, "Yurakucho": 3.78, "Tokyo": 3, "Kanda": 1.78,
                        "Akihabara": 1.03, "Okachimachi": 0, "Ueno": 0.77, "Uguisudani": 1.58, "Nippori": 2.33,
                        "Nishi-nippori": 2.82, "Tabata": 3.64, "Komagome": 4.09, "Sugamo": 4.32, "Otsuka": 5.01,
                        "Ikebukuro": 6.28, "Mejiro": 6.35, "Takadanobaba": 6.46, "Shin-okubo": 6.77,
                        "Sendagaya": 6.45, "Shinanomachi": 5.8, "Yotsuya": 4.68, "Ichigaya": 4,
                        "Iidabashi": 2.76, "Suidobashi": 2.02, "Ochanomizu": 1.25
                    }

# ********************************************************************

disAereaUeno = {
                    "Shinjuku": 7.46, "Yoyogi": 7.59, "Harajuku": 8.15, "Shibuya": 9.25, "Ebisu": 9.66,
                    "Meguro": 10.5, "Gotanda": 10.93, "Osaki": 11.37, "Shinagawa": 10.2, "Tamachi": 8.08,
                    "Hamamatsucho": 6.79, "Shimbashi": 5.6, "Yurakucho": 4.56, "Tokyo": 3.78, "Kanda": 2.55,
                    "Akihabara": 1.8, "Okachimachi": 0.77, "Ueno": 0, "Uguisudani": 0.786, "Nippori": 1.67,
                    "Nishi-nippori": 2.21, "Tabata": 3, "Komagome": 3.71, "Sugamo": 4.05, "Otsuka": 4.85,
                    "Ikebukuro": 6.25, "Mejiro": 6.43, "Takadanobaba": 6.66, "Shin-okubo": 7.06,
                    "Sendagaya": 7, "Shinanomachi": 6.39, "Yotsuya": 5.28, "Ichigaya": 4.61,
                    "Iidabashi": 3.25, "Suidobashi": 2.55, "Ochanomizu": 1.97
                }

# ********************************************************************

disAereaUguisudani = {
                        "Shinjuku": 7.84, "Yoyogi": 8.05, "Harajuku": 8.82, "Shibuya": 9.86, "Ebisu": 10.39,
                        "Meguro": 11.22, "Gotanda": 11.68, "Osaki": 12.17, "Shinagawa": 10.95, "Tamachi": 8.85,
                        "Hamamatsucho": 7.59, "Shimbashi": 6.38, "Yurakucho": 5.35, "Tokyo": 4.58, "Kanda": 3.36,
                        "Akihabara": 2.6, "Okachimachi": 1.58, "Ueno": 0.786, "Uguisudani": 0, "Nippori": 0.99,
                        "Nishi-nippori": 1.58, "Tabata": 2.42, "Komagome": 3.28, "Sugamo": 3.75, "Otsuka": 4.65,
                        "Ikebukuro": 6.14, "Mejiro": 6.45, "Takadanobaba": 6.79, "Shin-okubo": 7.39,
                        "Sendagaya": 7.51, "Shinanomachi": 6.95, "Yotsuya": 5.83, "Ichigaya": 5.11,
                        "Iidabashi": 3.68, "Suidobashi": 3.09, "Ochanomizu": 2.71
                    }

# ********************************************************************

disAereaNippori = {
                    "Shinjuku": 7.64, "Yoyogi": 7.91, "Harajuku": 8.82, "Shibuya": 9.98, "Ebisu": 10.57,
                    "Meguro": 11.58, "Gotanda": 12.11, "Osaki": 12.62, "Shinagawa": 11.45, "Tamachi": 9.4,
                    "Hamamatsucho": 8.18, "Shimbashi": 6.95, "Yurakucho":5.96, "Tokyo": 5.24, "Kanda": 4.04,
                    "Akihabara": 3.32, "Okachimachi": 2.33, "Ueno": 1.67, "Uguisudani": 0.99, "Nippori": 0,
                    "Nishi-nippori": 0.56, "Tabata": 1.42, "Komagome": 2.34, "Sugamo": 2.89, "Otsuka": 2.89,
                    "Ikebukuro": 5.4, "Mejiro": 5.82, "Takadanobaba": 6.29, "Shin-okubo": 7.01,
                    "Sendagaya": 7.5, "Shinanomachi": 7.02, "Yotsuya": 5.96, "Ichigaya": 5.2,
                    "Iidabashi": 3.71, "Suidobashi": 6.96, "Ochanomizu": 3.24
                    }

# ********************************************************************

disAereaNishiNippori = {
                            "Shinjuku": 7.63, "Yoyogi": 7.92, "Harajuku": 8.9, "Shibuya": 10.1, "Ebisu": 10.76,
                            "Meguro": 11.8, "Gotanda": 12.4, "Osaki": 12.94, "Shinagawa": 11.8, "Tamachi": 9.75,
                            "Hamamatsucho": 8.57, "Shimbashi": 7.34, "Yurakucho": 6.36, "Tokyo": 5.65, "Kanda": 4.48,
                            "Akihabara": 3.78, "Okachimachi": 2.82, "Ueno": 2.21, "Uguisudani": 1.58, "Nippori": 0.56,
                            "Nishi-nippori": 0, "Tabata": 0.85, "Komagome": 1.87, "Sugamo":2.49, "Otsuka": 3.46,
                            "Ikebukuro": 5.06, "Mejiro": 5.55, "Takadanobaba": 6.09, "Shin-okubo": 6.93,
                            "Sendagaya": 7.52, "Shinanomachi":7.11, "Yotsuya": 6.01, "Ichigaya": 5.37,
                            "Iidabashi": 3.88, "Suidobashi": 3.52, "Ochanomizu": 3.62
                        }

# ********************************************************************

disAereaTabata = {
                    "Shinjuku": 7.68, "Yoyogi": 8.05, "Harajuku": 9.15, "Shibuya": 10.38, "Ebisu": 11.18,
                    "Meguro": 11.25, "Gotanda": 12.9, "Osaki": 13.49, "Shinagawa": 12.35, "Tamachi": 10.35,
                    "Hamamatsucho": 9.21, "Shimbashi": 7.98, "Yurakucho": 7.03, "Tokyo": 6.35, "Kanda": 5.23,
                    "Akihabara": 4.56, "Okachimachi": 3.62, "Ueno": 3., "Uguisudani": 2.42, "Nippori":1.42,
                    "Nishi-nippori": 0.85, "Tabata": 0, "Komagome": 1.28, "Sugamo": 2.02, "Otsuka": 3.03,
                    "Ikebukuro": 4.62, "Mejiro": 5.24, "Takadanobaba": 5.9, "Shin-okubo": 6.86,
                    "Sendagaya": 7.76, "Shinanomachi": 7.42, "Yotsuya": 6.42, "Ichigaya": 5.72,
                    "Iidabashi": 4.26, "Suidobashi": 4.07, "Ochanomizu": 4.33
                }

# ********************************************************************

disAereaKomagome = {
                        "Shinjuku": 6.7, "Yoyogi": 7.13, "Harajuku": 8.32, "Shibuya":9.65, "Ebisu": 10.53,
                        "Meguro": 11.75, "Gotanda": 12.46, "Osaki": 13.08, "Shinagawa": 12.05, "Tamachi":10.1,
                        "Hamamatsucho": 9.07, "Shimbashi": 7.88, "Yurakucho": 7, "Tokyo": 6.42, "Kanda": 5.42,
                        "Akihabara": 4.84, "Okachimachi": 4.09, "Ueno": 3.71, "Uguisudani": 3.28, "Nippori":2.34,
                        "Nishi-nippori":1.87, "Tabata": 1.28, "Komagome": 0, "Sugamo": 0.778, "Otsuka": 1.76,
                        "Ikebukuro": 3.36, "Mejiro": 4.02, "Takadanobaba": 4.74, "Shin-okubo": 5.79,
                        "Sendagaya": 6.95, "Shinanomachi":6.72, "Yotsuya": 5.8, "Ichigaya":5.17,
                        "Iidabashi": 3.84, "Suidobashi": 3.89, "Ochanomizu": 4.46
                    }

# ********************************************************************

disAereaSugamo = {
                    "Shinjuku":6, "Yoyogi": 6.46, "Harajuku": 7.7, "Shibuya": 9.05, "Ebisu": 10,
                    "Meguro": 11.25, "Gotanda": 12.01, "Osaki": 12.62, "Shinagawa": 11.7, "Tamachi": 9.77,
                    "Hamamatsucho": 8.83, "Shimbashi": 7.65, "Yurakucho": 6.84, "Tokyo":6.32, "Kanda": 5.44,
                    "Akihabara":4.95, "Okachimachi": 4.32, "Ueno":4.05, "Uguisudani": 3.75, "Nippori": 2.89,
                    "Nishi-nippori": 2.49, "Tabata": 2.02, "Komagome": 0.778, "Sugamo": 0, "Otsuka": 1.01,
                    "Ikebukuro": 2.61, "Mejiro": 3.24, "Takadanobaba": 3.96, "Shin-okubo": 5.05,
                    "Sendagaya": 6.33, "Shinanomachi": 6.17, "Yotsuya": 5.32, "Ichigaya": 4.73,
                    "Iidabashi": 3.52, "Suidobashi": 3.72, "Ochanomizu": 4.46
                }

# ********************************************************************

disAereaOtsuka = {
                    "Shinjuku" : 5.32, "Yoyogi" : 5.84, "Harajuku" : 7.19, "Shibuya" : 8.55, "Ebisu" : 9.6, "Meguro" : 10.9, "Gotanda" : 11.76, "Osaki" : 12.45, "Shinagawa" : 11.55,
                    "Tamachi" : 9.74, "Hamamatsucho" : 8.9, "Shimbashi" : 7.77, "Yurakucho" : 7.05, "Tokyo" : 6.62, "Kanda" : 5.89, "Akihabara" : 5.49, "Okachimachi" : 5.01,
                    "Ueno" : 4.85, "Uguisudani" : 4.65, "Nippori" : 3.84, "Nishi-nippori" : 3.46, "Tabata" : 3.03, "Komagome" : 1.76, "Sugamo" : 1.01, "Otsuka" : 0, "Ikebukuro" : 1.59,
                    "Mejiro" : 2.27, "Takadanobaba" : 3.08, "Shin-okubo" : 4.27, "Sendagaya" : 5.83, "Shinanomachi" : 5.8, "Yotsuya" : 5.08, "Ichigaya" : 4.58, "Iidabashi" : 3.64,
                    "Suidobashi" : 4.02, "Ochanomizu" : 4.92
                }


# ********************************************************************

disAereaIkebukuro = {
                    "Shinjuku" : 4.53, "Yoyogi" : 5.15, "Harajuku" : 6.6, "Shibuya" : 8, "Ebisu" : 9.18, "Meguro" : 10.62, "Gotanda" : 11.55, "Osaki" : 12.29, "Shinagawa" : 11.52,
                    "Tamachi" : 9.89, "Hamamatsucho" : 9.25, "Shimbashi" : 8.22, "Yurakucho" : 7.67, "Tokyo" : 7.39, "Kanda" : 6.86, "Akihabara" : 6.6, "Okachimachi" : 6.28,
                    "Ueno" : 6.25, "Uguisudani" : 6.14, "Nippori" : 5.4, "Nishi-nippori" : 5.06, "Tabata" : 4.62, "Komagome" : 3.36, "Sugamo" : 2.61, "Otsuka" : 1.59, "Ikebukuro" : 0,
                    "Mejiro" : 1, "Takadanobaba" : 2, "Shin-okubo" : 3.33, "Sendagaya" : 5.37, "Shinanomachi" : 5.57, "Yotsuya" : 5.13, "Ichigaya" : 4.83, "Iidabashi" : 4.34,
                    "Suidobashi" : 4.91, "Ochanomizu" : 5.95
                }

# ********************************************************************

disAereaMejiro = {
                    "Shinjuku":3.54, "Yoyogi":4.18, "Harajuku":5.65, "Shibuya":7.05, "Ebisu":8.26,
                    "Meguro":9.72, "Gotanda":10.67, "Osaki":11.43, "Shinagawa":10.71, "Tamachi":9.61,
                    "Hamamatsucho":8.62, "Shimbashi":7.66, "Yurakucho":7.22, "Tokyo":7.03, "Kanda":6.66,
                    "Akihabara":6.5, "Okachimachi":6.35, "Ueno":6.43, "Uguisudani":6.45, "Nippori":5.82,
                    "Nishi-nippori":5.55, "Tabata":5.24, "Komagome":4.02, "Sugamo":3.24, "Otsuka":2.27,
                    "Ikebukuro":1, "Mejiro":0, "Takadanobaba":1, "Shin-okubo":2.33,
                    "Sendagaya":4.46, "Shinanomachi":4.73, "Yotsuya":4.43, "Ichigaya":4.24,
                    "Iidabashi":4.05, "Suidobashi":4.73, "Ochanomizu":5.83
                }

# ********************************************************************

disAereaTakadanobaba = {
                            "Shinjuku":2.58, "Yoyogi":3.2, "Harajuku":4.68, "Shibuya":6.07, "Ebisu":7.32,
                            "Meguro":8.78, "Gotanda":9.77, "Osaki":10.54, "Shinagawa":9.86, "Tamachi":8.43,
                            "Hamamatsucho":7.99, "Shimbashi":7.12, "Yurakucho":6.79, "Tokyo":6.71, "Kanda":6.51,
                            "Akihabara":6.46, "Okachimachi":6.46, "Ueno":6.66, "Uguisudani":6.79, "Nippori":6.29,
                            "Nishi-nippori":6.09, "Tabata":5.9, "Komagome":4.74, "Sugamo":3.96, "Otsuka":3.08,
                            "Ikebukuro":2, "Mejiro":1, "Takadanobaba":0, "Shin-okubo":1.34,
                            "Sendagaya":3.55, "Shinanomachi":3.91, "Yotsuya":3.82, "Ichigaya":3.73,
                            "Iidabashi":3.91, "Suidobashi":4.65, "Ochanomizu":5.76
                        }

# ********************************************************************

disAereaShinOkubo = {
                        "Shinjuku":1.29, "Yoyogi":1.95, "Harajuku":3.43, "Shibuya":4.8, "Ebisu":6.08,
                        "Meguro":7.55, "Gotanda":8.57, "Osaki":9.34, "Shinagawa":8.76, "Tamachi":7.48,
                        "Hamamatsucho":7.21, "Shimbashi":6.49, "Yurakucho":6.34, "Tokyo":6.37, "Kanda":6.48,
                        "Akihabara":6.57, "Okachimachi":6.77, "Ueno":7.06, "Uguisudani":7.39, "Nippori":7.01,
                        "Nishi-nippori":6.93, "Tabata":6.86, "Komagome":5.79, "Sugamo":5.05, "Otsuka":4.27,
                        "Ikebukuro":3.33, "Mejiro":2.33, "Takadanobaba":1.34, "Shin-okubo":0,
                        "Sendagaya":2.39, "Shinanomachi":2.94, "Yotsuya":3.19, "Ichigaya":3.35,
                        "Iidabashi":4.07, "Suidobashi":4.81, "Ochanomizu":5.88
                    }

# ********************************************************************

disAereaSendagaya = {
                        "Shinjuku":1.35, "Yoyogi":0.878, "Harajuku":1.4, "Shibuya":2.72, "Ebisu":3.84,
                        "Meguro":5.25, "Gotanda":6.99, "Osaki":6.99, "Shinagawa":6.38, "Tamachi":5.15,
                        "Hamamatsucho":5.04, "Shimbashi":4.55, "Yurakucho":4.71, "Tokyo":5.05, "Kanda":5.52,
                        "Akihabara":5.9, "Okachimachi":6.45, "Ueno":7, "Uguisudani":7.51, "Nippori":7.5,
                        "Nishi-nippori":7.52, "Tabata":7.76, "Komagome":6.95, "Sugamo":6.33, "Otsuka":5.83,
                        "Ikebukuro":5.37, "Mejiro":4.46, "Takadanobaba":3.55, "Shin-okubo":2.39,
                        "Sendagaya":0, "Shinanomachi":0.825, "Yotsuya":1.8, "Ichigaya":2.37,
                        "Iidabashi":3.84, "Suidobashi":4.46, "Ochanomizu":5.28
                    }

# ********************************************************************

disAereaShinanomachi = {
                            "Shinjuku":2.1, "Yoyogi":1.71, "Harajuku":1.9, "Shibuya":2.98, "Ebisu":3.82,
                            "Meguro":5.12, "Gotanda":6.73, "Osaki":6.73, "Shinagawa":6, "Tamachi":4.54,
                            "Hamamatsucho":4.31, "Shimbashi":3.75, "Yurakucho":3.88, "Tokyo":4.22, "Kanda":4.75,
                            "Akihabara":5.18, "Okachimachi":5.8, "Ueno":6.39, "Uguisudani":6.95, "Nippori":7.02,
                            "Nishi-nippori":7.11, "Tabata":7.42, "Komagome":6.72, "Sugamo":6.17, "Otsuka":5.8,
                            "Ikebukuro":5.57, "Mejiro":4.73, "Takadanobaba":3.91, "Shin-okubo":2.94,
                            "Sendagaya":0.825, "Shinanomachi":0, "Yotsuya":0.82, "Ichigaya":1.8,
                            "Iidabashi":2, "Suidobashi":3.87, "Ochanomizu":4.59
                        }

# ********************************************************************

disAereaYotsuya = {
                        "Shinjuku":2.72, "Yoyogi":2.59, "Harajuku":3, "Shibuya":4.05, "Ebisu":4.77,
                        "Meguro":5.95, "Gotanda":6.68, "Osaki":7.37, "Shinagawa":6.45, "Tamachi":4.76,
                        "Hamamatsucho":4.2, "Shimbashi":3.35, "Yurakucho":3.2, "Tokyo":3.4, "Kanda":3.73,
                        "Akihabara":4.1, "Okachimachi":4.68, "Ueno":5.28, "Uguisudani":5.83, "Nippori":5.96,
                        "Nishi-nippori":6.01, "Tabata":6.42, "Komagome":5.8, "Sugamo":5.32, "Otsuka":5.08,
                        "Ikebukuro":5.13, "Mejiro":4.43, "Takadanobaba":3.82, "Shin-okubo":3.19,
                        "Sendagaya":1.8, "Shinanomachi":0.82, "Yotsuya":0, "Ichigaya":0.67,
                        "Iidabashi":2.22, "Suidobashi":2.75, "Ochanomizu":3.5
                    }

# ********************************************************************

disAereaIichigaya = {
                        "Shinjuku":3.15, "Yoyogi":3.11, "Harajuku":3.62, "Shibuya":4.8, "Ebisu":5.42,
                        "Meguro":6.55, "Gotanda":7.29, "Osaki":7.94, "Shinagawa":6.96, "Tamachi":5.15,
                        "Hamamatsucho":4.42, "Shimbashi":3.42, "Yurakucho":3.04, "Tokyo":3.04, "Kanda":3.2,
                        "Akihabara":3.49, "Okachimachi":4, "Ueno":4.61, "Uguisudani":5.11, "Nippori":5.2,
                        "Nishi-nippori":5.37, "Tabata":5.72, "Komagome":5.17, "Sugamo":4.73, "Otsuka":4.58,
                        "Ikebukuro":4.83, "Mejiro":4.24, "Takadanobaba":3.73, "Shin-okubo":3.35,
                        "Sendagaya":2.37, "Shinanomachi":1.8, "Yotsuya":0.67, "Ichigaya":0,
                        "Iidabashi":1.6, "Suidobashi":2.07, "Ochanomizu":2.9
                    }

# ********************************************************************

disAereaIidabashi = {
                        "Shinjuku":4.25, "Yoyogi":4.4, "Harajuku":5.11, "Shibuya":6.3, "Ebisu":6.91,
                        "Meguro":8.02, "Gotanda":8.63, "Osaki":9.27, "Shinagawa":8.2, "Tamachi":6.27,
                        "Hamamatsucho":5.31, "Shimbashi":4.15, "Yurakucho":3.42, "Tokyo":3.06, "Kanda":2.6,
                        "Akihabara":2.57, "Okachimachi":2.76, "Ueno":3.25, "Uguisudani":3.68, "Nippori":3.71,
                        "Nishi-nippori":3.88, "Tabata":4.26, "Komagome":3.84, "Sugamo":3.52, "Otsuka":3.64,
                        "Ikebukuro":4.34, "Mejiro":4.05, "Takadanobaba":3.91, "Shin-okubo":4.07,
                        "Sendagaya":3.84, "Shinanomachi":2, "Yotsuya":2.22, "Ichigaya":1.6,
                        "Iidabashi":0, "Suidobashi":0.76, "Ochanomizu":1.85
                    }

# ********************************************************************

disAereaSuidobashi = {
                        "Shinjuku":4.95, "Yoyogi":5.07, "Harajuku":5.73, "Shibuya":6.78, "Ebisu":7.31,
                        "Meguro":8.3, "Gotanda":8.86, "Osaki":9.42, "Shinagawa":8.3, "Tamachi":6.28,
                        "Hamamatsucho":5.2, "Shimbashi":3.99, "Yurakucho":3.13, "Tokyo":2.62, "Kanda":1.94,
                        "Akihabara":1.81, "Okachimachi":2.02, "Ueno":2.55, "Uguisudani":3.09, "Nippori":6.96,
                        "Nishi-nippori":3.52, "Tabata":4.07, "Komagome":3.89, "Sugamo":3.72, "Otsuka":4.02,
                        "Ikebukuro":4.91, "Mejiro":4.73, "Takadanobaba":4.65, "Shin-okubo":4.81,
                        "Sendagaya":4.46, "Shinanomachi":3.87, "Yotsuya":2.75, "Ichigaya":2.07,
                        "Iidabashi":0.76, "Suidobashi":0, "Ochanomizu":1.1
                    }

# ********************************************************************

disAereaOchanomizu = {
                        "Shinjuku":5.93, "Yoyogi":5.97, "Harajuku":6.44, "Shibuya":7.4, "Ebisu":7.72,
                        "Meguro":8.5, "Gotanda":8.98, "Osaki":9.46, "Shinagawa":8.24, "Tamachi":6.18,
                        "Hamamatsucho":4.95, "Shimbashi":7.32, "Yurakucho":2.73, "Tokyo":2.04, "Kanda":0.98,
                        "Akihabara":1.25, "Okachimachi":1.97, "Ueno":2.71, "Uguisudani":3.24, "Nippori":3.62,
                        "Nishi-nippori":0.715, "Tabata":4.33, "Komagome":4.46, "Sugamo":4.46, "Otsuka":4.92,
                        "Ikebukuro":5.95, "Mejiro":5.83, "Takadanobaba":5.76, "Shin-okubo":5.88,
                        "Sendagaya":5.28, "Shinanomachi":4.59, "Yotsuya":3.5, "Ichigaya":2.9,
                        "Iidabashi":1.85, "Suidobashi":1.1, "Ochanomizu":0
                    }

# ********************************************************************

disEstacionesReales = {
                       "Shinjuku" : disAereaShinjuku, "Yoyogi" : disAereaYoyogi, "Harajuku" : disAereaHarajuku, "Shibuya" : disAereaShibuya, "Ebisu" : disAereaEbisu,
                       "Meguro" : disAereaMeguru, "Gotanda" : disAereaGotanda, "Osaki" : disAereaOsaki, "Shinagawa" : disAereaShinagawa, "Tamachi" : disAereaTamachi,
                        "Hamamatsucho" : disAereaHamamatsucho, "Shimbashi" : disAereaShimbashi, "Yurakucho" : disAereaYurakucho, "Tokyo" : disAereaTokyo,
                        "Kanda" : disAereaKanda, "Akihabara" : disAereaAkihabara, "Okachimachi" : disAereaOkachimachi, "Ueno" : disAereaUeno, "Uguisudani" : disAereaUguisudani,
                        "Nippori" : disAereaNippori, "Nishi-nippori" : disAereaNishiNippori, "Tabata" : disAereaTabata, "Komagome" : disAereaKomagome, "Sugamo" : disAereaSugamo,
                        "Otsuka" : disAereaOtsuka, "Ikebukuro" : disAereaIkebukuro, "Mejiro":disAereaMejiro, "Takadanobaba": disAereaTakadanobaba, "Shin-okubo":disAereaShinOkubo,
                        "Sendagaya":disAereaSendagaya, "Shinanomachi":disAereaShinanomachi, "Yotsuya":disAereaYotsuya,"Ichigaya":disAereaIichigaya, "Iidabashi":disAereaIidabashi, 
                        "Suidobashi":disAereaSuidobashi ,"Ochanomizu":disAereaOchanomizu
                       }



Estaciones = [ "Shinjuku", "Yoyogi", "Harajuku", "Shibuya", "Ebisu", "Meguro", "Gotanda", "Osaki", "Shinagawa", "Tamachi",
                "Hamamatsucho", "Shimbashi", "Yurakucho", "Tokyo", "Kanda", "Akihabara", "Okachimachi", "Ueno", "Uguisudani", 
                "Nippori", "Nishi-nippori", "Tabata", "Komagome", "Sugamo", "Otsuka", "Ikebukuro", "Mejiro", "Takadanobaba", 
                "Shin-okubo", "Sendagaya", "Shinanomachi", "Yotsuya", "Ichigaya","Iidabashi", "Suidobashi", "Ochanomizu"
             ]

# Calcula la g total que hay desde una estacion hasta otra
def calcularGtotal(path):
    gTotal = 0
    for i in range(len(path)-1):
        gTotal += disEstaciones[path[i]].get(path[i+1])
    return gTotal


# Devuelve la key asociada a un valor en un diccionario
def getKeyFromValue(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]

# Metodo usado para imprimir las rutas que quedan por explorar en el algoritmo
def imprimeRutas(rutas):
    print("\nLas rutas a explorar con sus pesos son: ")
    for  i in rutas:
        print("\t- ", str(rutas[i]), " -> ",i)

def imprimeResultado(list):
    for i in list:
        print(i)

def algoritmoEstrella(origen,destino):
    distAerea = disEstacionesReales[origen].get(destino)
    path = [origen]
    nodoPadre = ""
    ramificaciones = {}
    while distAerea != 0:
        estacionesAdyacentes = list(disEstaciones[origen].keys())
        if nodoPadre in estacionesAdyacentes:                               # Borra de la lista de estaciones adyacentes la estacion de donde viene para no volver hacia atras
            estacionesAdyacentes.remove(nodoPadre)
        gTotal = calcularGtotal(path)
        for i in estacionesAdyacentes:
            h = disEstacionesReales[i].get(destino)
            g = disEstaciones[origen].get(i)
            ramificaciones[g + gTotal + h] = path + [i]                     # Guarda el camino recorrido y el valor de su g() + h()
        shortest = min(ramificaciones.keys())                               # De entre todas las posibles rutas elige la que tiene menor coste, es decir, menor g() + h()
        path = ramificaciones[shortest]
        origen = path[-1]                                                   # Accede al ultimo elemento de la lista, que será el nuevo origen para la siguiente iteracion
        nodoPadre = path[-2]
        del ramificaciones[getKeyFromValue(ramificaciones,path)]            # Elimina de la lista de busqueda la ruta que se acaba de explorar
        distAerea = disEstacionesReales[origen].get(destino)                # Se calcula la distancia aerea desde el nuevo origen para comprobar si estamos en el destino     
    return path





