# https://www.wj0511.com/site/detail.html?id=154
import datetime
import random
import time
from random import randint, choice

a1=(2020,1,1,0,0,0,0,0,0)
a2=(2020,12,31,23,59,59,0,0,0)


prenomList = ["Martin", "Bernard", "Thomas", "Robert", "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau", "Vincent", "Muller", "Faure", "Mercier", "Blanc", "Guerin", "Boyer", "Garnier", "Chevalier", "Francois", "Legrand", "Gauthier", "Perrin", "Robin", "Clement", "Morin", "Henry", "Roussel", "Mathieu", "Gautier", "Masson", "Marchand", "Duval", "Dumont", "Marie", "Lemaire", "Noel", "Meyer", "Dufour", "Meunier", "Brun", "Blanchard", "Giraud", "Joly", "Riviere", "Lucas", "Brunet", "Gaillard", "Barbier", "Arnaud", "Martinez", "Gerard", "Roche", "Renard", "Schmitt", "Roy", "Leroux", "Colin", "Vidal", "Caron", "Picard", "Roger", "Fabre", "Aubert", "Lemoine", "Renaud", "Dumas", "Lacroix", "Olivier", "Philippe", "Bourgeois", "Pierre", "Benoit", "Rey", "Leclerc", "Payet", "Rolland", "Leclercq", "Guillaume", "Lecomte", "Lopez", "Jean", "Dupuy", "Guillot", "Hubert", "Berger", "Carpentier", "Sanchez", "Dupuis", "Moulin", "Louis", "Deschamps", "Huet", "Vasseur", "Boucher", "Fleury", "Royer", "Klein", "Jacquet", "Adam", "Paris"]
nomList = ["LANA", "MAÏLYS", "INÈS", "HAYLIE", "MONA", "TAIS", "ELÉA", "CHARLIE", "MYA", "VICTORIA", "MAËLINE", "THAIS", "ALYSSIA", "LOÉLINE", "JULINE", "LÉANA", "NOÉLYNE", "MAËLYNE", "ÉLISE", "NINA", "KALYANA", "PAULINE", "MADY", "ÉLÉNA", "LOUISA", "MALIA", "IZÏA", "MÉLINE", "JEANNE", "CHLOÉ", "BETTINA", "JOY", "EMMA", "KESSY", "ROMANE", "ÉLÉANORE", "MIA", "EDEN", "KAYLEEN", "ELSA", "FLAVIE", "FLORA", "ANASTASIA", "KIANA", "ZORA", "ELYNE", "ALICIA", "APOLLINE", "ZOÉ", "LÉONIE", "JOCELIN", "MATHIAS", "ÉTIENNE", "VIVIEN", "NINO", "LORYS", "MYLANN", "KENZO", "ADAM", "WYATT", "JÉRÉMY", "SACHA", "ALEXANDRE", "THÉODORE", "LÉON", "ERWANN", "ELIAKIM", "AXEL", "VINCENZO", "NATHANAËL", "ILAN", "JOAN", "NINHO", "ALEXIS", "TILIO", "ROMÉO", "CÔME", "LOAN", "MÉLIO", "EWEN", "ADRIANO", "GAËL", "PAUL", "ADONIS", "QUENTIN", "ÉMILIEN", "ZACHARIE", "CORENTIN", "GASPARD", "SOHAN", "SIDNEY", "ROMAN", "SANDRO", "MANAËL", "ALIM", "TILOUAN", "GIANNI", "SIRIUS", "GIANI", "MARIN"]
campusList = ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice']
internshipsList = ['Dev', 'DEVOPS', 'Cloud', 'Network', 'Infra', 'Management']
homeTownList = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille", "Rennes", "Reims", "Le Havre", "Saint-Étienne", "Toulon", "Grenoble", "Dijon", "Nîmes", "Angers", "Villeurbanne", "Le Mans", "Saint-Denis", "Aix-en-Provence", "Clermont-Ferrand", "Brest", "Limoges", "Tours", "Amiens", "Perpignan", "Metz", "Besançon", "Boulogne-Billancourt", "Orléans", "Mulhouse", "Rouen", "Saint-Denis", "Caen", "Argenteuil", "Saint-Paul", "Montreuil", "Nancy", "Roubaix", "Tourcoing", "Nanterre", "Avignon", "Vitry-sur-Seine", "Créteil", "Dunkirk", "Poitiers", "Asnières-sur-Seine", "Courbevoie", "Versailles", "Colombes", "Fort-de-France", "Aulnay-sous-Bois", "Saint-Pierre", "Rueil-Malmaison", "Pau", "Aubervilliers", "Le Tampon", "Champigny-sur-Marne", "Antibes", "Béziers", "La Rochelle", "Saint-Maur-des-Fossés", "Cannes", "Calais", "Saint-Nazaire", "Mérignac", "Drancy", "Colmar", "Ajaccio", "Bourges", "Issy-les-Moulineaux", "Levallois-Perret", "La Seyne-sur-Mer", "Quimper", "Noisy-le-Grand", "Villeneuve-d'Ascq", "Neuilly-sur-Seine", "Valence", "Antony", "Cergy", "Vénissieux", "Pessac", "Troyes", "Clichy", "Ivry-sur-Seine", "Chambéry", "Lorient", "Les Abymes", "Montauban", "Sarcelles", "Niort", "Villejuif", "Saint-André", "Hyères", "Saint-Quentin", "Beauvais", "Épinay-sur-Seine"]
dropOutList = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Economic', 'Negative', 'Fired']
schooleList = ['ESCE', 'University of Bordeaux', 'EURECOM', 'UPEC', 'EIT Digital Master School', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
companyList = ['', '', '', '', '', '', '', 'Axa', 'BNP', 'Carrefour', 'Airbus', 'Google', 'Bouygues', 'Celio', 'Free', 'Hermes', 'La Poste', 'Lancome', 'Rexel', 'Ubisoft']

# campusid
# attendance
# age

import csv
#open函数第一个参数是导出的文件名,第二个参数是w(表示写模式),在Python2中为wb(w表示写模式 b表示文件类型),在Python3中如果使用wb的话回报(TypeError: a bytes-like object is required, not 'str')错误第三个参数设置文件编码格式是utf-8,第四个参数是去除每行数据中间的空格,如果不加上newline='',导出文件成功,但是导出的文件每行之间会有一行空格
with open('students.csv', 'w', encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        #csv header
        result = ['Prenom', 'Nom', 'Age', 'Campus', 'Internship', 'Hometown', 'Attendance', 'Mobility', 'DropOut', 'Graduated_time', 'Company', 'Entry_time']

        # writer.writerow(result)
        # 100 new student into csv
        for i in range(100):
            # generate entry date

            start = time.mktime(a1)
            end = time.mktime(a2)
            t = random.randint(start, end)
            date_touple = time.localtime(t)  # Generate a time tuple of timestamps
            date = time.strftime("%Y-%m-%d", date_touple)


            li = []
            campusID = randint(100000,300000)

            li.append(choice(prenomList))
            li.append(choice(nomList))
            li.append(randint(18, 24))
            li.append(choice(campusList))
            li.append(choice(internshipsList))
            li.append(choice(homeTownList))
            li.append(randint(0,64))
            li.append(choice(schooleList))
            # dropout no Graduate time
            dropStatus = choice(dropOutList)
            if dropStatus == '':
                li.append(dropStatus)
                li.append('2020-04-01')
            else:
                li.append(dropStatus)
                li.append('')
            # no company no entry time
            companyStatus = choice(companyList)
            if companyStatus != '':
                li.append(companyStatus)
                li.append(date)
            else:
                li.append(companyStatus)
                li.append('')


            for m in range(12):
                lm = []
                lm.append(campusID)
                lm.append(result[m])
                lm.append(li[m])
                print(lm)
                writer.writerow(lm)