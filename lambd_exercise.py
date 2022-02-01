print('Lambdas Exercise')
# turning every function in lambda function

# First
print('---------------FIRST-EX------------------')
def f(x): return x + 5


print(f(2))


def add_x(x): return x+5


print(add_x(2))

print(' ')
# Second
print('---------------SECOND-EX------------------')


def strip_spaces(str):
    return ''.join(str.split(' '))


print(strip_spaces('Monty Pythons Flying Circus'))


def strip_space1(str): return ''.join(str.split(' '))


print(strip_spaces('Monty Pythons Flying Circus'))

print(' ')
# Thrid
print('---------------THIRD-EX------------------')


def join_list_no_duplicates(list_a, list_b):
    return list(set(list_a + list_b))


list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6, 7]
print(join_list_no_duplicates(list_a, list_b))


def join_list_no_duplicates1(list_a, list_b): return list(set(list_a+list_b))


print(join_list_no_duplicates(list_a, list_b))

print(' ')
# Fourth
print('---------------FOURTH-EX------------------')


def create_quad_func(a, b, c):
    return lambda x: a*x ** 2 + b*x + c


f = create_quad_func(2, 4, 6)
g = create_quad_func(3, 4, 6)
print(f(2))
print(g(5))

print(' ')
# Fifth
print('---------------FIFTH-EX------------------')
signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
a = signups

print(sorted(a, key= lambda id:int(id[3:])))

print(' ')
#Sixth
print('---------------SIXTH-EX------------------')

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

print(sorted([player.name for player in player_list], key= lambda score: score[1]))
