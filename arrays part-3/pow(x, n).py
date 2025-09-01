class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Tranform power to +ve if it's in -ve value
        n_copy = n
        if n < 0 : n_copy *=-1

        output = 1.0

        while(n_copy != 0):
            # If the power is odd take out the current value of x and reduce power by 1
            if n_copy % 2 != 0:
                output *= x
                n_copy = n_copy - 1
            else:
                # Multiply the current value of x with itself which means the current power is gone doen by half
                x = x * x
                n_copy = n_copy / 2
        
        if n < 0 : output = 1 / output
        return output


        