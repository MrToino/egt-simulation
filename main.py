"""
Project: EGT-Sim

Filename: main.py
Description: running and testing
"""


framework_data = {
    "Population": {
        "Size": (100,),
        "Intensities": (1.0, )
    },
    "LearningRules": ({
            "LR Label": "SL",
            "Game Type": "2P",
            "Game": "SG",
            "Game Specs": (3, 2, 4, 1),
        },
    )
}


def run():
    """Project runner for given input"""
    pass


if __name__ == '__main__':
    run()
