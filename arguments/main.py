# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
#deel 1
def greet(name: str, greeting_template = 'Hello, <name>!'):
    greeting = greeting_template.replace('<name>', name)
    return greeting

print(greet("Jochum"))
print(greet("Jochum", "What's up <name> !"))

#deel 2
def force(mass, body='earth'):
    bodies = {
    'Sun': 274,
    'Jupiter': 24.92,
    'Neptune': 11.15,
    'Saturn': 10.44,
    'Earth': 9.798,
    'Uranus': 8.87,
    'Venus': 8.87,
    'Mars': 3.71,
    'Mercury': 3.7,
    'Moon': 1.62,
    'Pluto': 0.58
    }
    gravity = bodies.get(body, "Undefined")
    if (gravity != "undefined"):
        print(f'the gravity from an object is {mass} kg on {body.lower()} is {round(mass*gravity,1)} Newton')
        answer = round(mass * gravity, 1)
        return answer
    else:
        return "undefined"
 
print(force(3.4, 'Moon'))
    

#deel 3
def pull(m1: float, m2: float, d: float, body: str):
    gravity = 6.674 * 10 ** (-11)
    if d != 0:
        pull = round(gravity * (m1 * m2) / d ** 2, 1)
        print(f'The gravity from an object is {m1} kg on {body.lower()} is {pull} Newton')
        return pull
    else:
        return 0

print(pull(0.1, 5.972*10**24, 6.371*10**6, "earth"))

