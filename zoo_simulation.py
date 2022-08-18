# %%
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class Animal_object: 
    """
    Creat animal with coresponding characteristics
    """
    def __init__(self,animal_type:str):
        
        """
        Each animal group located in the zoo is described by attributes:
            - call
            - biological class
            - mobility
        """

        # Define flamingos attributes
        if animal_type == 'flamingos':
            self.call = 'kle'
            self.bio_class = 'birds'
            self.mobility = 'in sky'
        
        # Define zebras attributes
        elif animal_type == 'zebras':
            self.call = 'yoyo'
            self.bio_class = 'mammals'
            self.mobility = 'to ground'

        # Define emus attributes
        elif animal_type == 'emus':
            self.call = 'brbr'
            self.bio_class = 'birds'
            self.mobility = 'to ground'

        # Define dolphin attributes
        elif animal_type == 'dolphins':
            self.call = 'er er'
            self.bio_class = 'mammals'
            self.mobility = 'in water'

        else:
            print(f'The zoo is not yet ready for {animal_type}.')

def Zoo(animals:list):
    """
    Function to plot the Zoo plan according to animals
    - input: list of animals in the zoo

    """
    zoo_size = [100, 100]
    number_of_cages = len(animals)

    cage_width = int(zoo_size[0]/number_of_cages)
    cage_height = zoo_size[1]
    cage_corner = 0

    # define Matplotlib figure and axis
    fig, ax = plt.subplots()

    for animal_type in animals:
        settings = {}

        # different setting for cages
        if animal_type.mobility == 'to ground':
            settings['edgecolor'] = 'black'
            settings['facecolor'] = 'none'
            settings['linewidth'] = '5'
        
        if animal_type.mobility == 'in sky':
            settings['edgecolor'] = 'pink'
            settings['facecolor'] = 'none'
            settings['hatch'] = '+'
        
        if animal_type.mobility == 'in water':
            settings['edgecolor'] = 'blue'
            settings['facecolor'] = 'blue'
            settings['alpha'] = 0.4


        # add a cage to plot
        ax.add_patch(Rectangle((cage_corner, 0), cage_width, cage_height, **settings))
        ax.text(cage_corner + cage_width/2-5, cage_height / 2, animal_type.call, fontsize = 15)
        
        # prepare for the next cage
        cage_corner = cage_corner + cage_width

    # display plot
    ax.autoscale_view()
    plt.title('Zoo plan')
    plt.xlabel('meters')
    plt.ylabel('meters')
    plt.show()
# %% Creat a zoo map

animal_list = ['flamingos', 'zebras', 'dolphins', 'emus']
object_list = []

for cage_number, animal in enumerate(animal_list):

    # Creat objects from animal_list
    new_animal = Animal_object(animal)

    # Put all animal objects in one list
    object_list.append(new_animal)

    print(f'Cage No{cage_number+1}: {animal}, animal class: {new_animal.bio_class}.')

# Plot zoo plan
Zoo(object_list)

