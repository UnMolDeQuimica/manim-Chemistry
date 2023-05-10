from setuptools import setup

if __name__ == "__main__":
    setup(
        entry_points={
            'manim.plugins': [
                'manim_chemistry = manim_chemistry',
            ],
        },
    )

