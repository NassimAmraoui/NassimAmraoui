import kivy
import kivy.uix
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
Window.size = (450,600)
Window.clearcolor = (64/255.0,64/255.0,64/255.0,10)

class Win_first(Screen):
    pass
class Win_second(Screen):
    pass
class Win_three(Screen):
    
    def show_moyenne(self):
            
            try :
                coff = self.inp_1.text
                td = self.inp_2.text   
                tp = self.inp_3.text
                examen = self.inp_4.text
                if tp !='' and td !='' and examen !='':
                    moyenne = ((float(tp)+float(td))/2)*0.4+float(examen)*0.6
                    self.k.text = str(moyenne)
                if tp =='' and td !='':
                    moyenne = float(td)*0.4 + float(examen)*0.6
                    self.k.text = str(moyenne)
                if tp =='' and td =='' and examen !='':
                    moyenne = float(examen)
                    self.k.text = str(moyenne)
                if coff == ''  and examen =='':
                    moyenne = 0
                    self.k.text = str(moyenne)
                
            
            


            
                coff2 = self.inp_5.text
                td2 = self.inp_6.text   
                tp2 = self.inp_7.text
                examen2 = self.inp_8.text
                if tp2 !='' and td2 !='' and examen2 !='':
                    moyenne2 = ((float(tp2)+float(td2))/2)*0.4+float(examen2)*0.6
                    self.k2.text = str(moyenne2)
                if tp2 =='' and td2 !='':
                    moyenne2 = float(td2)*0.4 + float(examen2)*0.6
                    self.k2.text = str(moyenne2)
                if tp2 =='' and td2 =='' and examen !='':
                    moyenne2 = float(examen2)
                    self.k2.text = str(moyenne2)
                if coff2 == ''  and examen2 =='':
                    moyenne2 = 0
                    self.k.text = str(moyenne2)



                coff3 = self.inp_9.text
                td3= self.inp_10.text   
                tp3 = self.inp_11.text
                examen3 = self.inp_12.text
                if tp3 !='' and td3 !='' and examen3 !='':
                    moyenne3 = ((float(tp3)+float(td3))/2)*0.4+float(examen3)*0.6
                    self.k3.text = str(moyenne3)
                if tp3 =='' and td3 !='':
                    moyenne3 = float(td3)*0.4 + float(examen3)*0.6
                    self.k3.text = str(moyenne3)
                if tp3 =='' and td3 =='' and examen2 !='':
                    moyenne3 = examen3
                    self.k3.text = str(moyenne3)
                if examen3 =='':
                    moyenne3 = 0
                    self.k3.text = str(moyenne3)
                
            
            
           
                coff4 = self.inp_13.text
                td4 = self.inp_14.text   
                tp4 = self.inp_15.text
                examen4 = self.inp_16.text
                if tp4 !='' and td4 !='' and examen4 !='':
                    moyenne4 = ((float(tp4)+float(td4))/2)*0.4+float(examen4)*0.6
                    self.k4.text = str(moyenne4)
                if tp4 =='' and td4 !='':
                    moyenne4 = float(td4)*0.4 + float(examen4)*0.6
                    self.k4.text = str(moyenne4)
                if tp4 =='' and td4 =='':
                    moyenne4 = float(examen4)
                    self.k4.text = str(moyenne4)
                if coff4 == ''  and examen4 =='':
                    moyenne4 = 0
                    coff4 = 0
                    self.k4.text = str(moyenne4)
                if coff4 == ''  and examen4 =='':
                    moyenne4 = 0
                    self.k4.text = str(moyenne4)                
                
                
            
          
        
            
                coff5 = self.inp_17.text
                td5 = self.inp_18.text   
                tp5 = self.inp_19.text
                examen5 = self.inp_20.text
                if tp5 !='' and td5 !='' and examen5 !='':
                    moyenne5 = ((float(tp5)+float(td5))/2)*0.4+float(examen5)*0.6
                    self.k5.text = str(moyenne5)
                if tp5 =='' and td5 !='':
                    moyenne5 = float(td5)*0.4 + float(examen5)*0.6
                    self.k5.text = str(moyenne5)
                if tp5 =='' and td5 =='':
                    moyenne5 = float(examen5)
                    self.k5.text = str(moyenne5)
                if coff5 == ''  and examen5 =='':
                    moyenne5 = 0
                    coff5 = 0
                    self.k5.text = str(moyenne5)
                if coff5 == ''  and examen5 =='':
                    moyenne5 = 0
                    self.k5.text = str(moyenne5)
            
                


           
                coff6 = self.inp_21.text
                td6 = self.inp_22.text   
                tp6 = self.inp_23.text
                examen6 = self.inp_24.text
                if tp6 !='' and td6 !='' and examen6 !='':
                    moyenne6 = ((float(tp6)+float(td6))/2)*0.4+float(examen6)*0.6
                    self.k6.text = str(moyenne6)
                if tp6 =='' and td6 !='':
                    moyenne6 = float(td6)*0.4 + float(examen6)*0.6
                    self.k6.text = str(moyenne6)
                if tp6 =='' and td6 =='':
                    moyenne6 = float(examen6)
                    self.k6.text = str(moyenne6)
                if coff6 == ''  and examen6 =='':
                    moyenne6 = 0
                    coff6 = 0
                    self.k6.text = str(moyenne6)
                if coff6 == ''  and examen6 =='':
                    moyenne6 = 0
                    self.k6.text = str(moyenne6)
            
             
            

            
                coff7 = self.inp_25.text
                td7 = self.inp_26.text   
                tp7 = self.inp_27.text
                examen7 = self.inp_28.text
                if tp7 !='' and td7 !='' and examen7 !='':
                    moyenne7 = ((float(tp7)+float(td7))/2)*0.4+float(examen7)*0.6
                    self.k7.text = str(moyenne7)
                if tp7 =='' and td7 !='':
                    moyenne7 = float(td7)*0.4 + float(examen7)*0.6
                    self.k7.text = str(moyenne7)
                if tp7 =='' and td7 =='':
                    moyenne7 = float(examen7)
                    self.k7.text = str(moyenne7)
                if coff7 == ''  and examen7 =='':
                    moyenne7 = 0
                    coff7 = 0
                    self.k7.text = str(moyenne7)
                if coff7 == ''  and examen7 =='':
                    moyenne7 = 0
                    self.k7.text = str(moyenne7)
            
            
            
                coff8 = self.inp_29.text
                td8 = self.inp_30.text   
                tp8 = self.inp_31.text
                examen8 = self.inp_32.text
                if tp8 !='' and td8 !='' and examen8 !='':
                    moyenne8 = ((float(tp8)+float(td8))/2)*0.4+float(examen8)*0.6
                    self.k8.text = str(moyenne8)
                if tp8 =='' and td8 !='':
                    moyenne8 = float(td8)*0.4 + float(examen8)*0.6
                    self.k8.text = str(moyenne8)
                if tp8 =='' and td8 =='':
                    moyenne8 = float(examen8)
                    self.k8.text = str(moyenne8)
                if coff8 == ''  and examen8 =='':
                    moyenne8 = 0
                    coff8 = 0
                    self.k7.text = str(moyenne8)
                if coff7 == ''  and examen7 =='':
                    moyenne7 = 0
                    self.k7.text = str(moyenne7)
            
            

            
                coff9 = self.inp_33.text
                td9 = self.inp_34.text   
                tp9= self.inp_35.text
                examen9 = self.inp_36.text
                if tp9 !='' and td9 !='' and examen9 !='':
                    moyenne9 = ((float(tp9)+float(td9))/2)*0.4+float(examen9)*0.6
                    self.k9.text = str(moyenne9)
                if tp9 =='' and td9 !='':
                    moyenne9 = float(td9)*0.4 + float(examen9)*0.6
                    self.k9.text = str(moyenne9)
                if tp9 =='' and td9 =='':
                    moyenne9 = float(examen9)
                    self.k9.text = str(moyenne9)
                if coff9 == ''  and examen9=='':
                    moyenne9 = 0
                    coff9 = 0
                    self.k9.text = str(moyenne9)
                if coff9 == ''  and examen9 =='':
                    moyenne9 = 0
                    self.k9.text = str(moyenne9)
            
                
            

            
                coff10 = self.inp_37.text
                td10 = self.inp_38.text   
                tp10 = self.inp_39.text
                examen10 = self.inp_40.text
                if tp10 !='' and td10 !='' and examen10 !='':
                    moyenne10 = ((float(tp10)+float(td10))/2)*0.4+float(examen10)*0.6
                    self.k10.text = str(moyenne10)
                if tp10 =='' and td10 !='':
                    moyenne10 = float(td10)*0.4 + float(examen10)*0.6
                    self.k10.text = str(moyenne10)
                if tp10 =='' and td10 =='':
                    moyenne10 = float(examen10)
                    self.k10.text = str(moyenne10)
                if coff10 == ''  and examen10 =='':
                    moyenne10 = 0
                    coff10 = 0
                    self.k10.text = str(moyenne10)
                if coff10 == ''  and examen10 =='':
                    moyenne10 = 0
                    self.k10.text = str(moyenne10)
                
                
            except ValueError:
                print(ValueError)
    

    def click(self):
        coff = self.inp_1.text
        td = self.inp_2.text   
        tp = self.inp_3.text
        examen = self.inp_4.text
        if tp !='' and td !='' and examen !='':
            moyenne = ((float(tp)+float(td))/2)*0.4+float(examen)*0.6
                    
        if tp =='' and td !='':
            moyenne = float(td)*0.4 + float(examen)*0.6
                    
        if tp =='' and td =='' and examen !='':
            moyenne = examen
        if coff == ''  and examen =='':
            moyenne = 0
            coff = 0
                    
                
                
            
            


            
        coff2 = self.inp_5.text
        td2 = self.inp_6.text   
        tp2 = self.inp_7.text
        examen2 = self.inp_8.text
        if tp2 !='' and td2 !='' and examen2 !='':
            moyenne2 = ((float(tp2)+float(td2))/2)*0.4+float(examen2)*0.6
                    
        if tp2 =='' and td2 !='':
            moyenne2 = float(td2)*0.4 + float(examen2)*0.6
                    
        if tp2 =='' and td2 =='' and examen != '':
            moyenne2 = examen2
        if coff2 == ''  and examen2 =='':
            moyenne2 = 0
            coff2 = 0           
        
        coff3 = self.inp_9.text
        td3 = self.inp_10.text   
        tp3 = self.inp_11.text
        examen3 = self.inp_12.text
        if tp3 !='' and td3 !='' and examen3 !='':
            moyenne3 = ((float(tp3)+float(td3))/2)*0.4+float(examen3)*0.6
                  
        if tp3 =='' and td3 !='':
            moyenne3 = float(td3)*0.4 + float(examen3)*0.6
                    
        if tp3 =='' and td3 =='' and examen3 !='':
            moyenne3 = examen3
        if coff3 == ''  and examen3 =='':
            moyenne3 = 0
            coff3 = 0 

        coff4 = self.inp_13.text
        td4 = self.inp_14.text   
        tp4 = self.inp_15.text
        examen4 = self.inp_16.text
        
        if tp4 !='' and td4 !='' and examen4 !='':
            moyenne4 = ((float(tp4)+float(td4))/2)*0.4+float(examen4)*0.6
                    
        if tp4 =='' and td4 !='':
            moyenne4 = float(td4)*0.4 + float(examen4)*0.6
                    
        if tp4 =='' and td4 =='' and examen4 !='':
            moyenne4 = examen4
        if coff4 == ''  and examen4 =='':
            moyenne4 = 0
            coff4 = 0            
                                
                
                
            
          
        
            
        coff5 = self.inp_17.text
        td5 = self.inp_18.text   
        tp5 = self.inp_19.text
        examen5 = self.inp_20.text
              
        if tp5 !='' and td5 !='' and examen5 !='':
            moyenne5 = ((float(tp5)+float(td5))/2)*0.4+float(examen5)*0.6
                    
        if tp5 =='' and td5 !='':
            moyenne5 = float(td5)*0.4 + float(examen5)*0.6
                    
        if tp5 =='' and td5 =='' and examen5 !='':
            moyenne5 = examen5
        if coff5 == ''  and examen5 =='':
            moyenne5 = 0
            coff5 = 0        
            
                


           
        coff6 = self.inp_21.text
        td6 = self.inp_22.text   
        tp6 = self.inp_23.text
        examen6 = self.inp_24.text
        if tp6 !='' and td6 !='' and examen6 !='':
            moyenne6 = ((float(tp6)+float(td6))/2)*0.4+float(examen6)*0.6
                    
        if tp6 =='' and td6 !='':
            moyenne6 = float(td6)*0.4 + float(examen6)*0.6
                    
        if tp6 =='' and td6 =='' and examen6 !='':
            moyenne6 = examen6
        if coff6 == ''  and examen6 =='':
            moyenne6 = 0
            coff6 = 0
            
             
            

            
        coff7 = self.inp_25.text
        td7 = self.inp_26.text   
        tp7 = self.inp_27.text
        examen7 = self.inp_28.text
        if tp7 !='' and td7 !='' and examen7 !='':
            moyenne = ((float(tp7)+float(td7))/2)*0.4+float(examen7)*0.6
                    
        if tp7 =='' and td7 !='':
            moyenne7 = float(td7)*0.4 + float(examen7)*0.6
                    
        if tp7 =='' and td7 =='' and examen7 !='':
            moyenne7 = examen7
        if coff7 == ''  and examen7 =='':
            moyenne7 = 0
            coff7 = 0
            
            
            
        coff8 = self.inp_29.text
        td8 = self.inp_30.text   
        tp8 = self.inp_31.text
        examen8 = self.inp_32.text
               
        if tp8 !='' and td8 !='' and examen8 !='':
            moyenne8 = ((float(tp8)+float(td8))/2)*0.4+float(examen8)*0.6
                    
        if tp8 =='' and td8 !='':
            moyenne8 = float(td8)*0.4 + float(examen8)*0.6
                    
        if tp8 =='' and td8 =='' and examen8 !='':
            moyenne8 = examen8
        if coff8 == ''  and examen8 =='':
            moyenne8 = 0
            coff8 = 0        
            
            

            
        coff9 = self.inp_33.text
        td9 = self.inp_34.text   
        tp9= self.inp_35.text
        examen9 = self.inp_36.text
        
        if tp9 !='' and td9 !='' and examen9 !='':
            moyenne9 = ((float(tp9)+float(td9))/2)*0.4+float(examen9)*0.6
                    
        if tp9 =='' and td9 !='':
            moyenne9 = float(td9)*0.4 + float(examen9)*0.6
                    
        if tp9 =='' and td9 =='' and examen9 !='':
            moyenne9 = examen9
        if coff9 == ''  and examen9 =='':
            moyenne9 = 0
            coff9 = 0
            
                
            

            
        coff10 = self.inp_37.text
        td10 = self.inp_38.text   
        tp10 = self.inp_39.text
        examen10 = self.inp_40.text
        if tp10 !='' and td10 !='' and examen10 !='':
            moyenne10 = ((float(tp10)+float(td10))/2)*0.4+float(examen10)*0.6
                    
        if tp10 =='' and td10 !='':
            moyenne10 = float(td10)*0.4 + float(examen10)*0.6
                    
        if tp10 =='' and td10 =='' and examen10 !='':
            moyenne10 = examen10
            
        if coff10 == ''  and examen10 =='':
            moyenne10 = 0
            coff10 = 0
       
        moyenne_general = (float(moyenne)*float(coff))+(float(moyenne2)*float(coff2))+(float(moyenne3)*float(coff3))+(float(moyenne4)*float(coff4))+(float(moyenne5)*float(coff5))+(float(moyenne6)*float(coff6))+(float(moyenne7)*float(coff7))+(float(moyenne8)*float(coff8))+(float(moyenne9)*float(coff9))+(float(moyenne10)*float(coff10))
        coff_general = float(coff)+float(coff2)+float(coff3)+float(coff4)+float(coff5)+float(coff6)+float(coff7)+float(coff8)+float(coff9)+float(coff10)        
        
        if(moyenne_general == 0 or coff_general == 0):
            self.lb.text = ''
            self.lb.text = '0'
        else :
            general = moyenne_general / coff_general
            general = "{:.2f}".format(general)
            self.lb.text = ''
            self.lb.text = str(general)
        

               
        

        
            

                

                  

    
        
        
class Win_p(ScreenManager):
    pass

class Main(App):
    def build(self):
        self.title ='MO3ADEL'
        return Builder.load_file('surface.kv')
        


if __name__ == '__main__':
    Main().run()
