import pandas as pd
import json

class Preprocessing():
    
    def __init__(self, data):
        self.df = data
        self.champ_dic = self.make_champ_dic()
        
    def fit(self):
        self.mk_to_wukong()
        champ_names_ohe = self.one_hot_encoding()
        champ_classes = self.class_counter()
        
        self.df.drop(['champ_name_p1', 'champ_name_p2', 'champ_name_p3', 'champ_name_p4', 'champ_name_p5'], axis=1, inplace=True)
        self.df.drop(['class_p1', 'class_p2', 'class_p3', 'class_p4', 'class_p5'], axis=1, inplace=True)
        
        self.df = pd.concat([self.df, pd.concat([champ_names_ohe, champ_classes], axis=1)], axis=1)
        
        return self.df
        
    def mk_to_wukong(self):
        for name in ['champ_name_p1', 'champ_name_p2', 'champ_name_p3', 'champ_name_p4', 'champ_name_p5']:
            self.df[name].replace(to_replace='MonkeyKing', value='Wukong', inplace=True)
            
    def one_hot_encoding(self):
        champ_names = ['champ_name_p1', 'champ_name_p2', 'champ_name_p3', 'champ_name_p4', 'champ_name_p5']
        # for champ in pd.unique(self.df[champ_names].stack()):
        #     self.champ_dic[champ] = []
                    
        for row, values in self.df[champ_names].iterrows():
            temp = values.to_list()
            for key in self.champ_dic.keys():
                if(key in temp):
                    self.champ_dic[key].append(1)
                else:
                    self.champ_dic[key].append(0)
        
        return pd.DataFrame(self.champ_dic)
    
    def string_to_list(self, x):
        return json.loads(x)
    
    def class_counter(self):
        champ_classes = ['class_p1', 'class_p2', 'class_p3', 'class_p4', 'class_p5']

        for column in champ_classes:
            self.df[column] = self.df[column].apply(self.string_to_list)
        assassins, fighters, mages, marksmen, supports, tanks = [], [], [], [], [], []

        for row, values in self.df[champ_classes].iterrows():
            temp = []
            for class_ in values:
                temp.extend(class_)
            
            assassins.append(temp.count('Assassin'))
            fighters.append(temp.count('Fighter'))
            mages.append(temp.count('Mage'))
            marksmen.append(temp.count('Marksman'))
            supports.append(temp.count('Support'))
            tanks.append(temp.count('Tank'))

        return pd.DataFrame({'num_assassin': assassins, 'num_fighters': fighters,
                    'num_mages': mages, 'num_marksmen': marksmen,
                    'num_supports': supports, 'num_tanks': tanks})
        
    def make_champ_dic(self):
        champ_dic = {'Cassiopeia': [], 'Evelynn': [], 'Nautilus': [], 'Mordekaiser': [],
        'Swain': [],
        'Soraka': [],
        'Gnar': [],
        'Zed': [],
        'Briar': [],
        'Draven': [],
        'Leona': [],
        'Lissandra': [],
        'Tryndamere': [],
        'Shyvana': [],
        'Ezreal': [],
        'Akali': [],
        'Lucian': [],
        'Ashe': [],
        'Yuumi': [],
        'Janna': [],
        'Malphite': [],
        'Aatrox': [],
        'Teemo': [],
        'JarvanIV': [],
        'Vladimir': [],
        'Morgana': [],
        'Nocturne': [],
        'Fiora': [],
        'Karma': [],
        'Zoe': [],
        'FiddleSticks': [],
        'Chogath': [],
        'Vayne': [],
        'Lillia': [],
        'Khazix': [],
        'Zeri': [],
        'Darius': [],
        'Malzahar': [],
        'Amumu': [],
        'Pyke': [],
        'Syndra': [],
        'TwistedFate': [],
        'Thresh': [],
        'Milio': [],
        'Jhin': [],
        'Garen': [],
        'Twitch': [],
        'Rumble': [],
        'Ornn': [],
        'Bard': [],
        'Renata': [],
        'Nunu': [],
        'Sivir': [],
        'Yasuo': [],
        'Samira': [],
        'Sona': [],
        'Zyra': [],
        'Tristana': [],
        'Kennen': [],
        'Belveth': [],
        'Elise': [],
        'Maokai': [],
        'Blitzcrank': [],
        'Lulu': [],
        'Vi': [],
        'Vex': [],
        'Gangplank': [],
        'MasterYi': [],
        'Zilean': [],
        'Caitlyn': [],
        'Irelia': [],
        'Annie': [],
        'Heimerdinger': [],
        'Nilah': [],
        'Gwen': [],
        'Xayah': [],
        'Ahri': [],
        'Nasus': [],
        'Ryze': [],
        'Veigar': [],
        'Viktor': [],
        'Neeko': [],
        'Rengar': [],
        'Nami': [],
        'Urgot': [],
        'Fizz': [],
        'Kindred': [],
        'Xerath': [],
        'Kayn': [],
        'Braum': [],
        'Jinx': [],
        'Katarina': [],
        'MonkeyKing': [],
        'Varus': [],
        'Orianna': [],
        'Pantheon': [],
        'Azir': [],
        'Seraphine': [],
        'Sett': [],
        'Graves': [],
        'Velkoz': [],
        'Trundle': [],
        'Karthus': [],
        'Anivia': [],
        'Gragas': [],
        'Hwei': [],
        'Kassadin': [],
        'Yone': [],
        'XinZhao': [],
        'Lux': [],
        'Shen': [],
        'DrMundo': [],
        'Corki': [],
        'Kled': [],
        'Zac': [],
        'Diana': [],
        'Senna': [],
        'Jax': [],
        'Sion': [],
        'Alistar': [],
        'Kaisa': [],
        'Rammus': [],
        'Sylas': [],
        'Warwick': [],
        'MissFortune': [],
        'Ziggs': [],
        'Rell': [],
        'Naafiri': [],
        'Brand': [],
        'Hecarim': [],
        'Skarner': [],
        'Viego': [],
        'Jayce': [],
        'Shaco': [],
        'KogMaw': [],
        'LeeSin': [],
        'Taliyah': [],
        'Yorick': [],
        'Leblanc': [],
        'Talon': [],
        'Olaf': [],
        'Nidalee': [],
        'Ivern': [],
        'Illaoi': [],
        'Kayle': [],
        'Galio': [],
        'Kalista': [],
        'Aphelios': [],
        'Taric': [],
        'Renekton': [],
        'Riven': [],
        'Ekko': [],
        'Rakan': [],
        'AurelionSol': [],
        'Quinn': [],
        'KSante': [],
        'Poppy': [],
        'Singed': [],
        'Volibear': [],
        'TahmKench': [],
        'Akshan': [],
        'Camille': [],
        'Sejuani': [],
        'Qiyana': [],
        'Udyr': [],
        'RekSai': []}
        return champ_dic