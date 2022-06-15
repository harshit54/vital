from __future__ import annotations
from abc import ABC, abstractmethod
import pyautogui as pag
from dotenv import dotenv_values

config = dotenv_values(".env")
DEADZONE = float(config['DEADZONE'])
SENSITIVITY = float(config['SENSITIVITY'])
MOVE_PRECISION = float(config['MOVE_PRECISION'])
SCROLL_PRECISION = float(config['SCROLL_PRECISION'])


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the
    current state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def changeState(self):
        self._state.transitionState()

    def changePrecision(self):
        self._state.transitionPrecision()

    def move(self, x, y):
        self._state.move(x, y)

    def center_mouse(self):
        res = pag.size()
        pag.moveTo(res[0] / 2, res[1] / 2)


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def transitionState(self) -> None:
        pass

    @abstractmethod
    def transitionPrecision(self) -> None:
        pass

    @abstractmethod
    def move(self, x, y) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class Move(State):
    def transitionState(self) -> None:
        '''
        Transition from Move state to Scroll state.
        '''
        self.context.transition_to(Scroll())

    def transitionPrecision(self) -> None:
        '''
        Transition from Move state to Precision Move state.
        '''
        self.context.transition_to(PreciseMove())

    def move(self, x, y) -> None:
        '''
        Move Mouse given x, y
        '''
        print(f"Move By: {(x,y)}")
        if x > DEADZONE or y > DEADZONE:
            pag.moveRel(-SENSITIVITY * x, 2 * SENSITIVITY * y)


class Scroll(State):
    def transitionState(self) -> None:
        '''
        Transition from Scroll State to Move State.
        '''
        self.context.transition_to(Move())

    def transitionPrecision(self) -> None:
        '''
        Transition from Scroll State to Move State.
        '''
        self.context.transition_to(PreciseScroll())

    def move(self, x, y) -> None:
        '''
        Scroll by x and y
        Horizontal scroll works only in Linux and Mac
        '''
        pag.hscroll(x)
        pag.vscroll(y)


class PreciseMove(State):
    def transitionState(self) -> None:
        '''
        Transition from Precise Move State to Precise Scroll State.
        '''
        self.context.transition_to(PreciseScroll())

    def transitionPrecision(self) -> None:
        '''
        Transition from Scroll State to Move State.
        '''
        self.context.transition_to(Move())

    def move(self, x, y) -> None:
        '''
        Move Mouse given x, y
        '''
        print(f"Move By: {(x,y)}")
        if x > DEADZONE or y > DEADZONE:
            pag.moveRel(-SENSITIVITY * x * MOVE_PRECISION,
                        2 * SENSITIVITY * y * MOVE_PRECISION)


class PreciseScroll(State):
    def transitionState(self) -> None:
        '''
        Transition from Precise Scroll State to Precise Move State.
        '''
        self.context.transition_to(PreciseMove())

    def transitionPrecision(self) -> None:
        '''
        Transition from Precise Scroll State to Scroll State.
        '''
        self.context.transition_to(Scroll())

    def move(self, x, y) -> None:
        '''
        Scroll by x and y
        Horizontal scroll works only in Linux and Mac
        '''
        pag.hscroll(SCROLL_PRECISION * x)
        pag.vscroll(SCROLL_PRECISION * y)
