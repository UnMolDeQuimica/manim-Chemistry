from setuptools import setup

if __name__ == "__main__":
    setup(
        entry_points={
            'manim.plugins': [
                'manim_chemistry = src.manim_chemistry',
            ],
        },
    )

