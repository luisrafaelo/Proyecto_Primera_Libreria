def monoestable(Resis,Capci):
    import pygame,sys
    import numpy as np


    pygame.init()
    Res=Resis
    Cap=Capci

    def Imagen(Ventana,x,y):
        Mi_imagen = pygame.image.load("Imagenes/Monoestable.png")
        Mi_imagen = pygame.transform.scale(Mi_imagen,(250,250))
        Ventana.blit(Mi_imagen,(20+x,40+y))
        
    def Dibujar_Señal(Ventana,x,y):
        pygame.draw.line(Ventana,ColorLinea,(340+x,165+y),(440+x,165+y),3)#primeroHorizontal
        pygame.draw.line(Ventana,ColorLinea,(440+x,165+y),(440+x,65+y),3)#PrimeroVertical
        pygame.draw.line(Ventana,ColorLinea,(440+x,65+y),(540+x,65+y),3)#SegundoHorizontal
        pygame.draw.line(Ventana,ColorLinea,(540+x,65+y),(540+x,165+y),3)#SegundoVertical
        pygame.draw.line(Ventana,ColorLinea,(540+x,165+y),(640+x,165+y),3)#TerceroVertical
        
    def Calculo_Tiempo(R,C):
        Tem = R* C
        return Tem

    def Salida_Tiempo(Ventana,texto,x,y):
        SalidaTiempo = miFuente.render(str((np.format_float_scientific(texto,precision=1,exp_digits=2))),True,ColorNumeroSalida)
        Ventana.blit(SalidaTiempo,(545+x,200+y))
        
    def Texto_Titulo (Ventana,x,y):
        Titulo = miFuente.render ("Circuito Monoestable",True,ColorTexto)
        Ventana.blit(Titulo,(10+x,10+y))
        
    def Texto_Resistencia(Ventana,x,y):
        Resistor = miFuente.render ("Resistor: ",True,ColorTexto)
        Ventana.blit(Resistor,(60+x,350+y))
        
    def Texto_Capacitor(Ventana,x,y):
        Capacitor = miFuente.render ("Capacitor: ",True,ColorTexto)
        Ventana.blit(Capacitor,(60+x,400+y))
        
    def Texto_Señal(Ventana,x,y):
        Señal = miFuente.render ("Señal de Salida",True,ColorTexto)
        Ventana.blit(Señal,(350+x,10+y))
        
    def Texto_Tiempo(Ventana,x,y):
        Tiempo = miFuente.render ("Tiempo: ",True,ColorTexto)
        Ventana.blit(Tiempo,(430+x,200+y))
    
    def Salida_Resistor(Ventana,Res,x,y):  
        SalidaResistor = miFuente.render(str(Res),True,ColorNumeroEntrada) 
        Ventana.blit(SalidaResistor,(200+x,350+y))
        
    def Salida_Capacitor(Ventana,Cap,x,y):
        SalidaCapacitor = miFuente.render(str(Cap),True,ColorNumeroEntrada)
        Ventana.blit(SalidaCapacitor,(200+x,400+y))
        
    ##Creacion de la ventana## 
    Ventana=pygame.display.set_mode((700,500))
    pygame.display.set_caption("CIRCUITO MONOESTABLE")
    ##Definicion de colores a usar##
    ColorVentana = pygame.Color(146,240,173)
    ColorLinea = pygame.Color(8,8,8)
    ColorTexto = pygame.Color(8,160,205)
    ColorNumeroSalida = pygame.Color(105,150,15)
    ColorNumeroEntrada = pygame.Color(255,15,15)
    ##Definicion de la fuente##
    miFuente = pygame.font.Font (None,35)
    ##bucle infinito
    while True:
        
        Ventana.fill(ColorVentana)
        Dato = Calculo_Tiempo(Res,Cap)
        Imagen(Ventana,0,0)
        Texto_Tiempo(Ventana,0,0)
        Texto_Señal(Ventana,0,0)
        Texto_Capacitor(Ventana,0,0)
        Salida_Capacitor(Ventana,Cap,0,0)
        Texto_Resistencia(Ventana,0,0)
        Salida_Resistor(Ventana,Res,0,0)
        Texto_Titulo(Ventana,0,0)
        Salida_Tiempo(Ventana,Dato,0,0)
        Dibujar_Señal(Ventana,0,0)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.update()