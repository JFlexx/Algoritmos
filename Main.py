
import wx, os, sys
import wx.lib.agw.shapedbutton as SB
from ProyectoIA import algoritmoEstrella as ae
 

class GUIProject(wx.Frame):
    def __init__(self,parent,title):

        self.origen = ""
        self.destino = ""
        path = self.resource_path('mapa.jpg')
        self.jpg = wx.Image(path,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.Frame.__init__(self,parent,title = title, size = (self.jpg.GetWidth()*2,708), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        #   Crea los paneles donde los widgets seran colocados

        self.panel = wx.Panel(self, size = (self.jpg.GetWidth(),self.jpg.GetHeight()))
        self.panel2 = wx.Panel(self, pos = (self.jpg.GetWidth(),0),size = (self.jpg.GetWidth(),self.jpg.GetHeight()))

        #   Coloca la imagen del mapa en el panel izquierdo

        self.imagen = wx.StaticBitmap(self.panel,-1,self.jpg, size = (self.jpg.GetWidth(),self.jpg.GetHeight()))


        #   Crea los botones de las estaciones

        self.initializeButtons()


        #   Crea y diseña el campo de datos "Estacion origen"

        self.labelOrigin = wx.StaticText(self.panel2, label = "Estacion origen:", pos = (70,105))
        self.inputOrigin = wx.TextCtrl(self.panel2,pos = (175,100) , size=(200,25), style = wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT, self.EvtOrigin, self.inputOrigin)

        #   Crea y diseña el campo de datos "Estacion destino"

        self.labelDestination = wx.StaticText(self.panel2, label = "Estacion destino:", pos = (70,205))
        self.inputDestination = wx.TextCtrl(self.panel2,pos = (175,200) , size=(200,25), style = wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT, self.EvtDestination, self.inputDestination)


        #   Crea y diseña el boton "Buscar"

        self.searchButton = wx.Button(self.panel2, label = "Buscar", pos = (230,280))
        self.Bind(wx.EVT_BUTTON, self.OnSearch, self.searchButton)

        #   Crea y diseña el campo de datoso donde se mostrara el resultado de la busqueda

        self.labelResults = wx.StaticText(self.panel2, label = "Recorrido mas corto", pos = (220,350))
        self.result = wx.TextCtrl(self.panel2, pos=(175,375), size=(200,250), style=wx.TE_MULTILINE | wx.TE_READONLY)

        
        #   Crea y establece el menu principal
        fileMenu = wx.Menu()

        menuAbout = fileMenu.Append(wx.ID_ABOUT,"&Informacion","Informacion sobre el programa")
        fileMenu.AppendSeparator()
        menuExit = fileMenu.Append(wx.ID_EXIT,"&Salir","Cierra el programa")


        helpMenu = wx.Menu()
        menuAyuda = helpMenu.Append(wx.ID_HELP, "&Ayuda","Instrucciones")


        #   Añade los campos "Archivo" y "Ayuda" en el menu
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,"&Archivo")
        menuBar.Append(helpMenu,"&Ayuda")
        self.SetMenuBar(menuBar)

        #   Añade acciones a los botones del menu

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnHelp, menuAyuda)

        #   Sizers para ajustar los paneles y widgets a la ventana

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel,1,wx.EXPAND)
        self.sizer.Add(self.panel2,1,wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self.panel2)

        #   Centra y muestra la ventana de la aplicacion

        self.Center()
        self.Show()


    
    #   Obtiene el path de los archivos usados en el programa
    def resource_path(self, relative_path):
        """ Obtiene el path absoluto """
        try:
            # PyInstaller crea una carpeta temporal y guarda el path en _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    #   Handler del boton de "Ayuda"
    def OnHelp(self,e):
        dlg = wx.MessageDialog(self," Instrucciones de uso: \n\n" + 
                                    " - Establecer origen: Click izquierdo sobre la estacion\n" +
                                    "                                    o rellenar campo \"Estacion origen\" \n\n" +
                                    " - Establcer destino: Click derecho sobre la estacion\n" + 
                                    "                                    o rellenar campo \"Estacion destino\" \n\n" +
                                    " - Buscar recorrido: Click en el boton \"buscar\"\n\n" + 
                                    " - El resultado se mostrará en el panel inferior central", "Ayuda",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()




    #   Handler del boton "Sobre" del menu "Archivo"
    def OnAbout(self,e):
        # Crea un mensaje de dialogo
        dlg = wx.MessageDialog(self," Un simple programa que\n busca la mejor ruta a seguir\n" + 
                                    " entre dos estaciones", "Sobre: Mejor recorrido",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    

    #   Handler del boton "Salir" del menu "Archivo"
    def OnExit(self,e):
        self.Close(True)                #   Cierra el frame
        

    #   Detecta los datos introducidos en el campo "Estacion origen"
    def EvtOrigin(self,e):
            self.origen = e.GetString()
    

    #   Detecta los datos introducidos en el campo "Estacion destino"
    def EvtDestination(self,e):
            self.destino = e.GetString()


    #   Handler del boton "Buscar"
    #   Cuando se hace click en el, ejecuta el algoritmo con los datos introducidos
    #   Y se muestra el resultado en el cuadro de datos  "Resultado"
    def OnSearch(self,e):
        self.result.Clear()
        path = ae(self.origen,self.destino)
        for i in path:
            self.result.AppendText('-%s \n' % i)


    #   Detecta cuando se hace click izquierdo en el boton de una estacion
    #   Escribe el nombre de la estacion en el campo "Estacion origen"
    def OnLeftDown(self,Event,estacion):
        self.origen = estacion
        self.inputOrigin.Clear()
        self.inputOrigin.AppendText("%s" %estacion)


    #   Detecta cuando se hace click derecho en el boton de una estacion
    #   Escribe el nombre de la estacion en el campo "Estacion destino"
    def OnRightDown(self,Event, estacion):
        self.destino = estacion
        self.inputDestination.Clear()
        self.inputDestination.AppendText("%s" %estacion)


    #   Crea e inicializa los botones de las estaciones con sus respectivos nombres
    def initializeButtons(self):
        self.Ikebukuro = SB.SButton(self.imagen,pos = (218,73),size = (15,15))
        self.Ikebukuro.SetUseFocusIndicator(False)
        self.Ikebukuro.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Ikebukuro" : self.OnLeftDown(evt,tmp))
        self.Ikebukuro.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Ikebukuro" : self.OnRightDown(evt,tmp))

        self.Otsuka = SB.SButton(self.imagen,pos = (284,73),size = (15,15))
        self.Otsuka.SetUseFocusIndicator(False)
        self.Otsuka.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Otsuka" : self.OnLeftDown(evt,tmp))
        self.Otsuka.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Otsuka" : self.OnRightDown(evt,tmp))

        self.Sugamo = SB.SButton(self.imagen,pos = (315,73),size = (15,15))
        self.Sugamo.SetUseFocusIndicator(False)
        self.Sugamo.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Sugamo" : self.OnLeftDown(evt,tmp))
        self.Sugamo.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Sugamo" : self.OnRightDown(evt,tmp))

        self.Komagome = SB.SButton(self.imagen,pos = (340,73),size = (15,15))
        self.Komagome.SetUseFocusIndicator(False)
        self.Komagome.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Komagome" : self.OnLeftDown(evt,tmp))
        self.Komagome.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Komagome" : self.OnRightDown(evt,tmp))

        self.Tabata = SB.SButton(self.imagen,pos = (382,89),size = (15,15))
        self.Tabata.SetUseFocusIndicator(False)
        self.Tabata.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Tabata" : self.OnLeftDown(evt,tmp))
        self.Tabata.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Tabata" : self.OnRightDown(evt,tmp))

        self.NishiNippori = SB.SButton(self.imagen,pos = (403,110),size = (15,15))
        self.NishiNippori.SetUseFocusIndicator(False)
        self.NishiNippori.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Nishi-nippori" : self.OnLeftDown(evt,tmp))
        self.NishiNippori.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Nishi-nippori" : self.OnRightDown(evt,tmp))

        self.Nippori = SB.SButton(self.imagen,pos = (405,135),size = (15,15))
        self.Nippori.SetUseFocusIndicator(False)
        self.Nippori.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Nippori" : self.OnLeftDown(evt,tmp))
        self.Nippori.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Nippori" : self.OnRightDown(evt,tmp))

        self.Uguisudani = SB.SButton(self.imagen,pos = (405,161),size = (15,15))
        self.Uguisudani.SetUseFocusIndicator(False)
        self.Uguisudani.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Uguisudani" : self.OnLeftDown(evt,tmp))
        self.Uguisudani.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Uguisudani" : self.OnRightDown(evt,tmp))

        self.Ueno = SB.SButton(self.imagen,pos = (405,183),size = (15,15))
        self.Ueno.SetUseFocusIndicator(False)
        self.Ueno.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Ueno" : self.OnLeftDown(evt,tmp))
        self.Ueno.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Ueno" : self.OnRightDown(evt,tmp))

        self.Okachimachi = SB.SButton(self.imagen,pos = (405,213),size = (15,15))
        self.Okachimachi.SetUseFocusIndicator(False)
        self.Okachimachi.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Okachimachi" : self.OnLeftDown(evt,tmp))
        self.Okachimachi.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Okachimachi" : self.OnRightDown(evt,tmp))

        self.Akihabara = SB.SButton(self.imagen,pos = (405,236),size = (15,15))
        self.Akihabara.SetUseFocusIndicator(False)
        self.Akihabara.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Akihabara" : self.OnLeftDown(evt,tmp))
        self.Akihabara.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Akihabara" : self.OnRightDown(evt,tmp))

        self.Kanda = SB.SButton(self.imagen,pos = (405,275),size = (15,15))
        self.Kanda.SetUseFocusIndicator(False)
        self.Kanda.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Kanda" : self.OnLeftDown(evt,tmp))
        self.Kanda.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Kanda" : self.OnRightDown(evt,tmp))

        self.Tokyo = SB.SButton(self.imagen,pos = (405,312),size = (15,15))
        self.Tokyo.SetUseFocusIndicator(False)
        self.Tokyo.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Tokyo" : self.OnLeftDown(evt,tmp))
        self.Tokyo.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Tokyo" : self.OnRightDown(evt,tmp))

        self.Yurakucho = SB.SButton(self.imagen,pos = (403,340),size = (15,15))
        self.Yurakucho.SetUseFocusIndicator(False)
        self.Yurakucho.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Yurakucho" : self.OnLeftDown(evt,tmp))
        self.Yurakucho.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Yurakucho" : self.OnRightDown(evt,tmp))

        self.Shimbashi = SB.SButton(self.imagen,pos = (379,368),size = (15,15))
        self.Shimbashi.SetUseFocusIndicator(False)
        self.Shimbashi.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Shimbashi" : self.OnLeftDown(evt,tmp))
        self.Shimbashi.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Shimbashi" : self.OnRightDown(evt,tmp))

        self.Hamamatsucho = SB.SButton(self.imagen,pos = (353,391),size = (15,15))
        self.Hamamatsucho.SetUseFocusIndicator(False)
        self.Hamamatsucho.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Hamamatsucho" : self.OnLeftDown(evt,tmp))
        self.Hamamatsucho.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Hamamatsucho" : self.OnRightDown(evt,tmp))

        self.Tamachi = SB.SButton(self.imagen,pos = (328,418),size = (15,15))
        self.Tamachi.SetUseFocusIndicator(False)
        self.Tamachi.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Tamachi" : self.OnLeftDown(evt,tmp))
        self.Tamachi.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Tamachi" : self.OnRightDown(evt,tmp))

        self.Shinagawa = SB.SButton(self.imagen,pos = (293,451),size = (15,15))
        self.Shinagawa.SetUseFocusIndicator(False)
        self.Shinagawa.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Shinagawa" : self.OnLeftDown(evt,tmp))
        self.Shinagawa.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Shinagawa" : self.OnRightDown(evt,tmp))

        self.Osaki = SB.SButton(self.imagen,pos = (240,458),size = (15,15))
        self.Osaki.SetUseFocusIndicator(False)
        self.Osaki.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Osaki" : self.OnLeftDown(evt,tmp))
        self.Osaki.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Osaki" : self.OnRightDown(evt,tmp))

        self.Gotanda = SB.SButton(self.imagen,pos = (208,458),size = (15,15))
        self.Gotanda.SetUseFocusIndicator(False)
        self.Gotanda.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Gotanda" : self.OnLeftDown(evt,tmp))
        self.Gotanda.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Gotanda" : self.OnRightDown(evt,tmp))

        self.Meguro = SB.SButton(self.imagen,pos = (175,458),size = (15,15))
        self.Meguro.SetUseFocusIndicator(False)
        self.Meguro.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Meguro" : self.OnLeftDown(evt,tmp))
        self.Meguro.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Meguro" : self.OnRightDown(evt,tmp))

        self.Ebisu = SB.SButton(self.imagen,pos = (130,440),size = (15,15))
        self.Ebisu.SetUseFocusIndicator(False)
        self.Ebisu.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Ebisu" : self.OnLeftDown(evt,tmp))
        self.Ebisu.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Ebisu" : self.OnRightDown(evt,tmp))

        self.Shibuya = SB.SButton(self.imagen,pos = (127,390),size = (15,15))
        self.Shibuya.SetUseFocusIndicator(False)
        self.Shibuya.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Shibuya" : self.OnLeftDown(evt,tmp))
        self.Shibuya.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Shibuya" : self.OnRightDown(evt,tmp))

        self.Harajuku = SB.SButton(self.imagen,pos = (127,348),size = (15,15))
        self.Harajuku.SetUseFocusIndicator(False)
        self.Harajuku.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Harajuku" : self.OnLeftDown(evt,tmp))
        self.Harajuku.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Harajuku" : self.OnRightDown(evt,tmp))

        self.Yoyogi2 = SB.SButton(self.imagen,pos = (127,281),size = (15,15))
        self.Yoyogi2.SetUseFocusIndicator(False)
        self.Yoyogi2.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Yoyogi" : self.OnLeftDown(evt,tmp))
        self.Yoyogi2.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Yoyogi" : self.OnRightDown(evt,tmp))

        self.Yoyogi1 = SB.SButton(self.imagen,pos = (87,281),size = (15,15))
        self.Yoyogi1.SetUseFocusIndicator(False)
        self.Yoyogi1.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Yoyogi" : self.OnLeftDown(evt,tmp))
        self.Yoyogi1.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Yoyogi" : self.OnRightDown(evt,tmp))

        self.Shinjuku3 = SB.SButton(self.imagen,pos = (127,247),size = (15,15))
        self.Shinjuku3.SetUseFocusIndicator(False)
        self.Shinjuku3.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Shinjuku" : self.OnLeftDown(evt,tmp))
        self.Shinjuku3.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Shinjuku" : self.OnRightDown(evt,tmp))

        self.Shinjuku2 = SB.SButton(self.imagen,pos = (106,247),size = (15,15))
        self.Shinjuku2.SetUseFocusIndicator(False)
        self.Shinjuku2.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Shinjuku" : self.OnLeftDown(evt,tmp))
        self.Shinjuku2.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Shinjuku" : self.OnRightDown(evt,tmp))

        self.Shinjuku1 = SB.SButton(self.imagen,pos = (87,247),size = (15,15))
        self.Shinjuku1.SetUseFocusIndicator(False)
        self.Shinjuku1.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Shinjuku" : self.OnLeftDown(evt,tmp))
        self.Shinjuku1.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Shinjuku" : self.OnRightDown(evt,tmp))

        self.ShinOkubo = SB.SButton(self.imagen,pos = (127,180),size = (15,15))
        self.ShinOkubo.SetUseFocusIndicator(False)
        self.ShinOkubo.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Shin-okubo" : self.OnLeftDown(evt,tmp))
        self.ShinOkubo.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Shin-okubo" : self.OnRightDown(evt,tmp))

        self.Takadanobaba = SB.SButton(self.imagen,pos = (134,139),size = (15,15))
        self.Takadanobaba.SetUseFocusIndicator(False)
        self.Takadanobaba.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Takadanobaba" : self.OnLeftDown(evt,tmp))
        self.Takadanobaba.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Takadanobaba" : self.OnRightDown(evt,tmp))

        self.Mejiro = SB.SButton(self.imagen,pos = (167,106),size = (15,15))
        self.Mejiro.SetUseFocusIndicator(False)
        self.Mejiro.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Mejiro" : self.OnLeftDown(evt,tmp))
        self.Mejiro.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Mejiro" : self.OnRightDown(evt,tmp))

        self.Sendagaya = SB.SButton(self.imagen,pos = (149,322),size = (15,15))
        self.Sendagaya.SetUseFocusIndicator(False)
        self.Sendagaya.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Sendagaya" : self.OnLeftDown(evt,tmp))
        self.Sendagaya.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Sendagaya" : self.OnRightDown(evt,tmp))

        self.Shinanomachi = SB.SButton(self.imagen,pos = (189,320),size = (15,15))
        self.Shinanomachi.SetUseFocusIndicator(False)
        self.Shinanomachi.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Shinanomachi" : self.OnLeftDown(evt,tmp))
        self.Shinanomachi.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Shinanomachi" : self.OnRightDown(evt,tmp))

        self.Yotsuya = SB.SButton(self.imagen,pos = (210,305),size = (15,15))
        self.Yotsuya.SetUseFocusIndicator(False)
        self.Yotsuya.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Yotsuya" : self.OnLeftDown(evt,tmp))
        self.Yotsuya.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Yotsuya" : self.OnRightDown(evt,tmp))

        self.Ichigaya = SB.SButton(self.imagen,pos = (229,286),size = (15,15))
        self.Ichigaya.SetUseFocusIndicator(False)
        self.Ichigaya.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Ichigaya" : self.OnLeftDown(evt,tmp))
        self.Ichigaya.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Ichigaya" : self.OnRightDown(evt,tmp))

        self.Iidabashi = SB.SButton(self.imagen,pos = (244,270),size = (15,15))
        self.Iidabashi.SetUseFocusIndicator(False)
        self.Iidabashi.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Iidabashi" : self.OnLeftDown(evt,tmp))
        self.Iidabashi.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Iidabashi" : self.OnRightDown(evt,tmp))

        self.Suidobashi = SB.SButton(self.imagen,pos = (259,255),size = (15,15))
        self.Suidobashi.SetUseFocusIndicator(False)
        self.Suidobashi.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Suidobashi" : self.OnLeftDown(evt,tmp))
        self.Suidobashi.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Suidobashi" : self.OnRightDown(evt,tmp))

        self.Ochanomizu1 = SB.SButton(self.imagen,pos = (284,236),size = (15,15))
        self.Ochanomizu1.SetUseFocusIndicator(False)
        self.Ochanomizu1.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Ochanomizu" : self.OnLeftDown(evt,tmp))
        self.Ochanomizu1.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Ochanomizu" : self.OnRightDown(evt,tmp))

        self.Ochanomizu2 = SB.SButton(self.imagen,pos = (300,217),size = (15,15))
        self.Ochanomizu2.SetUseFocusIndicator(False)
        self.Ochanomizu2.Bind(wx.EVT_LEFT_DOWN, lambda evt, tmp = "Ochanomizu" : self.OnLeftDown(evt,tmp))
        self.Ochanomizu2.Bind(wx.EVT_RIGHT_DOWN, lambda evt, tmp = "Ochanomizu" : self.OnRightDown(evt,tmp))




#   Ejecuta el programa
app = wx.App(False)
frame = GUIProject(None,'Mejor recorrido')
app.MainLoop()