import csv
from random import seed
from random import randrange
textList = [' has covid.', ' has covid 19.', ' has covid19 and in #isolation', ' has corona virus.', ' got covid.', ' got covid 19 and in #isolation', ' got corona virus. ', ' is sick. ', ' is feeling sick.', ' has high body temperature. ', ' has covid19 symptoms. '
            ' has covid may god protect her ', ' has covid 19 may god protect him ', ' has corona virus. Our prayers and hopes with her ', ' got covid, our wished with her ', ' got covid 19 and in #isolation ', ' got corona virus we hope him the best. ', ' is sick, lets hope she gets over it soon ',
            ' is feeling sick and is in quarantine for safety reasons ', ' has high body temperature and is in isolation because he might have covid ', ' has covid19 symptoms, let\' hope she gets better soon ', 
            ' has corona may god protect him ', ' caught the coronavirus may god protect her ', ' has received the corona virus. Our prayers and hopes with him', ' got covid, our wished with him', ' caught covid 19 and in #isolation ', ' tested positive for corona virus we hope her the best. ', ' is feeling sick, lets hope he gets over it soon ',
            ' said yesterday that has corona may god protect him ', ' announced on Tueday that caught the coronavirus may god protect her ', ' reported on Wednesday that has received the corona virus. Our prayers and hopes with him ', ' notified that he got covid, our wishes with him ', ' revealed at the morning that he caught covid 19 and in #isolation ', ' revealed that she tested positive for corona virus we hope her the best. ', ' notified that he is feeling sick, lets hope he gets over it soon ',
            ' says that has corona may god protect her ', ' announces that caught the coronavirus may god protect him ', ' reports that she has received the corona virus. Our prayers and hopes with her', ' notifies that he got covid, our wishes with him ', ' reveals at the morning that she caught covid 19 and is in #isolation ', ' reveals that he tested positive for corona virus we hope him the best. ', ' notifies that she is feeling sick, lets hope she gets over it soon ',
            ' tested positive for covid.', ' tested positive for corona. ', ' is waiting for results, possibly will be positive.','\'s results came positive for corona.',
            ' tested positive for covid19, praying for his speedy recovery ', ' tested positive for corona, sources told today. ', ' is waiting for results, possibly will be positive expert say',' \'s results came positive for corona, CNN reports ',
            ' has been tested positive to Covid19 ', "\'s aide tests positive for coronavirus 🇺🇸","\'s secretary tested positive for coronavirus ", ' after testing positive for COVID-19 ',
            " reveals he and son tested positive for coronavirus ", " reveals she and son tested positive for coronavirus ", " reveals that her cook did test positive for COVID-19 ",
            " tests possitive for covid19"," tests positive for coronavirus "," tests possitive for covid-19","\'s personal assistant has now tested positive for Covid ",
            " said on Monday that he was #tested #positive for the novel #coronavirus ", " said on Friday that he was #tested #positive for the covid19 "," said on Saturday that she was #tested #positive for the novel #coronavirus "]

text2 = [ " He is being #admitted to the #hospital. "," Asks people who came in contact with him to get #tested ", " Is being taken to the Medical Center after being #tested #positive covid19 ", 
          " Prayers and wishes for our friends to get well soon.", " Prayers and wishes for our friend to get well soon. ", " That is unlucky ", " Be careful people", " Stay safe ", "Mask up "
        " His family and friends are now in isolation too as they got in contract with him ", " He is also schedules to do the covid19 vaxin ", " She was always very careful "]

text4 = [" He is being #admitted to the #hospital. ", " Asks people who came in contact with him to get #tested ", " Is being taken to the Medical Center after being #tested #positive covid19 ",
         " That is unlucky ",  " He is also schedules to do the covid19 vaxin ", " She was always very careful " ]

text1 = [" \"I've #Tested #Positive For #Covid19\" Says ","BREAKING NEWS: ", " Well it happened... ", " Well it accured ", " Bad news ", " It is real ", " It exists ", " It isn\'t lie ", " Be careful people "]

Title = [" President ", " Multimillioner ", " Football star ", " Pop star ", " Rapper ", " Famous doctor ", " Tictoc star ", " Fighter ", " Bodybuilder ",]

text6 = [" CEO of ", " Owner Of ", " Manager of ", " Founder of "]

with open('C:/Users/HakiM/OneDrive/Documents/Visual Studio Code/Machine Learning/Neural Networks/RandomNames.csv', 'r', newline='') as rfile:
    reader = csv.reader(rfile)
    with open('C:/Users/HakiM/OneDrive/Documents/Visual Studio Code/Machine Learning/Neural Networks/TrueTweetsGenerated.csv', 'a', newline='', encoding="UTF-8") as wfile:
        writer = csv.writer(wfile)
        for row in reader:
            wantText2 = randrange(8)
            wantText1 = randrange(10)
            wantTitle = randrange(8)
            wantText6 = randrange(14)
            addRandomPhrase = randrange(14)
            text = row[0] + textList[randrange(62)]
            if wantText6 == 0:
                f = open('RandomCompanies.csv')
                f.seek(randrange(270))
                f.readline()
                randomCompany = f.readline()
                if len(randomCompany) == 0:       # we have hit the end
                    f.seek(1)
                    randomCompany = f.readline()  # so we'll grab the first line instead
                text = text6[randrange(3)] + text
            elif wantTitle == 0:
                text = Title[randrange(8)] + text
            if wantText1 == 0:
                text = text1[randrange(8)] + text
            if wantText2 == 0:
                text = text2[randrange(10)] + text
            if wantText6 == 0:
                f2 = open('RandomPhrases.csv')
                f2.seek(randrange(220))
                f2.readline()
                randomPhrase = f2.readline()
                if len(randomPhrase) == 0:       # we have hit the end
                    f2.seek(1)
                    randomPhrase = f2.readline()  # so we'll grab the first line instead
                text = text + randomPhrase
                text = text.rstrip()
            writer.writerow([text +",1"])
            