from psychopy import visual, core, event
import random
import itertools
import csv

# program można wyłąćzyć w trakcie trwania próby treningowej lub eksperymentalnej za pomocą przycisku 'x' na klawiaturze, może być wymagane zakończenie pętli poszzególnego bodzca, więc po naciśnięciu x, należy wcisnąć obojętnie którą strzałkę w celu zakończenia
def check_quit():
    if 'x' in event.getKeys():
        core.quit()

# Lista i -bodzce zgodne niezgodne i neutralne do części pierwszej eksperymentalnej -prawo i lewo
lista_i = [
    ("PRAWO", (0.65, 0)),   # right on the right
    ("PRAWO", (-0.65, 0)),  # right on the left
    ("PRAWO", (0, 0)),      # right in the center
    ("LEWO", (0.65, 0)),    # left on the right
    ("LEWO", (-0.65, 0)),   # left on the left
    ("LEWO", (0, 0))        # left in the center
]

# Lista j -bodzce zgodne, niezgodne i neutralne do części drugiej eksperymentu- gora i dol
lista_j = [
    ("GÓRA", (0.02, 0.65)),    # up at the top
    ("GÓRA", (0.02, -0.65)),   # up at the bottom
    ("GÓRA", (0.02, 0)),       # up in the center
    ("DÓŁ", (0.04, 0.65)),     # down at the top
    ("DÓŁ", (0.04, -0.65)),    # down at the bottom
    ("DÓŁ", (0.04, 0))         # down in the center
]
#lista k - część trzecia łączy wszystkie bodzce z dwóch poprzednich części 
lista_k = lista_i + lista_j

