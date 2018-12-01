###########################################################################
#                                 Bill Cypher                             #
#                                                                         #
#   Programmed by Alvaro Espinoza                                         #
#   Class:  CG120                                                         #
#   Instructor:  Dean Zeller                                              #
#                                                                         #
#   Description:  This is a picture of                                    #
#                                                                         #
###########################################################################
from tkinter import *
c = Canvas(width=900, height=900, bg='white')
c.pack(expand=YES, fill=BOTH)

#circle
c.create_oval((100,100),(750,750), width=3)
c.create_oval((110,110),(740,740), width=3)
c.create_oval((180,180),(670,670), width=3)
c.create_oval((190,190),(660,660), width=3)

c.create_line((425,110),(425,180), width=2)
c.create_line((425,670),(425,740), width=2)

#body
c.create_polygon((425,300),(550,525),(300,525),fill="yellow",width=3, outline="black")
c.create_line((380,525),(380,565), width=5)#leg
c.create_line((470,525),(470,565), width=5)#leg
c.create_arc((379,505),(420,595),width=5,start=-90,extent=-90,style=ARC)
c.create_line((400,595),(395,620),width=4)
c.create_arc((471,505),(430,595),width=5,start=-90,extent=90,style=ARC)
c.create_line((450,595),(455,620),width=4)





c.create_arc((510,440),(565,460), start=180,extent=180,style=ARC,width=4)#right arm
c.create_arc((561,453),(578,430), start=90,extent=150,style=ARC,width=4)#finger
c.create_arc((561,453),(595,433), start=180,extent=150,style=ARC,width=4)#finger
c.create_arc((566,428),(610,468), start=-90,extent=-90,style=ARC,width=4)#finger
c.create_arc((565,423),(580,475), start=-90,extent=-90,style=ARC,width=4)#finger

c.create_arc((340,440),(285,460), start=180,extent=180,style=ARC,width=4)#left arm
c.create_arc((289,453),(272,430), start=-90,extent=150,style=ARC,width=4)#finger
c.create_arc((289,453),(255,433), start=180,extent=150,style=ARC,width=4)#finger
c.create_arc((284,428),(240,468), start=-90,extent=90,style=ARC,width=4)#finger
c.create_arc((285,423),(270,475), start=-90,extent=90,style=ARC,width=4)#finger

c.create_line((350,439),(501,439), width=3)#horizontal line top
c.create_line((335,465),(515,465), width=3)#horizontal line middle
c.create_line((315,499),(535,499), width=3)#horizontal line bottom
c.create_line((425,465),(425,499), width=2)#vertical line
c.create_line((360,465),(360,499), width=2)#vertical line
c.create_line((490,465),(490,499), width=2)#vertical line
c.create_line((380,439),(380,465), width=2)#vertical line
c.create_line((470,439),(470,465), width=2)#vertical line

c.create_arc((390,360),(460,400),start=180,extent=359,style=CHORD,width=2,fill="white")#eye
c.create_arc((420,365),(430,395),start=90,extent=359,style=PIESLICE,width=2,fill="black")#pupil
c.create_line((425,350),(425,360),width=2)#eyelash top
c.create_line((445,352),(440,362),width=2,smooth=1)#eyelash top
c.create_line((405,352),(410,362),width=2,smooth=1)#eyelash top

c.create_line((425,400),(425,408),width=2)
c.create_line((445,405),(440,399),width=2)
c.create_line((405,405),(410,399),width=2)




#hat and bowtie
c.create_polygon((410,301),(440,301),(440,200),(410,200))#hat
c.create_line((392,303),(458,303), width=5)#hat

c.create_oval((420,460),(430,470),width=3,fill="black")#tie
c.create_polygon((400,452),(400,478),(450,452),(450,478),(400,452))#tie


