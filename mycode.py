
class Person:
    """
    A class used to represent a Person.

    Attributes
    ----------
    name : str
        The name of the person.
    age : int
        The age of the person, which must be a non-negative integer.

    Methods
    -------
    info():
        Returns a string containing a greeting with the person's name and age.
    __repr__():
        Returns a string representation of the Person object.
    """

    def __init__(self, name: str, age: int):
        """
        Constructs all the necessary attributes for the Person object.

        Parameters
        ----------
        name : str
            The name of the person.
        age : int
            The age of the person, which must be a non-negative integer.
        
        Raises
        ------
        ValueError
            If the name is not a string or if the age is not a non-negative integer.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.name = name
        self.age = age

    def information(self):
        """
        Returns a string containing a greeting with the person's name and age.

        Returns
        -------
        str
            A string in the format "[INFO] Hello, my name is {self.name} and I am {self.age} years old."
        """
        return f"[INFO] Hello, my name is {self.name} and I am {self.age} years old."

    def __repr__(self):
        """
        Returns a string representation of the Person object.

        Returns
        -------
        str
            A string in the format "Person(name={self.name}, age={self.age})"
        """
        return f"Person(name={self.name}, age={self.age})"

person1 = Person("Alice", 30)
print(person1.information())