from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
import random


class MyApp(App):
    def _make_spinner(self, text, values):
        return Spinner(text=text, values=tuple(values), size_hint=(1, None), height='30dp')

    def build(self):
        root = BoxLayout(orientation='vertical', padding=20, spacing=10)
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        #een lijn
        self.opponent_map = {
            #'name enemy':(AC, strenght save mod)
            'A': (69, 7), 
            'B': (18, 10), 
        }

        self.spinner1 = self._make_spinner('Welke tegenstander', self.opponent_map.keys())
        self.spinner2 = self._make_spinner('hoeveel wel charge', ('0', '1', '2', '3', '4', '5', '6', '7', '8'))
        self.spinner3 = self._make_spinner('hoeveel geen charge', ('0', '1', '2', '3', '4', '5', '6', '7', '8'))
        self.spinner4 = self._make_spinner('Proned?', ('proned', 'niet proned'))
        self.spinner5 = self._make_spinner('Eigen disadvantage/advantage op al mijn attack rolls',('advantage', 'disadvantage'))
        self.spinner6 = self._make_spinner('Hold person', ('ja', 'nee'))
        self.spinner7 = self._make_spinner('prone immune?', ('ja', 'nee'))

        for sp in (self.spinner1, self.spinner2, self.spinner3, self.spinner4, self.spinner5, self.spinner6, self.spinner7):
            root.add_widget(sp)

        # Run button
        run_btn = Button(text='Run', size_hint=(1, None), height='56dp')
        run_btn.bind(on_press=self.on_run_pressed)
        root.add_widget(run_btn)

        # Output
        self.output_label = Label(text='mooie resultaatjes', size_hint=(1, 1))
        root.add_widget(self.output_label)

        return root

    def on_run_pressed(self, instance):
        val1 = self.spinner1.text
        val2 = int(self.spinner2.text)
        val3 = int(self.spinner3.text)
        val44 = self.spinner4.text
        val4 = val44
        val5 = self.spinner5.text
        val6 = self.spinner6.text
        val7 = self.spinner7.text 

        # logic
        opponent_numbers = self.opponent_map.get(val1, (None, None))
        ACC, ssv = opponent_numbers
        AC = int(ACC) if ACC is not None else None
        ss = int(ssv) if ssv is not None else None
        

        ARcharge = []
        ARnocharge = []
        Saves = []
        FinalCharge = []
        Finalnocharge = []
        c = []
        if val2 > 0 :
            for i in range(0,2*val2):       #make the length of the list double as long, so that if there is advantage I can choose the highest value between list[i] and list[i + len(list)]
                ARcharge.append(random.randint(1,20) + 5)
            for i in range(0,val2):
                Saves.append(random.randint(1,20) + ss)  
            for i in range(0,val2):
                FinalCharge.append(i) 
        if val3 > 0:                        #make the length of the list double as long, so that if there is advantage I can choose the highest value between list[i] and list[i + len(list)]
            for i in range(0,2*val3):
                ARnocharge.append(random.randint(1,20) + 5)
            for i in range(0,val3):
                Finalnocharge.append(i)
        
        damage = 0
        dmg = []
        if val6 == 'ja':
            if val2 > 0:
                for i in range(0,val2):
                    if val5 == 'disadvantage':
                        roll = int(ARcharge[i])
                        FinalCharge[i] = roll
                        if ((roll >= AC) or (roll == 25)) and roll != 6:
                            damage += 3 + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18
                            dmg.append(damage)
                            if val7 == 'ja':
                                val4 = 'niet proned'
                            else:
                                val4 = 'proned'
                        c.append(val4)
                    else:
                        roll = max(int(ARcharge[i]),int(ARcharge[i+int(val2)]))
                        FinalCharge[i]=roll
                        if ((roll >= AC) or (roll == 25)) and roll != 6:
                            damage += 3 + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18
                            dmg.append(damage)
                            if val7 == 'ja':
                                val4 = 'niet proned'
                            else:
                                val4 = 'proned'
                        c.append(val4)

                        
            if val3 > 0:
                for i in range(0,val3):
                    if val4 == 'proned' and val5 == 'disadvantage':
                        Finalnocharge[i] = ARnocharge[i]
                        c.append(val4)
                        if ((Finalnocharge[i] >= AC) and (Finalnocharge[i] != 6)) or Finalnocharge[i] == 25:
                                damage += 3 + random.randint(1,4) + random.randint(1,4) + 8
                                dmg.append(damage)
                    elif val4 == 'proned':
                        Finalnocharge[i] = max(int(ARnocharge[i]),int(ARnocharge[i+int(val3)]))
                        c.append(val4)
                        if ((Finalnocharge[i] >= AC) and (Finalnocharge[i] != 6)) or Finalnocharge[i] == 25:
                            damage += 3 + random.randint(1,4) + random.randint(1,4) + 8
                            dmg.append(damage)
                    elif val5 == 'disadvantage':
                        Finalnocharge[i] = ARnocharge[i]
                        c.append(val4)
                        if ((Finalnocharge[i] >= AC) and (Finalnocharge[i] != 6)) or Finalnocharge[i] == 25:
                            damage += 3 + random.randint(1,6) + 6
                            dmg.append(damage)

                    else:
                        Finalnocharge[i] = max(int(ARnocharge[i]),int(ARnocharge[i+int(val3)]))
                        c.append(val4)
                        if ((Finalnocharge[i] >= AC) and (Finalnocharge[i] != 6)) or Finalnocharge[i] == 25:
                            damage += 3 + random.randint(1,6) + 6
                            dmg.append(damage)

        else:
            if val2 > 0:
                for i in range(0,val2):
                    if val4 == 'proned' and val5 == 'disadvantage':
                        FinalCharge[i] = ARcharge[i]
                        c.append(val4)
                    elif val4 == 'proned' or val5 == 'advantage':
                        FinalCharge[i] = max(int(ARcharge[i]),int(ARcharge[i+int(val2)]))
                        if FinalCharge[i] >= AC or FinalCharge[i] == 25:
                            if FinalCharge[i] != 6:
                                if Saves[i] < 13 or Saves[i] == (1+ss):
                                    if val7 == 'ja':
                                        val4 = 'niet proned'
                                    else:
                                        val4 = 'proned'
                        c.append(val4)
                    elif val5 == 'disadvantage':
                        FinalCharge[i] = min(int(ARcharge[i]),int(ARcharge[i+int(val2)]))
                        if FinalCharge[i] >= AC  or FinalCharge[i] == 25:
                            if FinalCharge[i] != 6:
                                if Saves[i] < 13 or Saves[i] == (1+ss):
                                    if val7 == 'ja':
                                        val4 = 'niet proned'
                                    else:
                                        val4 = 'proned'
                        c.append(val4)
                    else:
                        FinalCharge[i] = ARcharge[i]
                        if FinalCharge[i] >= AC  or FinalCharge[i] == 25:
                            if FinalCharge[i] != 6:
                                if Saves[i] < 13 or Saves[i] == (1+ss):
                                    if val7 == 'ja':
                                        val4 = 'niet proned'
                                    else:
                                        val4 = 'proned'
                        c.append(val4)
                        
            for i in range(0,val2):
                if ((FinalCharge[i] >= AC) and (FinalCharge[i] != 6)) or FinalCharge[i] == 25:
                    if FinalCharge[i] == 25: 
                        damage += 3 + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18
                        dmg.append(damage)
                    else:
                        damage += 3 + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
                        dmg.append(damage)
                        
            if val3 > 0:
                for i in range(0,val3):
                    if val4 == 'proned' and val5 == 'disadvantage':
                        Finalnocharge[i] = ARnocharge[i]
                        c.append(val4)
                        if ((Finalnocharge[i] >= AC) and (Finalnocharge[i] != 6)) or Finalnocharge[i] == 25:
                            if Finalnocharge[i] == 25: 
                                damage += 3 + random.randint(1,4) + random.randint(1,4) + 8
                                dmg.append(damage)
                            else:
                                damage += 3 + random.randint(1,4) + random.randint(1,4)
                                dmg.append(damage)
                    elif val4 == 'proned' or val5 == 'advantage':
                        Finalnocharge[i] = max(int(ARnocharge[i]),int(ARnocharge[i+int(val3)]))
                        c.append(val4)
                        if val4 == 'proned':
                            if ((Finalnocharge[i] >= AC) and (Finalnocharge[i] != 6)) or Finalnocharge[i] == 25:
                                if Finalnocharge[i] == 25: 
                                    damage += 3 + random.randint(1,4) + random.randint(1,4) + 8
                                    dmg.append(damage)
                                else:
                                    damage += 3 + random.randint(1,4) + random.randint(1,4)
                                    dmg.append(damage)
                        else:
                            if ((Finalnocharge[i] >= AC) and (Finalnocharge[i] != 6)) or Finalnocharge[i] == 25:
                                if Finalnocharge[i] == 25:
                                    damage += 3 + random.randint(1,6) + 6
                                    dmg.append(damage)
                                else:
                                    damage += 3 + random.randint(1,6)
                                    dmg.append(damage)
                    elif val5 == 'disadvantage':
                        Finalnocharge[i] = min(int(ARnocharge[i]),int(ARnocharge[i+int(val3)]))
                        c.append(val4)
                        if ((Finalnocharge[i] >= AC) and (Finalnocharge[i] != 6)) or Finalnocharge[i] == 25:
                            if Finalnocharge[i] == 25:
                                damage += 3 + random.randint(1,6) + 6
                                dmg.append(damage)
                            else:
                                damage += 3 + random.randint(1,6)
                                dmg.append(damage)
                    else:
                        Finalnocharge[i] = ARnocharge[i]
                        c.append(val4)
                        if ((Finalnocharge[i] >= AC) and (Finalnocharge[i] != 6)) or Finalnocharge[i] == 25:
                            if Finalnocharge[i] == 25:
                                damage += 3 + random.randint(1,6) + 6
                                dmg.append(damage)
                            else:
                                damage += 3 + random.randint(1,6)
                                dmg.append(damage)


        self.output_label.text = f"{ARcharge}\n{FinalCharge}\n{Saves}\n{c}\n{dmg}\n{ARnocharge}\n{Finalnocharge}\n{damage}"
        
if __name__ == "__main__":
    MyApp().run()
