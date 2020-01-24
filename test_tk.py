from flashcard import get_words,nClick,first_guess_points,next_guess_points
def test_correct_word():
    with open("/tmp/words.txt","w") as f:
        for i in ["get the one", "words  t wo", "word three"]:
            f.write(i+"\n")
    selected_word = get_words('/tmp/words.txt')
    assert selected_word == 'word three'


def test_right_button_pressed():
    press=1
    assert nClick(press) == 1

def test_wrong__button_pressed():
    press=2
    assert nClick(press) == 2

def test_befor_first_guess_point():
    counter =3
    assert first_guess_points(counter) == (3,0,0)
    
def test_correct_guess_point():
    counter =1
    assert first_guess_points(counter) == (1,1,0)
def test_wrong_guess_point():
    counter =2
    assert first_guess_points(counter) == (2,0,1)

def test_next_correct_point():
    counter=1
    right=0
    wrong=0
    assert next_guess_points(counter,right,wrong) == (1,1,0)

def test_next_wrong_point():
    counter=2
    right=0
    wrong=0
    assert next_guess_points(counter,right,wrong) == (2,0,1)

def test_again_correct_point():
    counter=1
    right=2
    wrong=0
    assert next_guess_points(counter,right,wrong) == (1,3,0)

def test_again_wrong_point():
    counter=2
    right=1
    wrong=1
    assert next_guess_points(counter,right,wrong) == (2,1,2)













