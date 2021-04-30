import pytest
import src.exercise

def test_exercise():
    input_values = ["Scott"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values[0]
        else:
            output.append("")
            return input_values[0]

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["What is your name?","Hi Scott"]
