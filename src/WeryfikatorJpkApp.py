from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from xml.etree import ElementTree
from kivy.core.window import Window



class WeryfikatorJpk(BoxLayout):
    sumNaliczony = 0
    sumNalezny = 0

    def getSum(self, files, naliczony_label, nalezny_label):
        ns = {'tns': 'http://jpk.mf.gov.pl/wzor/2017/11/13/1113/',
              'xsi': 'http://www.w3.org/2001/XMLSchema',
              'etd': 'http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/01/25/eD/DefinicjeTypy/'}

        if not files:
            print('No file is selected')
            return

        try:
            xml = ElementTree.parse(files[0])
            naliczony = float(xml.find('{http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}ZakupCtrl/{'
                                       'http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}PodatekNaliczony').text)
            nalezny = float(xml.find('{http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}SprzedazCtrl/{'
                                     'http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}PodatekNalezny').text)
        except:
            print('File ' + files[0] + ' is not a valid JPK xml file')
            return

        self.sumNaliczony = self.sumNaliczony + naliczony
        self.sumNalezny = self.sumNalezny + nalezny
        naliczony_label.text = 'Podatek naliczony: %.2f' % self.sumNaliczony
        naliczony_label.texture_update()
        nalezny_label.text = 'Podatek nalezny: %.2f' % self.sumNalezny
        nalezny_label.texture_update()

    def resetSum(self, naliczony_label, nalezny_label):
        self.sumNalezny = 0
        self.sumNaliczony = 0
        naliczony_label.text = 'Podatek naliczony: %.2f' % self.sumNaliczony
        naliczony_label.texture_update()
        nalezny_label.text = 'Podatek nalezny: %.2f' % self.sumNalezny
        nalezny_label.texture_update()


class WeryfikatorJpkApp(App):

    def build(self):
        return WeryfikatorJpk()


if __name__ == '__main__':
    WeryfikatorJpkApp().run()
