from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

def simulate_dice_rolls(num_sides_die1, num_sides_die2, num_simulations, asymmetric=False):
    die_1 = Die(num_sides_die1)
    die_2 = Die(num_sides_die2)

    if asymmetric:
        die_2.num_sides = num_sides_die2 + 3  # Asymmetric die with a coefficient equal to its side number

    results = []
    for _ in range(num_simulations):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    return results

def main():
    n = 3  # порядковий номер в журналі
    num_sides_symmetric = n + 3
    num_sides_asymmetric = n + 3

    results_symmetric = simulate_dice_rolls(num_sides_symmetric, num_sides_symmetric, 1000)
    results_asymmetric = simulate_dice_rolls(num_sides_symmetric, num_sides_asymmetric, 1000, asymmetric=True)

    # Analyze the results.
    max_result = num_sides_symmetric * 2
    frequencies_symmetric = [results_symmetric.count(value) for value in range(2, max_result+1)]
    frequencies_asymmetric = [results_asymmetric.count(value) for value in range(2, max_result+1)]

    # Visualize the results.
    x_values = list(range(2, max_result+1))
    data = [
        Bar(x=x_values, y=frequencies_symmetric, name='Symmetric'),
        Bar(x=x_values, y=frequencies_asymmetric, name='Asymmetric')
    ]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rolling two dice (symmetric and asymmetric) 1000 times',
                       xaxis=x_axis_config, yaxis=y_axis_config)
    
    offline.plot({'data': data, 'layout': my_layout}, filename='dice_simulation.html')

if __name__ == '__main__':
    main()
