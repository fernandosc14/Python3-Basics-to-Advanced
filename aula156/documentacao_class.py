class Foo:
    def soma(self, x, y):
        """Sum two values.

        Args:
            x (int): _first value to sum.
            y (int): _second value to sum.

        Returns:
            int  : the sum of x and y.
        """
        return x + y
    
    def bar(self) ->  int:
        """Just a method that does nothing.
        
            :raises NotImplementedError: always raised.
            :raises ValueError: if something bad happens.
        """
        
        raise NotImplementedError("Method not implemented yet.")
    