#randomizacja bodzców, aby bodźce wyświetlały się w randomowej kolejności, Randomizacja użyta, aby przypadkiem nie wprowadzić wzoru wyświetlania bodzców, który mógłby zostać zauważony przez osobę badaną, co zepsułoby badanie.
def randomize_stimuli(lista, num_trials):
    return random.sample(lista * ((num_trials // len(lista)) + 1), num_trials)

#faza treningowa - to 20 prób- wyświetlających się bodzców, poniżej jest zapisane 10, ponieważ używamy dwóch list po 10 bodzców z każdej
num_trials_training = 10
#każda z faz eksperymentalnych to po 75 wyświetlających się bodzców 
num_trials_experiment = 75

#randomizacja części treningowej, po 10 randomowo pokazanych bodzców z listy i i z listy j, wspólnie 20 bodzcó w trakcie fazy freningowej
randomized_i_training = randomize_stimuli(lista_i, num_trials_training )
randomized_j_training = randomize_stimuli(lista_j, num_trials_training )
#randomizacja części eksperymentalnych po 75 randomowo pokazanych bodzców w odpowiednich częściach
randomized_i_experiment = randomize_stimuli(lista_i, num_trials_experiment)
randomized_j_experiment = randomize_stimuli(lista_j, num_trials_experiment)
randomized_k_experiment = randomize_stimuli(lista_k, num_trials_experiment)

win = visual.Window(fullscr=True)

#instrukcje początkowe podzielone na kilka wyświetleń w celu polepszenia i poprawienia czytelności
text1 = visual.TextStim(win, text='Witaj! Przed rozpoczęciem badania upewnij się, że masz dostęp do klawiatury z działającymi przyciskami strzałek.',
                        color='black', height=0.05, font='Arial', pos=(0,0.4))
text2 = visual.TextStim(win, text='Po części treningowej zostaniesz przeniesiony/a do właściwej części eksperymentalnej podzielonej na trzy części. Każda z części będzie trwała około 2 minuty. Aby zakończyć przerwę po kolejnych częściach należy kliknąć przycisk Spacja.',
                        color='black', height=0.05, font='Arial', pos=(0,0.2))
text3 = visual.TextStim(win, text='Naciśnij przycisk spacja, aby przejść do instrukcji.',
                        color='black', height=0.05, font='Arial', pos=(0,-0.6))

text1.draw()
text2.draw()
text3.draw()
win.flip()

while not event.getKeys(['space']):
    pass

#Dokładne instrukcje jak należy odpowiadać na zaprogramowane bodźce
instructions = [
    ('Kiedy na ekranie pojawi się słowo „prawo” należy wcisnąć przycisk →', (0, 0.4)),
    ('Kiedy na ekranie pojawi się słowo „lewo” należy wcisnąć przycisk ←', (0, 0.3)),
    ('Kiedy na ekranie pojawi się słowo „góra” należy wcisnąć przycisk ↑', (0, 0.2)),
    ('Kiedy na ekranie pojawi się słowo „dół” należy wcisnąć przycisk ↓', (0, 0.1)),
    ('Miejsce w którym pojawia się słowo na ekranie nie ma wpływu na wybierany z klawiatury przycisk.', (0, -0.3)),
    ('Naciśnij przycisk spacja, aby przejść dalej.', (0, -0.6))
]

for text, pos in instructions:
    visual.TextStim(win, text=text, color='black', height=0.05, font='Arial', pos=pos).draw()

win.flip()
while not event.getKeys(['space']):
    pass

text1 = visual.TextStim(win, text='Odpowiadaj jak najszybciej oraz staraj się udzielać poprawne odpowiedzi, ponieważ badany będzie czas i poprawność reakcji.',
                        color='black', height=0.05, font='Arial', pos=(0, 0.4))
text2 = visual.TextStim(win, text='Aby przenieść się do części treningowej, podczas której będziesz mógł/mogła przetestować działanie programu, naciśnij przycisk Spacja.',
                        color='black', height=0.05, font='Arial', pos=(0,0.2))
text1.draw()
text2.draw()
win.flip()
while not event.getKeys(['space']):
    pass

# część treningowa- instrukcje 

trening = visual.TextStim(win, text='CZĘŚĆ TRENINGOWA', color='black', height=0.06, font='Arial', pos=(0,0.3))
trening1 = visual.TextStim(win, text='Odpowiadaj jak najszybciej, jeżeli poczujesz się gotowy/a do podjęcia części eksperymentalnej naciśnij przycisk Spacja',  
                           color='black', font='Arial', height=0.05, pos=(0,0))

trening.draw()
trening1.draw()
win.flip()
core.wait(1)


win.flip()

# punkt fiksacji któy będzie pojawiał się po każdym wyświetlonym bodzcu na dwie sekundy,
fiks = visual.TextStim(win, text='+', color='black', font='Arial', height=0.08, pos=(0,0))
fiks.draw()
win.flip()
core.wait(2)

#oczekiwane przyciski, których osoba badana używa z klawiatury w celu reakcji na bodziec
expected_keys_i = ['right', 'right', 'right', 'left', 'left', 'left'] * (num_trials_experiment // 6)
expected_keys_j = ['up', 'up', 'up', 'down', 'down', 'down'] * (num_trials_experiment // 6)
expected_keys_k = expected_keys_i + expected_keys_j

#definiowanie bodzców i graficzna prezentacja, czas reakcji 
def present_stimulus(win, stimulus, expected_key):
    stimulus_text, stimulus_pos = stimulus
    stimulus_box = visual.TextBox2(win,
        text=stimulus_text,
        color="black",
        font="Arial", letterHeight=0.06,
        size=(0.2, 0.1), pos=stimulus_pos)
    
    stimulus_box.draw()
    win.flip()
    
    start_time = core.Clock()
    response = event.waitKeys(keyList=['left', 'right', 'up', 'down'])
    reaction_time = start_time.getTime()
    
    correct = (response[0] == expected_key)
    
    return reaction_time, correct


#właściwy eksperyment i prezentacja- wyświetlanie podczas badania bodzców
def run_experiment(win, stimuli_list, expected_keys, num_trials, output_file):
    results = []
    for i in range(num_trials):
        stimulus = stimuli_list[i]
        expected_key = expected_keys_i
        reaction_time, correct = present_stimulus(win, stimulus, expected_key)
        results.append([stimulus[0], stimulus[1], reaction_time, correct])
        check_quit()
        fiks.draw()
        win.flip()
        core.wait(1)
# zapisywanie wyników eksperymentu -zapisują się wyniki zarówno z części treningowej jak i eksperymentalnej w pliku o rozszerzeniu csv, zapisują się inormacje  o wyświetlonym bodźcu, jego pozycji, dzięki czemu możemy wnioskować, czy bodziec był bodzcem zgodnym, niezgodnym czy neutralnym.
# w pliku zapisuje się również czas reakcji na bodziec, czyli od momentu pokazania się bodzca do naciśniecia strzałki, oraz informacja, czy reakcja była odpowiednia względem wyświetlonego bodźca
    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Stimulus", "Position", "Reaction Time", "Correct"])
        writer.writerows(results)
    
    return results

# Faza treningowa- 20 bodźców - prawo lewo, góra dół, faza treningowa jest jedynie pomocą dla osoby badanej, aby bezstresowo mogłą przyzwyczaić się do proccedury, do klawiszy i swoich reakcji, oraz ze względów technicznych, czy wszystko działa poprawnie w czasie zadania
training_results_i = run_experiment(win, randomized_i_training, expected_keys_i, len(randomized_i_training), 'training_results.csv')
training_results_j = run_experiment(win, randomized_j_training, expected_keys_j, len(randomized_j_training), 'training_results.csv')

# Do czesci 1
eks2 = visual.TextStim(win, text='Aby przejść do części eksperymentalnej naciśnij przycisk Spacja',
                        color='black', font='Arial', height=0.05, pos=(0,0))
eks2.draw()
win.flip()
while not event.getKeys(['space']):
    pass

# eksperyment 1 -instrukcje
eksp2 = visual.TextStim(win, text='CZĘŚĆ EKSPERYMENTALNA – 1', color='black', font='Arial', height=0.06, pos=(0,0))
eksp2.draw()
win.flip()
core.wait(1.5)

win.flip()


fiks = visual.TextStim(win, text='+', color='black', font='Arial', height=0.08, pos=(0,0))
fiks.draw()
win.flip()
core.wait(2)

# Faza 1 - 75 prezentowanych bodzców, bodźce prawo i lewo
experiment_results_i = run_experiment(win, randomized_i_experiment, expected_keys_i, len(randomized_i_experiment), 'experiment_results.csv')

# do czesci 2
eks2 = visual.TextStim(win, text='Aby przejść do części drugiej naciśnij przycisk Spacja',
                        color='black', font='Arial', height=0.05, pos=(0,0))
eks2.draw()
win.flip()
while not event.getKeys(['space']):
    pass

# eksperyment 2 -instrukcje
eksp2 = visual.TextStim(win, text='CZĘŚĆ EKSPERYMENTALNA – 2', color='black', font='Arial', height=0.06, pos=(0,0))
eksp2.draw()
win.flip()
core.wait(1.5)

# Faza 2 75 bodzców randomowo ułożonych - góra i dół
experiment_results_j = run_experiment(win, randomized_j_experiment, expected_keys_j, len(randomized_j_experiment), 'experiment_results.csv')

# do czesci 3
eks2 = visual.TextStim(win, text='Aby przejść do części trzeciej naciśnij przycisk Spacja',
                        color='black', font='Arial', height=0.05, pos=(0,0))
eks2.draw()
win.flip()
while not event.getKeys(['space']):
    pass

# eksperyment 3-instrucje
eksp3 = visual.TextStim(win, text='CZĘŚĆ EKSPERYMENTALNA – 3', color='black', font='Arial', height=0.06, pos=(0,0))
eksp3.draw()
win.flip()
core.wait(1.5)

# Faza 3 - czyli 75 uwspólnionych bodźców, góra dół, lewo prawo 
experiment_results_k = run_experiment(win, randomized_k_experiment, expected_keys_k, len(randomized_k_experiment), 'experiment_results.csv')

# zakończenie procedury - podziękowanie, wyjść po zakończeniu programu można naciskając przycisk x 
papa = visual.TextStim(win, text='Dziękujemy za udział w badaniu :)', color='black', height=0.05, font='Arial', pos=(0,0))
papa2 = visual.TextStim(win, text='aby wyjść z programu naciśnij przycisk X na klawiaturze', color='black', height=0.05, font='Arial', pos=(0,-0.6))
win.flip()
papa.draw()
papa2.draw()
while True: 
    win.flip() 
    papa.draw() 
    papa2.draw() 
    if 'x' in event.getKeys(): 
        break 

win.close()
core.quit()